Development moved
-----------------
Please see https://github.com/FelixWolf/pymetaverse for a rewrite using async!

Purpose
------
The purpose this is to provide a simple python API to connect to Second Life.<br/>
While [PyOGP](http://wiki.secondlife.com/wiki/PyOGP) already exists, to my experience
the docs are missing/poorly written and it includes a lot more than just a bot.

This aims to be simple, and easy to use with minimal packet construction.

Example of use
------
My original code(seen at pyverse_old) was way too complicated, this version is a lot simpler:
```python
#!/usr/bin/env python3
import sys, signal, time
import pyverse
from pyverse import llTypes

loginToken = pyverse.login("firstname","lastname","password")
print(loginToken["message"]) #Print MOTD
session = pyverse.regionConnection(loginToken, host = "0.0.0.0", port = (29000,29099)) #Host and Port are optional
print("Connected to %s:%i from %s:%i"%(session.host,session.port,session.clientHost,session.clientPort))

while True:
    if session.nextAgentUpdate > time.time():
        session.agentUpdate()
    data = session.recv()
    if not data:
        break
    if data.body.name == "ChatFromSimulator":
        if data.body.ChatData["ChatType"] == pyverse.const.CHAT_TYPING_START \
         or data.body.ChatData["ChatType"] == pyverse.const.CHAT_TYPING_STOP:
            pass
        else:
            print("%s: %s"%(
                    str(data.body.ChatData["FromName"])[:-1],
                    str(data.body.ChatData["Message"])[:-1]
                )
            )
```

Current status
------
Can connect and do THINGS, possibly decodes packets properly as well.<br/>
TODO:
* Add support for the llCABundle.crt file during login for FULL COMPATIBILITY!
* Helper functions that create stuff like say(session, 0, "message")
* Adhere to [PEP 8](https://www.python.org/dev/peps/pep-0008/#comments) and comment the code.

Contribution
------
Think you can help pyverse grow and become better? Commit your changes to the
main branch and help us out! (Feel free to add your name/info to
contributors.txt while you are at it too!)

License
------
I'll add the license in the code later, it's under the MIT license.

>The MIT License (MIT)
>
>Copyright (c) 2016 pyverse contributors(See contributors.txt)
>
>Permission is hereby granted, free of charge, to any person obtaining a copy
>of this software and associated documentation files (the "Software"), to deal
>in the Software without restriction, including without limitation the rights
>to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
>copies of the Software, and to permit persons to whom the Software is
>furnished to do so, subject to the following conditions:
>
>The above copyright notice and this permission notice shall be included in all
>copies or substantial portions of the Software.
>
>THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
>IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
>FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
>AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
>LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
>OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
>SOFTWARE.

Copyrights and disclaimers
------
Pyverse and it's contributors are not endorsed, affiliated, or sponsored by
Linden Lab, the creators of Second Life, or Second Life it's self.<br/>
Second Life is registered trademark of Linden Lab, Inc.
