def decode(bytedata):
    """Convert a zerocoded bytestring into a bytestring"""
    i = 0
    l = len(bytedata)
    while i < l:
        if bytedata[i] == 0:
            c = bytedata[i+1] - 1
            bytedata = bytedata[:i+1] + (b"\x00"*c) + bytedata[i+2:]
            i = i + c 
            l = l + c - 1
        i = i + 1
    return bytedata
    
def encode(bytedata):
    """Convert a bytestring into a zerocoded bytestring"""
    i = 0
    l = len(bytedata)
    c = 0
    start = 0
    while i < l:
        if c > 253 or (bytedata[i] != 0 and c != 0):
            bytedata = bytedata[:start+1] + bytes((c,)) + bytedata[i:]
            i = i - c + 1
            l = l - c + 2
            c = 0
        elif bytedata[i] == 0:
            if c == 0:
                start = i
            c = c + 1
        i = i + 1
    if c != 0:
        bytedata = bytedata[:start+1] + bytes((c,)) + bytedata[i:]
    return bytedata

if __name__ == "__main__":
    import errorHandler
    import random
    a = b""
    for i in range(512):
        a = a + b"\x00"
        if random.randint(0,10)==5:
            a = a + b"\xff"
    b = encode(a)
    c = decode(b)
    print(errorHandler.hexdump(b))
    #print(errorHandler.hexdump(c))
    print("Original = %i, encoded = %i, decoded = %i"%(len(a),len(b),len(c)))
