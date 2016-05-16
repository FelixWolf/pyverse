#!/usr/bin/env python3
from ..constraints import constraints
const = constraints()

class simMonitor:
    timeDilation   = 0
    FPS    = 0
    physFPS    = 0
    agentUpdates   = 0
    frameMS    = 0
    netMS  = 0
    otherMS    = 0
    physicsMS  = 0
    agentMS    = 0
    imagesMS   = 0
    scriptMS   = 0
    tasks  = 0
    tasksActive    = 0
    agentsMain = 0
    agentsChild    = 0
    scriptsActive  = 0
    LSLIPS = 0
    packetsIn  = 0
    packetsOut = 0
    pendingDownloads   = 0
    pendingUploads = 0
    pendingLocalUploads    = 0    
    totalUnackedBytes  = 0
    physicsPinnedTasks = 0
    physicsLODTasks    = 0
    simPhysicsStepMS   = 0
    simPhysicsShapeMS  = 0
    simPhysicsOtherMS  = 0
    simPhysicsMemory   = 0
    
    def __init__(self):
        pass
    
    def update(self, stats):
        for stat in stats:
            name = "None"
            if stat["StatID"] == const.LL_SIM_STAT_TIME_DILATION:
                name = "timeDilation"
            elif stat["StatID"] == const.LL_SIM_STAT_FPS:
                name = "FPS"
            elif stat["StatID"] == const.LL_SIM_STAT_PHYSFPS:
                name = "physFPS"
            elif stat["StatID"] == const.LL_SIM_STAT_AGENTUPS:
                name = "agentUpdates"
            elif stat["StatID"] == const.LL_SIM_STAT_FRAMEMS:
                name = "frameMS"
            elif stat["StatID"] == const.LL_SIM_STAT_NETMS:
                name = "netMS"
            elif stat["StatID"] == const.LL_SIM_STAT_SIMOTHERMS:
                name = "otherMS"
            elif stat["StatID"] == const.LL_SIM_STAT_SIMPHYSICSMS:
                name = "physicsMS"
            elif stat["StatID"] == const.LL_SIM_STAT_AGENTMS:
                name = "agentMS"
            elif stat["StatID"] == const.LL_SIM_STAT_IMAGESMS:
                name = "imagesMS"
            elif stat["StatID"] == const.LL_SIM_STAT_SCRIPTMS:
                name = "scriptMS"
            elif stat["StatID"] == const.LL_SIM_STAT_NUMTASKS:
                name = "tasks"
            elif stat["StatID"] == const.LL_SIM_STAT_NUMTASKSACTIVE:
                name = "tasksActive"
            elif stat["StatID"] == const.LL_SIM_STAT_NUMAGENTMAIN:
                name = "agentsMain"
            elif stat["StatID"] == const.LL_SIM_STAT_NUMAGENTCHILD:
                name = "agentsChild"
            elif stat["StatID"] == const.LL_SIM_STAT_NUMSCRIPTSACTIVE:
                name = "scriptsActive"
            elif stat["StatID"] == const.LL_SIM_STAT_LSLIPS:
                name = "LSLIPS"
            elif stat["StatID"] == const.LL_SIM_STAT_INPPS:
                name = "packetsIn"
            elif stat["StatID"] == const.LL_SIM_STAT_OUTPPS:
                name = "packetsOut"
            elif stat["StatID"] == const.LL_SIM_STAT_PENDING_DOWNLOADS:
                name = "pendingDownloads"
            elif stat["StatID"] == const.LL_SIM_STAT_PENDING_UPLOADS:
                name = "pendingUploads"
            elif stat["StatID"] == const.LL_SIM_STAT_PENDING_LOCAL_UPLOADS:
                name = "pendingLocalUploads"
            elif stat["StatID"] == const.LL_SIM_STAT_TOTAL_UNACKED_BYTES:
                name = "TotalUnackedBytes"
            elif stat["StatID"] == const.LL_SIM_STAT_PHYSICS_PINNED_TASKS:
                name = "physicsPinnedTasks"
            elif stat["StatID"] == const.LL_SIM_STAT_PHYSICS_LOD_TASKS:
                name = "physicsLODTasks"
            elif stat["StatID"] == const.LL_SIM_STAT_SIMPHYSICSSTEPMS:
                name = "simPhysicsStepMS"
            elif stat["StatID"] == const.LL_SIM_STAT_SIMPHYSICSSHAPEMS:
                name = "simPhysicsShapeMS"
            elif stat["StatID"] == const.LL_SIM_STAT_SIMPHYSICSOTHERMS:
                name = "simPhysicsOtherMS"
            elif stat["StatID"] == const.LL_SIM_STAT_SIMPHYSICSMEMORY:
                name = "simPhysicsMemory"
            setattr(self, name, stat["StatValue"])
