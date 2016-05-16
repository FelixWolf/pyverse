#!/usr/bin/env python3
import struct
import uuid as __uuid__
class null:
    def __bytes__(self):
        return b""
    def __str__(self):
        return "<NULL>"

class fixed:
    data = b""
    def __init__(self, data):
        if type(data) == bytes:
            self.data = data
        elif type(data) == str:
            self.data = data.encode("utf-8")
        elif hasattr(data, "__bytes__"):
            self.data = bytes(data)
        else:
            self.data = type(data).encode("utf-8")
    
    def __bytes__(self):
        return data
    
    def __len__(self):
        return len(data)
    
    def __str__(self):
        try:
            return self.data.decode()
        except:
            return "<FIXED: %i>"%len(self.data)

class variable:
    data = b""
    type = 0
    def __init__(self, ty = 1, data = b""):
        if type(data) == bytes:
            self.data = data
        elif type(data) == str:
            self.data = data.encode("utf-8")
        elif hasattr(data, "__bytes__"):
            self.data = bytes(data)
        else:
            self.data = type(data).encode("utf-8")
        self.type = ty
        if ty == 1:
            if len(self.data) >= 255:
                raise Exception("Data must be less than 256 bytes for Variable 1")
        elif ty == 2:
            if len(self.data) >= 65535:
                raise Exception("Data must be less than 65535 bytes for Variable 2")
        else:
            raise Exception("Type must be 1 or 2")
    
    def __bytes__(self):
        if type == 1:
            return struct.pack("<B", len(self.data)) + self.data
        elif type == 2:
            return struct.pack("<H", len(self.data)) + self.data
        #Fall back and hope for the best
        return struct.pack("<B", len(self.data)) + self.data
        
    def __len__(self):
        return len(data)
    
    def __str__(self):
        try:
            return self.data.decode()
        except:
            return "<VARIABLE %i: %i>"%(self.type,len(self.data))
            
    def __repr__(self):
        return "<VARIABLE %i: %i>"%(self.type,len(self.data))

class vector3:
    x = 0
    y = 0
    z = 0
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z
    
    def __bytes__(self):
        return struct.pack("<fff", self.x, self.y, self.z)
    
    def __str__(self):
        return "<%f, %f, %f>"%(self.x, self.y, self.z)
    
    def __eq__(self, cmp):
        if type(cmp) != vector3:
            return False
        if self.x != cmp.x:
            return False
        if self.y != cmp.y:
            return False
        if self.z != cmp.z:
            return False
        return True

class vector3d(vector3):
    def __bytes__(self):
        return struct.pack("<ddd", self.x, self.y, self.z)
    
    def __str__(self):
        return "<%f, %f, %f>"%(self.x, self.y, self.z)
    
    def __eq__(self, cmp):
        if type(cmp) != vector3d:
            return False
        if self.x != cmp.x:
            return False
        if self.y != cmp.y:
            return False
        if self.z != cmp.z:
            return False
        return True
    
class vector4:
    x = 0
    y = 0
    z = 0
    s = 0
    def __init__(self, x=0, y=0, z=0, s=0):
        self.x = x
        self.y = y
        self.z = z
        self.s = s
    
    def __bytes__(self):
        return struct.pack("<ffff", self.x, self.y, self.z, self.s)
    
    def __str__(self):
        return "<%f, %f, %f, %f>"%(self.x, self.y, self.z, self.s)
    
    def __eq__(self, cmp):
        if type(cmp) != vector4:
            return False
        if self.x != cmp.x:
            return False
        if self.y != cmp.y:
            return False
        if self.z != cmp.z:
            return False
        if self.s != cmp.s:
            return False
        return True

class quaternion:
    x = 0
    y = 0
    z = 0
    s = 0
    def __init__(self, s=0, x=0, y=0, z=0):
        self.s = s
        self.x = x
        self.y = y
        self.z = z
    
    def __bytes__(self):
        return struct.pack("<ffff", self.s, self.x, self.y, self.z)
    
    def __str__(self):
        return "<%f, %f, %f, %f>"%(self.s, self.x, self.y, self.z)
    
    def __eq__(self, cmp):
        if type(cmp) != quaternion:
            return False
        if self.x != cmp.x:
            return False
        if self.y != cmp.y:
            return False
        if self.z != cmp.z:
            return False
        if self.s != cmp.s:
            return False
        return True

#Alias for people who can't spell quaternion
rotation = quaternion

class color4U:
    r = 0
    g = 0
    b = 0
    a = 0
    def __init__(self, r=0, g=0, b=0, a=0):
        self.r = r
        self.g = g
        self.b = b
        self.a = a
    
    def __bytes__(self):
        return struct.pack("<BBBB", self.r, self.g, self.b, self.a)
    
    def __str__(self):
        return "<%i, %i, %i, %i>"%(self.r, self.g, self.b, self.a)
    
    def __eq__(self, cmp):
        if type(cmp) != color4U:
            return False
        if self.r != cmp.r:
            return False
        if self.g != cmp.g:
            return False
        if self.b != cmp.b:
            return False
        if self.a != cmp.a:
            return False
        return True

