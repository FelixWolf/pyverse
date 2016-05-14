import sys, xmlrpc.client, hashlib, ssl
from uuid import getnode as get_mac
def getMacAddress():
    mac = get_mac()
    return ':'.join(("%012X" % mac)[i:i+2] for i in range(0, 12, 2))

__PLATFORM_STRING__ = "Unknown"
if sys.platform == "linux" or sys.platform == "linux2":
    __PLATFORM_STRING__ = "Lnx"
elif sys.platform == "darwin":
    __PLATFORM_STRING__ = "Mac"
elif sys.platform == "win32":
    __PLATFORM_STRING__ = "Win"

grid_uri = "https://login.agni.lindenlab.com/cgi-bin/login.cgi"
def login(firstname, lastname, password, mac=None, start="last", grid=grid_uri):
    if mac == None:
        mac = getMacAddress()
    proxy = xmlrpc.client.ServerProxy(
        grid,
        verbose=False, use_datetime=True, 
        context=ssl._create_unverified_context()
    )
    return proxy.login_to_simulator({
        "first": firstname,
        "last": lastname,
        "passwd": "$1$"+hashlib.md5(password.encode("latin")).hexdigest(),
        "start": start,
        "channel": "CZ_Python",
        "version": "Python "+sys.version,
        "platform": __PLATFORM_STRING__,
        #I dunno, just trust the scripter, if they wanted to
        #lie they would modify this
        "mac": mac,
        "id0": hashlib.md5(("%s:%s:%s"%(__PLATFORM_STRING__,mac,sys.version)).encode("latin")).hexdigest(),
        "agree_to_tos": True,
        "last_exec_event": 0,
        "options": [
            "inventory-root",
            #"inventory-skeleton",
            "inventory-lib-root",
            "inventory-lib-owner",
            #"inventory-skel-lib",
            #"gestures",
            #"event_notifications",
            #"event_categories",
            #"classified_categories",
            "buddy-list",
            #"ui-config",
            "login-flags",
            "global-textures"
            "adult_compliant",
            #"initial-outfit",
            #"max_groups", 
            #"max-agent-groups",
            #"map-server-url",
            #"tutorial_setting"
        ]
    })
    