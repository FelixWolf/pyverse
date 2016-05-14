from . import messages
from . import message
import socket, time, random, struct
from .llTypes import *
from . import packet

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
    def __init__(self, loginToken, host = "0.0.0.0", port = 0):
        self.loginToken = loginToken
        self.host = loginToken["sim_ip"]
        self.port = loginToken["sim_port"]
        self.session_id = uuid(loginToken["session_id"])
        self.agent_id = uuid(loginToken["agent_id"])
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
        if type(port) == tuple:
            port = random.randint(port[0],port[1])
        self.sock.bind((host, port))
        self.clientHost = self.sock.getsockname()[0]
        self.clientPort = self.sock.getsockname()[1]
        ccode = struct.pack("<L",loginToken["circuit_code"])
        #Wave hello
        myMessage = messages.getMessageByName("UseCircuitCode")
        myMessage.CircuitCode["Code"] = ccode
        myMessage.CircuitCode["SessionID"] = self.session_id
        myMessage.CircuitCode["ID"] = self.agent_id
        self.send(myMessage)
        #Enter the region
        myMessage = messages.getMessageByName("CompleteAgentMovement")
        myMessage.AgentData["AgentID"] = self.agent_id
        myMessage.AgentData["SessionID"] = self.session_id
        myMessage.AgentData["CircuitCode"] = ccode
        self.send(myMessage)
    
    @property
    def seq(self):
        self.sequence = self.sequence + 1
        return self.sequence - 1
    
    def handleInternalPackets(self, pck):
        if pck.body.name == "StartPingCheck":
            myMessage = messages.getMessageByName("CompletePingCheck")
            myMessage.PingID["PingID"] = pck.body.PingID["PingID"]
            self.send(myMessage)
        if pck.reliable:
            self.acks = self.acks + [pck.sequence]
        if self.nextAck < time.time() and len(self.acks) > 0:
            self.sendAcks()
        
    def sendAcks(self):
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
        
    def recv(self):
        try:
            blob = self.sock.recv(65507)
            blob = packet.packet(bytes=blob)
            if not hasattr(blob, "body"):
                blob.body = messages.TestMessage()
            self.handleInternalPackets(blob)
            return blob
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
    
    def agentUpdate(self, controls = 0, cameraPos = vector3(0, 0, 0), state = 0, flags = 0, far = 1024, rate = 1):
        try:
            myMessage = messages.getMessageByName("AgentUpdate")
            myMessage.AgentData["AgentID"] = self.agent_id
            myMessage.AgentData["SessionID"] = self.session_id
            myMessage.AgentData["BodyRotation"] = rotation(0, 0, 0, 0)
            myMessage.AgentData["HeadRotation"] = rotation(0, 0, 0, 0)
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
            return True
        except Exception as e:
            return e
    
    def sendPing(self, pid):
        try:
            myMessage = messages.getMessageByName("CompletePingCheck")
            myMessage.PingID["PingID"] = pid
            self.send(myMessage)
            self.lastAgentUpdate = time.time()
            return True
        except Exception as e:
            return e
    