class LLUUID:
    UUID = __uuid__.UUID("00000000-0000-0000-0000-000000000000")
    def __init__(self, key = "00000000-0000-0000-0000-000000000000"):
        if type(key) == bytes:
            if len(key) == 16:
                self.UUID = __uuid__.UUID(bytes=key)
            else:
                raise Exception("Expected byte length of 16, got length %i"%len(key))
        elif type(key) == str:
            self.UUID = __uuid__.UUID(key)
    
    def __bytes__(self):
        return self.UUID.bytes
    
    def __str__(self):
        return str(self.UUID)
    
    def __len__(self):
        #Always returns 16
        return 16
        
    def __eq__(self, other):
        if type(other) == LLUUID:
            if bytes(self) == bytes(other):
                return True
        return False

class IPAddr:
    addr = [0,0,0,0]
    def __init__(self, a=0,b=0,c=0,d=0):
        if type(a) == str:
            a = a.split(".")
            if len(a) == 4:
                b = int(a[1])
                c = int(a[2])
                d = int(a[3])
                a = int(a[0])
            else:
                raise Exception("Malformed IP address: "+a)
        if type(a) == int and type(b) == int and type(c) == int and type(d) == int:
            if 0 <= a < 256 and 0 <= b < 256 and 0 <= c < 256 and 0 <= d < 256:
                self.addr = [a,b,c,d]
            else:
                raise Exception("Malformed IP address(Range error): %i.%i.%i.%i"%(a,b,c,d))
        else:
            raise Exception("Malformed IP address(Type error): %s.%s.%s.%s"%(str(type(a)),str(type(b)),str(type(c)),str(type(d))))

    def __bytes__(self):
        return struct.pack("BBBB", self.addr[0], self.addr[1], self.addr[2], self.addr[3])
    
    def __str__(self):
        return "%i.%i.%i.%i"%(self.addr[0], self.addr[1], self.addr[2], self.addr[3])

class IPPort:
    port = 0
    def __init__(self, a=0):
        if type(a) == str:
            a = int(a)
        if type(a) == int:
            if 0 <= a < 0xffff:
                self.port = a
            else:
                raise Exception("Malformed port(Range error): %i"%(a))

    def __bytes__(self):
        return struct.pack("H", self.port)
    
    def __str__(self):
        return str(self.port)

def llDecodeType(t, ty = None):
    a = type(t)
    if a == null or a == fixed or a == variable or a == vector3 or \
        a == vector3d or a == vector4 or a == quaternion or a == LLUUID or \
        a == IPAddr or a == IPPort:
        return bytes(t)
    elif a == bytes:
        return t
    elif ty == "U8":
        return struct.pack("<B", t)
    elif ty == "U16":
        return struct.pack("<H", t)
    elif ty == "U32":
        return struct.pack("<I", t)
    elif ty == "U64":
        return struct.pack("<Q", t)
    elif ty == "S8":
        return struct.pack("<b", t)
    elif ty == "S16":
        return struct.pack("<h", t)
    elif ty == "S32":
        return struct.pack("<i", t)
    elif ty == "S64":
        return struct.pack("<q", t)
    elif ty == "F32":
        return struct.pack("<f", t)
    elif ty == "F64":
        return struct.pack("<d", t)
    elif ty == "BOOL" or t == bool:
        return struct.pack(">B", 1 if t == True else 0)
        
def llEncodeType(t, ty = None, vlen = None):
    if ty == "Null":
        return null()
    elif ty == "Fixed":
        return fixed(t)
    elif ty == "Variable":
        return variable(vlen, t)
    elif ty == "U8":
        return struct.unpack("<B", t)[0]
    elif ty == "U16":
        return struct.unpack("<H", t)[0]
    elif ty == "U32":
        return struct.unpack("<I", t)[0]
    elif ty == "U64":
        return struct.unpack("<Q", t)[0]
    elif ty == "S8":
        return struct.unpack("<b", t)[0]
    elif ty == "S16":
        return struct.unpack("<h", t)[0]
    elif ty == "S32":
        return struct.unpack("<i", t)[0]
    elif ty == "S64":
        return struct.unpack("<q", t)[0]
    elif ty == "F32":
        return struct.unpack("<f", t)[0]
    elif ty == "F64":
        return struct.unpack("<d", t)[0]
    elif ty == "LLVector3":
        tmp = struct.unpack("<fff", t)
        return vector3(tmp[0],tmp[1],tmp[2])
    elif ty == "LLVector3d":
        tmp = struct.unpack("<ddd", t)
        return vector3d(tmp[0],tmp[1],tmp[2])
    elif ty == "LLVector4":
        tmp = struct.unpack("<ffff", t)
        return vector4(tmp[0],tmp[1],tmp[2],tmp[3])
    elif ty == "LLQuaternion":
        tmp = struct.unpack("<ffff", t)
        return vector4(tmp[0],tmp[1],tmp[2],tmp[3])
    elif ty == "IPAddr":
        tmp = struct.unpack("<BBBB", t)[0]
        return IPAddr(tmp[0],tmp[1],tmp[2],tmp[3])
    elif ty == "IPPort":
        return IPAddr(struct.unpack("<H", t)[0])
    elif ty == "BOOL" or t == bool:
        return struct.pack("B", 1 if t == True else 0)
    elif ty == "LLUUID":
        return LLUUID(t)