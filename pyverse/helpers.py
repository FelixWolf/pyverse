from . import messages
from . import message
import time, random, struct
from .llTypes import *
from .constraints import constraints
const = constraints()
class interaction:
    session = None
    def __init__(self, session):
        self.session = session
    
    def say(self, chn, msg, ty=1):
        myMessage = messages.getMessageByName("ChatFromViewer")
        myMessage.AgentData["AgentID"] = self.session.agent_id
        myMessage.AgentData["SessionID"] = self.session.session_id
        myMessage.ChatData["Message"] = variable(2, msg+"\u0000")
        myMessage.ChatData["Type"] = ty
        myMessage.ChatData["Channel"] = chn
        self.session.send(myMessage)
    
    def sit(self, target, offset=vector3(0,0,0)):
        myMessage = messages.getMessageByName("AgentRequestSit")
        myMessage.AgentData["AgentID"] = self.session.agent_id
        myMessage.AgentData["SessionID"] = self.session.session_id
        myMessage.TargetObject["TargetID"] = target
        myMessage.TargetObject["Offset"] = offset
        self.session.send(myMessage)
        
    def stand(self):
        self.session.agentUpdate(controls=65536)
        self.session.agentUpdate(controls=0)
    
    def touch(self, target, UV=vector3(0,0,0), ST=vector3(0,0,0), face=0):
        self.grab(target, UV, ST, face)
        self.deGrab(target, UV, ST, face)
    
    def grab(self, target, UV=vector3(0,0,0), ST=vector3(0,0,0), face=0):
        myMessage = messages.getMessageByName("ObjectGrab")
        myMessage.AgentData["AgentID"] = self.session.agent_id
        myMessage.AgentData["SessionID"] = self.session.session_id
        myMessage.ObjectData["LocalID"] = target
        myMessage.ObjectData["GrabOffset"] = vector3(0, 0, 0)
        myMessage.SurfaceInfo = [
            {
                "UVCoord": UV,
                "STCoord": ST,
                "FaceIndex": face,
                "Position": vector3(0,0,0),
                "Normal": vector3(0,0,0),
                "Binormal": vector3(0,0,0)
            }
        ]
        self.session.send(myMessage)
    
    def control(self, c, once=False):
        if once:
            self.session.controls_once = c
        else:
            self.session.controls = c
            
    def deGrab(self, target, UV=vector3(0,0,0), ST=vector3(0,0,0), face=0):
        myMessage = messages.getMessageByName("ObjectDeGrab")
        myMessage.AgentData["AgentID"] = self.session.agent_id
        myMessage.AgentData["SessionID"] = self.session.session_id
        myMessage.ObjectData["LocalID"] = target
        myMessage.ObjectData["GrabOffset"] = vector3(0, 0, 0)
        myMessage.SurfaceInfo = [
            {
                "UVCoord": UV,
                "STCoord": ST,
                "FaceIndex": face,
                "Position": vector3(0,0,0),
                "Normal": vector3(0,0,0),
                "Binormal": vector3(0,0,0)
            }
        ]
        self.session.send(myMessage)
