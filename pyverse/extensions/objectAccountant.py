#!/usr/bin/env python3
from ..llTypes import *

class llObject:
    id = 0
    state = 0
    uuid = LLUUID()
    pCode = 0
    material = 0
    clickAction = 0
    scale = vector3(0, 0, 0)
    objectData = {}
    parent = 0
    flags = 0
    pathCurve = 0
    profileCurve = 0
    pathBegin = 0
    pathEnd = 0
    pathScale = vector3(0, 0, 0)
    pathShear = vector3(0, 0, 0)
    pathTwist = 0
    pathtwistBegin = 0
    pathRadiusOffset = 0
    pathTaper = vector3(0, 0, 0)
    pathRevolutions = 0
    pathSkew = 0
    profileBegin = 0
    profileEnd = 0
    profileHollow = 0
    textures = {}
    name = ""
    data = {}
    text = ""
    textColour = color4U(0,0,0,0)
    mediaURL = ""
    particles = {}
    extraParams = {}
    sound = LLUUID()
    owner = LLUUID()
    soundFlags = 0
    radius = 0
    jointType = 0
    jointPivot = vector3(0,0,0)
    jointAxis = vector3(0,0,0)

def decodeObjectData(data):
    return {}

def decodeTextureData(textures, animations):
    return {}
    
def decodeGenericData(data):
    return {}
    
def decodePSBlock(data):
    return {}

def decodeExtraParams(data):
    return {}

class objectAccountant:
    objectDB = {}
    def __init__(self):
        pass
    
    def updateObject(self, objectData):
        """Register/update an object from message data"""
        id = objectData["ID"]
        if id not in self.objectDB:
            self.objectDB[id] = llObject()
        self.objectDB[id].id = id #For self referencing
        self.objectDB[id].state = objectData["State"]
        self.objectDB[id].uuid = objectData["FullID"]
        self.objectDB[id].pCode = objectData["PCode"]
        self.objectDB[id].material = objectData["Material"]
        self.objectDB[id].clickAction = objectData["ClickAction"]
        self.objectDB[id].scale = objectData["Scale"]
        #Impliment objectData decoder here: self.objectDB[id].objectData = decodeObjectData(objectData["ObjectData"])
        self.objectDB[id].parent = objectData["ParentID"]
        self.objectDB[id].flags = objectData["UpdateFlags"]
        self.objectDB[id].profileCurve = objectData["ProfileCurve"]
        self.objectDB[id].pathBegin = objectData["PathBegin"]
        self.objectDB[id].pathEnd = objectData["PathEnd"]
        self.objectDB[id].pathScale = vector3(objectData["PathScaleX"], objectData["PathScaleY"], 0)
        self.objectDB[id].pathShear = vector3(objectData["PathShearX"], objectData["PathShearY"], 0)
        self.objectDB[id].pathTwist = objectData["PathTwist"]
        self.objectDB[id].pathRadiusOffset = objectData["PathRadiusOffset"]
        self.objectDB[id].pathTaper = vector3(objectData["PathTaperX"], objectData["PathTaperY"], 0)
        self.objectDB[id].pathRevolutions = objectData["PathRevolutions"]
        self.objectDB[id].pathSkew = objectData["PathSkew"]
        self.objectDB[id].profileBegin = objectData["ProfileBegin"]
        self.objectDB[id].profileEnd = objectData["ProfileEnd"]
        self.objectDB[id].profileHollow = objectData["ProfileHollow"]
        
        #Impliment texture decoder here: self.objectDB[id].textures = decodeTextureData(objectData["TextureEntry"], objectData["TextureAnim"])

        self.objectDB[id].name = str(objectData["NameValue"])
        #Impliment data decoder here: self.objectDB[id].data = decodeGenericData(objectData["Data"])
        self.objectDB[id].text = str(objectData["Text"])
        self.objectDB[id].textColor = objectData["TextColor"]
        self.objectDB[id].mediaURL = str(objectData["MediaURL"])
        
        #Impliment PS decoder here: self.objectDB[id].particles = decodePSBlock(objectData["PSBlock"])

        #Impliment Extra decoder here: self.objectDB[id].extraParams = decodeExtraParams(objectData["ExtraParams"])

        self.objectDB[id].sound = objectData["Sound"]
        self.objectDB[id].owner = objectData["OwnerID"]
        self.objectDB[id].soundGain = objectData["Gain"]
        self.objectDB[id].soundFlags = objectData["Flags"]
        self.objectDB[id].soundRadius = objectData["Radius"]
        
        self.objectDB[id].jointType = objectData["JointType"]
        self.objectDB[id].jointPivot = objectData["JointPivot"]
        self.objectDB[id].jointAxis = objectData["JointAxisOrAnchor"]
        
    def deleteObject(self, id):
        """Delete an object from message data"""
        if id in self.objectDB:
            del self.objectDB[id]
        
    def findObject(self, objUUID = None, localID = None, name = None, desc = None):
        """Find an object where objUUID, localID, name, or desc matches"""
        if localID:
            if localID in self.objectDB:
                return self.objectDB[localID]
        
        #Compare once, loop multiple.
        #More efficient than loop all, compare all
        if objUUID:
            for i in self.objectDB:
                if self.objectDB[i]["uuid"] == objUUID:
                    return self.objectDB[i]
        
        if name:
            for i in self.objectDB:
                if self.objectDB[i]["name"] == name:
                    return self.objectDB[i]
        
        if desc:
            for i in self.objectDB:
                if self.objectDB[i]["desc"] == desc:
                    return self.objectDB[i]
