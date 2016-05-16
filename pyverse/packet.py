from . import messages
from . import zerocode
import struct
class packet:
    """Load a packet"""
    #Body byte data, incase we need it
    bytes = b""
    body = None
    MID = 0
    sequence = 0
    extra = b""
    acks = []
    
    #Flags
    flags = 0
    zero_coded = 0
    reliable = 0
    resent = 0
    ack = True
    
    def __init__(self, bytes=None, message=None, mid = 0, sequence = 0, zero_coded = 0, reliable = 0, resent = 0, ack = 0, acks = []):
        if bytes:
            """Read an entire packet"""
            #Load in the header data
            self.flags, self.sequence, self.extra_bytes = \
                struct.unpack_from(">BiB", bytes[:6])
                
            #Unpack the flags
            self.zero_coded = (self.flags&0x80 == 0x80)
            self.reliable = (self.flags&0x40 == 0x40)
            self.resent = (self.flags&0x20 == 0x20)
            self.ack = (self.flags&0x10 == 0x10)
            self.extra = bytes[6:6+self.extra_bytes]
            if self.zero_coded:
                self.bytes = zerocode.decode(bytes[6+self.extra_bytes:])
            else:
                self.bytes = bytes[6+self.extra_bytes:]
            offset = 1
            self.MID = struct.unpack_from(">I", self.bytes, 0)[0]
            realID = self.MID
            if self.MID & 0xFFFFFFFA == 0xFFFFFFFA:
                realID = self.MID
                self.MID = self.MID & 0x000000FA
                offset = 4
            elif self.MID & 0xFFFF0000 == 0xFFFF0000:
                self.MID = self.MID & 0x0000FFFF
                realID = self.MID + 0xFFFF0000
                offset = 4
            elif self.MID & 0xFF000000 == 0xFF000000:
                self.MID = (self.MID >> 16) & 0xFF
                realID = self.MID + 0xFF00
                offset = 2
            else:
                self.MID = (self.MID >> 24) & 0xFF
                realID = self.MID
            self.body = messages.getMessageByID(realID, self.bytes[offset:])
            if self.ack:
                ackcount = bytes[len(bytes)-1]
                offset = len(bytes) - (ackcount * 4) - 1
                for i in range(ackcount):
                    self.acks.append(struct.unpack_from(">I", offset)[0])
                    offset = offset + 4
            else:
                self.acks = acks
        elif message:
            self.MID = message.id
            if len(acks) > 0 or ack:
                self.ack = True
            self.zero_coded = message.zero_coded
            self.sequence = sequence
            self.body = message
            self.acks = acks
        else:
            if MID:
                self.MID = MID
                if self.MID & 0xFFFFFFFA == 0xFFFFFFFA:
                    self.MID = self.MID & 0x000000FA
                    offset = 4
                elif self.MID & 0xFFFF0000 == 0xFFFF0000:
                    self.MID = self.MID & 0x0000FFFF
                    offset = 4
                elif self.MID & 0xFF000000 == 0xFF000000:
                    self.MID = (self.MID >> 16) & 0xFF
                    offset = 2
                else:
                    self.MID = (self.MID >> 24) & 0xFF
            if sequence:
                self.sequence = sequence
            if zero_coded == True:
                self.zero_coded = True
            if reliable == True:
                self.reliable == True
            if resent == True:
                self.resent == True
            if ack == True or len(acks) > 0:
                self.ack == True
                self.acks = acks
    
    def __bytes__(self):
        self.flags = 0
        if self.zero_coded:
            #self.flags = self.flags | 0x80
            self.zero_coded = False
        if self.reliable:
            self.flags = self.flags | 0x40
        if self.resent:
            self.flags = self.flags | 0x20
        if self.ack:
            self.flags = self.flags | 0x10
        acks = b""
        if self.ack:
            for i in self.acks:
                acks = acks + struct.pack(">I", i)
            acks = acks + struct.pack(">b", len(self.acks))
        body = bytes(self.body)
        if self.zero_coded:
            body = zerocode.encode(body)
        if self.body.freq == 3:
            result = struct.pack(">I", self.MID)
        elif self.body.freq == 2:
            result = struct.pack(">I", self.MID + 0xFFFF0000)
        elif self.body.freq == 1:
            result = struct.pack(">H", self.MID + 0xFF00)
        elif self.body.freq == 0:
            result = struct.pack(">B", self.MID)
        return struct.pack(">BiB", self.flags, self.sequence, len(self.extra)) + result + self.extra + body + acks