class constraints:
    constraints = {
        #http://wiki.secondlife.com/wiki/SimStats
        #Ratio of time passage in region to real time passage.
        "LL_SIM_STAT_TIME_DILATION": 0,
        #Number of timesteps taken per second, rolling scale. Perfect is 45.0
        "LL_SIM_STAT_FPS": 1,
        #Number of timesteps taken in the physics engine per second, rolling scale. Perfect is 45.0
        "LL_SIM_STAT_PHYSFPS": 2,
        #Number of updates sent for agent objects per second. Should be one for every main agent and child agent connected to the region.
        "LL_SIM_STAT_AGENTUPS": 3,
        #Number of milliseconds spent processing each frame(Sum of all others). Averaged over each second. Should ideally be below 25.0
        "LL_SIM_STAT_FRAMEMS": 4,
        #Number of milliseconds spent processing network messages or connections. Averaged over each second. Should ideally be below 5.0
        "LL_SIM_STAT_NETMS": 5,
        #Number of milliseconds spent doing "other" things. Averaged over each second. Should ideally be below 5.0
        "LL_SIM_STAT_SIMOTHERMS": 6,
        #Number of milliseconds spent inside the physics engine(Sum of physics times.) Averaged over each second. Should ideally be below 10.0
        "LL_SIM_STAT_SIMPHYSICSMS": 7,
        #Number of milliseconds spent calculating agent visibility, interest lists, status, and preparing physical entity. Averaged over each second. Should ideally be below 5.0
        "LL_SIM_STAT_AGENTMS": 8,
        #Number of milliseconds spent processing image data, separating discard levels, decoding images. Averaged over each second. Should ideally be below 3.0
        "LL_SIM_STAT_IMAGESMS": 9,
        #Number of milliseconds spent running scripts and updating script states. Averaged over each second. Should ideally be below 25.0
        "LL_SIM_STAT_SCRIPTMS": 10,
        #Number of prims(tasks) within the region, including temporary tasks.
        "LL_SIM_STAT_NUMTASKS": 11,
        #Number of prims(tasks) that are active(physical, have scripts, changing status, being stood on.)
        "LL_SIM_STAT_NUMTASKSACTIVE": 12,
        #Number of agents that are within the region
        "LL_SIM_STAT_NUMAGENTMAIN": 13,
        #Number of agents that are not located within the region but can see into it.(Looking into the region from another region.)
        "LL_SIM_STAT_NUMAGENTCHILD": 14,
        #Number of scripts that are loaded onto tasks and set to running within the region. Scripts no set to running do not count towards this value.
        "LL_SIM_STAT_NUMSCRIPTSACTIVE": 15,
        #Number of LSL virtual machine instructions executed within the last second.
        "LL_SIM_STAT_LSLIPS": 16,
        #Number of packets simulator received that were related to the region in the last second.
        "LL_SIM_STAT_INPPS": 17,
        #Number of packets sent by the region in the last second.
        "LL_SIM_STAT_OUTPPS": 18,
        #Number of asset download requests waiting for a response.
        "LL_SIM_STAT_PENDING_DOWNLOADS": 19,
        #Number of asset upload requests waiting for authorization, response or to complete transfer.
        "LL_SIM_STAT_PENDING_UPLOADS": 20,
        #Unknown. Number of locally stored assets trying to transfer to another sim?(Skin bakes.)
        "LL_SIM_STAT_PENDING_LOCAL_UPLOADS": 23,
        #Number of kilobytes of network messages that have yet to be acknowledged. Ideally below 1000.
        "LL_SIM_STAT_TOTAL_UNACKED_BYTES": 24,
        #Number of prims that are marked as pinned within the physics system. Usually 0.
        "LL_SIM_STAT_PHYSICS_PINNED_TASKS": 25,
        #Number of prims that have had their level of detail reduced to help alleviate physics load. Ideally 0.
        "LL_SIM_STAT_PHYSICS_LOD_TASKS": 26,
        #Number of milliseconds spent running the physics time step. Averaged over a second. Ideally should be below 15.0
        "LL_SIM_STAT_SIMPHYSICSSTEPMS": 27,
        #Number of milliseconds spent updating the physical shape of an object. Averaged over a second. Ideally should be below 3.0
        "LL_SIM_STAT_SIMPHYSICSSHAPEMS": 28,
        #Number of milliseconds spent inside the physics engine not updating shapes or running physics step. Averaged over a second. Ideally should be below 3.0
        "LL_SIM_STAT_SIMPHYSICSOTHERMS": 29,
        #Number of megabytes of RAM allocated on the simulator for physics.
        "LL_SIM_STAT_SIMPHYSICSMEMORY": 30,
        
        #Damage system forced to on for entire region.
        "REGION_FLAGS_ALLOW_DAMAGE": 0x01,
        #If agents can create landmarks anywhere within the region.(Forced on)
        "REGION_FLAGS_ALLOW_LANDMARK": 0x02,
        #If agents can set their home location to anywhere within the region.(Forced on)
        "REGION_FLAGS_ALLOW_SET_HOME": 0x04,
        #If agents home location is set to the destination upon teleporting out of the region.
        "REGION_FLAGS_RESET_HOME_ON_TELEPORT": 0x08,
        #If the sun should not move with time.
        "REGION_FLAGS_SUN_FIXED": 0x10,
        #If taxes should not apply to this region.(Deprecated)
        "REGION_FLAGS_TAX_FREE": 0x20,
        #Land cannot be changed anywhere within the region. Trees and plants may still be placed.
        "REGION_FLAGS_BLOCK_TERRAFORM": 0x40,
        #Land cannot be released, sold, or bought within the entire region.
        "REGION_FLAGS_BLOCK_LAND_RESELL": 0x80,
        #Region is a sandbox and is wiped every 12 hours.(Appears deprecated.)
        "REGION_FLAGS_SANDBOX": 0x100,
        #Unknown: Related to the availability of an overview world map tile.(Think mainland images when zoomed out.)
        "REGION_FLAGS_NULL_LAYER": 0x200,
        #Unknown: Related to region debug flags. Possibly to skip processing of agent interaction with world.
        "REGION_FLAGS_SKIP_AGENT_ACTION": 0x400,
        #Region does not update agent prim interest lists. Internal debugging option.
        "REGION_FLAGS_SKIP_UPDATE_INTEREST_LIST": 0x800,
        #Makes all objects phantom and or pins them in place, does not affect agents.
        "REGION_FLAGS_SKIP_COLLISIONS": 0x1000,
        #Region does not run scripts, affects whole region.
        "REGION_FLAGS_SKIP_SCRIPTS": 0x2000,
        #Region does not run physics timesteps. All objects are frozen, including agents.
        "REGION_FLAGS_SKIP_PHYSICS": 0x4000,
        #Region can be seen from other regions on world map. (Legacy world map option?)
        "REGION_FLAGS_EXTERNALLY_VISIBLE": 0x8000,
        #Region can be seen from mainland on world map. (Legacy world map option?)
        "REGION_FLAGS_MAINLAND_VISIBLE": 0x10000,
        #Agents not explicitly on the access list can visit the region.
        "REGION_FLAGS_PUBLIC_ALLOWED": 0x20000,
        #Traffic calculations are not run across entire region, overrides parcel settings.
        "REGION_FLAGS_BLOCK_DWELL": 0x40000,
        #Flight is disabled for the entire region, overrides parcel settings.
        "REGION_FLAGS_BLOCK_FLY": 0x80000,
        #If teleports are allowed to exactly locations, if not on, agent is routed to nearest telehub. Overrides parcel settings.
        "REGION_FLAGS_ALLOW_DIRECT_TELEPORT": 0x100000,
        #Region is not running scripts, persisted in database. Set on an estate level.
        "REGION_FLAGS_ESTATE_SKIP_SCRIPTS": 0x200000,
        #Restricts the usage of the LSL llPushObject function, applies to whole region.
        "REGION_FLAGS_RESTRICT_PUSHOBJECT": 0x400000,
        #Denys "hackers on steroids" with no payment info from entering the region.
        "REGION_FLAGS_DENY_ANONYMOUS": 0x800000,
        #Denys agents with payment info from entering the region.(Legacy removed option.)
        "REGION_FLAGS_DENY_IDENTIFIED": 0x1000000,
        #Denys agents with payment info that has been used from entering the region.(Legacy removed option.)
        "REGION_FLAGS_DENY_TRANSACTED": 0x2000000,
        #Parcels within the region may be joined or divided by anyone, not just estate owners/managers.
        "REGION_FLAGS_ALLOW_PARCEL_CHANGES": 0x4000000,
        #Abuse reports sent from within this region are sent to the estate owner defined email.
        "REGION_FLAGS_ABUSE_EMAIL_TO_ESTATE_OWNER": 0x8000000,
        #Voice can be enabled within the region.
        "REGION_FLAGS_ALLOW_VOICE": 0x10000000,
        #Removes the ability from parcel owners to set their parcels to show in search.
        "REGION_FLAGS_BLOCK_PARCEL_SEARCH": 0x20000000,
        #Denys agents who have not been age verified from entering the region.
        "REGION_FLAGS_DENY_AGEUNVERIFIED": 0x40000000,

        #OpenMetaverse/AgentManager.cs
        #Placeholder for empty values, shouldn't ever see this
        "PERMISSION_NONE": 0,
        #Script wants ability to take money from you
        "PERMISSION_DEBIT": 1,
        #Script wants to take camera controls for you
        "PERMISSION_TAKECONTROLS": 2,
        #Script wants to remap avatars controls
        "PERMISSION_REMAPCONTROLS": 4,
        #Script wants to trigger avatar animations
        "PERMISSION_TRIGGERANIMATION": 8,
        #Script wants to attach or detach the prim or primset to your avatar
        "PERMISSION_ATTACH": 16,
        #Script wants permission to release ownership
        "PERMISSION_RELEASEOWNERSHIP": 32,
        #Script wants ability to link/delink with other prims
        "PERMISSION_CHANGELINKS": 64,
        #Script wants permission to change joints
        "PERMISSION_CHANGEJOINTS": 128,
        #Script wants permissions to change permissions
        "PERMISSION_CHANGEPERMISSIONS": 256,
        #Script wants to track avatars camera position and rotation 
        "PERMISSION_TRACKCAMERA": 512,
        #Script wants to control your camera
        "PERMISSION_CONTROLCAMERA": 1024,
        #Script wants the ability to teleport you
        "PERMISSION_TELEPORT": 4096,

        #Indicates a regular IM from another agent
        "IM_MESSAGEFROMAGENT": 0,
        #Simple notification box with an OK button
        "IM_MESSAGEBOX": 1,
        #Used to show a countdown notification with an OK button, deprecated now
        "IM_MESSAGEBOXCOUNTDOWN": 2,
        #You've been invited to join a group.
        "IM_GROUPINVITATION": 3,
        #Inventory offer
        "IM_INVENTORYOFFERED": 4,
        #Accepted inventory offer
        "IM_INVENTORYACCEPTED": 5,
        #Declined inventory offer
        "IM_INVENTORYDECLINED": 6,
        #Group vote
        "IM_GROUPVOTE": 7,
        #A message to everyone in the agent's group, no longer used
        "IM_DEPRECATEDGROUPMESSAGE": 8,
        #An object is offering its inventory
        "IM_TASKINVENTORYOFFERED": 9,
        #Accept an inventory offer from an object
        "IM_TASKINVENTORYACCEPTED": 10,
        #Decline an inventory offer from an object
        "IM_TASKINVENTORYDECLINED": 11,
        #Unknown
        "IM_NEWUSERDEFAULT": 12,
        #Start a session, or add users to a session
        "IM_SESSIONADD": 13,
        #Start a session, but don't prune offline users
        "IM_SESSIONOFFLINEADD": 14,
        #Start a session with your group
        "IM_SESSIONGROUPSTART": 15,
        #Start a session without a calling card (finder or objects)
        "IM_SESSIONCARDLESSSTART": 16,
        #Send a message to a session
        "IM_SESSIONSEND": 17,
        #Leave a session
        "IM_SESSIONDROP": 18,
        #Indicates that the IM is from an object
        "IM_MESSAGEFROMOBJECT": 19,
        #Sent an IM to a busy user, this is the auto response
        "IM_BUSYAUTORESPONSE": 20,
        #Shows the message in the console and chat history
        "IM_CONSOLEANDCHATHISTORY": 21,
        #Send a teleport lure
        "IM_REQUESTTELEPORT": 22,
        #Response sent to the agent which inititiated a teleport invitation
        "IM_ACCEPTTELEPORT": 23,
        #Response sent to the agent which inititiated a teleport invitation
        "IM_DENYTELEPORT": 24,
        #Only useful if you have Linden permissions
        "IM_GODLIKEREQUESTTELEPORT": 25,
        #Request a teleport lure
        "IM_REQUESTLURE": 26,
        #Notification of a new group election, this is deprecated
        "IM_DEPRECATEDGROUPELECTION": 27,
        #IM to tell the user to go to an URL
        "IM_GOTOURL": 28,
        #IM for help
        "IM_SESSION911START": 29,
        #IM sent automatically on call for help, sends a lure to each
        #Helper reached
        "IM_LURE911": 30,
        #Like an IM but won't go to email
        "IM_FROMTASKASALERT": 31,
        #IM from a group officer to all group members
        "IM_GROUPNOTICE": 32,
        #Unknown
        "IM_GROUPNOTICEINVENTORYACCEPTED": 33,
        #Unknown
        "IM_GROUPNOTICEINVENTORYDECLINED": 34,
        #Accept a group invitation
        "IM_GROUPINVITATIONACCEPT": 35,
        #Decline a group invitation
        "IM_GROUPINVITATIONDECLINE": 36,
        #Unknown
        "IM_GROUPNOTICEREQUESTED": 37,
        #An avatar is offering you friendship
        "IM_FRIENDSHIPOFFERED": 38,
        #An avatar has accepted your friendship offer
        "IM_FRIENDSHIPACCEPTED": 39,
        #An avatar has declined your friendship offer
        "IM_FRIENDSHIPDECLINED": 40,
        #Indicates that a user has started typing
        "IM_STARTTYPING": 41,
        #Indicates that a user has stopped typing
        "IM_STOPTYPING": 42,
        #Only deliver to online avatars
        "IM_ONLINE": 0,
        #If the avatar is offline the message will be held until they login next
        "IM_OFFLINE": 1,

        #Whisper (5m radius)
        "CHAT_WHISPER": 0,
        #Normal chat (10/20m radius), what the official viewer typically sends
        "CHAT_NORMAL": 1,
        #Shouting! (100m radius)
        "CHAT_SHOUT": 2,
        #Say chat (10/20m radius) - The official viewer will print
        #"[4:15] You say, hey" instead of "[4:15] You: hey"
        "CHAT_SAY": 3,
        #Event message when an Avatar has begun to type
        "CHAT_TYPING_START": 4,
        #Event message when an Avatar has stopped typing
        "CHAT_TYPING_STOP": 5,
        #Send the message to the debug channel
        "CHAT_DEBUG": 6,
        #Event message when an object uses llOwnerSay
        "CHAT_OWNER_SAY": 8,
        #Event message when an object uses llRegionSayTo
        "CHAT_REGION_SAY_TO": 9,
        #Special value to support llRegionSay, never sent to the client
        "CHAT_REGION_SAY": 255,

        #ChatSourceType
        #Chat from the grid or simulator
        "CHAT_SOURCE_SYSTEM": 0,
        #Chat from another avatar
        "CHAT_SOURCE_AVATAR": 1,
        #Chat from an object
        "CHAT_SOURCE_OBJECT": 2,

        "CHAT_AUDIBLE_NOT": -1,
        "CHAT_AUDIBLE_BARELY": 0,
        "CHAT_AUDIBLE_FULLY": 1,

        #ViewerEffect
        "VIEWER_EFFECT_TEXT": 0,
        "VIEWER_EFFECT_ICON": 1,
        "VIEWER_EFFECT_CONNECTOR": 2,
        "VIEWER_EFFECT_FLEXIBLEOBJECT": 3,
        "VIEWER_EFFECT_ANIMALCONTROLS": 4,
        "VIEWER_EFFECT_ANIMATIONOBJECT": 5,
        "VIEWER_EFFECT_CLOTH": 6,
        #Project a beam from a source to a destination
        "VIEWER_EFFECT_BEAM": 7,
        "VIEWER_EFFECT_GLOW": 8,
        "VIEWER_EFFECT_POINT": 9,
        "VIEWER_EFFECT_TRAIL": 10,
        #Create a swirl of particles around an object
        "VIEWER_EFFECT_SPHERE": 11,
        "VIEWER_EFFECT_SPIRAL": 12,
        "VIEWER_EFFECT_EDIT": 13,
        #Cause an avatar to look at an object
        "VIEWER_EFFECT_LOOKAT": 14,
        #Cause an avatar to point at an object
        "VIEWER_EFFECT_POINTAT": 15,

        "LOOK_AT_TYPE_NONE": 0,
        "LOOK_AT_TYPE_IDLE": 1,
        "LOOK_AT_TYPE_AUTOLISTEN": 2,
        "LOOK_AT_TYPE_FREELOOK": 3,
        "LOOK_AT_TYPE_RESPOND": 4,
        "LOOK_AT_TYPE_HOVER": 5,
        "LOOK_AT_TYPE_CONVERSATION": 6,
        "LOOK_AT_TYPE_SELECT": 7,
        "LOOK_AT_TYPE_FOCUS": 8,
        "LOOK_AT_TYPE_MOUSELOOK": 9,
        "LOOK_AT_TYPE_CLEAR": 10,
        "POINT_AT_TYPE_NONE": 0,
        "POINT_AT_TYPE_SELECT": 1,
        "POINT_AT_TYPE_GRAB": 2,
        "POINT_AT_TYPE_CLEAR": 3,

        "TRANSACTION_NONE": 0,
        "TRANSACTION_FAILSIMULATORTIMEOUT": 1,
        "TRANSACTION_FAILDATASERVERTIMEOUT": 2,
        "TRANSACTION_OBJECTCLAIM": 1000,
        "TRANSACTION_LANDCLAIM": 1001,
        "TRANSACTION_GROUPCREATE": 1002,
        "TRANSACTION_OBJECTPUBLICCLAIM": 1003,
        "TRANSACTION_GROUPJOIN": 1004,
        "TRANSACTION_TELEPORTCHARGE": 1100,
        "TRANSACTION_UPLOADCHARGE": 1101,
        "TRANSACTION_LANDAUCTION": 1102,
        "TRANSACTION_CLASSIFIEDCHARGE": 1103,
        "TRANSACTION_OBJECTTAX": 2000,
        "TRANSACTION_LANDTAX": 2001,
        "TRANSACTION_LIGHTTAX": 2002,
        "TRANSACTION_PARCELDIRFEE": 2003,
        "TRANSACTION_GROUPTAX": 2004,
        "TRANSACTION_CLASSIFIEDRENEW": 2005,
        "TRANSACTION_GIVEINVENTORY": 3000,
        "TRANSACTION_OBJECTSALE": 5000,
        "TRANSACTION_GIFT": 5001,
        "TRANSACTION_LANDSALE": 5002,
        "TRANSACTION_REFERBONUS": 5003,
        "TRANSACTION_INVENTORYSALE": 5004,
        "TRANSACTION_REFUNDPURCHASE": 5005,
        "TRANSACTION_LANDPASSSALE": 5006,
        "TRANSACTION_DWELLBONUS": 5007,
        "TRANSACTION_PAYOBJECT": 5008,
        "TRANSACTION_OBJECTPAYS": 5009,
        "TRANSACTION_GROUPLANDDEED": 6001,
        "TRANSACTION_GROUPOBJECTDEED": 6002,
        "TRANSACTION_GROUPLIABILITY": 6003,
        "TRANSACTION_GROUPDIVIDEND": 6004,
        "TRANSACTION_GROUPMEMBERSHIPDUES": 6005,
        "TRANSACTION_OBJECTRELEASE": 8000,
        "TRANSACTION_LANDRELEASE": 8001,
        "TRANSACTION_OBJECTDELETE": 8002,
        "TRANSACTION_OBJECTPUBLICDECAY": 8003,
        "TRANSACTION_OBJECTPUBLICDELETE": 8004,
        "TRANSACTION_LINDENADJUSTMENT": 9000,
        "TRANSACTION_LINDENGRANT": 9001,
        "TRANSACTION_LINDENPENALTY": 9002,
        "TRANSACTION_EVENTFEE": 9003,
        "TRANSACTION_EVENTPRIZE": 9004,
        "TRANSACTION_STIPENDBASIC": 10000,
        "TRANSACTION_STIPENDDEVELOPER": 10001,
        "TRANSACTION_STIPENDALWAYS": 10002,
        "TRANSACTION_STIPENDDAILY": 10003,
        "TRANSACTION_STIPENDRATING": 10004,
        "TRANSACTION_STIPENDDELTA": 10005,

        "TRANSACTION_FLAGS_NONE": 0,
        "TRANSACTION_FLAGS_SOURCEGROUP": 1,
        "TRANSACTION_FLAGS_DESTGROUP": 2,
        "TRANSACTION_FLAGS_OWNERGROUP": 4,
        "TRANSACTION_FLAGS_SIMULTANEOUSCONTRIBUTION": 8,
        "TRANSACTION_FLAGS_CONTRIBUTIONREMOVAL": 16,

        "COLLISION_NONE": 0,
        "COLLISION_BUMP": 1,
        "COLLISION_LLPUSHOBJECT": 2,
        "COLLISION_SELECTEDOBJECTCOLLIDE": 3,
        "COLLISION_SCRIPTEDOBJECTCOLLIDE": 4,
        "COLLISION_PHYSICALOBJECTCOLLIDE": 5,

        #Unknown status
        "TELEPORT_NONE": 0,
        #Teleport initialized
        "TELEPORT_START": 1,
        #Teleport in progress
        "TELEPORT_PROGRESS": 2,
        #Teleport failed
        "TELEPORT_FAILED": 3,
        #Teleport completed
        "TELEPORT_FINISHED": 4,
        #Teleport cancelled
        "TELEPORT_CANCELLED": 5,

        #No flags set or teleport failed
        "TELEPORT_FLAG_DEFAULT": 0,
        #Set when newbie leaves help island for first time
        "TELEPORT_FLAG_SETHOMETOTARGET": 1,
        "TELEPORT_FLAG_SETLASTTOTARGET": 2,
        #Via Lure
        "TELEPORT_FLAG_VIALURE": 4,
        #Via Landmark
        "TELEPORT_FLAG_VIALANDMARK": 8,
        #Via Location
        "TELEPORT_FLAG_VIALOCATION": 16,
        #Via Home
        "TELEPORT_FLAG_VIAHOME": 32,
        #Via Telehub
        "TELEPORT_FLAG_VIATELEHUB": 64,
        #Via Login
        "TELEPORT_FLAG_VIALOGIN": 128,
        #Linden Summoned
        "TELEPORT_FLAG_VIAGODLIKELURE": 256,
        #Linden Forced me
        "TELEPORT_FLAG_GODLIKE": 512,
        "TELEPORT_FLAG_NINEONEONE": 1024,
        #Agent Teleported Home via Script
        "TELEPORT_FLAG_DISABLECANCEL": 2048,
        "TELEPORT_FLAG_VIAREGIONID": 4096,
        "TELEPORT_FLAG_ISFLYING": 8192,
        "TELEPORT_FLAG_RESETHOME": 16384,
        #forced to new location for example when avatar is banned or ejected
        "TELEPORT_FLAG_FORCEREDIRECT": 32768,
        #Teleport Finished via a Lure
        "TELEPORT_FLAG_FINISHEDVIALURE": 67108864,
        #Finished Sim Changed
        "TELEPORT_FLAG_FINISHEDVIANEWSIM": 268435456,
        #Finished Same Sim
        "TELEPORT_FLAG_FINISHEDVIASAMESIM": 536870912,

        "TELEPORT_LURE_FLAG_NORMALLURE": 0,
        "TELEPORT_LURE_FLAG_GODLIKELURE": 1,
        "TELEPORT_LURE_FLAG_GODLIKEPURSUIT": 2,

        #Object muted by name
        "MUTE_TYPE_BYNAME": 0,
        #Muted residet
        "MUTE_TYPE_RESIDENT": 1,
        #Object muted by UUID
        "MUTE_TYPE_OBJECT": 2,
        #Muted group
        "MUTE_TYPE_GROUP": 3,
        #Muted external entry
        "MUTE_TYPE_EXTERNAL": 4,

        #No exceptions
        "MUTE_FLAG_DEFAULT": 0x0,
        #Don't mute text chat
        "MUTE_FLAG_TEXTCHAT": 0x1,
        #Don't mute voice chat
        "MUTE_FLAG_VOICECHAT": 0x2,
        #Don't mute particles
        "MUTE_FLAG_PARTICLES": 0x4,
        #Don't mute sounds
        "MUTE_FLAG_OBJECTSOUNDS": 0x8,
        #Don't mute
        "MUTE_FLAG_ALL": 0xF,

        #http://wiki.secondlife.com/wiki/AgentUpdate
        #The agent is currently playing the typing animation or typing is
        #occurring.
        "AGENT_STATE_TYPING": 0x04,
        #Agent has the tools window open and objects are selected.
        "AGENT_STATE_EDITING": 0x10,
        "AU_FLAGS_NONE": 0x00, #No flags at all.
        "AU_FLAGS_HIDETITLE": 0x01,

        #Stolen from http://lib.openmetaverse.co/wiki/AgentUpdate

        #Keyboard input: AGENT_CONTROL_AT/LEFT/UP flags always 
        #OR'd with corresponding AGENT_CONTROL_FAST_AT/LEFT/UP
        #Flags are only used without AGENT_CONTROL_FAST_* combination during
        #autopilot
        #Move Forward (Keybinding: W/Up Arrow)
        "AGENT_CONTROL_AT_POS": 1,
        #Move Backward (Keybinding: S/Down Arrow)
        "AGENT_CONTROL_AT_NEG": 2,
        #Move Left (Keybinding: Shift-(A/Left Arrow))
        "AGENT_CONTROL_LEFT_POS": 4,
        #Move Right (Keybinding: Shift-(D/Right Arrow))
        "AGENT_CONTROL_LEFT_NEG": 8,
        #Not Flying: Jump/Flying: Move Up (Keybinding: E)
        "AGENT_CONTROL_UP_POS": 16,
        #Not Flying: Croutch/Flying: Move Down (Keybinding: C)
        "AGENT_CONTROL_UP_NEG": 32,

        #Not used
        "AGENT_CONTROL_PITCH_POS": 64,
        "AGENT_CONTROL_PITCH_NEG": 128,
        "AGENT_CONTROL_YAW_POS": 256,
        "AGENT_CONTROL_YAW_NEG": 512,

        #These flags are always OR'd with the AGENT_CONTROL_AT/LEFT/UP
        #flags if the keyboard is being used.
        "AGENT_CONTROL_FAST_AT": 1024,
        "AGENT_CONTROL_FAST_LEFT": 2048,
        "AGENT_CONTROL_FAST_UP": 4096,

        "AGENT_CONTROL_FLY": 8192,
        "AGENT_CONTROL_STOP": 16384,
        "AGENT_CONTROL_FINISH_ANIM": 32768,
        "AGENT_CONTROL_STAND_UP": 65536,
        "AGENT_CONTROL_SIT_ON_GROUND": 131072,
        "AGENT_CONTROL_MOUSELOOK": 262144,

        #Nudge is a legacy flag that was used if a key was pressed for less than
        #a certain amount of time. Can be ignored.
        "AGENT_CONTROL_NUDGE_AT_POS": 524288,
        "AGENT_CONTROL_NUDGE_AT_NEG": 1048576,
        "AGENT_CONTROL_NUDGE_LEFT_POS": 2097152,
        "AGENT_CONTROL_NUDGE_LEFT_NEG": 4194304,
        "AGENT_CONTROL_NUDGE_UP_POS": 8388608,
        "AGENT_CONTROL_NUDGE_UP_NEG": 16777216,
        "AGENT_CONTROL_TURN_LEFT": 33554432,
        "AGENT_CONTROL_TURN_RIGHT": 67108864,

        #Set when Agent had idled/set away.
        #Cleared on most actions involving the viewer window.
        #Note that away animation is activated separately from setting this flag
        "AGENT_CONTROL_AWAY": 134217728,
                                        
        "AGENT_CONTROL_LBUTTON_DOWN": 268435456,
        "AGENT_CONTROL_LBUTTON_UP": 536870912,
        "AGENT_CONTROL_ML_LBUTTON_DOWN": 1073741824,
        "AGENT_CONTROL_ML_LBUTTON_UP": 2147483648,

        #AGENT_CONTROL_AT_POS | AGENT_CONTROL_AT_NEG
        #| AGENT_CONTROL_NUDGE_AT_POS | AGENT_CONTROL_NUDGE_AT_NEG                          
        "AGENT_CONTROL_AT": 1572867,

        #AGENT_CONTROL_LEFT_POS | AGENT_CONTROL_LEFT_NEG
        #| AGENT_CONTROL_NUDGE_LEFT_POS | AGENT_CONTROL_NUDGE_LEFT_NEG
        "AGENT_CONTROL_LEFT": 6291468,

        #AGENT_CONTROL_UP_POS | AGENT_CONTROL_UP_NEG
        #| AGENT_CONTROL_NUDGE_UP_POS | AGENT_CONTROL_NUDGE_UP_NEG
        "AGENT_CONTROL_UP": 25165872,

        #AGENT_CONTROL_AT | AGENT_CONTROL_LEFT
        "AGENT_CONTROL_HORIZONTAL": 7864335,

        #AGENT_CONTROL_FLY | AGENT_CONTROL_STOP | AGENT_CONTROL_FINISH_ANIM
        #| AGENT_CONTROL_STAND_UP | AGENT_CONTROL_SIT_ON_GROUND
        #| AGENT_CONTROL_MOUSELOOK | AGENT_CONTROL_AWAY
        "AGENT_CONTROL_NOT_USED_BY_LSL": 134733824,

        #| AGENT_CONTROL_AT | AGENT_CONTROL_LEFT | AGENT_CONTROL_UP
        "AGENT_CONTROL_MOVEMENT": 33030207,

        #AGENT_CONTROL_PITCH_POS | AGENT_CONTROL_PITCH_NEG
        #| AGENT_CONTROL_YAW_POS | AGENT_CONTROL_YAW_NEG
        "AGENT_CONTROL_ROTATION": 960,

        #AGENT_CONTROL_NUDGE_AT_POS | AGENT_CONTROL_NUDGE_AT_NEG
        #| AGENT_CONTROL_NUDGE_LEFT_POS | AGENT_CONTROL_NUDGE_LEFT_NEG
        "AGENT_CONTROL_NUDGE": 7864320
    }
    def __init__(self):
        for const in self.constraints:
            setattr(self, const, self.constraints[const])
