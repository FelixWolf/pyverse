from . import messages
from . import message
import socket, time, random, struct
from .llTypes import *
from . import packet
from . import errorHandler
from .extensions.objectAccountant import objectAccountant
from .extensions.simMonitor import simMonitor

class region:
    host = ""
    port = 0
    clientPort = 0
    sock = None
    agent_id = None
    session_id = None
    loginToken = {}
    nextPing = 0
    nextAck = 0
    nextAgentUpdate = 0
    sequence = 1
    acks = []
    objects = None
    circuit_code = None
    debug = False
    controls = 0
    controls_once = 0
    sim = {
        "name": "",
        "owner": "",
        "terrain": {
            "water": 0,
            "base": [],
            "detail": [],
            "height": [],
            "range": []
        },
        "CPUClassID": 0,
        "CPURatio": 0,
        "ColoName": "",
        "ProductSKU": "",
        "ProductName": ""
    }
    def __init__(self, loginToken, host = "0.0.0.0", port = 0, debug=False):
        self.debug = debug
        if loginToken["login"] != "true":
            raise ConnectionError("Unable to log into simulator:\n    %s"%(
                loginToken["message"] if "message" in loginToken else "Unknown error"
            ))
        self.loginToken = loginToken
        self.host = loginToken["sim_ip"]
        self.port = loginToken["sim_port"]
        self.session_id = LLUUID(loginToken["session_id"])
        self.agent_id = LLUUID(loginToken["agent_id"])
        
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
        if type(port) == tuple:
            port = random.randint(port[0],port[1])
            
        self.sock.bind((host, port))
        self.clientHost = self.sock.getsockname()[0]
        self.clientPort = self.sock.getsockname()[1]
        
        self.circuit_code = struct.pack("<L",loginToken["circuit_code"])
        
        #Wave hello
        myMessage = messages.getMessageByName("UseCircuitCode")
        myMessage.CircuitCode["Code"] = self.circuit_code
        myMessage.CircuitCode["SessionID"] = self.session_id
        myMessage.CircuitCode["ID"] = self.agent_id
        self.send(myMessage)
        
        #Enter the region
        myMessage = messages.getMessageByName("CompleteAgentMovement")
        myMessage.AgentData["AgentID"] = self.agent_id
        myMessage.AgentData["SessionID"] = self.session_id
        myMessage.AgentData["CircuitCode"] = self.circuit_code
        self.send(myMessage)
        
        #These modules are optional, I'll add a method of plugins later
        #Fire up the object accountant
        self.objects = objectAccountant()
        #Sim status monitor
        self.status = simMonitor()
    
    @property
    def seq(self):
        self.sequence = self.sequence + 1
        return self.sequence - 1
    
    def handleInternalPackets(self, pck):
        if pck.body.name == "StartPingCheck":
            myMessage = messages.getMessageByName("CompletePingCheck")
            myMessage.PingID["PingID"] = pck.body.PingID["PingID"]
            self.send(myMessage)
        elif pck.body.name == "RegionHandshake":
            self.sim = {
                "name": pck.body.RegionInfo["SimName"],
                "owner": pck.body.RegionInfo["SimOwner"],
                "UUID": pck.body.RegionInfo2["RegionID"],
                "terrain": {
                    "water": pck.body.RegionInfo["WaterHeight"],
                    "base": [
                        pck.body.RegionInfo["TerrainBase0"],
                        pck.body.RegionInfo["TerrainBase1"],
                        pck.body.RegionInfo["TerrainBase2"],
                        pck.body.RegionInfo["TerrainBase3"]
                    ],
                    "detail": [
                        pck.body.RegionInfo["TerrainBase0"],
                        pck.body.RegionInfo["TerrainBase1"],
                        pck.body.RegionInfo["TerrainBase2"],
                        pck.body.RegionInfo["TerrainBase3"]
                    ],
                    "height": [
                        pck.body.RegionInfo["TerrainStartHeight00"],
                        pck.body.RegionInfo["TerrainStartHeight01"],
                        pck.body.RegionInfo["TerrainStartHeight10"],
                        pck.body.RegionInfo["TerrainStartHeight11"]
                    ],
                    "range": [
                        pck.body.RegionInfo["TerrainHeightRange00"],
                        pck.body.RegionInfo["TerrainHeightRange01"],
                        pck.body.RegionInfo["TerrainHeightRange10"],
                        pck.body.RegionInfo["TerrainHeightRange11"]
                    ]
                },
                "CPUClassID": pck.body.RegionInfo3["CPUClassID"],
                "CPURatio": pck.body.RegionInfo3["CPURatio"],
                "ColoName": str(pck.body.RegionInfo3["ColoName"]),
                "ProductSKU": str(pck.body.RegionInfo3["ProductSKU"]),
                "ProductName": str(pck.body.RegionInfo3["ProductName"])
            }
            myMessage = messages.getMessageByName("RegionHandshakeReply")
            myMessage.AgentData["AgentID"] = self.agent_id
            myMessage.AgentData["SessionID"] = self.session_id
            myMessage.RegionInfo["Flags"] = 0
            self.send(myMessage)
            
            #Informative packets
            self.throttle()
            self.setFOV()
            self.setWindowSize()
            
        elif pck.body.name == "ObjectUpdate":
            for obj in pck.body.ObjectData:
                self.objects.updateObject(obj)
            
        elif pck.body.name == "KillObject":
            for obj in pck.body.ObjectData:
                self.objects.deleteObject(obj["ID"])
                
        elif pck.body.name == "SimStats":
            self.status.update(pck.body.Stat)
        
        if pck.reliable:
            self.acks = self.acks + [pck.sequence]
        
        ctime = time.time()
        if self.nextAck < ctime:
            self.sendAcks()
        if self.nextAgentUpdate < ctime:
            self.agentUpdate(controls=self.controls_once|self.controls)
            self.controls_once = 0
            
    def recv(self):
        try:
            blob = self.sock.recv(65507)
            try:
                pck = packet.packet(data=blob)
            except:
                if self.debug:
                    print(errorHandler.packetErrorTrace(blob))
                pck = packet.packet(message = messages.TestMessage())
            if not hasattr(pck, "body"):
                print("Missing body!:")
                print(blob)
                pck.body = messages.TestMessage()
            self.handleInternalPackets(pck)
            return pck
        except KeyboardInterrupt:
            #Gracefully exit
            self.logout()
            
    
    def send(self, blob):
        if type(blob) is not packet.packet:
            if type(blob) == bytes:
                blob = packet.packet(sequence = self.seq, bytes = blob, acks = self.acks[0:255])
                self.acks = self.acks[255:]
                self.nextAck = time.time() + 1
            else:
                blob = packet.packet(sequence = self.seq, message = blob, acks = self.acks[0:255])
                self.acks = self.acks[255:]
                self.nextAck = time.time() + 1
        self.sock.sendto(bytes(blob), (self.host,self.port))
        return True
    
    def logout(self):
        try:
            myMessage = messages.getMessageByName("LogoutRequest")
            myMessage.AgentData["AgentID"] = self.agent_id
            myMessage.AgentData["SessionID"] = self.session_id
            self.send(myMessage)
            return True
        except Exception as e:
            return e
    
    def throttle(self, resend = 150000, land = 170000, wind = 34000, \
            cloud = 34000, task = 446000, texture = 446000, asset = 220000):
        myMessage = messages.getMessageByName("AgentThrottle")
        myMessage.AgentData["AgentID"] = self.agent_id
        myMessage.AgentData["SessionID"] = self.session_id
        myMessage.AgentData["CircuitCode"] = self.circuit_code
        myMessage.Throttle["GenCounter"] = 0
        myMessage.Throttle["Throttles"] = variable(1,
            struct.pack("<fffffff",
                #http://wiki.secondlife.com/wiki/AgentThrottle
                resend,  #Resend
                land,    #Land
                wind,    #Wind
                cloud,   #Cloud
                task,    #Task
                texture, #Texture
                asset    #Asset
            )
        )
        self.send(myMessage)
    
    fovGenCounter = 0
    def setFOV(self, FOV=6.233185307179586):
        myMessage = messages.getMessageByName("AgentFOV")
        myMessage.AgentData["AgentID"] = self.agent_id
        myMessage.AgentData["SessionID"] = self.session_id
        myMessage.AgentData["CircuitCode"] = self.circuit_code
        myMessage.FOVBlock["GenCounter"] = self.fovGenCounter
        myMessage.FOVBlock["VerticalAngle"] = 6.233185307179586
        self.send(myMessage)
        self.fovGenCounter = self.fovGenCounter + 1
        
    AHWGenCounter = 0
    def setWindowSize(self, width=0xffff, height=0xffff):
        myMessage = messages.getMessageByName("AgentHeightWidth")
        myMessage.AgentData["AgentID"] = self.agent_id
        myMessage.AgentData["SessionID"] = self.session_id
        myMessage.AgentData["CircuitCode"] = self.circuit_code
        myMessage.HeightWidthBlock["GenCounter"] = self.AHWGenCounter
        myMessage.HeightWidthBlock["Height"] = height
        myMessage.HeightWidthBlock["Width"] = width
        self.send(myMessage)
        self.AHWGenCounter = self.AHWGenCounter + 1
    
    def sendAcks(self):
        if len(self.acks) > 0:
            myMessage = messages.getMessageByName("PacketAck")
            tmp = self.acks[0:255]
            self.acks = self.acks[255:]
            myMessage.Packets = []
            for i in range(len(tmp)):
                myMessage.Packets.append({
                    "ID": tmp[i]
                })
            self.send(myMessage)
            self.nextAck = time.time() + 1
    
    def agentUpdate(self, controls = 0, cameraPos = vector3(128, 128, 0), state = 0, flags = 0, far = 1024, rate = 0.1):
        myMessage = messages.getMessageByName("AgentUpdate")
        myMessage.AgentData["AgentID"] = self.agent_id
        myMessage.AgentData["SessionID"] = self.session_id
        myMessage.AgentData["BodyRotation"] = rotation(0, 0, 0, 1)
        myMessage.AgentData["HeadRotation"] = rotation(0, 0, 0, 1)
        myMessage.AgentData["State"] = state
        myMessage.AgentData["CameraCenter"] = cameraPos
        myMessage.AgentData["CameraAtAxis"] = vector3(0, 0.999999, 0)
        myMessage.AgentData["CameraLeftAxis"] = vector3(0.999999, 0, 0)
        myMessage.AgentData["CameraUpAxis"] = vector3(0, 0, 0.999999)
        myMessage.AgentData["Far"] = far
        myMessage.AgentData["ControlFlags"] = controls
        myMessage.AgentData["Flags"] = flags
        self.send(myMessage)
        self.nextAgentUpdate = time.time() + rate

    def sendPing(self, pid):
        try:
            myMessage = messages.getMessageByName("CompletePingCheck")
            myMessage.PingID["PingID"] = pid
            self.send(myMessage)
            return True
        except Exception as e:
            return e
    
