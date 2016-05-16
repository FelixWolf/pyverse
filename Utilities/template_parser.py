#!/usr/bin/env python3
import json
# Input:
#{
#	TestMessage Low 1 NotTrusted Zerocoded
#	{
#		TestBlock1		Single
#		{	Test1		U32	}
#	}
#	{
#		NeighborBlock		Multiple		4
#		{	Test0		U32	}
#		{	Test1		U32	}
#		{	Test2		U32	}
#	}
#}
# Desired output:
#[
#    ["TestMessage","Low","1","NotTrusted","ZeroCoded"],
#    [
#        ["TestBlock1","Single"],
#        [
#            ["Test1", "U32"]
#        ]
#    ],
#    [
#        ["NeighborBlock","Multiple","4"],
#        [
#            ["Test0", "U32"],
#            ["Test1", "U32"],
#            ["Test2", "U32"]
#        ]
#    ]
#]
def parse(input):
    inComment = False
    blocks = []
    blockKeys = []
    lastChar = ""
    lastStr = ""
    inBlock = False
    for c in input:
        if c == "/" and lastChar == "/":
            inComment = True
            lastStr = lastStr[:-1]
        if not inComment:
            if inBlock > 0:
                if c == "{":
                    if inBlock > 0:
                        lastStr = lastStr + c
                    inBlock = inBlock + 1
                elif c == "}":
                    inBlock = inBlock - 1
                    if inBlock == 0:
                        blocks.append(parse(lastStr))
                        lastStr = ""
                        inBlock = False
                    elif inBlock > 0:
                        lastStr = lastStr + c
                else:
                    lastStr = lastStr + c
            elif c == "{":
                inBlock = inBlock + 1
            elif (c == "\t" or c == " " or c == "\n"):
                if lastStr.strip() != "":
                    blockKeys.append(lastStr)
                    lastStr = ""
            elif c == "}":
                pass
            else:
                lastStr = lastStr + c
        elif c == "\n":
            inComment = False
            lastStr = ""
        lastChar = c
    blocks.insert(0, blockKeys)
    return blocks

f = open("message_template_nocomments.msg", "r+")
a = parse(f.read())
f.close()
template = """class %s(message.baseMessage):
    name = "%s"
    id = %s
    freq = %s
    trusted = %s
    zero_coded = %s
    blocks = [
%s
    ]
    structure = {
%s
    }
registerMessage(%s)

"""
result = ""
for message in a:
    if message[0] == "version":
        pass
    else:
        messageName = message[0][0]
        frequency = ["High","Medium","Low","Fixed"].index(message[0][1])
        id = message[0][2]
        if id[0:2] == "0x":
            id = int(id,16)
        else:
            id = int(id)
        trusted = True if message[0][3] == "Trusted" else False
        zerocoded = True if message[0][4] == "Zerocoded" else False
        blocks = ""
        for i in range(1,len(message)):
            cou = message[i][0][1]
            if cou == "Single":
                cou = 1
            elif cou == "Variable":
                cou = 0
            else:
                cou = int(message[i][0][2])
            blocks = blocks + "        (\"%s\", %i),\n"%(message[i][0][0],cou)
        blocks = blocks[:-2]
        structures = ""
        for i in range(1,len(message)):
            structures = structures + "        \"%s\": [\n"%message[i][0][0]
            for x in message[i]:
                if type(x[0]) != str:
                    add = ""
                    if x[0][1] == "Variable" or x[0][1] == "Fixed":
                        add = ", %s"%x[0][2]
                    structures = structures + "            (\"%s\", \"%s\"%s),\n"%(x[0][0],x[0][1],add)
            structures = structures[:-2]+"\n"
            structures = structures + "        ],\n"
        result = result + template%(messageName,messageName,id,frequency,"True" if trusted else "False","True" if zerocoded else "False",blocks,structures[:-2],messageName)

f = open("result.py","w+")
f.write(result)
f.close()
