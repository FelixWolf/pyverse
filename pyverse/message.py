#!/usr/bin/env python3
from . import llTypes
import struct

baseTypes = {
    "Null": llTypes.null(),
    "Fixed": llTypes.fixed(b""),
    "Variable1": llTypes.variable(1, b""),
    "Variable2": llTypes.variable(2, b""),
    "U8": 0,
    "U16": 0,
    "U32": 0,
    "U64": 0,
    "S8": 0,
    "S16": 0,
    "S32": 0,
    "S64": 0,
    "F32": 0.0,
    "F64": 0.0,
    "LLVector3": llTypes.vector3(),
    "LLVector3d": llTypes.vector3d(),
    "LLVector4": llTypes.vector4(),
    "LLQuaternion": llTypes.quaternion(),
    "LLUUID": llTypes.uuid(),
    "BOOL": False,
    "IPADDR": llTypes.IPAddr(),
    "IPPORT": llTypes.IPPort()
}
typeLengths = {
    "Null": 0,
    "Fixed": 0,
    "Variable1": 0,
    "Variable2": 0,
    "U8": 1,
    "U16": 2,
    "U32": 4,
    "U64": 8,
    "S8": 1,
    "S16": 2,
    "S32": 4,
    "S64": 8,
    "F32": 4,
    "F64": 8,
    "LLVector3": 12,
    "LLVector3d": 24,
    "LLVector4": 16,
    "LLQuaternion": 16,
    "LLUUID": 16,
    "BOOL": 1,
    "IPADDR": 4,
    "IPPORT": 2
}

class baseMessage:
    id = 0
    freq = 0
    trusted = False
    zero_coded = False
    blocks = [
        ("TestBlock1", 1),
        ("NeighborBlock", 4)
    ]
    structure = {
        "TestBlock1": [
            ["Test1", "U32"]
        ],
        "NeighborBlock": [
            ["Test0", "U32"],
            ["Test1", "U32"],
            ["Test2", "U32"]
        ]
    }
    def __init__(self, data=None):
        if not data:
            for key in self.blocks:
                if key[1] == 1:
                    tmp = {}
                    for value in self.structure[key[0]]:
                        tmp[value[0]] = baseTypes[value[1]]
                    setattr(self, key[0], tmp)
                else:
                    tmp = {}
                    for value in self.structure[key[0]]:
                        tmp[value[0]] = baseTypes[value[1]]
                    tmp2 = []
                    for i in range(key[1]):
                        tmp2.append(tmp)
                    setattr(self, key[0], tmp2)
        else:
            self.load(data)
    
    def load(self, data):
        offset = 0
        for key in self.blocks:
            if key[1] == 1:
                tmp = {}
                for value in self.structure[key[0]]:
                    tlen = 0
                    if value[1] == "Variable1":
                        tlen = struct.unpack_from(">B", data, offset)[0]
                        offset = offset + 1
                    elif value[1] == "Variable2":
                        tlen = struct.unpack_from(">H", data, offset)[0]
                        offset = offset + 2
                    else:
                        tlen = typeLengths[value[1]]
                    tmp[value[0]] = llTypes.llEncodeType(data[offset:offset+tlen], value[1])
                    offset = offset + tlen
                setattr(self, key[0], tmp)
            elif key[1] == 0:
                count = struct.unpack_from(">B", data, offset)[0]
                offset = offset + 1
                tmp2 = []
                for i in range(count):
                    tmp = {}
                    for value in self.structure[key[0]]:
                        tlen = 0
                        if value[1] == "Variable1":
                            tlen = struct.unpack_from(">B", data, offset)[0]
                            offset = offset + 1
                        elif value[1] == "Variable2":
                            tlen = struct.unpack_from(">H", data, offset)[0]
                            offset = offset + 2
                        else:
                            tlen = typeLengths[value[1]]
                        tmp[value[0]] = llTypes.llEncodeType(data[offset:offset+tlen], value[1])
                        offset = offset + tlen
                    tmp2.append(tmp)
                setattr(self, key[0], tmp2)
            else:
                outblock = []
                for i in range(key[1]):
                    tmp = {}
                    for value in self.structure[key[0]]:
                        tlen = 0
                        if value[1] == "Variable1":
                            tlen = struct.unpack_from(">B", data, offset)[0]
                            offset = offset + 1
                        elif value[1] == "Variable2":
                            tlen = struct.unpack_from(">H", data, offset)[0]
                            offset = offset + 2
                        else:
                            tlen = typeLengths[value[1]]
                        tmp[value[0]] = llTypes.llEncodeType(data[offset:offset+tlen], value[1])
                        offset = offset + tlen
                    outblock.append(tmp)
                setattr(self, key[0], outblock)

    def __bytes__(self):
        result = b""
        for key in self.blocks:
            if key[1] == 1:
                tmp = getattr(self, key[0])
                for value in self.structure[key[0]]:
                    result = result + llTypes.llDecodeType(tmp[value[0]], value[1])
            elif key[1] == 0:
                tmp = getattr(self, key[0])
                result = result + struct.pack("B", len(tmp))
                for i in range(len(tmp)):
                    tmp2 = tmp[i]
                    for value in self.structure[key[0]]:
                        result = result + llTypes.llDecodeType(tmp2[value[0]], value[1])
            else:
                tmp = getattr(self, key[0])
                for i in range(key[1]):
                    tmp2 = tmp[i]
                    for value in self.structure[key[0]]:
                        result = result + llTypes.llDecodeType(tmp2[value[0]], value[1])
        return result
