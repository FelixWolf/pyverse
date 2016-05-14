import messages
import zerocode
import struct
class packet:
    """Load a packet"""
    #Body byte data, incase we need it
    bytes = b""
    body = None
    mid = 0
    sequence = 0
    extra = b""
    acks = []
    
    #Flags
    flags = 0
    zero_coded = 0
    reliable = 0
    resent = 0
    ack = 0
    
    def __init__(self, bytes=None, mid = 0, sequence = 0, zero_coded = 0, reliable = 0, resent = 0, ack = 0):
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
            self.MID = struct.unpack_from(">I", self.bytes, 0)
            if self.MID & 0xFFFF0000 == 0xFFFF0000:
                self.MID = self.MID & 0x0000FFFF
            elif self.MID & 0xFF000000 == 0xFF000000:
                self.MID = self.MID & 0xFFFF0000
            else:
                self.MID = self.MID & 0xFF000000
            self.body = messages.getMessageByID(self.MID, self.bytes)
            if self.ack:
                ackcount = bytes[len(bytes)-1]
                offset = len(bytes) - (ackcount * 4) - 1
                for i in range(ackcount):
                    self.acks.append(struct.unpack_from(">I", offset)[0])
                    offset = offset + 4
        else:
            if mid:
                self.mid = mid
            if sequence:
                self.sequence = sequence
            if zero_coded == True:
                self.zero_coded = True
            if reliable == True:
                self.reliable == True
            if resent == True:
                self.resent == True
            if ack == True:
                self.ack == True
    
    def __bytes__(self):
        self.flags = 0
        if self.zero_coded:
            self.flags = self.flags | 0x80
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
        body = self.body
        if self.zero_coded:
            body = zerocode.encode(body)
        return struct.pack(">BiB", self.flags, self.sequence, len(self.extra)) + extra + bytes(body) + acks