import traceback
import struct

def printsafe(data):
    result = ""
    for i in data:
        if 0x20 <= i <= 0x7E:
            result = result + chr(i)
        else:
            result = result + "."
    return result

def hexdump(data):
    info = ""
    l = len(data)
    for i in range(0, l, 0x10):
        hexdump = ""
        for x in range(i, i+0x8 if i+0x8 <= l else l):
            hexdump = hexdump + "{0:02X} ".format(data[x])
        hexdump = hexdump + " "
        for x in range(i+0x8, i+0x10 if i+0x10 <= l else l):
            hexdump = hexdump + "{0:02X} ".format(data[x])
        info = info + "{0:04X}     {1: <49s}     {2:s}\n".format(i, hexdump, printsafe(data[i:i+0x10]))
    return info

def packetErrorTrace(data):
    a = traceback.format_exc()
    if not a:
        return "Error: No error"
    flags, seq, exlen = struct.unpack_from(">BIB", data, 0)
    mid = struct.unpack_from(">I", data, 6+exlen)[0]
    freq = "FX"
    if mid & 0xFFFFFFFA == 0xFFFFFFFA:
        mid = mid & 0x000000FA
        freq = "FX"
    elif mid & 0xFFFF0000 == 0xFFFF0000:
        mid = mid & 0x0000FFFF
        freq = "LO"
    elif mid & 0xFF000000 == 0xFF000000:
        mid = (mid >> 16) & 0xFF
        freq = "MD"
    else:
        mid = (mid >> 24) & 0xFF
        freq = "HI"
    b = "{0: >3s} {1: >3s} {2: >3s} {3: >3s}  {4:08X}  {5: >2s} {6:08X}".format(
        "ZER" if flags&0x80 == 0x80 else "",
        "REL" if flags&0x40 == 0x40 else "",
        "RES" if flags&0x20 == 0x20 else "",
        "ACK" if flags&0x10 == 0x10 else "",
        seq,
        freq,
        mid
    )
    return "%s\n%s\n%s"%(a, b, ("-"*79)+"\n"+hexdump(data)+"\n"+("-"*79))
