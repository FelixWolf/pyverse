from . import messages
import socket, time
from .llTypes import *
from . import packet

class region:
    host = ""
    port = 0
    sock = None
    agent_id = None
    session_id = None
    loginToken = {}
    lastPing = 0
    nextAgentUpdate = 0
    sequence = 1
    def __init__(self, loginToken):
        self.loginToken = loginToken
        self.host = loginToken["sim_ip"]
        self.port = loginToken["sim_port"]
        self.session_id = uuid(loginToken["session_id"])
        self.agent_id = uuid(loginToken["agent_id"])
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        #Wave hello
        myMessage = messages.getMessageByName("UseCircuitCode")
        myMessage.CircuitCode["Code"] = loginToken["circuit_code"]
        myMessage.CircuitCode["SessionID"] = self.session_id
        myMessage.CircuitCode["AgentID"] = self.agent_id
        self.send(myMessage)
        #Enter the region
        myMessage = messages.getMessageByName("CompleteAgentMovement")
        myMessage.AgentData["AgentID"] = uuid(loginToken["agent_id"])
        myMessage.AgentData["SessionID"] = uuid(loginToken["session_id"])
        myMessage.AgentData["CircuitCode"] = loginToken["circuit_code"]
        self.send(myMessage)
    
    @property
    def seq(self):
        self.sequence = self.sequence + 1
        return self.sequence - 1
    
    def handleInternalpackets(self, blob):
        return True
        
    def recv(self):
        blob = self.sock.recvfrom(65507)
        if self.handleInternalPackets(blob):
            return self.sock.recvfrom(65507)
    
    def send(self, blob):
        try:
            self.sock.sendto(bytes(blob), (self.host,self.port))
            return True
        except Exception as e:
            return e
    
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
    