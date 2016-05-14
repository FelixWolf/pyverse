from . import message
message_lookup = {}
def registerMessage(name, msg):
    freq = 0
    mid = 0
    if msg.freq == 3:
        mid = mid + 0xFFFFFF00
    elif msg.freq == 2:
        mid = mid + 0xFFFF0000
    elif msg.freq == 1:
        mid = mid + 0xFF00
    message_lookup[mid] = msg
    message_lookup[name.lower()] = msg

def getMessageByID(key, data = None):
    if key in message_lookup:
        return message_lookup[key](data)
    else:
        return None

def getMessageByName(key, data = None):
    key = key.lower()
    if key in message_lookup:
        return message_lookup[key](data)
    else:
        return None
        
class TestMessage(message.baseMessage):
    id = 1
    freq = 2
    trusted = False
    zero_coded = True
    blocks = [
        ("TestBlock1", 1),
        ("NeighborBlock", 4)
    ]
    structure = {
        "TestBlock1": [
            ["Test1", "U32"]
        ],
        "NeighborBlock": [
            ["Test0", "U32"],
            ["Test1", "U32"],
            ["Test2", "U32"]
        ]
    }
registerMessage("TestMessage", TestMessage)

class PacketAck(message.baseMessage):
    id = 17
    freq = 3
    trusted = False
    zero_coded = False
    blocks = [
        ("Packets", 0)
    ]
    structure = {
        "Packets": [
            ["ID", "U32"]
        ]
    }
registerMessage("PacketAck", PacketAck)

class OpenCircuit(message.baseMessage):
    id = 17
    freq = 3
    trusted = False
    zero_coded = False
    blocks = [
        ("CircuitInfo", 1)
    ]
    structure = {
        "CircuitInfo": [
            ["IP", "IPADDR"],
            ["Port", "IPPORT"]
        ]
    }
registerMessage("OpenCircuit", OpenCircuit)

class CloseCircuit(message.baseMessage):
    id = 17
    freq = 3
    trusted = False
    zero_coded = False
    blocks = [

    ]
    structure = {

    }
registerMessage("CloseCircuit", CloseCircuit)

class StartPingCheck(message.baseMessage):
    id = 1
    freq = 0
    trusted = False
    zero_coded = False
    blocks = [
        ("PingID", 1)
    ]
    structure = {
        "PingID": [
            ["PingID", "U8"],
            ["OldestUnacked", "U32"]
        ]
    }
registerMessage("StartPingCheck", StartPingCheck)

class CompletePingCheck(message.baseMessage):
    id = 2
    freq = 0
    trusted = False
    zero_coded = False
    blocks = [
        ("PingID", 1)
    ]
    structure = {
        "PingID": [
            ["PingID", "U8"]
        ]
    }
registerMessage("CompletePingCheck", CompletePingCheck)

class AddCircuitCode(message.baseMessage):
    id = 2
    freq = 2
    trusted = True
    zero_coded = False
    blocks = [
        ("CircuitCode", 1)
    ]
    structure = {
        "CircuitCode": [
            ["Code", "U32"],
            ["SessionID", "LLUUID"],
            ["AgentID", "LLUUID"]
        ]
    }
registerMessage("AddCircuitCode", AddCircuitCode)

class UseCircuitCode(message.baseMessage):
    id = 3
    freq = 2
    trusted = False
    zero_coded = False
    blocks = [
        ("CircuitCode", 1)
    ]
    structure = {
        "CircuitCode": [
            ["Code", "U32"],
            ["SessionID", "LLUUID"],
            ["ID", "LLUUID"]
        ]
    }
registerMessage("UseCircuitCode", UseCircuitCode)

class NeighborList(message.baseMessage):
    id = 3
    freq = 0
    trusted = True
    zero_coded = False
    blocks = [
        ("NeighborBlock", 4)
    ]
    structure = {
        "NeighborBlock": [
            ["IP", "IPADDR"],
            ["Port", "IPPORT"],
            ["PublicIP", "IPADDR"],
            ["PublicPort", "IPPORT"],
            ["RegionID", "LLUUID"],
            ["Name", "Variable1"],
            ["SimAccess", "U8"]
        ]
    }
registerMessage("NeighborList", NeighborList)

class AvatarTextureUpdate(message.baseMessage):
    id = 4
    freq = 2
    trusted = True
    zero_coded = True
    blocks = [
        ("AgentData", 1),
        ("WearableData", 0),
        ("TextureData", 0)
    ]
    structure = {
        "AgentData": [
            ["AgentID", "LLUUID"],
            ["TexturesChanged", "BOOL"]
        ],
        "WearableData": [
            ["CacheID", "LLUUID"],
            ["TextureIndex", "U8"],
            ["HostName", "Variable1"]
        ],
        "TextureData": [
            ["TextureID", "LLUUID"]
        ]
    }
registerMessage("AvatarTextureUpdate", AvatarTextureUpdate)

class SimulatorMapUpdate(message.baseMessage):
    id = 5
    freq = 2
    trusted = True
    zero_coded = False
    blocks = [
        ("MapData", 1)
    ]
    structure = {
        "MapData": [
            ["Flags", "U32"]
        ]
    }
registerMessage("SimulatorMapUpdate", SimulatorMapUpdate)

class SimulatorSetMap(message.baseMessage):
    id = 6
    freq = 2
    trusted = True
    zero_coded = False
    blocks = [
        ("MapData", 1)
    ]
    structure = {
        "MapData": [
            ["RegionHandle", "U64"],
            ["Type", "S32"],
            ["MapImage", "LLUUID"]
        ]
    }
registerMessage("SimulatorSetMap", SimulatorSetMap)

class SubscribeLoad(message.baseMessage):
    id = 7
    freq = 2
    trusted = True
    zero_coded = False
    blocks = [

    ]
    structure = {

    }
registerMessage("SubscribeLoad", SubscribeLoad)

class UnsubscribeLoad(message.baseMessage):
    id = 8
    freq = 2
    trusted = True
    zero_coded = False
    blocks = [

    ]
    structure = {

    }
registerMessage("UnsubscribeLoad", UnsubscribeLoad)

class SimulatorReady(message.baseMessage):
    id = 9
    freq = 2
    trusted = True
    zero_coded = True
    blocks = [
        ("SimulatorBlock", 1),
        ("TelehubBlock", 1)
    ]
    structure = {
        "SimulatorBlock": [
            ["SimName", "Variable1"],
            ["SimAccess", "U8"],
            ["RegionFlags", "U32"],
            ["RegionID", "LLUUID"],
            ["EstateID", "U32"],
            ["ParentEstateID", "U32"]
        ],
        "TelehubBlock": [
            ["HasTelehub", "BOOL"],
            ["TelehubPos", "LLVector3"]
        ]
    }
registerMessage("SimulatorReady", SimulatorReady)

class TelehubInfo(message.baseMessage):
    id = 10
    freq = 2
    trusted = True
    zero_coded = False
    blocks = [
        ("TelehubBlock", 1),
        ("SpawnPointBlock", 0)
    ]
    structure = {
        "TelehubBlock": [
            ["ObjectID", "LLUUID"],
            ["ObjectName", "Variable1"],
            ["TelehubPos", "LLVector3"],
            ["TelehubRot", "LLQuaternion"]
        ],
        "SpawnPointBlock": [
            ["SpawnPointPos", "LLVector3"]
        ]
    }
registerMessage("TelehubInfo", TelehubInfo)

class SimulatorPresentAtLocation(message.baseMessage):
    id = 11
    freq = 2
    trusted = True
    zero_coded = False
    blocks = [
        ("SimulatorPublicHostBlock", 1),
        ("NeighborBlock", 4),
        ("SimulatorBlock", 1),
        ("TelehubBlock", 0)
    ]
    structure = {
        "SimulatorPublicHostBlock": [
            ["Port", "IPPORT"],
            ["SimulatorIP", "IPADDR"],
            ["GridX", "U32"],
            ["GridY", "U32"]
        ],
        "NeighborBlock": [
            ["IP", "IPADDR"],
            ["Port", "IPPORT"]
        ],
        "SimulatorBlock": [
            ["SimName", "Variable1"],
            ["SimAccess", "U8"],
            ["RegionFlags", "U32"],
            ["RegionID", "LLUUID"],
            ["EstateID", "U32"],
            ["ParentEstateID", "U32"]
        ],
        "TelehubBlock": [
            ["HasTelehub", "BOOL"],
            ["TelehubPos", "LLVector3"]
        ]
    }
registerMessage("SimulatorPresentAtLocation", SimulatorPresentAtLocation)

class SimulatorLoad(message.baseMessage):
    id = 12
    freq = 2
    trusted = True
    zero_coded = False
    blocks = [
        ("SimulatorLoad", 1),
        ("AgentList", 0)
    ]
    structure = {
        "SimulatorLoad": [
            ["TimeDilation", "F32"],
            ["AgentCount", "S32"],
            ["CanAcceptAgents", "BOOL"]
        ],
        "AgentList": [
            ["CircuitCode", "U32"],
            ["X", "U8"],
            ["Y", "U8"]
        ]
    }
registerMessage("SimulatorLoad", SimulatorLoad)

class SimulatorShutdownRequest(message.baseMessage):
    id = 13
    freq = 2
    trusted = True
    zero_coded = False
    blocks = [

    ]
    structure = {

    }
registerMessage("SimulatorShutdownRequest", SimulatorShutdownRequest)

class RegionPresenceRequestByRegionID(message.baseMessage):
    id = 14
    freq = 2
    trusted = True
    zero_coded = False
    blocks = [
        ("RegionData", 0)
    ]
    structure = {
        "RegionData": [
            ["RegionID", "LLUUID"]
        ]
    }
registerMessage("RegionPresenceRequestByRegionID", RegionPresenceRequestByRegionID)

class RegionPresenceRequestByHandle(message.baseMessage):
    id = 15
    freq = 2
    trusted = True
    zero_coded = False
    blocks = [
        ("RegionData", 0)
    ]
    structure = {
        "RegionData": [
            ["RegionHandle", "U64"]
        ]
    }
registerMessage("RegionPresenceRequestByHandle", RegionPresenceRequestByHandle)

class RegionPresenceResponse(message.baseMessage):
    id = 16
    freq = 2
    trusted = True
    zero_coded = True
    blocks = [
        ("RegionData", 0)
    ]
    structure = {
        "RegionData": [
            ["RegionID", "LLUUID"],
            ["RegionHandle", "U64"],
            ["InternalRegionIP", "IPADDR"],
            ["ExternalRegionIP", "IPADDR"],
            ["RegionPort", "IPPORT"],
            ["ValidUntil", "F64"],
            ["Message", "Variable1"]
        ]
    }
registerMessage("RegionPresenceResponse", RegionPresenceResponse)

class UpdateSimulator(message.baseMessage):
    id = 17
    freq = 2
    trusted = True
    zero_coded = False
    blocks = [
        ("SimulatorInfo", 1)
    ]
    structure = {
        "SimulatorInfo": [
            ["RegionID", "LLUUID"],
            ["SimName", "Variable1"],
            ["EstateID", "U32"],
            ["SimAccess", "U8"]
        ]
    }
registerMessage("UpdateSimulator", UpdateSimulator)

class LogDwellTime(message.baseMessage):
    id = 18
    freq = 2
    trusted = True
    zero_coded = False
    blocks = [
        ("DwellInfo", 1)
    ]
    structure = {
        "DwellInfo": [
            ["AgentID", "LLUUID"],
            ["SessionID", "LLUUID"],
            ["Duration", "F32"],
            ["SimName", "Variable1"],
            ["RegionX", "U32"],
            ["RegionY", "U32"],
            ["AvgAgentsInView", "U8"],
            ["AvgViewerFPS", "U8"]
        ]
    }
registerMessage("LogDwellTime", LogDwellTime)

class FeatureDisabled(message.baseMessage):
    id = 19
    freq = 2
    trusted = True
    zero_coded = False
    blocks = [
        ("FailureInfo", 1)
    ]
    structure = {
        "FailureInfo": [
            ["ErrorMessage", "Variable1"],
            ["AgentID", "LLUUID"],
            ["TransactionID", "LLUUID"]
        ]
    }
registerMessage("FeatureDisabled", FeatureDisabled)

class LogFailedMoneyTransaction(message.baseMessage):
    id = 20
    freq = 2
    trusted = True
    zero_coded = False
    blocks = [
        ("TransactionData", 1)
    ]
    structure = {
        "TransactionData": [
            ["TransactionID", "LLUUID"],
            ["TransactionTime", "U32"],
            ["TransactionType", "S32"],
            ["SourceID", "LLUUID"],
            ["DestID", "LLUUID"],
            ["Flags", "U8"],
            ["Amount", "S32"],
            ["SimulatorIP", "IPADDR"],
            ["GridX", "U32"],
            ["GridY", "U32"],
            ["FailureType", "U8"]
        ]
    }
registerMessage("LogFailedMoneyTransaction", LogFailedMoneyTransaction)

class UserReportInternal(message.baseMessage):
    id = 21
    freq = 2
    trusted = True
    zero_coded = True
    blocks = [
        ("ReportData", 1)
    ]
    structure = {
        "ReportData": [
            ["ReportType", "U8"],
            ["Category", "U8"],
            ["ReporterID", "LLUUID"],
            ["ViewerPosition", "LLVector3"],
            ["AgentPosition", "LLVector3"],
            ["ScreenshotID", "LLUUID"],
            ["ObjectID", "LLUUID"],
            ["OwnerID", "LLUUID"],
            ["LastOwnerID", "LLUUID"],
            ["CreatorID", "LLUUID"],
            ["RegionID", "LLUUID"],
            ["AbuserID", "LLUUID"],
            ["AbuseRegionName", "Variable1"],
            ["AbuseRegionID", "LLUUID"],
            ["Summary", "Variable1"],
            ["Details", "Variable2"],
            ["VersionString", "Variable1"]
        ]
    }
registerMessage("UserReportInternal", UserReportInternal)

class SetSimStatusInDatabase(message.baseMessage):
    id = 22
    freq = 2
    trusted = True
    zero_coded = False
    blocks = [
        ("Data", 1)
    ]
    structure = {
        "Data": [
            ["RegionID", "LLUUID"],
            ["HostName", "Variable1"],
            ["X", "S32"],
            ["Y", "S32"],
            ["PID", "S32"],
            ["AgentCount", "S32"],
            ["TimeToLive", "S32"],
            ["Status", "Variable1"]
        ]
    }
registerMessage("SetSimStatusInDatabase", SetSimStatusInDatabase)

class SetSimPresenceInDatabase(message.baseMessage):
    id = 23
    freq = 2
    trusted = True
    zero_coded = False
    blocks = [
        ("SimData", 1)
    ]
    structure = {
        "SimData": [
            ["RegionID", "LLUUID"],
            ["HostName", "Variable1"],
            ["GridX", "U32"],
            ["GridY", "U32"],
            ["PID", "S32"],
            ["AgentCount", "S32"],
            ["TimeToLive", "S32"],
            ["Status", "Variable1"]
        ]
    }
registerMessage("SetSimPresenceInDatabase", SetSimPresenceInDatabase)

class EconomyDataRequest(message.baseMessage):
    id = 24
    freq = 2
    trusted = False
    zero_coded = False
    blocks = [

    ]
    structure = {

    }
registerMessage("EconomyDataRequest", EconomyDataRequest)

class EconomyData(message.baseMessage):
    id = 25
    freq = 2
    trusted = True
    zero_coded = True
    blocks = [
        ("Info", 1)
    ]
    structure = {
        "Info": [
            ["ObjectCapacity", "S32"],
            ["ObjectCount", "S32"],
            ["PriceEnergyUnit", "S32"],
            ["PriceObjectClaim", "S32"],
            ["PricePublicObjectDecay", "S32"],
            ["PricePublicObjectDelete", "S32"],
            ["PriceParcelClaim", "S32"],
            ["PriceParcelClaimFactor", "F32"],
            ["PriceUpload", "S32"],
            ["PriceRentLight", "S32"],
            ["TeleportMinPrice", "S32"],
            ["TeleportPriceExponent", "F32"],
            ["EnergyEfficiency", "F32"],
            ["PriceObjectRent", "F32"],
            ["PriceObjectScaleFactor", "F32"],
            ["PriceParcelRent", "S32"],
            ["PriceGroupCreate", "S32"]
        ]
    }
registerMessage("EconomyData", EconomyData)

class AvatarPickerRequest(message.baseMessage):
    id = 26
    freq = 2
    trusted = False
    zero_coded = False
    blocks = [
        ("AgentData", 1),
        ("Data", 1)
    ]
    structure = {
        "AgentData": [
            ["AgentID", "LLUUID"],
            ["SessionID", "LLUUID"],
            ["QueryID", "LLUUID"]
        ],
        "Data": [
            ["Name", "Variable1"]
        ]
    }
registerMessage("AvatarPickerRequest", AvatarPickerRequest)

class AvatarPickerRequestBackend(message.baseMessage):
    id = 27
    freq = 2
    trusted = True
    zero_coded = False
    blocks = [
        ("AgentData", 1),
        ("Data", 1)
    ]
    structure = {
        "AgentData": [
            ["AgentID", "LLUUID"],
            ["SessionID", "LLUUID"],
            ["QueryID", "LLUUID"],
            ["GodLevel", "U8"]
        ],
        "Data": [
            ["Name", "Variable1"]
        ]
    }
registerMessage("AvatarPickerRequestBackend", AvatarPickerRequestBackend)

class AvatarPickerReply(message.baseMessage):
    id = 28
    freq = 2
    trusted = True
    zero_coded = False
    blocks = [
        ("AgentData", 1),
        ("Data", 0)
    ]
    structure = {
        "AgentData": [
            ["AgentID", "LLUUID"],
            ["QueryID", "LLUUID"]
        ],
        "Data": [
            ["AvatarID", "LLUUID"],
            ["FirstName", "Variable1"],
            ["LastName", "Variable1"]
        ]
    }
registerMessage("AvatarPickerReply", AvatarPickerReply)

class PlacesQuery(message.baseMessage):
    id = 29
    freq = 2
    trusted = False
    zero_coded = True
    blocks = [
        ("AgentData", 1),
        ("TransactionData", 1),
        ("QueryData", 1)
    ]
    structure = {
        "AgentData": [
            ["AgentID", "LLUUID"],
            ["SessionID", "LLUUID"],
            ["QueryID", "LLUUID"]
        ],
        "TransactionData": [
            ["TransactionID", "LLUUID"]
        ],
        "QueryData": [
            ["QueryText", "Variable1"],
            ["QueryFlags", "U32"],
            ["Category", "S8"],
            ["SimName", "Variable1"]
        ]
    }
registerMessage("PlacesQuery", PlacesQuery)

class PlacesReply(message.baseMessage):
    id = 30
    freq = 2
    trusted = True
    zero_coded = True
    blocks = [
        ("AgentData", 1),
        ("TransactionData", 1),
        ("QueryData", 0)
    ]
    structure = {
        "AgentData": [
            ["AgentID", "LLUUID"],
            ["QueryID", "LLUUID"]
        ],
        "TransactionData": [
            ["TransactionID", "LLUUID"]
        ],
        "QueryData": [
            ["OwnerID", "LLUUID"],
            ["Name", "Variable1"],
            ["Desc", "Variable1"],
            ["ActualArea", "S32"],
            ["BillableArea", "S32"],
            ["Flags", "U8"],
            ["GlobalX", "F32"],
            ["GlobalY", "F32"],
            ["GlobalZ", "F32"],
            ["SimName", "Variable1"],
            ["SnapshotID", "LLUUID"],
            ["Dwell", "F32"],
            ["Price", "S32"]
        ]
    }
registerMessage("PlacesReply", PlacesReply)

class DirFindQuery(message.baseMessage):
    id = 31
    freq = 2
    trusted = False
    zero_coded = True
    blocks = [
        ("AgentData", 1),
        ("QueryData", 1)
    ]
    structure = {
        "AgentData": [
            ["AgentID", "LLUUID"],
            ["SessionID", "LLUUID"]
        ],
        "QueryData": [
            ["QueryID", "LLUUID"],
            ["QueryText", "Variable1"],
            ["QueryFlags", "U32"],
            ["QueryStart", "S32"]
        ]
    }
registerMessage("DirFindQuery", DirFindQuery)

class DirFindQueryBackend(message.baseMessage):
    id = 32
    freq = 2
    trusted = True
    zero_coded = True
    blocks = [
        ("AgentData", 1),
        ("QueryData", 1)
    ]
    structure = {
        "AgentData": [
            ["AgentID", "LLUUID"]
        ],
        "QueryData": [
            ["QueryID", "LLUUID"],
            ["QueryText", "Variable1"],
            ["QueryFlags", "U32"],
            ["QueryStart", "S32"],
            ["EstateID", "U32"],
            ["Godlike", "BOOL"]
        ]
    }
registerMessage("DirFindQueryBackend", DirFindQueryBackend)

class DirPlacesQuery(message.baseMessage):
    id = 33
    freq = 2
    trusted = False
    zero_coded = True
    blocks = [
        ("AgentData", 1),
        ("QueryData", 1)
    ]
    structure = {
        "AgentData": [
            ["AgentID", "LLUUID"],
            ["SessionID", "LLUUID"]
        ],
        "QueryData": [
            ["QueryID", "LLUUID"],
            ["QueryText", "Variable1"],
            ["QueryFlags", "U32"],
            ["Category", "S8"],
            ["SimName", "Variable1"],
            ["QueryStart", "S32"]
        ]
    }
registerMessage("DirPlacesQuery", DirPlacesQuery)

class DirPlacesQueryBackend(message.baseMessage):
    id = 34
    freq = 2
    trusted = True
    zero_coded = True
    blocks = [
        ("AgentData", 1),
        ("QueryData", 1)
    ]
    structure = {
        "AgentData": [
            ["AgentID", "LLUUID"]
        ],
        "QueryData": [
            ["QueryID", "LLUUID"],
            ["QueryText", "Variable1"],
            ["QueryFlags", "U32"],
            ["Category", "S8"],
            ["SimName", "Variable1"],
            ["EstateID", "U32"],
            ["Godlike", "BOOL"],
            ["QueryStart", "S32"]
        ]
    }
registerMessage("DirPlacesQueryBackend", DirPlacesQueryBackend)

class DirPlacesReply(message.baseMessage):
    id = 35
    freq = 2
    trusted = True
    zero_coded = True
    blocks = [
        ("AgentData", 1),
        ("QueryData", 0),
        ("QueryReplies", 0),
        ("StatusData", 0)
    ]
    structure = {
        "AgentData": [
            ["AgentID", "LLUUID"]
        ],
        "QueryData": [
            ["QueryID", "LLUUID"]
        ],
        "QueryReplies": [
            ["ParcelID", "LLUUID"],
            ["Name", "Variable1"],
            ["ForSale", "BOOL"],
            ["Auction", "BOOL"],
            ["Dwell", "F32"]
        ],
        "StatusData": [
            ["Status", "U32"]
        ]
    }
registerMessage("DirPlacesReply", DirPlacesReply)

class DirPeopleReply(message.baseMessage):
    id = 36
    freq = 2
    trusted = True
    zero_coded = True
    blocks = [
        ("AgentData", 1),
        ("QueryData", 1),
        ("QueryReplies", 0)
    ]
    structure = {
        "AgentData": [
            ["AgentID", "LLUUID"]
        ],
        "QueryData": [
            ["QueryID", "LLUUID"]
        ],
        "QueryReplies": [
            ["AgentID", "LLUUID"],
            ["FirstName", "Variable1"],
            ["LastName", "Variable1"],
            ["Group", "Variable1"],
            ["Online", "BOOL"],
            ["Reputation", "S32"]
        ]
    }
registerMessage("DirPeopleReply", DirPeopleReply)

class DirEventsReply(message.baseMessage):
    id = 37
    freq = 2
    trusted = True
    zero_coded = True
    blocks = [
        ("AgentData", 1),
        ("QueryData", 1),
        ("QueryReplies", 0),
        ("StatusData", 0)
    ]
    structure = {
        "AgentData": [
            ["AgentID", "LLUUID"]
        ],
        "QueryData": [
            ["QueryID", "LLUUID"]
        ],
        "QueryReplies": [
            ["OwnerID", "LLUUID"],
            ["Name", "Variable1"],
            ["EventID", "U32"],
            ["Date", "Variable1"],
            ["UnixTime", "U32"],
            ["EventFlags", "U32"]
        ],
        "StatusData": [
            ["Status", "U32"]
        ]
    }
registerMessage("DirEventsReply", DirEventsReply)

class DirGroupsReply(message.baseMessage):
    id = 38
    freq = 2
    trusted = True
    zero_coded = True
    blocks = [
        ("AgentData", 1),
        ("QueryData", 1),
        ("QueryReplies", 0)
    ]
    structure = {
        "AgentData": [
            ["AgentID", "LLUUID"]
        ],
        "QueryData": [
            ["QueryID", "LLUUID"]
        ],
        "QueryReplies": [
            ["GroupID", "LLUUID"],
            ["GroupName", "Variable1"],
            ["Members", "S32"],
            ["SearchOrder", "F32"]
        ]
    }
registerMessage("DirGroupsReply", DirGroupsReply)

class DirClassifiedQuery(message.baseMessage):
    id = 39
    freq = 2
    trusted = False
    zero_coded = True
    blocks = [
        ("AgentData", 1),
        ("QueryData", 1)
    ]
    structure = {
        "AgentData": [
            ["AgentID", "LLUUID"],
            ["SessionID", "LLUUID"]
        ],
        "QueryData": [
            ["QueryID", "LLUUID"],
            ["QueryText", "Variable1"],
            ["QueryFlags", "U32"],
            ["Category", "U32"],
            ["QueryStart", "S32"]
        ]
    }
registerMessage("DirClassifiedQuery", DirClassifiedQuery)

class DirClassifiedQueryBackend(message.baseMessage):
    id = 40
    freq = 2
    trusted = True
    zero_coded = True
    blocks = [
        ("AgentData", 1),
        ("QueryData", 1)
    ]
    structure = {
        "AgentData": [
            ["AgentID", "LLUUID"]
        ],
        "QueryData": [
            ["QueryID", "LLUUID"],
            ["QueryText", "Variable1"],
            ["QueryFlags", "U32"],
            ["Category", "U32"],
            ["EstateID", "U32"],
            ["Godlike", "BOOL"],
            ["QueryStart", "S32"]
        ]
    }
registerMessage("DirClassifiedQueryBackend", DirClassifiedQueryBackend)

class DirClassifiedReply(message.baseMessage):
    id = 41
    freq = 2
    trusted = True
    zero_coded = True
    blocks = [
        ("AgentData", 1),
        ("QueryData", 1),
        ("QueryReplies", 0),
        ("StatusData", 0)
    ]
    structure = {
        "AgentData": [
            ["AgentID", "LLUUID"]
        ],
        "QueryData": [
            ["QueryID", "LLUUID"]
        ],
        "QueryReplies": [
            ["ClassifiedID", "LLUUID"],
            ["Name", "Variable1"],
            ["ClassifiedFlags", "U8"],
            ["CreationDate", "U32"],
            ["ExpirationDate", "U32"],
            ["PriceForListing", "S32"]
        ],
        "StatusData": [
            ["Status", "U32"]
        ]
    }
registerMessage("DirClassifiedReply", DirClassifiedReply)

class AvatarClassifiedReply(message.baseMessage):
    id = 42
    freq = 2
    trusted = True
    zero_coded = False
    blocks = [
        ("AgentData", 1),
        ("Data", 0)
    ]
    structure = {
        "AgentData": [
            ["AgentID", "LLUUID"],
            ["TargetID", "LLUUID"]
        ],
        "Data": [
            ["ClassifiedID", "LLUUID"],
            ["Name", "Variable1"]
        ]
    }
registerMessage("AvatarClassifiedReply", AvatarClassifiedReply)

class ClassifiedInfoRequest(message.baseMessage):
    id = 43
    freq = 2
    trusted = False
    zero_coded = True
    blocks = [
        ("AgentData", 1),
        ("Data", 1)
    ]
    structure = {
        "AgentData": [
            ["AgentID", "LLUUID"],
            ["SessionID", "LLUUID"]
        ],
        "Data": [
            ["ClassifiedID", "LLUUID"]
        ]
    }
registerMessage("ClassifiedInfoRequest", ClassifiedInfoRequest)

class ClassifiedInfoReply(message.baseMessage):
    id = 44
    freq = 2
    trusted = True
    zero_coded = False
    blocks = [
        ("AgentData", 1),
        ("Data", 1)
    ]
    structure = {
        "AgentData": [
            ["AgentID", "LLUUID"]
        ],
        "Data": [
            ["ClassifiedID", "LLUUID"],
            ["CreatorID", "LLUUID"],
            ["CreationDate", "U32"],
            ["ExpirationDate", "U32"],
            ["Category", "U32"],
            ["Name", "Variable1"],
            ["Desc", "Variable2"],
            ["ParcelID", "LLUUID"],
            ["ParentEstate", "U32"],
            ["SnapshotID", "LLUUID"],
            ["SimName", "Variable1"],
            ["PosGlobal", "LLVector3d"],
            ["ParcelName", "Variable1"],
            ["ClassifiedFlags", "U8"],
            ["PriceForListing", "S32"]
        ]
    }
registerMessage("ClassifiedInfoReply", ClassifiedInfoReply)

class ClassifiedInfoUpdate(message.baseMessage):
    id = 45
    freq = 2
    trusted = False
    zero_coded = False
    blocks = [
        ("AgentData", 1),
        ("Data", 1)
    ]
    structure = {
        "AgentData": [
            ["AgentID", "LLUUID"],
            ["SessionID", "LLUUID"]
        ],
        "Data": [
            ["ClassifiedID", "LLUUID"],
            ["Category", "U32"],
            ["Name", "Variable1"],
            ["Desc", "Variable2"],
            ["ParcelID", "LLUUID"],
            ["ParentEstate", "U32"],
            ["SnapshotID", "LLUUID"],
            ["PosGlobal", "LLVector3d"],
            ["ClassifiedFlags", "U8"],
            ["PriceForListing", "S32"]
        ]
    }
registerMessage("ClassifiedInfoUpdate", ClassifiedInfoUpdate)

class ClassifiedDelete(message.baseMessage):
    id = 46
    freq = 2
    trusted = False
    zero_coded = False
    blocks = [
        ("AgentData", 1),
        ("Data", 1)
    ]
    structure = {
        "AgentData": [
            ["AgentID", "LLUUID"],
            ["SessionID", "LLUUID"]
        ],
        "Data": [
            ["ClassifiedID", "LLUUID"]
        ]
    }
registerMessage("ClassifiedDelete", ClassifiedDelete)

class ClassifiedGodDelete(message.baseMessage):
    id = 47
    freq = 2
    trusted = False
    zero_coded = False
    blocks = [
        ("AgentData", 1),
        ("Data", 1)
    ]
    structure = {
        "AgentData": [
            ["AgentID", "LLUUID"],
            ["SessionID", "LLUUID"]
        ],
        "Data": [
            ["ClassifiedID", "LLUUID"],
            ["QueryID", "LLUUID"]
        ]
    }
registerMessage("ClassifiedGodDelete", ClassifiedGodDelete)

class DirLandQuery(message.baseMessage):
    id = 48
    freq = 2
    trusted = False
    zero_coded = True
    blocks = [
        ("AgentData", 1),
        ("QueryData", 1)
    ]
    structure = {
        "AgentData": [
            ["AgentID", "LLUUID"],
            ["SessionID", "LLUUID"]
        ],
        "QueryData": [
            ["QueryID", "LLUUID"],
            ["QueryFlags", "U32"],
            ["SearchType", "U32"],
            ["Price", "S32"],
            ["Area", "S32"],
            ["QueryStart", "S32"]
        ]
    }
registerMessage("DirLandQuery", DirLandQuery)

class DirLandQueryBackend(message.baseMessage):
    id = 49
    freq = 2
    trusted = True
    zero_coded = True
    blocks = [
        ("AgentData", 1),
        ("QueryData", 1)
    ]
    structure = {
        "AgentData": [
            ["AgentID", "LLUUID"]
        ],
        "QueryData": [
            ["QueryID", "LLUUID"],
            ["QueryFlags", "U32"],
            ["SearchType", "U32"],
            ["Price", "S32"],
            ["Area", "S32"],
            ["QueryStart", "S32"],
            ["EstateID", "U32"],
            ["Godlike", "BOOL"]
        ]
    }
registerMessage("DirLandQueryBackend", DirLandQueryBackend)

class DirLandReply(message.baseMessage):
    id = 50
    freq = 2
    trusted = True
    zero_coded = True
    blocks = [
        ("AgentData", 1),
        ("QueryData", 1),
        ("QueryReplies", 0)
    ]
    structure = {
        "AgentData": [
            ["AgentID", "LLUUID"]
        ],
        "QueryData": [
            ["QueryID", "LLUUID"]
        ],
        "QueryReplies": [
            ["ParcelID", "LLUUID"],
            ["Name", "Variable1"],
            ["Auction", "BOOL"],
            ["ForSale", "BOOL"],
            ["SalePrice", "S32"],
            ["ActualArea", "S32"]
        ]
    }
registerMessage("DirLandReply", DirLandReply)

class DirPopularQuery(message.baseMessage):
    id = 51
    freq = 2
    trusted = False
    zero_coded = True
    blocks = [
        ("AgentData", 1),
        ("QueryData", 1)
    ]
    structure = {
        "AgentData": [
            ["AgentID", "LLUUID"],
            ["SessionID", "LLUUID"]
        ],
        "QueryData": [
            ["QueryID", "LLUUID"],
            ["QueryFlags", "U32"]
        ]
    }
registerMessage("DirPopularQuery", DirPopularQuery)

class DirPopularQueryBackend(message.baseMessage):
    id = 52
    freq = 2
    trusted = True
    zero_coded = True
    blocks = [
        ("AgentData", 1),
        ("QueryData", 1)
    ]
    structure = {
        "AgentData": [
            ["AgentID", "LLUUID"]
        ],
        "QueryData": [
            ["QueryID", "LLUUID"],
            ["QueryFlags", "U32"],
            ["EstateID", "U32"],
            ["Godlike", "BOOL"]
        ]
    }
registerMessage("DirPopularQueryBackend", DirPopularQueryBackend)

class DirPopularReply(message.baseMessage):
    id = 53
    freq = 2
    trusted = True
    zero_coded = True
    blocks = [
        ("AgentData", 1),
        ("QueryData", 1),
        ("QueryReplies", 0)
    ]
    structure = {
        "AgentData": [
            ["AgentID", "LLUUID"]
        ],
        "QueryData": [
            ["QueryID", "LLUUID"]
        ],
        "QueryReplies": [
            ["ParcelID", "LLUUID"],
            ["Name", "Variable1"],
            ["Dwell", "F32"]
        ]
    }
registerMessage("DirPopularReply", DirPopularReply)

class ParcelInfoRequest(message.baseMessage):
    id = 54
    freq = 2
    trusted = False
    zero_coded = False
    blocks = [
        ("AgentData", 1),
        ("Data", 1)
    ]
    structure = {
        "AgentData": [
            ["AgentID", "LLUUID"],
            ["SessionID", "LLUUID"]
        ],
        "Data": [
            ["ParcelID", "LLUUID"]
        ]
    }
registerMessage("ParcelInfoRequest", ParcelInfoRequest)

class ParcelInfoReply(message.baseMessage):
    id = 55
    freq = 2
    trusted = True
    zero_coded = True
    blocks = [
        ("AgentData", 1),
        ("Data", 1)
    ]
    structure = {
        "AgentData": [
            ["AgentID", "LLUUID"]
        ],
        "Data": [
            ["ParcelID", "LLUUID"],
            ["OwnerID", "LLUUID"],
            ["Name", "Variable1"],
            ["Desc", "Variable1"],
            ["ActualArea", "S32"],
            ["BillableArea", "S32"],
            ["Flags", "U8"],
            ["GlobalX", "F32"],
            ["GlobalY", "F32"],
            ["GlobalZ", "F32"],
            ["SimName", "Variable1"],
            ["SnapshotID", "LLUUID"],
            ["Dwell", "F32"],
            ["SalePrice", "S32"],
            ["AuctionID", "S32"]
        ]
    }
registerMessage("ParcelInfoReply", ParcelInfoReply)

class ParcelObjectOwnersRequest(message.baseMessage):
    id = 56
    freq = 2
    trusted = False
    zero_coded = False
    blocks = [
        ("AgentData", 1),
        ("ParcelData", 1)
    ]
    structure = {
        "AgentData": [
            ["AgentID", "LLUUID"],
            ["SessionID", "LLUUID"]
        ],
        "ParcelData": [
            ["LocalID", "S32"]
        ]
    }
registerMessage("ParcelObjectOwnersRequest", ParcelObjectOwnersRequest)

class ParcelObjectOwnersReply(message.baseMessage):
    id = 57
    freq = 2
    trusted = True
    zero_coded = True
    blocks = [
        ("Data", 0)
    ]
    structure = {
        "Data": [
            ["OwnerID", "LLUUID"],
            ["IsGroupOwned", "BOOL"],
            ["Count", "S32"],
            ["OnlineStatus", "BOOL"]
        ]
    }
registerMessage("ParcelObjectOwnersReply", ParcelObjectOwnersReply)

class GroupNoticesListRequest(message.baseMessage):
    id = 58
    freq = 2
    trusted = False
    zero_coded = False
    blocks = [
        ("AgentData", 1),
        ("Data", 1)
    ]
    structure = {
        "AgentData": [
            ["AgentID", "LLUUID"],
            ["SessionID", "LLUUID"]
        ],
        "Data": [
            ["GroupID", "LLUUID"]
        ]
    }
registerMessage("GroupNoticesListRequest", GroupNoticesListRequest)

class GroupNoticesListReply(message.baseMessage):
    id = 59
    freq = 2
    trusted = True
    zero_coded = False
    blocks = [
        ("AgentData", 1),
        ("Data", 0)
    ]
    structure = {
        "AgentData": [
            ["AgentID", "LLUUID"],
            ["GroupID", "LLUUID"]
        ],
        "Data": [
            ["NoticeID", "LLUUID"],
            ["Timestamp", "U32"],
            ["FromName", "Variable2"],
            ["Subject", "Variable2"],
            ["HasAttachment", "BOOL"],
            ["AssetType", "U8"]
        ]
    }
registerMessage("GroupNoticesListReply", GroupNoticesListReply)

class GroupNoticeRequest(message.baseMessage):
    id = 60
    freq = 2
    trusted = False
    zero_coded = False
    blocks = [
        ("AgentData", 1),
        ("Data", 1)
    ]
    structure = {
        "AgentData": [
            ["AgentID", "LLUUID"],
            ["SessionID", "LLUUID"]
        ],
        "Data": [
            ["GroupNoticeID", "LLUUID"]
        ]
    }
registerMessage("GroupNoticeRequest", GroupNoticeRequest)

class GroupNoticeAdd(message.baseMessage):
    id = 61
    freq = 2
    trusted = True
    zero_coded = False
    blocks = [
        ("AgentData", 1),
        ("MessageBlock", 1)
    ]
    structure = {
        "AgentData": [
            ["AgentID", "LLUUID"]
        ],
        "MessageBlock": [
            ["ToGroupID", "LLUUID"],
            ["ID", "LLUUID"],
            ["Dialog", "U8"],
            ["FromAgentName", "Variable1"],
            ["Message", "Variable2"],
            ["BinaryBucket", "Variable2"]
        ]
    }
registerMessage("GroupNoticeAdd", GroupNoticeAdd)

class TeleportRequest(message.baseMessage):
    id = 62
    freq = 2
    trusted = False
    zero_coded = False
    blocks = [
        ("AgentData", 1),
        ("Info", 1)
    ]
    structure = {
        "AgentData": [
            ["AgentID", "LLUUID"],
            ["SessionID", "LLUUID"]
        ],
        "Info": [
            ["RegionID", "LLUUID"],
            ["Position", "LLVector3"],
            ["LookAt", "LLVector3"]
        ]
    }
registerMessage("TeleportRequest", TeleportRequest)

class TeleportLocationRequest(message.baseMessage):
    id = 63
    freq = 2
    trusted = False
    zero_coded = False
    blocks = [
        ("AgentData", 1),
        ("Info", 1)
    ]
    structure = {
        "AgentData": [
            ["AgentID", "LLUUID"],
            ["SessionID", "LLUUID"]
        ],
        "Info": [
            ["RegionHandle", "U64"],
            ["Position", "LLVector3"],
            ["LookAt", "LLVector3"]
        ]
    }
registerMessage("TeleportLocationRequest", TeleportLocationRequest)

class TeleportLocal(message.baseMessage):
    id = 64
    freq = 2
    trusted = True
    zero_coded = False
    blocks = [
        ("Info", 1)
    ]
    structure = {
        "Info": [
            ["AgentID", "LLUUID"],
            ["LocationID", "U32"],
            ["Position", "LLVector3"],
            ["LookAt", "LLVector3"],
            ["TeleportFlags", "U32"]
        ]
    }
registerMessage("TeleportLocal", TeleportLocal)

class TeleportLandmarkRequest(message.baseMessage):
    id = 65
    freq = 2
    trusted = False
    zero_coded = True
    blocks = [
        ("Info", 1)
    ]
    structure = {
        "Info": [
            ["AgentID", "LLUUID"],
            ["SessionID", "LLUUID"],
            ["LandmarkID", "LLUUID"]
        ]
    }
registerMessage("TeleportLandmarkRequest", TeleportLandmarkRequest)

class TeleportProgress(message.baseMessage):
    id = 66
    freq = 2
    trusted = True
    zero_coded = False
    blocks = [
        ("AgentData", 1),
        ("Info", 1)
    ]
    structure = {
        "AgentData": [
            ["AgentID", "LLUUID"]
        ],
        "Info": [
            ["TeleportFlags", "U32"],
            ["Message", "Variable1"]
        ]
    }
registerMessage("TeleportProgress", TeleportProgress)

class DataHomeLocationRequest(message.baseMessage):
    id = 67
    freq = 2
    trusted = True
    zero_coded = True
    blocks = [
        ("Info", 1),
        ("AgentInfo", 1)
    ]
    structure = {
        "Info": [
            ["AgentID", "LLUUID"],
            ["KickedFromEstateID", "U32"]
        ],
        "AgentInfo": [
            ["AgentEffectiveMaturity", "U32"]
        ]
    }
registerMessage("DataHomeLocationRequest", DataHomeLocationRequest)

class DataHomeLocationReply(message.baseMessage):
    id = 68
    freq = 2
    trusted = True
    zero_coded = False
    blocks = [
        ("Info", 1)
    ]
    structure = {
        "Info": [
            ["AgentID", "LLUUID"],
            ["RegionHandle", "U64"],
            ["Position", "LLVector3"],
            ["LookAt", "LLVector3"]
        ]
    }
registerMessage("DataHomeLocationReply", DataHomeLocationReply)

class TeleportFinish(message.baseMessage):
    id = 69
    freq = 2
    trusted = True
    zero_coded = False
    blocks = [
        ("Info", 1)
    ]
    structure = {
        "Info": [
            ["AgentID", "LLUUID"],
            ["LocationID", "U32"],
            ["SimIP", "IPADDR"],
            ["SimPort", "IPPORT"],
            ["RegionHandle", "U64"],
            ["SeedCapability", "Variable2"],
            ["SimAccess", "U8"],
            ["TeleportFlags", "U32"]
        ]
    }
registerMessage("TeleportFinish", TeleportFinish)

class StartLure(message.baseMessage):
    id = 70
    freq = 2
    trusted = False
    zero_coded = False
    blocks = [
        ("AgentData", 1),
        ("Info", 1),
        ("TargetData", 0)
    ]
    structure = {
        "AgentData": [
            ["AgentID", "LLUUID"],
            ["SessionID", "LLUUID"]
        ],
        "Info": [
            ["LureType", "U8"],
            ["Message", "Variable1"]
        ],
        "TargetData": [
            ["TargetID", "LLUUID"]
        ]
    }
registerMessage("StartLure", StartLure)

class TeleportLureRequest(message.baseMessage):
    id = 71
    freq = 2
    trusted = False
    zero_coded = False
    blocks = [
        ("Info", 1)
    ]
    structure = {
        "Info": [
            ["AgentID", "LLUUID"],
            ["SessionID", "LLUUID"],
            ["LureID", "LLUUID"],
            ["TeleportFlags", "U32"]
        ]
    }
registerMessage("TeleportLureRequest", TeleportLureRequest)

class TeleportCancel(message.baseMessage):
    id = 72
    freq = 2
    trusted = False
    zero_coded = False
    blocks = [
        ("Info", 1)
    ]
    structure = {
        "Info": [
            ["AgentID", "LLUUID"],
            ["SessionID", "LLUUID"]
        ]
    }
registerMessage("TeleportCancel", TeleportCancel)

class TeleportStart(message.baseMessage):
    id = 73
    freq = 2
    trusted = True
    zero_coded = False
    blocks = [
        ("Info", 1)
    ]
    structure = {
        "Info": [
            ["TeleportFlags", "U32"]
        ]
    }
registerMessage("TeleportStart", TeleportStart)

class TeleportFailed(message.baseMessage):
    id = 74
    freq = 2
    trusted = True
    zero_coded = False
    blocks = [
        ("Info", 1),
        ("AlertInfo", 0)
    ]
    structure = {
        "Info": [
            ["AgentID", "LLUUID"],
            ["Reason", "Variable1"]
        ],
        "AlertInfo": [
            ["Message", "Variable1"],
            ["ExtraParams", "Variable1"]
        ]
    }
registerMessage("TeleportFailed", TeleportFailed)

class Undo(message.baseMessage):
    id = 75
    freq = 2
    trusted = False
    zero_coded = False
    blocks = [
        ("AgentData", 1),
        ("ObjectData", 0)
    ]
    structure = {
        "AgentData": [
            ["AgentID", "LLUUID"],
            ["SessionID", "LLUUID"],
            ["GroupID", "LLUUID"]
        ],
        "ObjectData": [
            ["ObjectID", "LLUUID"]
        ]
    }
registerMessage("Undo", Undo)

class Redo(message.baseMessage):
    id = 76
    freq = 2
    trusted = False
    zero_coded = False
    blocks = [
        ("AgentData", 1),
        ("ObjectData", 0)
    ]
    structure = {
        "AgentData": [
            ["AgentID", "LLUUID"],
            ["SessionID", "LLUUID"],
            ["GroupID", "LLUUID"]
        ],
        "ObjectData": [
            ["ObjectID", "LLUUID"]
        ]
    }
registerMessage("Redo", Redo)

class UndoLand(message.baseMessage):
    id = 77
    freq = 2
    trusted = False
    zero_coded = False
    blocks = [
        ("AgentData", 1)
    ]
    structure = {
        "AgentData": [
            ["AgentID", "LLUUID"],
            ["SessionID", "LLUUID"]
        ]
    }
registerMessage("UndoLand", UndoLand)

class AgentPause(message.baseMessage):
    id = 78
    freq = 2
    trusted = False
    zero_coded = False
    blocks = [
        ("AgentData", 1)
    ]
    structure = {
        "AgentData": [
            ["AgentID", "LLUUID"],
            ["SessionID", "LLUUID"],
            ["SerialNum", "U32"]
        ]
    }
registerMessage("AgentPause", AgentPause)

class AgentResume(message.baseMessage):
    id = 79
    freq = 2
    trusted = False
    zero_coded = False
    blocks = [
        ("AgentData", 1)
    ]
    structure = {
        "AgentData": [
            ["AgentID", "LLUUID"],
            ["SessionID", "LLUUID"],
            ["SerialNum", "U32"]
        ]
    }
registerMessage("AgentResume", AgentResume)

class AgentUpdate(message.baseMessage):
    id = 4
    freq = 0
    trusted = False
    zero_coded = True
    blocks = [
        ("AgentData", 1)
    ]
    structure = {
        "AgentData": [
            ["AgentID", "LLUUID"],
            ["SessionID", "LLUUID"],
            ["BodyRotation", "LLQuaternion"],
            ["HeadRotation", "LLQuaternion"],
            ["State", "U8"],
            ["CameraCenter", "LLVector3"],
            ["CameraAtAxis", "LLVector3"],
            ["CameraLeftAxis", "LLVector3"],
            ["CameraUpAxis", "LLVector3"],
            ["Far", "F32"],
            ["ControlFlags", "U32"],
            ["Flags", "U8"]
        ]
    }
registerMessage("AgentUpdate", AgentUpdate)

class ChatFromViewer(message.baseMessage):
    id = 80
    freq = 2
    trusted = False
    zero_coded = True
    blocks = [
        ("AgentData", 1),
        ("ChatData", 1)
    ]
    structure = {
        "AgentData": [
            ["AgentID", "LLUUID"],
            ["SessionID", "LLUUID"]
        ],
        "ChatData": [
            ["Message", "Variable2"],
            ["Type", "U8"],
            ["Channel", "S32"]
        ]
    }
registerMessage("ChatFromViewer", ChatFromViewer)

class AgentThrottle(message.baseMessage):
    id = 81
    freq = 2
    trusted = False
    zero_coded = True
    blocks = [
        ("AgentData", 1),
        ("Throttle", 1)
    ]
    structure = {
        "AgentData": [
            ["AgentID", "LLUUID"],
            ["SessionID", "LLUUID"],
            ["CircuitCode", "U32"]
        ],
        "Throttle": [
            ["GenCounter", "U32"],
            ["Throttles", "Variable1"]
        ]
    }
registerMessage("AgentThrottle", AgentThrottle)

class AgentFOV(message.baseMessage):
    id = 82
    freq = 2
    trusted = False
    zero_coded = False
    blocks = [
        ("AgentData", 1),
        ("FOVBlock", 1)
    ]
    structure = {
        "AgentData": [
            ["AgentID", "LLUUID"],
            ["SessionID", "LLUUID"],
            ["CircuitCode", "U32"]
        ],
        "FOVBlock": [
            ["GenCounter", "U32"],
            ["VerticalAngle", "F32"]
        ]
    }
registerMessage("AgentFOV", AgentFOV)

class AgentHeightWidth(message.baseMessage):
    id = 83
    freq = 2
    trusted = False
    zero_coded = False
    blocks = [
        ("AgentData", 1),
        ("HeightWidthBlock", 1)
    ]
    structure = {
        "AgentData": [
            ["AgentID", "LLUUID"],
            ["SessionID", "LLUUID"],
            ["CircuitCode", "U32"]
        ],
        "HeightWidthBlock": [
            ["GenCounter", "U32"],
            ["Height", "U16"],
            ["Width", "U16"]
        ]
    }
registerMessage("AgentHeightWidth", AgentHeightWidth)

class AgentSetAppearance(message.baseMessage):
    id = 84
    freq = 2
    trusted = False
    zero_coded = True
    blocks = [
        ("AgentData", 1),
        ("WearableData", 0),
        ("ObjectData", 1),
        ("VisualParam", 0)
    ]
    structure = {
        "AgentData": [
            ["AgentID", "LLUUID"],
            ["SessionID", "LLUUID"],
            ["SerialNum", "U32"],
            ["Size", "LLVector3"]
        ],
        "WearableData": [
            ["CacheID", "LLUUID"],
            ["TextureIndex", "U8"]
        ],
        "ObjectData": [
            ["TextureEntry", "Variable2"]
        ],
        "VisualParam": [
            ["ParamValue", "U8"]
        ]
    }
registerMessage("AgentSetAppearance", AgentSetAppearance)

class AgentAnimation(message.baseMessage):
    id = 5
    freq = 0
    trusted = False
    zero_coded = False
    blocks = [
        ("AgentData", 1),
        ("AnimationList", 0),
        ("PhysicalAvatarEventList", 0)
    ]
    structure = {
        "AgentData": [
            ["AgentID", "LLUUID"],
            ["SessionID", "LLUUID"]
        ],
        "AnimationList": [
            ["AnimID", "LLUUID"],
            ["StartAnim", "BOOL"]
        ],
        "PhysicalAvatarEventList": [
            ["TypeData", "Variable1"]
        ]
    }
registerMessage("AgentAnimation", AgentAnimation)

class AgentRequestSit(message.baseMessage):
    id = 6
    freq = 0
    trusted = False
    zero_coded = True
    blocks = [
        ("AgentData", 1),
        ("TargetObject", 1)
    ]
    structure = {
        "AgentData": [
            ["AgentID", "LLUUID"],
            ["SessionID", "LLUUID"]
        ],
        "TargetObject": [
            ["TargetID", "LLUUID"],
            ["Offset", "LLVector3"]
        ]
    }
registerMessage("AgentRequestSit", AgentRequestSit)

class AgentSit(message.baseMessage):
    id = 7
    freq = 0
    trusted = False
    zero_coded = False
    blocks = [
        ("AgentData", 1)
    ]
    structure = {
        "AgentData": [
            ["AgentID", "LLUUID"],
            ["SessionID", "LLUUID"]
        ]
    }
registerMessage("AgentSit", AgentSit)

class AgentQuitCopy(message.baseMessage):
    id = 85
    freq = 2
    trusted = False
    zero_coded = False
    blocks = [
        ("AgentData", 1),
        ("FuseBlock", 1)
    ]
    structure = {
        "AgentData": [
            ["AgentID", "LLUUID"],
            ["SessionID", "LLUUID"]
        ],
        "FuseBlock": [
            ["ViewerCircuitCode", "U32"]
        ]
    }
registerMessage("AgentQuitCopy", AgentQuitCopy)

class RequestImage(message.baseMessage):
    id = 8
    freq = 0
    trusted = False
    zero_coded = False
    blocks = [
        ("AgentData", 1),
        ("RequestImage", 0)
    ]
    structure = {
        "AgentData": [
            ["AgentID", "LLUUID"],
            ["SessionID", "LLUUID"]
        ],
        "RequestImage": [
            ["Image", "LLUUID"],
            ["DiscardLevel", "S8"],
            ["DownloadPriority", "F32"],
            ["Packet", "U32"],
            ["Type", "U8"]
        ]
    }
registerMessage("RequestImage", RequestImage)

class ImageNotInDatabase(message.baseMessage):
    id = 86
    freq = 2
    trusted = True
    zero_coded = False
    blocks = [
        ("ImageID", 1)
    ]
    structure = {
        "ImageID": [
            ["ID", "LLUUID"]
        ]
    }
registerMessage("ImageNotInDatabase", ImageNotInDatabase)

class RebakeAvatarTextures(message.baseMessage):
    id = 87
    freq = 2
    trusted = True
    zero_coded = False
    blocks = [
        ("TextureData", 1)
    ]
    structure = {
        "TextureData": [
            ["TextureID", "LLUUID"]
        ]
    }
registerMessage("RebakeAvatarTextures", RebakeAvatarTextures)

class SetAlwaysRun(message.baseMessage):
    id = 88
    freq = 2
    trusted = False
    zero_coded = False
    blocks = [
        ("AgentData", 1)
    ]
    structure = {
        "AgentData": [
            ["AgentID", "LLUUID"],
            ["SessionID", "LLUUID"],
            ["AlwaysRun", "BOOL"]
        ]
    }
registerMessage("SetAlwaysRun", SetAlwaysRun)

class ObjectAdd(message.baseMessage):
    id = 1
    freq = 1
    trusted = False
    zero_coded = True
    blocks = [
        ("AgentData", 1),
        ("ObjectData", 1)
    ]
    structure = {
        "AgentData": [
            ["AgentID", "LLUUID"],
            ["SessionID", "LLUUID"],
            ["GroupID", "LLUUID"]
        ],
        "ObjectData": [
            ["PCode", "U8"],
            ["Material", "U8"],
            ["AddFlags", "U32"],
            ["PathCurve", "U8"],
            ["ProfileCurve", "U8"],
            ["PathBegin", "U16"],
            ["PathEnd", "U16"],
            ["PathScaleX", "U8"],
            ["PathScaleY", "U8"],
            ["PathShearX", "U8"],
            ["PathShearY", "U8"],
            ["PathTwist", "S8"],
            ["PathTwistBegin", "S8"],
            ["PathRadiusOffset", "S8"],
            ["PathTaperX", "S8"],
            ["PathTaperY", "S8"],
            ["PathRevolutions", "U8"],
            ["PathSkew", "S8"],
            ["ProfileBegin", "U16"],
            ["ProfileEnd", "U16"],
            ["ProfileHollow", "U16"],
            ["BypassRaycast", "U8"],
            ["RayStart", "LLVector3"],
            ["RayEnd", "LLVector3"],
            ["RayTargetID", "LLUUID"],
            ["RayEndIsIntersection", "U8"],
            ["Scale", "LLVector3"],
            ["Rotation", "LLQuaternion"],
            ["State", "U8"]
        ]
    }
registerMessage("ObjectAdd", ObjectAdd)

class ObjectDelete(message.baseMessage):
    id = 89
    freq = 2
    trusted = False
    zero_coded = True
    blocks = [
        ("AgentData", 1),
        ("ObjectData", 0)
    ]
    structure = {
        "AgentData": [
            ["AgentID", "LLUUID"],
            ["SessionID", "LLUUID"],
            ["Force", "BOOL"]
        ],
        "ObjectData": [
            ["ObjectLocalID", "U32"]
        ]
    }
registerMessage("ObjectDelete", ObjectDelete)

class ObjectDuplicate(message.baseMessage):
    id = 90
    freq = 2
    trusted = False
    zero_coded = True
    blocks = [
        ("AgentData", 1),
        ("SharedData", 1),
        ("ObjectData", 0)
    ]
    structure = {
        "AgentData": [
            ["AgentID", "LLUUID"],
            ["SessionID", "LLUUID"],
            ["GroupID", "LLUUID"]
        ],
        "SharedData": [
            ["Offset", "LLVector3"],
            ["DuplicateFlags", "U32"]
        ],
        "ObjectData": [
            ["ObjectLocalID", "U32"]
        ]
    }
registerMessage("ObjectDuplicate", ObjectDuplicate)

class ObjectDuplicateOnRay(message.baseMessage):
    id = 91
    freq = 2
    trusted = False
    zero_coded = True
    blocks = [
        ("AgentData", 1),
        ("ObjectData", 0)
    ]
    structure = {
        "AgentData": [
            ["AgentID", "LLUUID"],
            ["SessionID", "LLUUID"],
            ["GroupID", "LLUUID"],
            ["RayStart", "LLVector3"],
            ["RayEnd", "LLVector3"],
            ["BypassRaycast", "BOOL"],
            ["RayEndIsIntersection", "BOOL"],
            ["CopyCenters", "BOOL"],
            ["CopyRotates", "BOOL"],
            ["RayTargetID", "LLUUID"],
            ["DuplicateFlags", "U32"]
        ],
        "ObjectData": [
            ["ObjectLocalID", "U32"]
        ]
    }
registerMessage("ObjectDuplicateOnRay", ObjectDuplicateOnRay)

class MultipleObjectUpdate(message.baseMessage):
    id = 2
    freq = 1
    trusted = False
    zero_coded = True
    blocks = [
        ("AgentData", 1),
        ("ObjectData", 0)
    ]
    structure = {
        "AgentData": [
            ["AgentID", "LLUUID"],
            ["SessionID", "LLUUID"]
        ],
        "ObjectData": [
            ["ObjectLocalID", "U32"],
            ["Type", "U8"],
            ["Data", "Variable1"]
        ]
    }
registerMessage("MultipleObjectUpdate", MultipleObjectUpdate)

class RequestMultipleObjects(message.baseMessage):
    id = 3
    freq = 1
    trusted = False
    zero_coded = True
    blocks = [
        ("AgentData", 1),
        ("ObjectData", 0)
    ]
    structure = {
        "AgentData": [
            ["AgentID", "LLUUID"],
            ["SessionID", "LLUUID"]
        ],
        "ObjectData": [
            ["CacheMissType", "U8"],
            ["ID", "U32"]
        ]
    }
registerMessage("RequestMultipleObjects", RequestMultipleObjects)

class ObjectPosition(message.baseMessage):
    id = 4
    freq = 1
    trusted = False
    zero_coded = True
    blocks = [
        ("AgentData", 1),
        ("ObjectData", 0)
    ]
    structure = {
        "AgentData": [
            ["AgentID", "LLUUID"],
            ["SessionID", "LLUUID"]
        ],
        "ObjectData": [
            ["ObjectLocalID", "U32"],
            ["Position", "LLVector3"]
        ]
    }
registerMessage("ObjectPosition", ObjectPosition)

class ObjectScale(message.baseMessage):
    id = 92
    freq = 2
    trusted = False
    zero_coded = True
    blocks = [
        ("AgentData", 1),
        ("ObjectData", 0)
    ]
    structure = {
        "AgentData": [
            ["AgentID", "LLUUID"],
            ["SessionID", "LLUUID"]
        ],
        "ObjectData": [
            ["ObjectLocalID", "U32"],
            ["Scale", "LLVector3"]
        ]
    }
registerMessage("ObjectScale", ObjectScale)

class ObjectRotation(message.baseMessage):
    id = 93
    freq = 2
    trusted = False
    zero_coded = True
    blocks = [
        ("AgentData", 1),
        ("ObjectData", 0)
    ]
    structure = {
        "AgentData": [
            ["AgentID", "LLUUID"],
            ["SessionID", "LLUUID"]
        ],
        "ObjectData": [
            ["ObjectLocalID", "U32"],
            ["Rotation", "LLQuaternion"]
        ]
    }
registerMessage("ObjectRotation", ObjectRotation)

class ObjectFlagUpdate(message.baseMessage):
    id = 94
    freq = 2
    trusted = False
    zero_coded = True
    blocks = [
        ("AgentData", 1),
        ("ExtraPhysics", 0)
    ]
    structure = {
        "AgentData": [
            ["AgentID", "LLUUID"],
            ["SessionID", "LLUUID"],
            ["ObjectLocalID", "U32"],
            ["UsePhysics", "BOOL"],
            ["IsTemporary", "BOOL"],
            ["IsPhantom", "BOOL"],
            ["CastsShadows", "BOOL"]
        ],
        "ExtraPhysics": [
            ["PhysicsShapeType", "U8"],
            ["Density", "F32"],
            ["Friction", "F32"],
            ["Restitution", "F32"],
            ["GravityMultiplier", "F32"]
        ]
    }
registerMessage("ObjectFlagUpdate", ObjectFlagUpdate)

class ObjectClickAction(message.baseMessage):
    id = 95
    freq = 2
    trusted = False
    zero_coded = True
    blocks = [
        ("AgentData", 1),
        ("ObjectData", 0)
    ]
    structure = {
        "AgentData": [
            ["AgentID", "LLUUID"],
            ["SessionID", "LLUUID"]
        ],
        "ObjectData": [
            ["ObjectLocalID", "U32"],
            ["ClickAction", "U8"]
        ]
    }
registerMessage("ObjectClickAction", ObjectClickAction)

class ObjectImage(message.baseMessage):
    id = 96
    freq = 2
    trusted = False
    zero_coded = True
    blocks = [
        ("AgentData", 1),
        ("ObjectData", 0)
    ]
    structure = {
        "AgentData": [
            ["AgentID", "LLUUID"],
            ["SessionID", "LLUUID"]
        ],
        "ObjectData": [
            ["ObjectLocalID", "U32"],
            ["MediaURL", "Variable1"],
            ["TextureEntry", "Variable2"]
        ]
    }
registerMessage("ObjectImage", ObjectImage)

class ObjectMaterial(message.baseMessage):
    id = 97
    freq = 2
    trusted = False
    zero_coded = True
    blocks = [
        ("AgentData", 1),
        ("ObjectData", 0)
    ]
    structure = {
        "AgentData": [
            ["AgentID", "LLUUID"],
            ["SessionID", "LLUUID"]
        ],
        "ObjectData": [
            ["ObjectLocalID", "U32"],
            ["Material", "U8"]
        ]
    }
registerMessage("ObjectMaterial", ObjectMaterial)

class ObjectShape(message.baseMessage):
    id = 98
    freq = 2
    trusted = False
    zero_coded = True
    blocks = [
        ("AgentData", 1),
        ("ObjectData", 0)
    ]
    structure = {
        "AgentData": [
            ["AgentID", "LLUUID"],
            ["SessionID", "LLUUID"]
        ],
        "ObjectData": [
            ["ObjectLocalID", "U32"],
            ["PathCurve", "U8"],
            ["ProfileCurve", "U8"],
            ["PathBegin", "U16"],
            ["PathEnd", "U16"],
            ["PathScaleX", "U8"],
            ["PathScaleY", "U8"],
            ["PathShearX", "U8"],
            ["PathShearY", "U8"],
            ["PathTwist", "S8"],
            ["PathTwistBegin", "S8"],
            ["PathRadiusOffset", "S8"],
            ["PathTaperX", "S8"],
            ["PathTaperY", "S8"],
            ["PathRevolutions", "U8"],
            ["PathSkew", "S8"],
            ["ProfileBegin", "U16"],
            ["ProfileEnd", "U16"],
            ["ProfileHollow", "U16"]
        ]
    }
registerMessage("ObjectShape", ObjectShape)

class ObjectExtraParams(message.baseMessage):
    id = 99
    freq = 2
    trusted = False
    zero_coded = True
    blocks = [
        ("AgentData", 1),
        ("ObjectData", 0)
    ]
    structure = {
        "AgentData": [
            ["AgentID", "LLUUID"],
            ["SessionID", "LLUUID"]
        ],
        "ObjectData": [
            ["ObjectLocalID", "U32"],
            ["ParamType", "U16"],
            ["ParamInUse", "BOOL"],
            ["ParamSize", "U32"],
            ["ParamData", "Variable1"]
        ]
    }
registerMessage("ObjectExtraParams", ObjectExtraParams)

class ObjectOwner(message.baseMessage):
    id = 100
    freq = 2
    trusted = False
    zero_coded = True
    blocks = [
        ("AgentData", 1),
        ("HeaderData", 1),
        ("ObjectData", 0)
    ]
    structure = {
        "AgentData": [
            ["AgentID", "LLUUID"],
            ["SessionID", "LLUUID"]
        ],
        "HeaderData": [
            ["Override", "BOOL"],
            ["OwnerID", "LLUUID"],
            ["GroupID", "LLUUID"]
        ],
        "ObjectData": [
            ["ObjectLocalID", "U32"]
        ]
    }
registerMessage("ObjectOwner", ObjectOwner)

class ObjectGroup(message.baseMessage):
    id = 101
    freq = 2
    trusted = False
    zero_coded = True
    blocks = [
        ("AgentData", 1),
        ("ObjectData", 0)
    ]
    structure = {
        "AgentData": [
            ["AgentID", "LLUUID"],
            ["SessionID", "LLUUID"],
            ["GroupID", "LLUUID"]
        ],
        "ObjectData": [
            ["ObjectLocalID", "U32"]
        ]
    }
registerMessage("ObjectGroup", ObjectGroup)

class ObjectBuy(message.baseMessage):
    id = 102
    freq = 2
    trusted = False
    zero_coded = True
    blocks = [
        ("AgentData", 1),
        ("ObjectData", 0)
    ]
    structure = {
        "AgentData": [
            ["AgentID", "LLUUID"],
            ["SessionID", "LLUUID"],
            ["GroupID", "LLUUID"],
            ["CategoryID", "LLUUID"]
        ],
        "ObjectData": [
            ["ObjectLocalID", "U32"],
            ["SaleType", "U8"],
            ["SalePrice", "S32"]
        ]
    }
registerMessage("ObjectBuy", ObjectBuy)

class BuyObjectInventory(message.baseMessage):
    id = 103
    freq = 2
    trusted = False
    zero_coded = True
    blocks = [
        ("AgentData", 1),
        ("Data", 1)
    ]
    structure = {
        "AgentData": [
            ["AgentID", "LLUUID"],
            ["SessionID", "LLUUID"]
        ],
        "Data": [
            ["ObjectID", "LLUUID"],
            ["ItemID", "LLUUID"],
            ["FolderID", "LLUUID"]
        ]
    }
registerMessage("BuyObjectInventory", BuyObjectInventory)

class DerezContainer(message.baseMessage):
    id = 104
    freq = 2
    trusted = True
    zero_coded = True
    blocks = [
        ("Data", 1)
    ]
    structure = {
        "Data": [
            ["ObjectID", "LLUUID"],
            ["Delete", "BOOL"]
        ]
    }
registerMessage("DerezContainer", DerezContainer)

class ObjectPermissions(message.baseMessage):
    id = 105
    freq = 2
    trusted = False
    zero_coded = True
    blocks = [
        ("AgentData", 1),
        ("HeaderData", 1),
        ("ObjectData", 0)
    ]
    structure = {
        "AgentData": [
            ["AgentID", "LLUUID"],
            ["SessionID", "LLUUID"]
        ],
        "HeaderData": [
            ["Override", "BOOL"]
        ],
        "ObjectData": [
            ["ObjectLocalID", "U32"],
            ["Field", "U8"],
            ["Set", "U8"],
            ["Mask", "U32"]
        ]
    }
registerMessage("ObjectPermissions", ObjectPermissions)

class ObjectSaleInfo(message.baseMessage):
    id = 106
    freq = 2
    trusted = False
    zero_coded = True
    blocks = [
        ("AgentData", 1),
        ("ObjectData", 0)
    ]
    structure = {
        "AgentData": [
            ["AgentID", "LLUUID"],
            ["SessionID", "LLUUID"]
        ],
        "ObjectData": [
            ["LocalID", "U32"],
            ["SaleType", "U8"],
            ["SalePrice", "S32"]
        ]
    }
registerMessage("ObjectSaleInfo", ObjectSaleInfo)

class ObjectName(message.baseMessage):
    id = 107
    freq = 2
    trusted = False
    zero_coded = True
    blocks = [
        ("AgentData", 1),
        ("ObjectData", 0)
    ]
    structure = {
        "AgentData": [
            ["AgentID", "LLUUID"],
            ["SessionID", "LLUUID"]
        ],
        "ObjectData": [
            ["LocalID", "U32"],
            ["Name", "Variable1"]
        ]
    }
registerMessage("ObjectName", ObjectName)

class ObjectDescription(message.baseMessage):
    id = 108
    freq = 2
    trusted = False
    zero_coded = True
    blocks = [
        ("AgentData", 1),
        ("ObjectData", 0)
    ]
    structure = {
        "AgentData": [
            ["AgentID", "LLUUID"],
            ["SessionID", "LLUUID"]
        ],
        "ObjectData": [
            ["LocalID", "U32"],
            ["Description", "Variable1"]
        ]
    }
registerMessage("ObjectDescription", ObjectDescription)

class ObjectCategory(message.baseMessage):
    id = 109
    freq = 2
    trusted = False
    zero_coded = True
    blocks = [
        ("AgentData", 1),
        ("ObjectData", 0)
    ]
    structure = {
        "AgentData": [
            ["AgentID", "LLUUID"],
            ["SessionID", "LLUUID"]
        ],
        "ObjectData": [
            ["LocalID", "U32"],
            ["Category", "U32"]
        ]
    }
registerMessage("ObjectCategory", ObjectCategory)

class ObjectSelect(message.baseMessage):
    id = 110
    freq = 2
    trusted = False
    zero_coded = True
    blocks = [
        ("AgentData", 1),
        ("ObjectData", 0)
    ]
    structure = {
        "AgentData": [
            ["AgentID", "LLUUID"],
            ["SessionID", "LLUUID"]
        ],
        "ObjectData": [
            ["ObjectLocalID", "U32"]
        ]
    }
registerMessage("ObjectSelect", ObjectSelect)

class ObjectDeselect(message.baseMessage):
    id = 111
    freq = 2
    trusted = False
    zero_coded = True
    blocks = [
        ("AgentData", 1),
        ("ObjectData", 0)
    ]
    structure = {
        "AgentData": [
            ["AgentID", "LLUUID"],
            ["SessionID", "LLUUID"]
        ],
        "ObjectData": [
            ["ObjectLocalID", "U32"]
        ]
    }
registerMessage("ObjectDeselect", ObjectDeselect)

class ObjectAttach(message.baseMessage):
    id = 112
    freq = 2
    trusted = False
    zero_coded = True
    blocks = [
        ("AgentData", 1),
        ("ObjectData", 0)
    ]
    structure = {
        "AgentData": [
            ["AgentID", "LLUUID"],
            ["SessionID", "LLUUID"],
            ["AttachmentPoint", "U8"]
        ],
        "ObjectData": [
            ["ObjectLocalID", "U32"],
            ["Rotation", "LLQuaternion"]
        ]
    }
registerMessage("ObjectAttach", ObjectAttach)

class ObjectDetach(message.baseMessage):
    id = 113
    freq = 2
    trusted = False
    zero_coded = False
    blocks = [
        ("AgentData", 1),
        ("ObjectData", 0)
    ]
    structure = {
        "AgentData": [
            ["AgentID", "LLUUID"],
            ["SessionID", "LLUUID"]
        ],
        "ObjectData": [
            ["ObjectLocalID", "U32"]
        ]
    }
registerMessage("ObjectDetach", ObjectDetach)

class ObjectDrop(message.baseMessage):
    id = 114
    freq = 2
    trusted = False
    zero_coded = False
    blocks = [
        ("AgentData", 1),
        ("ObjectData", 0)
    ]
    structure = {
        "AgentData": [
            ["AgentID", "LLUUID"],
            ["SessionID", "LLUUID"]
        ],
        "ObjectData": [
            ["ObjectLocalID", "U32"]
        ]
    }
registerMessage("ObjectDrop", ObjectDrop)

class ObjectLink(message.baseMessage):
    id = 115
    freq = 2
    trusted = False
    zero_coded = False
    blocks = [
        ("AgentData", 1),
        ("ObjectData", 0)
    ]
    structure = {
        "AgentData": [
            ["AgentID", "LLUUID"],
            ["SessionID", "LLUUID"]
        ],
        "ObjectData": [
            ["ObjectLocalID", "U32"]
        ]
    }
registerMessage("ObjectLink", ObjectLink)

class ObjectDelink(message.baseMessage):
    id = 116
    freq = 2
    trusted = False
    zero_coded = False
    blocks = [
        ("AgentData", 1),
        ("ObjectData", 0)
    ]
    structure = {
        "AgentData": [
            ["AgentID", "LLUUID"],
            ["SessionID", "LLUUID"]
        ],
        "ObjectData": [
            ["ObjectLocalID", "U32"]
        ]
    }
registerMessage("ObjectDelink", ObjectDelink)

class ObjectGrab(message.baseMessage):
    id = 117
    freq = 2
    trusted = False
    zero_coded = True
    blocks = [
        ("AgentData", 1),
        ("ObjectData", 1),
        ("SurfaceInfo", 0)
    ]
    structure = {
        "AgentData": [
            ["AgentID", "LLUUID"],
            ["SessionID", "LLUUID"]
        ],
        "ObjectData": [
            ["LocalID", "U32"],
            ["GrabOffset", "LLVector3"]
        ],
        "SurfaceInfo": [
            ["UVCoord", "LLVector3"],
            ["STCoord", "LLVector3"],
            ["FaceIndex", "S32"],
            ["Position", "LLVector3"],
            ["Normal", "LLVector3"],
            ["Binormal", "LLVector3"]
        ]
    }
registerMessage("ObjectGrab", ObjectGrab)

class ObjectGrabUpdate(message.baseMessage):
    id = 118
    freq = 2
    trusted = False
    zero_coded = True
    blocks = [
        ("AgentData", 1),
        ("ObjectData", 1),
        ("SurfaceInfo", 0)
    ]
    structure = {
        "AgentData": [
            ["AgentID", "LLUUID"],
            ["SessionID", "LLUUID"]
        ],
        "ObjectData": [
            ["ObjectID", "LLUUID"],
            ["GrabOffsetInitial", "LLVector3"],
            ["GrabPosition", "LLVector3"],
            ["TimeSinceLast", "U32"]
        ],
        "SurfaceInfo": [
            ["UVCoord", "LLVector3"],
            ["STCoord", "LLVector3"],
            ["FaceIndex", "S32"],
            ["Position", "LLVector3"],
            ["Normal", "LLVector3"],
            ["Binormal", "LLVector3"]
        ]
    }
registerMessage("ObjectGrabUpdate", ObjectGrabUpdate)

class ObjectDeGrab(message.baseMessage):
    id = 119
    freq = 2
    trusted = False
    zero_coded = False
    blocks = [
        ("AgentData", 1),
        ("ObjectData", 1),
        ("SurfaceInfo", 0)
    ]
    structure = {
        "AgentData": [
            ["AgentID", "LLUUID"],
            ["SessionID", "LLUUID"]
        ],
        "ObjectData": [
            ["LocalID", "U32"]
        ],
        "SurfaceInfo": [
            ["UVCoord", "LLVector3"],
            ["STCoord", "LLVector3"],
            ["FaceIndex", "S32"],
            ["Position", "LLVector3"],
            ["Normal", "LLVector3"],
            ["Binormal", "LLVector3"]
        ]
    }
registerMessage("ObjectDeGrab", ObjectDeGrab)

class ObjectSpinStart(message.baseMessage):
    id = 120
    freq = 2
    trusted = False
    zero_coded = True
    blocks = [
        ("AgentData", 1),
        ("ObjectData", 1)
    ]
    structure = {
        "AgentData": [
            ["AgentID", "LLUUID"],
            ["SessionID", "LLUUID"]
        ],
        "ObjectData": [
            ["ObjectID", "LLUUID"]
        ]
    }
registerMessage("ObjectSpinStart", ObjectSpinStart)

class ObjectSpinUpdate(message.baseMessage):
    id = 121
    freq = 2
    trusted = False
    zero_coded = True
    blocks = [
        ("AgentData", 1),
        ("ObjectData", 1)
    ]
    structure = {
        "AgentData": [
            ["AgentID", "LLUUID"],
            ["SessionID", "LLUUID"]
        ],
        "ObjectData": [
            ["ObjectID", "LLUUID"],
            ["Rotation", "LLQuaternion"]
        ]
    }
registerMessage("ObjectSpinUpdate", ObjectSpinUpdate)

class ObjectSpinStop(message.baseMessage):
    id = 122
    freq = 2
    trusted = False
    zero_coded = True
    blocks = [
        ("AgentData", 1),
        ("ObjectData", 1)
    ]
    structure = {
        "AgentData": [
            ["AgentID", "LLUUID"],
            ["SessionID", "LLUUID"]
        ],
        "ObjectData": [
            ["ObjectID", "LLUUID"]
        ]
    }
registerMessage("ObjectSpinStop", ObjectSpinStop)

class ObjectExportSelected(message.baseMessage):
    id = 123
    freq = 2
    trusted = False
    zero_coded = True
    blocks = [
        ("AgentData", 1),
        ("ObjectData", 0)
    ]
    structure = {
        "AgentData": [
            ["AgentID", "LLUUID"],
            ["RequestID", "LLUUID"],
            ["VolumeDetail", "S16"]
        ],
        "ObjectData": [
            ["ObjectID", "LLUUID"]
        ]
    }
registerMessage("ObjectExportSelected", ObjectExportSelected)

class ModifyLand(message.baseMessage):
    id = 124
    freq = 2
    trusted = False
    zero_coded = True
    blocks = [
        ("AgentData", 1),
        ("ModifyBlock", 1),
        ("ParcelData", 0),
        ("ModifyBlockExtended", 0)
    ]
    structure = {
        "AgentData": [
            ["AgentID", "LLUUID"],
            ["SessionID", "LLUUID"]
        ],
        "ModifyBlock": [
            ["Action", "U8"],
            ["BrushSize", "U8"],
            ["Seconds", "F32"],
            ["Height", "F32"]
        ],
        "ParcelData": [
            ["LocalID", "S32"],
            ["West", "F32"],
            ["South", "F32"],
            ["East", "F32"],
            ["North", "F32"]
        ],
        "ModifyBlockExtended": [
            ["BrushSize", "F32"]
        ]
    }
registerMessage("ModifyLand", ModifyLand)

class VelocityInterpolateOn(message.baseMessage):
    id = 125
    freq = 2
    trusted = False
    zero_coded = False
    blocks = [
        ("AgentData", 1)
    ]
    structure = {
        "AgentData": [
            ["AgentID", "LLUUID"],
            ["SessionID", "LLUUID"]
        ]
    }
registerMessage("VelocityInterpolateOn", VelocityInterpolateOn)

class VelocityInterpolateOff(message.baseMessage):
    id = 126
    freq = 2
    trusted = False
    zero_coded = False
    blocks = [
        ("AgentData", 1)
    ]
    structure = {
        "AgentData": [
            ["AgentID", "LLUUID"],
            ["SessionID", "LLUUID"]
        ]
    }
registerMessage("VelocityInterpolateOff", VelocityInterpolateOff)

class StateSave(message.baseMessage):
    id = 127
    freq = 2
    trusted = False
    zero_coded = False
    blocks = [
        ("AgentData", 1),
        ("DataBlock", 1)
    ]
    structure = {
        "AgentData": [
            ["AgentID", "LLUUID"],
            ["SessionID", "LLUUID"]
        ],
        "DataBlock": [
            ["Filename", "Variable1"]
        ]
    }
registerMessage("StateSave", StateSave)

class ReportAutosaveCrash(message.baseMessage):
    id = 128
    freq = 2
    trusted = False
    zero_coded = False
    blocks = [
        ("AutosaveData", 1)
    ]
    structure = {
        "AutosaveData": [
            ["PID", "S32"],
            ["Status", "S32"]
        ]
    }
registerMessage("ReportAutosaveCrash", ReportAutosaveCrash)

class SimWideDeletes(message.baseMessage):
    id = 129
    freq = 2
    trusted = False
    zero_coded = False
    blocks = [
        ("AgentData", 1),
        ("DataBlock", 1)
    ]
    structure = {
        "AgentData": [
            ["AgentID", "LLUUID"],
            ["SessionID", "LLUUID"]
        ],
        "DataBlock": [
            ["TargetID", "LLUUID"],
            ["Flags", "U32"]
        ]
    }
registerMessage("SimWideDeletes", SimWideDeletes)

class RequestObjectPropertiesFamily(message.baseMessage):
    id = 5
    freq = 1
    trusted = False
    zero_coded = True
    blocks = [
        ("AgentData", 1),
        ("ObjectData", 1)
    ]
    structure = {
        "AgentData": [
            ["AgentID", "LLUUID"],
            ["SessionID", "LLUUID"]
        ],
        "ObjectData": [
            ["RequestFlags", "U32"],
            ["ObjectID", "LLUUID"]
        ]
    }
registerMessage("RequestObjectPropertiesFamily", RequestObjectPropertiesFamily)

class TrackAgent(message.baseMessage):
    id = 130
    freq = 2
    trusted = False
    zero_coded = False
    blocks = [
        ("AgentData", 1),
        ("TargetData", 1)
    ]
    structure = {
        "AgentData": [
            ["AgentID", "LLUUID"],
            ["SessionID", "LLUUID"]
        ],
        "TargetData": [
            ["PreyID", "LLUUID"]
        ]
    }
registerMessage("TrackAgent", TrackAgent)

class ViewerStats(message.baseMessage):
    id = 131
    freq = 2
    trusted = False
    zero_coded = True
    blocks = [
        ("AgentData", 1),
        ("DownloadTotals", 1),
        ("NetStats", 2),
        ("FailStats", 1),
        ("MiscStats", 0)
    ]
    structure = {
        "AgentData": [
            ["AgentID", "LLUUID"],
            ["SessionID", "LLUUID"],
            ["IP", "IPADDR"],
            ["StartTime", "U32"],
            ["RunTime", "F32"],
            ["SimFPS", "F32"],
            ["FPS", "F32"],
            ["AgentsInView", "U8"],
            ["Ping", "F32"],
            ["MetersTraveled", "F64"],
            ["RegionsVisited", "S32"],
            ["SysRAM", "U32"],
            ["SysOS", "Variable1"],
            ["SysCPU", "Variable1"],
            ["SysGPU", "Variable1"]
        ],
        "DownloadTotals": [
            ["World", "U32"],
            ["Objects", "U32"],
            ["Textures", "U32"]
        ],
        "NetStats": [
            ["Bytes", "U32"],
            ["Packets", "U32"],
            ["Compressed", "U32"],
            ["Savings", "U32"]
        ],
        "FailStats": [
            ["SendPacket", "U32"],
            ["Dropped", "U32"],
            ["Resent", "U32"],
            ["FailedResends", "U32"],
            ["OffCircuit", "U32"],
            ["Invalid", "U32"]
        ],
        "MiscStats": [
            ["Type", "U32"],
            ["Value", "F64"]
        ]
    }
registerMessage("ViewerStats", ViewerStats)

class ScriptAnswerYes(message.baseMessage):
    id = 132
    freq = 2
    trusted = False
    zero_coded = False
    blocks = [
        ("AgentData", 1),
        ("Data", 1)
    ]
    structure = {
        "AgentData": [
            ["AgentID", "LLUUID"],
            ["SessionID", "LLUUID"]
        ],
        "Data": [
            ["TaskID", "LLUUID"],
            ["ItemID", "LLUUID"],
            ["Questions", "S32"]
        ]
    }
registerMessage("ScriptAnswerYes", ScriptAnswerYes)

class UserReport(message.baseMessage):
    id = 133
    freq = 2
    trusted = False
    zero_coded = True
    blocks = [
        ("AgentData", 1),
        ("ReportData", 1)
    ]
    structure = {
        "AgentData": [
            ["AgentID", "LLUUID"],
            ["SessionID", "LLUUID"]
        ],
        "ReportData": [
            ["ReportType", "U8"],
            ["Category", "U8"],
            ["Position", "LLVector3"],
            ["CheckFlags", "U8"],
            ["ScreenshotID", "LLUUID"],
            ["ObjectID", "LLUUID"],
            ["AbuserID", "LLUUID"],
            ["AbuseRegionName", "Variable1"],
            ["AbuseRegionID", "LLUUID"],
            ["Summary", "Variable1"],
            ["Details", "Variable2"],
            ["VersionString", "Variable1"]
        ]
    }
registerMessage("UserReport", UserReport)

class AlertMessage(message.baseMessage):
    id = 134
    freq = 2
    trusted = True
    zero_coded = False
    blocks = [
        ("AlertData", 1),
        ("AlertInfo", 0)
    ]
    structure = {
        "AlertData": [
            ["Message", "Variable1"]
        ],
        "AlertInfo": [
            ["Message", "Variable1"],
            ["ExtraParams", "Variable1"]
        ]
    }
registerMessage("AlertMessage", AlertMessage)

class AgentAlertMessage(message.baseMessage):
    id = 135
    freq = 2
    trusted = True
    zero_coded = False
    blocks = [
        ("AgentData", 1),
        ("AlertData", 1)
    ]
    structure = {
        "AgentData": [
            ["AgentID", "LLUUID"]
        ],
        "AlertData": [
            ["Modal", "BOOL"],
            ["Message", "Variable1"]
        ]
    }
registerMessage("AgentAlertMessage", AgentAlertMessage)

class MeanCollisionAlert(message.baseMessage):
    id = 136
    freq = 2
    trusted = True
    zero_coded = True
    blocks = [
        ("MeanCollision", 0)
    ]
    structure = {
        "MeanCollision": [
            ["Victim", "LLUUID"],
            ["Perp", "LLUUID"],
            ["Time", "U32"],
            ["Mag", "F32"],
            ["Type", "U8"]
        ]
    }
registerMessage("MeanCollisionAlert", MeanCollisionAlert)

class ViewerFrozenMessage(message.baseMessage):
    id = 137
    freq = 2
    trusted = True
    zero_coded = False
    blocks = [
        ("FrozenData", 1)
    ]
    structure = {
        "FrozenData": [
            ["Data", "BOOL"]
        ]
    }
registerMessage("ViewerFrozenMessage", ViewerFrozenMessage)

class HealthMessage(message.baseMessage):
    id = 138
    freq = 2
    trusted = True
    zero_coded = True
    blocks = [
        ("HealthData", 1)
    ]
    structure = {
        "HealthData": [
            ["Health", "F32"]
        ]
    }
registerMessage("HealthMessage", HealthMessage)

class ChatFromSimulator(message.baseMessage):
    id = 139
    freq = 2
    trusted = True
    zero_coded = False
    blocks = [
        ("ChatData", 1)
    ]
    structure = {
        "ChatData": [
            ["FromName", "Variable1"],
            ["SourceID", "LLUUID"],
            ["OwnerID", "LLUUID"],
            ["SourceType", "U8"],
            ["ChatType", "U8"],
            ["Audible", "U8"],
            ["Position", "LLVector3"],
            ["Message", "Variable2"]
        ]
    }
registerMessage("ChatFromSimulator", ChatFromSimulator)

class SimStats(message.baseMessage):
    id = 140
    freq = 2
    trusted = True
    zero_coded = False
    blocks = [
        ("Region", 1),
        ("Stat", 0),
        ("PidStat", 1),
        ("RegionInfo", 0)
    ]
    structure = {
        "Region": [
            ["RegionX", "U32"],
            ["RegionY", "U32"],
            ["RegionFlags", "U32"],
            ["ObjectCapacity", "U32"]
        ],
        "Stat": [
            ["StatID", "U32"],
            ["StatValue", "F32"]
        ],
        "PidStat": [
            ["PID", "S32"]
        ],
        "RegionInfo": [
            ["RegionFlagsExtended", "U64"]
        ]
    }
registerMessage("SimStats", SimStats)

class RequestRegionInfo(message.baseMessage):
    id = 141
    freq = 2
    trusted = False
    zero_coded = False
    blocks = [
        ("AgentData", 1)
    ]
    structure = {
        "AgentData": [
            ["AgentID", "LLUUID"],
            ["SessionID", "LLUUID"]
        ]
    }
registerMessage("RequestRegionInfo", RequestRegionInfo)

class RegionInfo(message.baseMessage):
    id = 142
    freq = 2
    trusted = False
    zero_coded = True
    blocks = [
        ("AgentData", 1),
        ("RegionInfo", 1),
        ("RegionInfo2", 1),
        ("RegionInfo3", 0)
    ]
    structure = {
        "AgentData": [
            ["AgentID", "LLUUID"],
            ["SessionID", "LLUUID"]
        ],
        "RegionInfo": [
            ["SimName", "Variable1"],
            ["EstateID", "U32"],
            ["ParentEstateID", "U32"],
            ["RegionFlags", "U32"],
            ["SimAccess", "U8"],
            ["MaxAgents", "U8"],
            ["BillableFactor", "F32"],
            ["ObjectBonusFactor", "F32"],
            ["WaterHeight", "F32"],
            ["TerrainRaiseLimit", "F32"],
            ["TerrainLowerLimit", "F32"],
            ["PricePerMeter", "S32"],
            ["RedirectGridX", "S32"],
            ["RedirectGridY", "S32"],
            ["UseEstateSun", "BOOL"],
            ["SunHour", "F32"]
        ],
        "RegionInfo2": [
            ["ProductSKU", "Variable1"],
            ["ProductName", "Variable1"],
            ["MaxAgents32", "U32"],
            ["HardMaxAgents", "U32"],
            ["HardMaxObjects", "U32"]
        ],
        "RegionInfo3": [
            ["RegionFlagsExtended", "U64"]
        ]
    }
registerMessage("RegionInfo", RegionInfo)

class GodUpdateRegionInfo(message.baseMessage):
    id = 143
    freq = 2
    trusted = False
    zero_coded = True
    blocks = [
        ("AgentData", 1),
        ("RegionInfo", 1),
        ("RegionInfo2", 0)
    ]
    structure = {
        "AgentData": [
            ["AgentID", "LLUUID"],
            ["SessionID", "LLUUID"]
        ],
        "RegionInfo": [
            ["SimName", "Variable1"],
            ["EstateID", "U32"],
            ["ParentEstateID", "U32"],
            ["RegionFlags", "U32"],
            ["BillableFactor", "F32"],
            ["PricePerMeter", "S32"],
            ["RedirectGridX", "S32"],
            ["RedirectGridY", "S32"]
        ],
        "RegionInfo2": [
            ["RegionFlagsExtended", "U64"]
        ]
    }
registerMessage("GodUpdateRegionInfo", GodUpdateRegionInfo)

class NearestLandingRegionRequest(message.baseMessage):
    id = 144
    freq = 2
    trusted = True
    zero_coded = False
    blocks = [
        ("RequestingRegionData", 1)
    ]
    structure = {
        "RequestingRegionData": [
            ["RegionHandle", "U64"]
        ]
    }
registerMessage("NearestLandingRegionRequest", NearestLandingRegionRequest)

class NearestLandingRegionReply(message.baseMessage):
    id = 145
    freq = 2
    trusted = True
    zero_coded = False
    blocks = [
        ("LandingRegionData", 1)
    ]
    structure = {
        "LandingRegionData": [
            ["RegionHandle", "U64"]
        ]
    }
registerMessage("NearestLandingRegionReply", NearestLandingRegionReply)

class NearestLandingRegionUpdated(message.baseMessage):
    id = 146
    freq = 2
    trusted = True
    zero_coded = False
    blocks = [
        ("RegionData", 1)
    ]
    structure = {
        "RegionData": [
            ["RegionHandle", "U64"]
        ]
    }
registerMessage("NearestLandingRegionUpdated", NearestLandingRegionUpdated)

class TeleportLandingStatusChanged(message.baseMessage):
    id = 147
    freq = 2
    trusted = True
    zero_coded = False
    blocks = [
        ("RegionData", 1)
    ]
    structure = {
        "RegionData": [
            ["RegionHandle", "U64"]
        ]
    }
registerMessage("TeleportLandingStatusChanged", TeleportLandingStatusChanged)

class RegionHandshake(message.baseMessage):
    id = 148
    freq = 2
    trusted = True
    zero_coded = True
    blocks = [
        ("RegionInfo", 1),
        ("RegionInfo2", 1),
        ("RegionInfo3", 1),
        ("RegionInfo4", 0)
    ]
    structure = {
        "RegionInfo": [
            ["RegionFlags", "U32"],
            ["SimAccess", "U8"],
            ["SimName", "Variable1"],
            ["SimOwner", "LLUUID"],
            ["IsEstateManager", "BOOL"],
            ["WaterHeight", "F32"],
            ["BillableFactor", "F32"],
            ["CacheID", "LLUUID"],
            ["TerrainBase0", "LLUUID"],
            ["TerrainBase1", "LLUUID"],
            ["TerrainBase2", "LLUUID"],
            ["TerrainBase3", "LLUUID"],
            ["TerrainDetail0", "LLUUID"],
            ["TerrainDetail1", "LLUUID"],
            ["TerrainDetail2", "LLUUID"],
            ["TerrainDetail3", "LLUUID"],
            ["TerrainStartHeight00", "F32"],
            ["TerrainStartHeight01", "F32"],
            ["TerrainStartHeight10", "F32"],
            ["TerrainStartHeight11", "F32"],
            ["TerrainHeightRange00", "F32"],
            ["TerrainHeightRange01", "F32"],
            ["TerrainHeightRange10", "F32"],
            ["TerrainHeightRange11", "F32"]
        ],
        "RegionInfo2": [
            ["RegionID", "LLUUID"]
        ],
        "RegionInfo3": [
            ["CPUClassID", "S32"],
            ["CPURatio", "S32"],
            ["ColoName", "Variable1"],
            ["ProductSKU", "Variable1"],
            ["ProductName", "Variable1"]
        ],
        "RegionInfo4": [
            ["RegionFlagsExtended", "U64"],
            ["RegionProtocols", "U64"]
        ]
    }
registerMessage("RegionHandshake", RegionHandshake)

class RegionHandshakeReply(message.baseMessage):
    id = 149
    freq = 2
    trusted = False
    zero_coded = True
    blocks = [
        ("AgentData", 1),
        ("RegionInfo", 1)
    ]
    structure = {
        "AgentData": [
            ["AgentID", "LLUUID"],
            ["SessionID", "LLUUID"]
        ],
        "RegionInfo": [
            ["Flags", "U32"]
        ]
    }
registerMessage("RegionHandshakeReply", RegionHandshakeReply)

class CoarseLocationUpdate(message.baseMessage):
    id = 6
    freq = 1
    trusted = True
    zero_coded = False
    blocks = [
        ("Location", 0),
        ("Index", 1),
        ("AgentData", 0)
    ]
    structure = {
        "Location": [
            ["X", "U8"],
            ["Y", "U8"],
            ["Z", "U8"]
        ],
        "Index": [
            ["You", "S16"],
            ["Prey", "S16"]
        ],
        "AgentData": [
            ["AgentID", "LLUUID"]
        ]
    }
registerMessage("CoarseLocationUpdate", CoarseLocationUpdate)

class ImageData(message.baseMessage):
    id = 9
    freq = 0
    trusted = True
    zero_coded = False
    blocks = [
        ("ImageID", 1),
        ("ImageData", 1)
    ]
    structure = {
        "ImageID": [
            ["ID", "LLUUID"],
            ["Codec", "U8"],
            ["Size", "U32"],
            ["Packets", "U16"]
        ],
        "ImageData": [
            ["Data", "Variable2"]
        ]
    }
registerMessage("ImageData", ImageData)

class ImagePacket(message.baseMessage):
    id = 10
    freq = 0
    trusted = True
    zero_coded = False
    blocks = [
        ("ImageID", 1),
        ("ImageData", 1)
    ]
    structure = {
        "ImageID": [
            ["ID", "LLUUID"],
            ["Packet", "U16"]
        ],
        "ImageData": [
            ["Data", "Variable2"]
        ]
    }
registerMessage("ImagePacket", ImagePacket)

class LayerData(message.baseMessage):
    id = 11
    freq = 0
    trusted = True
    zero_coded = False
    blocks = [
        ("LayerID", 1),
        ("LayerData", 1)
    ]
    structure = {
        "LayerID": [
            ["Type", "U8"]
        ],
        "LayerData": [
            ["Data", "Variable2"]
        ]
    }
registerMessage("LayerData", LayerData)

class ObjectUpdate(message.baseMessage):
    id = 12
    freq = 0
    trusted = True
    zero_coded = True
    blocks = [
        ("RegionData", 1),
        ("ObjectData", 0)
    ]
    structure = {
        "RegionData": [
            ["RegionHandle", "U64"],
            ["TimeDilation", "U16"]
        ],
        "ObjectData": [
            ["ID", "U32"],
            ["State", "U8"],
            ["FullID", "LLUUID"],
            ["CRC", "U32"],
            ["PCode", "U8"],
            ["Material", "U8"],
            ["ClickAction", "U8"],
            ["Scale", "LLVector3"],
            ["ObjectData", "Variable1"],
            ["ParentID", "U32"],
            ["UpdateFlags", "U32"],
            ["PathCurve", "U8"],
            ["ProfileCurve", "U8"],
            ["PathBegin", "U16"],
            ["PathEnd", "U16"],
            ["PathScaleX", "U8"],
            ["PathScaleY", "U8"],
            ["PathShearX", "U8"],
            ["PathShearY", "U8"],
            ["PathTwist", "S8"],
            ["PathTwistBegin", "S8"],
            ["PathRadiusOffset", "S8"],
            ["PathTaperX", "S8"],
            ["PathTaperY", "S8"],
            ["PathRevolutions", "U8"],
            ["PathSkew", "S8"],
            ["ProfileBegin", "U16"],
            ["ProfileEnd", "U16"],
            ["ProfileHollow", "U16"],
            ["TextureEntry", "Variable2"],
            ["TextureAnim", "Variable1"],
            ["NameValue", "Variable2"],
            ["Data", "Variable2"],
            ["Text", "Variable1"],
            ["TextColor", "Fixed"],
            ["MediaURL", "Variable1"],
            ["PSBlock", "Variable1"],
            ["ExtraParams", "Variable1"],
            ["Sound", "LLUUID"],
            ["OwnerID", "LLUUID"],
            ["Gain", "F32"],
            ["Flags", "U8"],
            ["Radius", "F32"],
            ["JointType", "U8"],
            ["JointPivot", "LLVector3"],
            ["JointAxisOrAnchor", "LLVector3"]
        ]
    }
registerMessage("ObjectUpdate", ObjectUpdate)

class ObjectUpdateCompressed(message.baseMessage):
    id = 13
    freq = 0
    trusted = True
    zero_coded = False
    blocks = [
        ("RegionData", 1),
        ("ObjectData", 0)
    ]
    structure = {
        "RegionData": [
            ["RegionHandle", "U64"],
            ["TimeDilation", "U16"]
        ],
        "ObjectData": [
            ["UpdateFlags", "U32"],
            ["Data", "Variable2"]
        ]
    }
registerMessage("ObjectUpdateCompressed", ObjectUpdateCompressed)

class ObjectUpdateCached(message.baseMessage):
    id = 14
    freq = 0
    trusted = True
    zero_coded = False
    blocks = [
        ("RegionData", 1),
        ("ObjectData", 0)
    ]
    structure = {
        "RegionData": [
            ["RegionHandle", "U64"],
            ["TimeDilation", "U16"]
        ],
        "ObjectData": [
            ["ID", "U32"],
            ["CRC", "U32"],
            ["UpdateFlags", "U32"]
        ]
    }
registerMessage("ObjectUpdateCached", ObjectUpdateCached)

class ImprovedTerseObjectUpdate(message.baseMessage):
    id = 15
    freq = 0
    trusted = True
    zero_coded = False
    blocks = [
        ("RegionData", 1),
        ("ObjectData", 0)
    ]
    structure = {
        "RegionData": [
            ["RegionHandle", "U64"],
            ["TimeDilation", "U16"]
        ],
        "ObjectData": [
            ["Data", "Variable1"],
            ["TextureEntry", "Variable2"]
        ]
    }
registerMessage("ImprovedTerseObjectUpdate", ImprovedTerseObjectUpdate)

class KillObject(message.baseMessage):
    id = 16
    freq = 0
    trusted = True
    zero_coded = False
    blocks = [
        ("ObjectData", 0)
    ]
    structure = {
        "ObjectData": [
            ["ID", "U32"]
        ]
    }
registerMessage("KillObject", KillObject)

class CrossedRegion(message.baseMessage):
    id = 7
    freq = 1
    trusted = True
    zero_coded = False
    blocks = [
        ("AgentData", 1),
        ("RegionData", 1),
        ("Info", 1)
    ]
    structure = {
        "AgentData": [
            ["AgentID", "LLUUID"],
            ["SessionID", "LLUUID"]
        ],
        "RegionData": [
            ["SimIP", "IPADDR"],
            ["SimPort", "IPPORT"],
            ["RegionHandle", "U64"],
            ["SeedCapability", "Variable2"]
        ],
        "Info": [
            ["Position", "LLVector3"],
            ["LookAt", "LLVector3"]
        ]
    }
registerMessage("CrossedRegion", CrossedRegion)

class SimulatorViewerTimeMessage(message.baseMessage):
    id = 150
    freq = 2
    trusted = True
    zero_coded = False
    blocks = [
        ("TimeInfo", 1)
    ]
    structure = {
        "TimeInfo": [
            ["UsecSinceStart", "U64"],
            ["SecPerDay", "U32"],
            ["SecPerYear", "U32"],
            ["SunDirection", "LLVector3"],
            ["SunPhase", "F32"],
            ["SunAngVelocity", "LLVector3"]
        ]
    }
registerMessage("SimulatorViewerTimeMessage", SimulatorViewerTimeMessage)

class EnableSimulator(message.baseMessage):
    id = 151
    freq = 2
    trusted = True
    zero_coded = False
    blocks = [
        ("SimulatorInfo", 1)
    ]
    structure = {
        "SimulatorInfo": [
            ["Handle", "U64"],
            ["IP", "IPADDR"],
            ["Port", "IPPORT"]
        ]
    }
registerMessage("EnableSimulator", EnableSimulator)

class DisableSimulator(message.baseMessage):
    id = 152
    freq = 2
    trusted = True
    zero_coded = False
    blocks = [

    ]
    structure = {

    }
registerMessage("DisableSimulator", DisableSimulator)

class ConfirmEnableSimulator(message.baseMessage):
    id = 8
    freq = 1
    trusted = True
    zero_coded = False
    blocks = [
        ("AgentData", 1)
    ]
    structure = {
        "AgentData": [
            ["AgentID", "LLUUID"],
            ["SessionID", "LLUUID"]
        ]
    }
registerMessage("ConfirmEnableSimulator", ConfirmEnableSimulator)

class TransferRequest(message.baseMessage):
    id = 153
    freq = 2
    trusted = False
    zero_coded = True
    blocks = [
        ("TransferInfo", 1)
    ]
    structure = {
        "TransferInfo": [
            ["TransferID", "LLUUID"],
            ["ChannelType", "S32"],
            ["SourceType", "S32"],
            ["Priority", "F32"],
            ["Params", "Variable2"]
        ]
    }
registerMessage("TransferRequest", TransferRequest)

class TransferInfo(message.baseMessage):
    id = 154
    freq = 2
    trusted = False
    zero_coded = True
    blocks = [
        ("TransferInfo", 1)
    ]
    structure = {
        "TransferInfo": [
            ["TransferID", "LLUUID"],
            ["ChannelType", "S32"],
            ["TargetType", "S32"],
            ["Status", "S32"],
            ["Size", "S32"],
            ["Params", "Variable2"]
        ]
    }
registerMessage("TransferInfo", TransferInfo)

class TransferPacket(message.baseMessage):
    id = 17
    freq = 0
    trusted = False
    zero_coded = False
    blocks = [
        ("TransferData", 1)
    ]
    structure = {
        "TransferData": [
            ["TransferID", "LLUUID"],
            ["ChannelType", "S32"],
            ["Packet", "S32"],
            ["Status", "S32"],
            ["Data", "Variable2"]
        ]
    }
registerMessage("TransferPacket", TransferPacket)

class TransferAbort(message.baseMessage):
    id = 155
    freq = 2
    trusted = False
    zero_coded = True
    blocks = [
        ("TransferInfo", 1)
    ]
    structure = {
        "TransferInfo": [
            ["TransferID", "LLUUID"],
            ["ChannelType", "S32"]
        ]
    }
registerMessage("TransferAbort", TransferAbort)

class RequestXfer(message.baseMessage):
    id = 156
    freq = 2
    trusted = False
    zero_coded = True
    blocks = [
        ("XferID", 1)
    ]
    structure = {
        "XferID": [
            ["ID", "U64"],
            ["Filename", "Variable1"],
            ["FilePath", "U8"],
            ["DeleteOnCompletion", "BOOL"],
            ["UseBigPackets", "BOOL"],
            ["VFileID", "LLUUID"],
            ["VFileType", "S16"]
        ]
    }
registerMessage("RequestXfer", RequestXfer)

class SendXferPacket(message.baseMessage):
    id = 18
    freq = 0
    trusted = False
    zero_coded = False
    blocks = [
        ("XferID", 1),
        ("DataPacket", 1)
    ]
    structure = {
        "XferID": [
            ["ID", "U64"],
            ["Packet", "U32"]
        ],
        "DataPacket": [
            ["Data", "Variable2"]
        ]
    }
registerMessage("SendXferPacket", SendXferPacket)

class ConfirmXferPacket(message.baseMessage):
    id = 19
    freq = 0
    trusted = False
    zero_coded = False
    blocks = [
        ("XferID", 1)
    ]
    structure = {
        "XferID": [
            ["ID", "U64"],
            ["Packet", "U32"]
        ]
    }
registerMessage("ConfirmXferPacket", ConfirmXferPacket)

class AbortXfer(message.baseMessage):
    id = 157
    freq = 2
    trusted = False
    zero_coded = False
    blocks = [
        ("XferID", 1)
    ]
    structure = {
        "XferID": [
            ["ID", "U64"],
            ["Result", "S32"]
        ]
    }
registerMessage("AbortXfer", AbortXfer)

class AvatarAnimation(message.baseMessage):
    id = 20
    freq = 0
    trusted = True
    zero_coded = False
    blocks = [
        ("Sender", 1),
        ("AnimationList", 0),
        ("AnimationSourceList", 0),
        ("PhysicalAvatarEventList", 0)
    ]
    structure = {
        "Sender": [
            ["ID", "LLUUID"]
        ],
        "AnimationList": [
            ["AnimID", "LLUUID"],
            ["AnimSequenceID", "S32"]
        ],
        "AnimationSourceList": [
            ["ObjectID", "LLUUID"]
        ],
        "PhysicalAvatarEventList": [
            ["TypeData", "Variable1"]
        ]
    }
registerMessage("AvatarAnimation", AvatarAnimation)

class AvatarAppearance(message.baseMessage):
    id = 158
    freq = 2
    trusted = True
    zero_coded = True
    blocks = [
        ("Sender", 1),
        ("ObjectData", 1),
        ("VisualParam", 0),
        ("AppearanceData", 0),
        ("AppearanceHover", 0)
    ]
    structure = {
        "Sender": [
            ["ID", "LLUUID"],
            ["IsTrial", "BOOL"]
        ],
        "ObjectData": [
            ["TextureEntry", "Variable2"]
        ],
        "VisualParam": [
            ["ParamValue", "U8"]
        ],
        "AppearanceData": [
            ["AppearanceVersion", "U8"],
            ["CofVersion", "S32"],
            ["Flags", "U32"]
        ],
        "AppearanceHover": [
            ["HoverHeight", "LLVector3"]
        ]
    }
registerMessage("AvatarAppearance", AvatarAppearance)

class AvatarSitResponse(message.baseMessage):
    id = 21
    freq = 0
    trusted = True
    zero_coded = True
    blocks = [
        ("SitObject", 1),
        ("SitTransform", 1)
    ]
    structure = {
        "SitObject": [
            ["ID", "LLUUID"]
        ],
        "SitTransform": [
            ["AutoPilot", "BOOL"],
            ["SitPosition", "LLVector3"],
            ["SitRotation", "LLQuaternion"],
            ["CameraEyeOffset", "LLVector3"],
            ["CameraAtOffset", "LLVector3"],
            ["ForceMouselook", "BOOL"]
        ]
    }
registerMessage("AvatarSitResponse", AvatarSitResponse)

class SetFollowCamProperties(message.baseMessage):
    id = 159
    freq = 2
    trusted = True
    zero_coded = False
    blocks = [
        ("ObjectData", 1),
        ("CameraProperty", 0)
    ]
    structure = {
        "ObjectData": [
            ["ObjectID", "LLUUID"]
        ],
        "CameraProperty": [
            ["Type", "S32"],
            ["Value", "F32"]
        ]
    }
registerMessage("SetFollowCamProperties", SetFollowCamProperties)

class ClearFollowCamProperties(message.baseMessage):
    id = 160
    freq = 2
    trusted = True
    zero_coded = False
    blocks = [
        ("ObjectData", 1)
    ]
    structure = {
        "ObjectData": [
            ["ObjectID", "LLUUID"]
        ]
    }
registerMessage("ClearFollowCamProperties", ClearFollowCamProperties)

class CameraConstraint(message.baseMessage):
    id = 22
    freq = 0
    trusted = True
    zero_coded = True
    blocks = [
        ("CameraCollidePlane", 1)
    ]
    structure = {
        "CameraCollidePlane": [
            ["Plane", "LLVector4"]
        ]
    }
registerMessage("CameraConstraint", CameraConstraint)

class ObjectProperties(message.baseMessage):
    id = 9
    freq = 1
    trusted = True
    zero_coded = True
    blocks = [
        ("ObjectData", 0)
    ]
    structure = {
        "ObjectData": [
            ["ObjectID", "LLUUID"],
            ["CreatorID", "LLUUID"],
            ["OwnerID", "LLUUID"],
            ["GroupID", "LLUUID"],
            ["CreationDate", "U64"],
            ["BaseMask", "U32"],
            ["OwnerMask", "U32"],
            ["GroupMask", "U32"],
            ["EveryoneMask", "U32"],
            ["NextOwnerMask", "U32"],
            ["OwnershipCost", "S32"],
            ["SaleType", "U8"],
            ["SalePrice", "S32"],
            ["AggregatePerms", "U8"],
            ["AggregatePermTextures", "U8"],
            ["AggregatePermTexturesOwner", "U8"],
            ["Category", "U32"],
            ["InventorySerial", "S16"],
            ["ItemID", "LLUUID"],
            ["FolderID", "LLUUID"],
            ["FromTaskID", "LLUUID"],
            ["LastOwnerID", "LLUUID"],
            ["Name", "Variable1"],
            ["Description", "Variable1"],
            ["TouchName", "Variable1"],
            ["SitName", "Variable1"],
            ["TextureID", "Variable1"]
        ]
    }
registerMessage("ObjectProperties", ObjectProperties)

class ObjectPropertiesFamily(message.baseMessage):
    id = 10
    freq = 1
    trusted = True
    zero_coded = True
    blocks = [
        ("ObjectData", 1)
    ]
    structure = {
        "ObjectData": [
            ["RequestFlags", "U32"],
            ["ObjectID", "LLUUID"],
            ["OwnerID", "LLUUID"],
            ["GroupID", "LLUUID"],
            ["BaseMask", "U32"],
            ["OwnerMask", "U32"],
            ["GroupMask", "U32"],
            ["EveryoneMask", "U32"],
            ["NextOwnerMask", "U32"],
            ["OwnershipCost", "S32"],
            ["SaleType", "U8"],
            ["SalePrice", "S32"],
            ["Category", "U32"],
            ["LastOwnerID", "LLUUID"],
            ["Name", "Variable1"],
            ["Description", "Variable1"]
        ]
    }
registerMessage("ObjectPropertiesFamily", ObjectPropertiesFamily)

class RequestPayPrice(message.baseMessage):
    id = 161
    freq = 2
    trusted = False
    zero_coded = False
    blocks = [
        ("ObjectData", 1)
    ]
    structure = {
        "ObjectData": [
            ["ObjectID", "LLUUID"]
        ]
    }
registerMessage("RequestPayPrice", RequestPayPrice)

class PayPriceReply(message.baseMessage):
    id = 162
    freq = 2
    trusted = True
    zero_coded = False
    blocks = [
        ("ObjectData", 1),
        ("ButtonData", 0)
    ]
    structure = {
        "ObjectData": [
            ["ObjectID", "LLUUID"],
            ["DefaultPayPrice", "S32"]
        ],
        "ButtonData": [
            ["PayButton", "S32"]
        ]
    }
registerMessage("PayPriceReply", PayPriceReply)

class KickUser(message.baseMessage):
    id = 163
    freq = 2
    trusted = True
    zero_coded = False
    blocks = [
        ("TargetBlock", 1),
        ("UserInfo", 1)
    ]
    structure = {
        "TargetBlock": [
            ["TargetIP", "IPADDR"],
            ["TargetPort", "IPPORT"]
        ],
        "UserInfo": [
            ["AgentID", "LLUUID"],
            ["SessionID", "LLUUID"],
            ["Reason", "Variable2"]
        ]
    }
registerMessage("KickUser", KickUser)

class KickUserAck(message.baseMessage):
    id = 164
    freq = 2
    trusted = True
    zero_coded = False
    blocks = [
        ("UserInfo", 1)
    ]
    structure = {
        "UserInfo": [
            ["SessionID", "LLUUID"],
            ["Flags", "U32"]
        ]
    }
registerMessage("KickUserAck", KickUserAck)

class GodKickUser(message.baseMessage):
    id = 165
    freq = 2
    trusted = False
    zero_coded = False
    blocks = [
        ("UserInfo", 1)
    ]
    structure = {
        "UserInfo": [
            ["GodID", "LLUUID"],
            ["GodSessionID", "LLUUID"],
            ["AgentID", "LLUUID"],
            ["KickFlags", "U32"],
            ["Reason", "Variable2"]
        ]
    }
registerMessage("GodKickUser", GodKickUser)

class SystemKickUser(message.baseMessage):
    id = 166
    freq = 2
    trusted = True
    zero_coded = False
    blocks = [
        ("AgentInfo", 0)
    ]
    structure = {
        "AgentInfo": [
            ["AgentID", "LLUUID"]
        ]
    }
registerMessage("SystemKickUser", SystemKickUser)

class EjectUser(message.baseMessage):
    id = 167
    freq = 2
    trusted = False
    zero_coded = False
    blocks = [
        ("AgentData", 1),
        ("Data", 1)
    ]
    structure = {
        "AgentData": [
            ["AgentID", "LLUUID"],
            ["SessionID", "LLUUID"]
        ],
        "Data": [
            ["TargetID", "LLUUID"],
            ["Flags", "U32"]
        ]
    }
registerMessage("EjectUser", EjectUser)

class FreezeUser(message.baseMessage):
    id = 168
    freq = 2
    trusted = False
    zero_coded = False
    blocks = [
        ("AgentData", 1),
        ("Data", 1)
    ]
    structure = {
        "AgentData": [
            ["AgentID", "LLUUID"],
            ["SessionID", "LLUUID"]
        ],
        "Data": [
            ["TargetID", "LLUUID"],
            ["Flags", "U32"]
        ]
    }
registerMessage("FreezeUser", FreezeUser)

class AvatarPropertiesRequest(message.baseMessage):
    id = 169
    freq = 2
    trusted = False
    zero_coded = False
    blocks = [
        ("AgentData", 1)
    ]
    structure = {
        "AgentData": [
            ["AgentID", "LLUUID"],
            ["SessionID", "LLUUID"],
            ["AvatarID", "LLUUID"]
        ]
    }
registerMessage("AvatarPropertiesRequest", AvatarPropertiesRequest)

class AvatarPropertiesRequestBackend(message.baseMessage):
    id = 170
    freq = 2
    trusted = True
    zero_coded = False
    blocks = [
        ("AgentData", 1)
    ]
    structure = {
        "AgentData": [
            ["AgentID", "LLUUID"],
            ["AvatarID", "LLUUID"],
            ["GodLevel", "U8"],
            ["WebProfilesDisabled", "BOOL"]
        ]
    }
registerMessage("AvatarPropertiesRequestBackend", AvatarPropertiesRequestBackend)

class AvatarPropertiesReply(message.baseMessage):
    id = 171
    freq = 2
    trusted = True
    zero_coded = True
    blocks = [
        ("AgentData", 1),
        ("PropertiesData", 1)
    ]
    structure = {
        "AgentData": [
            ["AgentID", "LLUUID"],
            ["AvatarID", "LLUUID"]
        ],
        "PropertiesData": [
            ["ImageID", "LLUUID"],
            ["FLImageID", "LLUUID"],
            ["PartnerID", "LLUUID"],
            ["AboutText", "Variable2"],
            ["FLAboutText", "Variable1"],
            ["BornOn", "Variable1"],
            ["ProfileURL", "Variable1"],
            ["CharterMember", "Variable1"],
            ["Flags", "U32"]
        ]
    }
registerMessage("AvatarPropertiesReply", AvatarPropertiesReply)

class AvatarInterestsReply(message.baseMessage):
    id = 172
    freq = 2
    trusted = True
    zero_coded = True
    blocks = [
        ("AgentData", 1),
        ("PropertiesData", 1)
    ]
    structure = {
        "AgentData": [
            ["AgentID", "LLUUID"],
            ["AvatarID", "LLUUID"]
        ],
        "PropertiesData": [
            ["WantToMask", "U32"],
            ["WantToText", "Variable1"],
            ["SkillsMask", "U32"],
            ["SkillsText", "Variable1"],
            ["LanguagesText", "Variable1"]
        ]
    }
registerMessage("AvatarInterestsReply", AvatarInterestsReply)

class AvatarGroupsReply(message.baseMessage):
    id = 173
    freq = 2
    trusted = True
    zero_coded = True
    blocks = [
        ("AgentData", 1),
        ("GroupData", 0),
        ("NewGroupData", 1)
    ]
    structure = {
        "AgentData": [
            ["AgentID", "LLUUID"],
            ["AvatarID", "LLUUID"]
        ],
        "GroupData": [
            ["GroupPowers", "U64"],
            ["AcceptNotices", "BOOL"],
            ["GroupTitle", "Variable1"],
            ["GroupID", "LLUUID"],
            ["GroupName", "Variable1"],
            ["GroupInsigniaID", "LLUUID"]
        ],
        "NewGroupData": [
            ["ListInProfile", "BOOL"]
        ]
    }
registerMessage("AvatarGroupsReply", AvatarGroupsReply)

class AvatarPropertiesUpdate(message.baseMessage):
    id = 174
    freq = 2
    trusted = False
    zero_coded = True
    blocks = [
        ("AgentData", 1),
        ("PropertiesData", 1)
    ]
    structure = {
        "AgentData": [
            ["AgentID", "LLUUID"],
            ["SessionID", "LLUUID"]
        ],
        "PropertiesData": [
            ["ImageID", "LLUUID"],
            ["FLImageID", "LLUUID"],
            ["AboutText", "Variable2"],
            ["FLAboutText", "Variable1"],
            ["AllowPublish", "BOOL"],
            ["MaturePublish", "BOOL"],
            ["ProfileURL", "Variable1"]
        ]
    }
registerMessage("AvatarPropertiesUpdate", AvatarPropertiesUpdate)

class AvatarInterestsUpdate(message.baseMessage):
    id = 175
    freq = 2
    trusted = False
    zero_coded = True
    blocks = [
        ("AgentData", 1),
        ("PropertiesData", 1)
    ]
    structure = {
        "AgentData": [
            ["AgentID", "LLUUID"],
            ["SessionID", "LLUUID"]
        ],
        "PropertiesData": [
            ["WantToMask", "U32"],
            ["WantToText", "Variable1"],
            ["SkillsMask", "U32"],
            ["SkillsText", "Variable1"],
            ["LanguagesText", "Variable1"]
        ]
    }
registerMessage("AvatarInterestsUpdate", AvatarInterestsUpdate)

class AvatarNotesReply(message.baseMessage):
    id = 176
    freq = 2
    trusted = True
    zero_coded = False
    blocks = [
        ("AgentData", 1),
        ("Data", 1)
    ]
    structure = {
        "AgentData": [
            ["AgentID", "LLUUID"]
        ],
        "Data": [
            ["TargetID", "LLUUID"],
            ["Notes", "Variable2"]
        ]
    }
registerMessage("AvatarNotesReply", AvatarNotesReply)

class AvatarNotesUpdate(message.baseMessage):
    id = 177
    freq = 2
    trusted = False
    zero_coded = False
    blocks = [
        ("AgentData", 1),
        ("Data", 1)
    ]
    structure = {
        "AgentData": [
            ["AgentID", "LLUUID"],
            ["SessionID", "LLUUID"]
        ],
        "Data": [
            ["TargetID", "LLUUID"],
            ["Notes", "Variable2"]
        ]
    }
registerMessage("AvatarNotesUpdate", AvatarNotesUpdate)

class AvatarPicksReply(message.baseMessage):
    id = 178
    freq = 2
    trusted = True
    zero_coded = False
    blocks = [
        ("AgentData", 1),
        ("Data", 0)
    ]
    structure = {
        "AgentData": [
            ["AgentID", "LLUUID"],
            ["TargetID", "LLUUID"]
        ],
        "Data": [
            ["PickID", "LLUUID"],
            ["PickName", "Variable1"]
        ]
    }
registerMessage("AvatarPicksReply", AvatarPicksReply)

class EventInfoRequest(message.baseMessage):
    id = 179
    freq = 2
    trusted = False
    zero_coded = False
    blocks = [
        ("AgentData", 1),
        ("EventData", 1)
    ]
    structure = {
        "AgentData": [
            ["AgentID", "LLUUID"],
            ["SessionID", "LLUUID"]
        ],
        "EventData": [
            ["EventID", "U32"]
        ]
    }
registerMessage("EventInfoRequest", EventInfoRequest)

class EventInfoReply(message.baseMessage):
    id = 180
    freq = 2
    trusted = True
    zero_coded = False
    blocks = [
        ("AgentData", 1),
        ("EventData", 1)
    ]
    structure = {
        "AgentData": [
            ["AgentID", "LLUUID"]
        ],
        "EventData": [
            ["EventID", "U32"],
            ["Creator", "Variable1"],
            ["Name", "Variable1"],
            ["Category", "Variable1"],
            ["Desc", "Variable2"],
            ["Date", "Variable1"],
            ["DateUTC", "U32"],
            ["Duration", "U32"],
            ["Cover", "U32"],
            ["Amount", "U32"],
            ["SimName", "Variable1"],
            ["GlobalPos", "LLVector3d"],
            ["EventFlags", "U32"]
        ]
    }
registerMessage("EventInfoReply", EventInfoReply)

class EventNotificationAddRequest(message.baseMessage):
    id = 181
    freq = 2
    trusted = False
    zero_coded = False
    blocks = [
        ("AgentData", 1),
        ("EventData", 1)
    ]
    structure = {
        "AgentData": [
            ["AgentID", "LLUUID"],
            ["SessionID", "LLUUID"]
        ],
        "EventData": [
            ["EventID", "U32"]
        ]
    }
registerMessage("EventNotificationAddRequest", EventNotificationAddRequest)

class EventNotificationRemoveRequest(message.baseMessage):
    id = 182
    freq = 2
    trusted = False
    zero_coded = False
    blocks = [
        ("AgentData", 1),
        ("EventData", 1)
    ]
    structure = {
        "AgentData": [
            ["AgentID", "LLUUID"],
            ["SessionID", "LLUUID"]
        ],
        "EventData": [
            ["EventID", "U32"]
        ]
    }
registerMessage("EventNotificationRemoveRequest", EventNotificationRemoveRequest)

class EventGodDelete(message.baseMessage):
    id = 183
    freq = 2
    trusted = False
    zero_coded = False
    blocks = [
        ("AgentData", 1),
        ("EventData", 1),
        ("QueryData", 1)
    ]
    structure = {
        "AgentData": [
            ["AgentID", "LLUUID"],
            ["SessionID", "LLUUID"]
        ],
        "EventData": [
            ["EventID", "U32"]
        ],
        "QueryData": [
            ["QueryID", "LLUUID"],
            ["QueryText", "Variable1"],
            ["QueryFlags", "U32"],
            ["QueryStart", "S32"]
        ]
    }
registerMessage("EventGodDelete", EventGodDelete)

class PickInfoReply(message.baseMessage):
    id = 184
    freq = 2
    trusted = True
    zero_coded = False
    blocks = [
        ("AgentData", 1),
        ("Data", 1)
    ]
    structure = {
        "AgentData": [
            ["AgentID", "LLUUID"]
        ],
        "Data": [
            ["PickID", "LLUUID"],
            ["CreatorID", "LLUUID"],
            ["TopPick", "BOOL"],
            ["ParcelID", "LLUUID"],
            ["Name", "Variable1"],
            ["Desc", "Variable2"],
            ["SnapshotID", "LLUUID"],
            ["User", "Variable1"],
            ["OriginalName", "Variable1"],
            ["SimName", "Variable1"],
            ["PosGlobal", "LLVector3d"],
            ["SortOrder", "S32"],
            ["Enabled", "BOOL"]
        ]
    }
registerMessage("PickInfoReply", PickInfoReply)

class PickInfoUpdate(message.baseMessage):
    id = 185
    freq = 2
    trusted = False
    zero_coded = False
    blocks = [
        ("AgentData", 1),
        ("Data", 1)
    ]
    structure = {
        "AgentData": [
            ["AgentID", "LLUUID"],
            ["SessionID", "LLUUID"]
        ],
        "Data": [
            ["PickID", "LLUUID"],
            ["CreatorID", "LLUUID"],
            ["TopPick", "BOOL"],
            ["ParcelID", "LLUUID"],
            ["Name", "Variable1"],
            ["Desc", "Variable2"],
            ["SnapshotID", "LLUUID"],
            ["PosGlobal", "LLVector3d"],
            ["SortOrder", "S32"],
            ["Enabled", "BOOL"]
        ]
    }
registerMessage("PickInfoUpdate", PickInfoUpdate)

class PickDelete(message.baseMessage):
    id = 186
    freq = 2
    trusted = False
    zero_coded = False
    blocks = [
        ("AgentData", 1),
        ("Data", 1)
    ]
    structure = {
        "AgentData": [
            ["AgentID", "LLUUID"],
            ["SessionID", "LLUUID"]
        ],
        "Data": [
            ["PickID", "LLUUID"]
        ]
    }
registerMessage("PickDelete", PickDelete)

class PickGodDelete(message.baseMessage):
    id = 187
    freq = 2
    trusted = False
    zero_coded = False
    blocks = [
        ("AgentData", 1),
        ("Data", 1)
    ]
    structure = {
        "AgentData": [
            ["AgentID", "LLUUID"],
            ["SessionID", "LLUUID"]
        ],
        "Data": [
            ["PickID", "LLUUID"],
            ["QueryID", "LLUUID"]
        ]
    }
registerMessage("PickGodDelete", PickGodDelete)

class ScriptQuestion(message.baseMessage):
    id = 188
    freq = 2
    trusted = True
    zero_coded = False
    blocks = [
        ("Data", 1),
        ("Experience", 1)
    ]
    structure = {
        "Data": [
            ["TaskID", "LLUUID"],
            ["ItemID", "LLUUID"],
            ["ObjectName", "Variable1"],
            ["ObjectOwner", "Variable1"],
            ["Questions", "S32"]
        ],
        "Experience": [
            ["ExperienceID", "LLUUID"]
        ]
    }
registerMessage("ScriptQuestion", ScriptQuestion)

class ScriptControlChange(message.baseMessage):
    id = 189
    freq = 2
    trusted = True
    zero_coded = False
    blocks = [
        ("Data", 0)
    ]
    structure = {
        "Data": [
            ["TakeControls", "BOOL"],
            ["Controls", "U32"],
            ["PassToAgent", "BOOL"]
        ]
    }
registerMessage("ScriptControlChange", ScriptControlChange)

class ScriptDialog(message.baseMessage):
    id = 190
    freq = 2
    trusted = True
    zero_coded = True
    blocks = [
        ("Data", 1),
        ("Buttons", 0),
        ("OwnerData", 0)
    ]
    structure = {
        "Data": [
            ["ObjectID", "LLUUID"],
            ["FirstName", "Variable1"],
            ["LastName", "Variable1"],
            ["ObjectName", "Variable1"],
            ["Message", "Variable2"],
            ["ChatChannel", "S32"],
            ["ImageID", "LLUUID"]
        ],
        "Buttons": [
            ["ButtonLabel", "Variable1"]
        ],
        "OwnerData": [
            ["OwnerID", "LLUUID"]
        ]
    }
registerMessage("ScriptDialog", ScriptDialog)

class ScriptDialogReply(message.baseMessage):
    id = 191
    freq = 2
    trusted = False
    zero_coded = True
    blocks = [
        ("AgentData", 1),
        ("Data", 1)
    ]
    structure = {
        "AgentData": [
            ["AgentID", "LLUUID"],
            ["SessionID", "LLUUID"]
        ],
        "Data": [
            ["ObjectID", "LLUUID"],
            ["ChatChannel", "S32"],
            ["ButtonIndex", "S32"],
            ["ButtonLabel", "Variable1"]
        ]
    }
registerMessage("ScriptDialogReply", ScriptDialogReply)

class ForceScriptControlRelease(message.baseMessage):
    id = 192
    freq = 2
    trusted = False
    zero_coded = False
    blocks = [
        ("AgentData", 1)
    ]
    structure = {
        "AgentData": [
            ["AgentID", "LLUUID"],
            ["SessionID", "LLUUID"]
        ]
    }
registerMessage("ForceScriptControlRelease", ForceScriptControlRelease)

class RevokePermissions(message.baseMessage):
    id = 193
    freq = 2
    trusted = False
    zero_coded = False
    blocks = [
        ("AgentData", 1),
        ("Data", 1)
    ]
    structure = {
        "AgentData": [
            ["AgentID", "LLUUID"],
            ["SessionID", "LLUUID"]
        ],
        "Data": [
            ["ObjectID", "LLUUID"],
            ["ObjectPermissions", "U32"]
        ]
    }
registerMessage("RevokePermissions", RevokePermissions)

class LoadURL(message.baseMessage):
    id = 194
    freq = 2
    trusted = True
    zero_coded = False
    blocks = [
        ("Data", 1)
    ]
    structure = {
        "Data": [
            ["ObjectName", "Variable1"],
            ["ObjectID", "LLUUID"],
            ["OwnerID", "LLUUID"],
            ["OwnerIsGroup", "BOOL"],
            ["Message", "Variable1"],
            ["URL", "Variable1"]
        ]
    }
registerMessage("LoadURL", LoadURL)

class ScriptTeleportRequest(message.baseMessage):
    id = 195
    freq = 2
    trusted = True
    zero_coded = False
    blocks = [
        ("Data", 1)
    ]
    structure = {
        "Data": [
            ["ObjectName", "Variable1"],
            ["SimName", "Variable1"],
            ["SimPosition", "LLVector3"],
            ["LookAt", "LLVector3"]
        ]
    }
registerMessage("ScriptTeleportRequest", ScriptTeleportRequest)

class ParcelOverlay(message.baseMessage):
    id = 196
    freq = 2
    trusted = True
    zero_coded = True
    blocks = [
        ("ParcelData", 1)
    ]
    structure = {
        "ParcelData": [
            ["SequenceID", "S32"],
            ["Data", "Variable2"]
        ]
    }
registerMessage("ParcelOverlay", ParcelOverlay)

class ParcelPropertiesRequest(message.baseMessage):
    id = 11
    freq = 1
    trusted = False
    zero_coded = True
    blocks = [
        ("AgentData", 1),
        ("ParcelData", 1)
    ]
    structure = {
        "AgentData": [
            ["AgentID", "LLUUID"],
            ["SessionID", "LLUUID"]
        ],
        "ParcelData": [
            ["SequenceID", "S32"],
            ["West", "F32"],
            ["South", "F32"],
            ["East", "F32"],
            ["North", "F32"],
            ["SnapSelection", "BOOL"]
        ]
    }
registerMessage("ParcelPropertiesRequest", ParcelPropertiesRequest)

class ParcelPropertiesRequestByID(message.baseMessage):
    id = 197
    freq = 2
    trusted = False
    zero_coded = True
    blocks = [
        ("AgentData", 1),
        ("ParcelData", 1)
    ]
    structure = {
        "AgentData": [
            ["AgentID", "LLUUID"],
            ["SessionID", "LLUUID"]
        ],
        "ParcelData": [
            ["SequenceID", "S32"],
            ["LocalID", "S32"]
        ]
    }
registerMessage("ParcelPropertiesRequestByID", ParcelPropertiesRequestByID)

class ParcelProperties(message.baseMessage):
    id = 23
    freq = 0
    trusted = True
    zero_coded = True
    blocks = [
        ("ParcelData", 1),
        ("AgeVerificationBlock", 1)
    ]
    structure = {
        "ParcelData": [
            ["RequestResult", "S32"],
            ["SequenceID", "S32"],
            ["SnapSelection", "BOOL"],
            ["SelfCount", "S32"],
            ["OtherCount", "S32"],
            ["PublicCount", "S32"],
            ["LocalID", "S32"],
            ["OwnerID", "LLUUID"],
            ["IsGroupOwned", "BOOL"],
            ["AuctionID", "U32"],
            ["ClaimDate", "S32"],
            ["ClaimPrice", "S32"],
            ["RentPrice", "S32"],
            ["AABBMin", "LLVector3"],
            ["AABBMax", "LLVector3"],
            ["Bitmap", "Variable2"],
            ["Area", "S32"],
            ["Status", "U8"],
            ["SimWideMaxPrims", "S32"],
            ["SimWideTotalPrims", "S32"],
            ["MaxPrims", "S32"],
            ["TotalPrims", "S32"],
            ["OwnerPrims", "S32"],
            ["GroupPrims", "S32"],
            ["OtherPrims", "S32"],
            ["SelectedPrims", "S32"],
            ["ParcelPrimBonus", "F32"],
            ["OtherCleanTime", "S32"],
            ["ParcelFlags", "U32"],
            ["SalePrice", "S32"],
            ["Name", "Variable1"],
            ["Desc", "Variable1"],
            ["MusicURL", "Variable1"],
            ["MediaURL", "Variable1"],
            ["MediaID", "LLUUID"],
            ["MediaAutoScale", "U8"],
            ["GroupID", "LLUUID"],
            ["PassPrice", "S32"],
            ["PassHours", "F32"],
            ["Category", "U8"],
            ["AuthBuyerID", "LLUUID"],
            ["SnapshotID", "LLUUID"],
            ["UserLocation", "LLVector3"],
            ["UserLookAt", "LLVector3"],
            ["LandingType", "U8"],
            ["RegionPushOverride", "BOOL"],
            ["RegionDenyAnonymous", "BOOL"],
            ["RegionDenyIdentified", "BOOL"],
            ["RegionDenyTransacted", "BOOL"]
        ],
        "AgeVerificationBlock": [
            ["RegionDenyAgeUnverified", "BOOL"]
        ]
    }
registerMessage("ParcelProperties", ParcelProperties)

class ParcelPropertiesUpdate(message.baseMessage):
    id = 198
    freq = 2
    trusted = False
    zero_coded = True
    blocks = [
        ("AgentData", 1),
        ("ParcelData", 1)
    ]
    structure = {
        "AgentData": [
            ["AgentID", "LLUUID"],
            ["SessionID", "LLUUID"]
        ],
        "ParcelData": [
            ["LocalID", "S32"],
            ["Flags", "U32"],
            ["ParcelFlags", "U32"],
            ["SalePrice", "S32"],
            ["Name", "Variable1"],
            ["Desc", "Variable1"],
            ["MusicURL", "Variable1"],
            ["MediaURL", "Variable1"],
            ["MediaID", "LLUUID"],
            ["MediaAutoScale", "U8"],
            ["GroupID", "LLUUID"],
            ["PassPrice", "S32"],
            ["PassHours", "F32"],
            ["Category", "U8"],
            ["AuthBuyerID", "LLUUID"],
            ["SnapshotID", "LLUUID"],
            ["UserLocation", "LLVector3"],
            ["UserLookAt", "LLVector3"],
            ["LandingType", "U8"]
        ]
    }
registerMessage("ParcelPropertiesUpdate", ParcelPropertiesUpdate)

class ParcelReturnObjects(message.baseMessage):
    id = 199
    freq = 2
    trusted = False
    zero_coded = True
    blocks = [
        ("AgentData", 1),
        ("ParcelData", 1),
        ("TaskIDs", 0),
        ("OwnerIDs", 0)
    ]
    structure = {
        "AgentData": [
            ["AgentID", "LLUUID"],
            ["SessionID", "LLUUID"]
        ],
        "ParcelData": [
            ["LocalID", "S32"],
            ["ReturnType", "U32"]
        ],
        "TaskIDs": [
            ["TaskID", "LLUUID"]
        ],
        "OwnerIDs": [
            ["OwnerID", "LLUUID"]
        ]
    }
registerMessage("ParcelReturnObjects", ParcelReturnObjects)

class ParcelSetOtherCleanTime(message.baseMessage):
    id = 200
    freq = 2
    trusted = False
    zero_coded = True
    blocks = [
        ("AgentData", 1),
        ("ParcelData", 1)
    ]
    structure = {
        "AgentData": [
            ["AgentID", "LLUUID"],
            ["SessionID", "LLUUID"]
        ],
        "ParcelData": [
            ["LocalID", "S32"],
            ["OtherCleanTime", "S32"]
        ]
    }
registerMessage("ParcelSetOtherCleanTime", ParcelSetOtherCleanTime)

class ParcelDisableObjects(message.baseMessage):
    id = 201
    freq = 2
    trusted = False
    zero_coded = True
    blocks = [
        ("AgentData", 1),
        ("ParcelData", 1),
        ("TaskIDs", 0),
        ("OwnerIDs", 0)
    ]
    structure = {
        "AgentData": [
            ["AgentID", "LLUUID"],
            ["SessionID", "LLUUID"]
        ],
        "ParcelData": [
            ["LocalID", "S32"],
            ["ReturnType", "U32"]
        ],
        "TaskIDs": [
            ["TaskID", "LLUUID"]
        ],
        "OwnerIDs": [
            ["OwnerID", "LLUUID"]
        ]
    }
registerMessage("ParcelDisableObjects", ParcelDisableObjects)

class ParcelSelectObjects(message.baseMessage):
    id = 202
    freq = 2
    trusted = False
    zero_coded = True
    blocks = [
        ("AgentData", 1),
        ("ParcelData", 1),
        ("ReturnIDs", 0)
    ]
    structure = {
        "AgentData": [
            ["AgentID", "LLUUID"],
            ["SessionID", "LLUUID"]
        ],
        "ParcelData": [
            ["LocalID", "S32"],
            ["ReturnType", "U32"]
        ],
        "ReturnIDs": [
            ["ReturnID", "LLUUID"]
        ]
    }
registerMessage("ParcelSelectObjects", ParcelSelectObjects)

class EstateCovenantRequest(message.baseMessage):
    id = 203
    freq = 2
    trusted = False
    zero_coded = False
    blocks = [
        ("AgentData", 1)
    ]
    structure = {
        "AgentData": [
            ["AgentID", "LLUUID"],
            ["SessionID", "LLUUID"]
        ]
    }
registerMessage("EstateCovenantRequest", EstateCovenantRequest)

class EstateCovenantReply(message.baseMessage):
    id = 204
    freq = 2
    trusted = True
    zero_coded = False
    blocks = [
        ("Data", 1)
    ]
    structure = {
        "Data": [
            ["CovenantID", "LLUUID"],
            ["CovenantTimestamp", "U32"],
            ["EstateName", "Variable1"],
            ["EstateOwnerID", "LLUUID"]
        ]
    }
registerMessage("EstateCovenantReply", EstateCovenantReply)

class ForceObjectSelect(message.baseMessage):
    id = 205
    freq = 2
    trusted = True
    zero_coded = False
    blocks = [
        ("Header", 1),
        ("Data", 0)
    ]
    structure = {
        "Header": [
            ["ResetList", "BOOL"]
        ],
        "Data": [
            ["LocalID", "U32"]
        ]
    }
registerMessage("ForceObjectSelect", ForceObjectSelect)

class ParcelBuyPass(message.baseMessage):
    id = 206
    freq = 2
    trusted = False
    zero_coded = False
    blocks = [
        ("AgentData", 1),
        ("ParcelData", 1)
    ]
    structure = {
        "AgentData": [
            ["AgentID", "LLUUID"],
            ["SessionID", "LLUUID"]
        ],
        "ParcelData": [
            ["LocalID", "S32"]
        ]
    }
registerMessage("ParcelBuyPass", ParcelBuyPass)

class ParcelDeedToGroup(message.baseMessage):
    id = 207
    freq = 2
    trusted = False
    zero_coded = False
    blocks = [
        ("AgentData", 1),
        ("Data", 1)
    ]
    structure = {
        "AgentData": [
            ["AgentID", "LLUUID"],
            ["SessionID", "LLUUID"]
        ],
        "Data": [
            ["GroupID", "LLUUID"],
            ["LocalID", "S32"]
        ]
    }
registerMessage("ParcelDeedToGroup", ParcelDeedToGroup)

class ParcelReclaim(message.baseMessage):
    id = 208
    freq = 2
    trusted = False
    zero_coded = False
    blocks = [
        ("AgentData", 1),
        ("Data", 1)
    ]
    structure = {
        "AgentData": [
            ["AgentID", "LLUUID"],
            ["SessionID", "LLUUID"]
        ],
        "Data": [
            ["LocalID", "S32"]
        ]
    }
registerMessage("ParcelReclaim", ParcelReclaim)

class ParcelClaim(message.baseMessage):
    id = 209
    freq = 2
    trusted = False
    zero_coded = True
    blocks = [
        ("AgentData", 1),
        ("Data", 1),
        ("ParcelData", 0)
    ]
    structure = {
        "AgentData": [
            ["AgentID", "LLUUID"],
            ["SessionID", "LLUUID"]
        ],
        "Data": [
            ["GroupID", "LLUUID"],
            ["IsGroupOwned", "BOOL"],
            ["Final", "BOOL"]
        ],
        "ParcelData": [
            ["West", "F32"],
            ["South", "F32"],
            ["East", "F32"],
            ["North", "F32"]
        ]
    }
registerMessage("ParcelClaim", ParcelClaim)

class ParcelJoin(message.baseMessage):
    id = 210
    freq = 2
    trusted = False
    zero_coded = False
    blocks = [
        ("AgentData", 1),
        ("ParcelData", 1)
    ]
    structure = {
        "AgentData": [
            ["AgentID", "LLUUID"],
            ["SessionID", "LLUUID"]
        ],
        "ParcelData": [
            ["West", "F32"],
            ["South", "F32"],
            ["East", "F32"],
            ["North", "F32"]
        ]
    }
registerMessage("ParcelJoin", ParcelJoin)

class ParcelDivide(message.baseMessage):
    id = 211
    freq = 2
    trusted = False
    zero_coded = False
    blocks = [
        ("AgentData", 1),
        ("ParcelData", 1)
    ]
    structure = {
        "AgentData": [
            ["AgentID", "LLUUID"],
            ["SessionID", "LLUUID"]
        ],
        "ParcelData": [
            ["West", "F32"],
            ["South", "F32"],
            ["East", "F32"],
            ["North", "F32"]
        ]
    }
registerMessage("ParcelDivide", ParcelDivide)

class ParcelRelease(message.baseMessage):
    id = 212
    freq = 2
    trusted = False
    zero_coded = False
    blocks = [
        ("AgentData", 1),
        ("Data", 1)
    ]
    structure = {
        "AgentData": [
            ["AgentID", "LLUUID"],
            ["SessionID", "LLUUID"]
        ],
        "Data": [
            ["LocalID", "S32"]
        ]
    }
registerMessage("ParcelRelease", ParcelRelease)

class ParcelBuy(message.baseMessage):
    id = 213
    freq = 2
    trusted = False
    zero_coded = True
    blocks = [
        ("AgentData", 1),
        ("Data", 1),
        ("ParcelData", 1)
    ]
    structure = {
        "AgentData": [
            ["AgentID", "LLUUID"],
            ["SessionID", "LLUUID"]
        ],
        "Data": [
            ["GroupID", "LLUUID"],
            ["IsGroupOwned", "BOOL"],
            ["RemoveContribution", "BOOL"],
            ["LocalID", "S32"],
            ["Final", "BOOL"]
        ],
        "ParcelData": [
            ["Price", "S32"],
            ["Area", "S32"]
        ]
    }
registerMessage("ParcelBuy", ParcelBuy)

class ParcelGodForceOwner(message.baseMessage):
    id = 214
    freq = 2
    trusted = False
    zero_coded = True
    blocks = [
        ("AgentData", 1),
        ("Data", 1)
    ]
    structure = {
        "AgentData": [
            ["AgentID", "LLUUID"],
            ["SessionID", "LLUUID"]
        ],
        "Data": [
            ["OwnerID", "LLUUID"],
            ["LocalID", "S32"]
        ]
    }
registerMessage("ParcelGodForceOwner", ParcelGodForceOwner)

class ParcelAccessListRequest(message.baseMessage):
    id = 215
    freq = 2
    trusted = False
    zero_coded = True
    blocks = [
        ("AgentData", 1),
        ("Data", 1)
    ]
    structure = {
        "AgentData": [
            ["AgentID", "LLUUID"],
            ["SessionID", "LLUUID"]
        ],
        "Data": [
            ["SequenceID", "S32"],
            ["Flags", "U32"],
            ["LocalID", "S32"]
        ]
    }
registerMessage("ParcelAccessListRequest", ParcelAccessListRequest)

class ParcelAccessListReply(message.baseMessage):
    id = 216
    freq = 2
    trusted = True
    zero_coded = True
    blocks = [
        ("Data", 1),
        ("List", 0)
    ]
    structure = {
        "Data": [
            ["AgentID", "LLUUID"],
            ["SequenceID", "S32"],
            ["Flags", "U32"],
            ["LocalID", "S32"]
        ],
        "List": [
            ["ID", "LLUUID"],
            ["Time", "S32"],
            ["Flags", "U32"]
        ]
    }
registerMessage("ParcelAccessListReply", ParcelAccessListReply)

class ParcelAccessListUpdate(message.baseMessage):
    id = 217
    freq = 2
    trusted = False
    zero_coded = True
    blocks = [
        ("AgentData", 1),
        ("Data", 1),
        ("List", 0)
    ]
    structure = {
        "AgentData": [
            ["AgentID", "LLUUID"],
            ["SessionID", "LLUUID"]
        ],
        "Data": [
            ["Flags", "U32"],
            ["LocalID", "S32"],
            ["TransactionID", "LLUUID"],
            ["SequenceID", "S32"],
            ["Sections", "S32"]
        ],
        "List": [
            ["ID", "LLUUID"],
            ["Time", "S32"],
            ["Flags", "U32"]
        ]
    }
registerMessage("ParcelAccessListUpdate", ParcelAccessListUpdate)

class ParcelDwellRequest(message.baseMessage):
    id = 218
    freq = 2
    trusted = False
    zero_coded = False
    blocks = [
        ("AgentData", 1),
        ("Data", 1)
    ]
    structure = {
        "AgentData": [
            ["AgentID", "LLUUID"],
            ["SessionID", "LLUUID"]
        ],
        "Data": [
            ["LocalID", "S32"],
            ["ParcelID", "LLUUID"]
        ]
    }
registerMessage("ParcelDwellRequest", ParcelDwellRequest)

class ParcelDwellReply(message.baseMessage):
    id = 219
    freq = 2
    trusted = True
    zero_coded = False
    blocks = [
        ("AgentData", 1),
        ("Data", 1)
    ]
    structure = {
        "AgentData": [
            ["AgentID", "LLUUID"]
        ],
        "Data": [
            ["LocalID", "S32"],
            ["ParcelID", "LLUUID"],
            ["Dwell", "F32"]
        ]
    }
registerMessage("ParcelDwellReply", ParcelDwellReply)

class RequestParcelTransfer(message.baseMessage):
    id = 220
    freq = 2
    trusted = True
    zero_coded = True
    blocks = [
        ("Data", 1),
        ("RegionData", 1)
    ]
    structure = {
        "Data": [
            ["TransactionID", "LLUUID"],
            ["TransactionTime", "U32"],
            ["SourceID", "LLUUID"],
            ["DestID", "LLUUID"],
            ["OwnerID", "LLUUID"],
            ["Flags", "U8"],
            ["TransactionType", "S32"],
            ["Amount", "S32"],
            ["BillableArea", "S32"],
            ["ActualArea", "S32"],
            ["Final", "BOOL"]
        ],
        "RegionData": [
            ["RegionID", "LLUUID"],
            ["GridX", "U32"],
            ["GridY", "U32"]
        ]
    }
registerMessage("RequestParcelTransfer", RequestParcelTransfer)

class UpdateParcel(message.baseMessage):
    id = 221
    freq = 2
    trusted = True
    zero_coded = True
    blocks = [
        ("ParcelData", 1)
    ]
    structure = {
        "ParcelData": [
            ["ParcelID", "LLUUID"],
            ["RegionHandle", "U64"],
            ["OwnerID", "LLUUID"],
            ["GroupOwned", "BOOL"],
            ["Status", "U8"],
            ["Name", "Variable1"],
            ["Description", "Variable1"],
            ["MusicURL", "Variable1"],
            ["RegionX", "F32"],
            ["RegionY", "F32"],
            ["ActualArea", "S32"],
            ["BillableArea", "S32"],
            ["ShowDir", "BOOL"],
            ["IsForSale", "BOOL"],
            ["Category", "U8"],
            ["SnapshotID", "LLUUID"],
            ["UserLocation", "LLVector3"],
            ["SalePrice", "S32"],
            ["AuthorizedBuyerID", "LLUUID"],
            ["AllowPublish", "BOOL"],
            ["MaturePublish", "BOOL"]
        ]
    }
registerMessage("UpdateParcel", UpdateParcel)

class RemoveParcel(message.baseMessage):
    id = 222
    freq = 2
    trusted = True
    zero_coded = False
    blocks = [
        ("ParcelData", 0)
    ]
    structure = {
        "ParcelData": [
            ["ParcelID", "LLUUID"]
        ]
    }
registerMessage("RemoveParcel", RemoveParcel)

class MergeParcel(message.baseMessage):
    id = 223
    freq = 2
    trusted = True
    zero_coded = False
    blocks = [
        ("MasterParcelData", 1),
        ("SlaveParcelData", 0)
    ]
    structure = {
        "MasterParcelData": [
            ["MasterID", "LLUUID"]
        ],
        "SlaveParcelData": [
            ["SlaveID", "LLUUID"]
        ]
    }
registerMessage("MergeParcel", MergeParcel)

class LogParcelChanges(message.baseMessage):
    id = 224
    freq = 2
    trusted = True
    zero_coded = True
    blocks = [
        ("AgentData", 1),
        ("RegionData", 1),
        ("ParcelData", 0)
    ]
    structure = {
        "AgentData": [
            ["AgentID", "LLUUID"]
        ],
        "RegionData": [
            ["RegionHandle", "U64"]
        ],
        "ParcelData": [
            ["ParcelID", "LLUUID"],
            ["OwnerID", "LLUUID"],
            ["IsOwnerGroup", "BOOL"],
            ["ActualArea", "S32"],
            ["Action", "S8"],
            ["TransactionID", "LLUUID"]
        ]
    }
registerMessage("LogParcelChanges", LogParcelChanges)

class CheckParcelSales(message.baseMessage):
    id = 225
    freq = 2
    trusted = True
    zero_coded = False
    blocks = [
        ("RegionData", 0)
    ]
    structure = {
        "RegionData": [
            ["RegionHandle", "U64"]
        ]
    }
registerMessage("CheckParcelSales", CheckParcelSales)

class ParcelSales(message.baseMessage):
    id = 226
    freq = 2
    trusted = True
    zero_coded = False
    blocks = [
        ("ParcelData", 0)
    ]
    structure = {
        "ParcelData": [
            ["ParcelID", "LLUUID"],
            ["BuyerID", "LLUUID"]
        ]
    }
registerMessage("ParcelSales", ParcelSales)

class ParcelGodMarkAsContent(message.baseMessage):
    id = 227
    freq = 2
    trusted = False
    zero_coded = False
    blocks = [
        ("AgentData", 1),
        ("ParcelData", 1)
    ]
    structure = {
        "AgentData": [
            ["AgentID", "LLUUID"],
            ["SessionID", "LLUUID"]
        ],
        "ParcelData": [
            ["LocalID", "S32"]
        ]
    }
registerMessage("ParcelGodMarkAsContent", ParcelGodMarkAsContent)

class ViewerStartAuction(message.baseMessage):
    id = 228
    freq = 2
    trusted = False
    zero_coded = False
    blocks = [
        ("AgentData", 1),
        ("ParcelData", 1)
    ]
    structure = {
        "AgentData": [
            ["AgentID", "LLUUID"],
            ["SessionID", "LLUUID"]
        ],
        "ParcelData": [
            ["LocalID", "S32"],
            ["SnapshotID", "LLUUID"]
        ]
    }
registerMessage("ViewerStartAuction", ViewerStartAuction)

class StartAuction(message.baseMessage):
    id = 229
    freq = 2
    trusted = True
    zero_coded = False
    blocks = [
        ("AgentData", 1),
        ("ParcelData", 1)
    ]
    structure = {
        "AgentData": [
            ["AgentID", "LLUUID"]
        ],
        "ParcelData": [
            ["ParcelID", "LLUUID"],
            ["SnapshotID", "LLUUID"],
            ["Name", "Variable1"]
        ]
    }
registerMessage("StartAuction", StartAuction)

class ConfirmAuctionStart(message.baseMessage):
    id = 230
    freq = 2
    trusted = True
    zero_coded = False
    blocks = [
        ("AuctionData", 1)
    ]
    structure = {
        "AuctionData": [
            ["ParcelID", "LLUUID"],
            ["AuctionID", "U32"]
        ]
    }
registerMessage("ConfirmAuctionStart", ConfirmAuctionStart)

class CompleteAuction(message.baseMessage):
    id = 231
    freq = 2
    trusted = True
    zero_coded = False
    blocks = [
        ("ParcelData", 0)
    ]
    structure = {
        "ParcelData": [
            ["ParcelID", "LLUUID"]
        ]
    }
registerMessage("CompleteAuction", CompleteAuction)

class CancelAuction(message.baseMessage):
    id = 232
    freq = 2
    trusted = True
    zero_coded = False
    blocks = [
        ("ParcelData", 0)
    ]
    structure = {
        "ParcelData": [
            ["ParcelID", "LLUUID"]
        ]
    }
registerMessage("CancelAuction", CancelAuction)

class CheckParcelAuctions(message.baseMessage):
    id = 233
    freq = 2
    trusted = True
    zero_coded = False
    blocks = [
        ("RegionData", 0)
    ]
    structure = {
        "RegionData": [
            ["RegionHandle", "U64"]
        ]
    }
registerMessage("CheckParcelAuctions", CheckParcelAuctions)

class ParcelAuctions(message.baseMessage):
    id = 234
    freq = 2
    trusted = True
    zero_coded = False
    blocks = [
        ("ParcelData", 0)
    ]
    structure = {
        "ParcelData": [
            ["ParcelID", "LLUUID"],
            ["WinnerID", "LLUUID"]
        ]
    }
registerMessage("ParcelAuctions", ParcelAuctions)

class UUIDNameRequest(message.baseMessage):
    id = 235
    freq = 2
    trusted = False
    zero_coded = False
    blocks = [
        ("UUIDNameBlock", 0)
    ]
    structure = {
        "UUIDNameBlock": [
            ["ID", "LLUUID"]
        ]
    }
registerMessage("UUIDNameRequest", UUIDNameRequest)

class UUIDNameReply(message.baseMessage):
    id = 236
    freq = 2
    trusted = True
    zero_coded = False
    blocks = [
        ("UUIDNameBlock", 0)
    ]
    structure = {
        "UUIDNameBlock": [
            ["ID", "LLUUID"],
            ["FirstName", "Variable1"],
            ["LastName", "Variable1"]
        ]
    }
registerMessage("UUIDNameReply", UUIDNameReply)

class UUIDGroupNameRequest(message.baseMessage):
    id = 237
    freq = 2
    trusted = False
    zero_coded = False
    blocks = [
        ("UUIDNameBlock", 0)
    ]
    structure = {
        "UUIDNameBlock": [
            ["ID", "LLUUID"]
        ]
    }
registerMessage("UUIDGroupNameRequest", UUIDGroupNameRequest)

class UUIDGroupNameReply(message.baseMessage):
    id = 238
    freq = 2
    trusted = True
    zero_coded = False
    blocks = [
        ("UUIDNameBlock", 0)
    ]
    structure = {
        "UUIDNameBlock": [
            ["ID", "LLUUID"],
            ["GroupName", "Variable1"]
        ]
    }
registerMessage("UUIDGroupNameReply", UUIDGroupNameReply)

class ChatPass(message.baseMessage):
    id = 239
    freq = 2
    trusted = True
    zero_coded = True
    blocks = [
        ("ChatData", 1)
    ]
    structure = {
        "ChatData": [
            ["Channel", "S32"],
            ["Position", "LLVector3"],
            ["ID", "LLUUID"],
            ["OwnerID", "LLUUID"],
            ["Name", "Variable1"],
            ["SourceType", "U8"],
            ["Type", "U8"],
            ["Radius", "F32"],
            ["SimAccess", "U8"],
            ["Message", "Variable2"]
        ]
    }
registerMessage("ChatPass", ChatPass)

class EdgeDataPacket(message.baseMessage):
    id = 24
    freq = 0
    trusted = True
    zero_coded = True
    blocks = [
        ("EdgeData", 1)
    ]
    structure = {
        "EdgeData": [
            ["LayerType", "U8"],
            ["Direction", "U8"],
            ["LayerData", "Variable2"]
        ]
    }
registerMessage("EdgeDataPacket", EdgeDataPacket)

class SimStatus(message.baseMessage):
    id = 12
    freq = 1
    trusted = True
    zero_coded = False
    blocks = [
        ("SimStatus", 1)
    ]
    structure = {
        "SimStatus": [
            ["CanAcceptAgents", "BOOL"],
            ["CanAcceptTasks", "BOOL"]
        ]
    }
registerMessage("SimStatus", SimStatus)

class ChildAgentUpdate(message.baseMessage):
    id = 25
    freq = 0
    trusted = True
    zero_coded = True
    blocks = [
        ("AgentData", 1),
        ("GroupData", 0),
        ("AnimationData", 0),
        ("GranterBlock", 0),
        ("NVPairData", 0),
        ("VisualParam", 0),
        ("AgentAccess", 0),
        ("AgentInfo", 0)
    ]
    structure = {
        "AgentData": [
            ["RegionHandle", "U64"],
            ["ViewerCircuitCode", "U32"],
            ["AgentID", "LLUUID"],
            ["SessionID", "LLUUID"],
            ["AgentPos", "LLVector3"],
            ["AgentVel", "LLVector3"],
            ["Center", "LLVector3"],
            ["Size", "LLVector3"],
            ["AtAxis", "LLVector3"],
            ["LeftAxis", "LLVector3"],
            ["UpAxis", "LLVector3"],
            ["ChangedGrid", "BOOL"],
            ["Far", "F32"],
            ["Aspect", "F32"],
            ["Throttles", "Variable1"],
            ["LocomotionState", "U32"],
            ["HeadRotation", "LLQuaternion"],
            ["BodyRotation", "LLQuaternion"],
            ["ControlFlags", "U32"],
            ["EnergyLevel", "F32"],
            ["GodLevel", "U8"],
            ["AlwaysRun", "BOOL"],
            ["PreyAgent", "LLUUID"],
            ["AgentAccess", "U8"],
            ["AgentTextures", "Variable2"],
            ["ActiveGroupID", "LLUUID"]
        ],
        "GroupData": [
            ["GroupID", "LLUUID"],
            ["GroupPowers", "U64"],
            ["AcceptNotices", "BOOL"]
        ],
        "AnimationData": [
            ["Animation", "LLUUID"],
            ["ObjectID", "LLUUID"]
        ],
        "GranterBlock": [
            ["GranterID", "LLUUID"]
        ],
        "NVPairData": [
            ["NVPairs", "Variable2"]
        ],
        "VisualParam": [
            ["ParamValue", "U8"]
        ],
        "AgentAccess": [
            ["AgentLegacyAccess", "U8"],
            ["AgentMaxAccess", "U8"]
        ],
        "AgentInfo": [
            ["Flags", "U32"]
        ]
    }
registerMessage("ChildAgentUpdate", ChildAgentUpdate)

class ChildAgentAlive(message.baseMessage):
    id = 26
    freq = 0
    trusted = True
    zero_coded = False
    blocks = [
        ("AgentData", 1)
    ]
    structure = {
        "AgentData": [
            ["RegionHandle", "U64"],
            ["ViewerCircuitCode", "U32"],
            ["AgentID", "LLUUID"],
            ["SessionID", "LLUUID"]
        ]
    }
registerMessage("ChildAgentAlive", ChildAgentAlive)

class ChildAgentPositionUpdate(message.baseMessage):
    id = 27
    freq = 0
    trusted = True
    zero_coded = False
    blocks = [
        ("AgentData", 1)
    ]
    structure = {
        "AgentData": [
            ["RegionHandle", "U64"],
            ["ViewerCircuitCode", "U32"],
            ["AgentID", "LLUUID"],
            ["SessionID", "LLUUID"],
            ["AgentPos", "LLVector3"],
            ["AgentVel", "LLVector3"],
            ["Center", "LLVector3"],
            ["Size", "LLVector3"],
            ["AtAxis", "LLVector3"],
            ["LeftAxis", "LLVector3"],
            ["UpAxis", "LLVector3"],
            ["ChangedGrid", "BOOL"]
        ]
    }
registerMessage("ChildAgentPositionUpdate", ChildAgentPositionUpdate)

class ChildAgentDying(message.baseMessage):
    id = 240
    freq = 2
    trusted = True
    zero_coded = True
    blocks = [
        ("AgentData", 1)
    ]
    structure = {
        "AgentData": [
            ["AgentID", "LLUUID"],
            ["SessionID", "LLUUID"]
        ]
    }
registerMessage("ChildAgentDying", ChildAgentDying)

class ChildAgentUnknown(message.baseMessage):
    id = 241
    freq = 2
    trusted = True
    zero_coded = False
    blocks = [
        ("AgentData", 1)
    ]
    structure = {
        "AgentData": [
            ["AgentID", "LLUUID"],
            ["SessionID", "LLUUID"]
        ]
    }
registerMessage("ChildAgentUnknown", ChildAgentUnknown)

class AtomicPassObject(message.baseMessage):
    id = 28
    freq = 0
    trusted = True
    zero_coded = False
    blocks = [
        ("TaskData", 1)
    ]
    structure = {
        "TaskData": [
            ["TaskID", "LLUUID"],
            ["AttachmentNeedsSave", "BOOL"]
        ]
    }
registerMessage("AtomicPassObject", AtomicPassObject)

class KillChildAgents(message.baseMessage):
    id = 242
    freq = 2
    trusted = True
    zero_coded = False
    blocks = [
        ("IDBlock", 1)
    ]
    structure = {
        "IDBlock": [
            ["AgentID", "LLUUID"]
        ]
    }
registerMessage("KillChildAgents", KillChildAgents)

class GetScriptRunning(message.baseMessage):
    id = 243
    freq = 2
    trusted = False
    zero_coded = False
    blocks = [
        ("Script", 1)
    ]
    structure = {
        "Script": [
            ["ObjectID", "LLUUID"],
            ["ItemID", "LLUUID"]
        ]
    }
registerMessage("GetScriptRunning", GetScriptRunning)

class ScriptRunningReply(message.baseMessage):
    id = 244
    freq = 2
    trusted = False
    zero_coded = False
    blocks = [
        ("Script", 1)
    ]
    structure = {
        "Script": [
            ["ObjectID", "LLUUID"],
            ["ItemID", "LLUUID"],
            ["Running", "BOOL"]
        ]
    }
registerMessage("ScriptRunningReply", ScriptRunningReply)

class SetScriptRunning(message.baseMessage):
    id = 245
    freq = 2
    trusted = False
    zero_coded = False
    blocks = [
        ("AgentData", 1),
        ("Script", 1)
    ]
    structure = {
        "AgentData": [
            ["AgentID", "LLUUID"],
            ["SessionID", "LLUUID"]
        ],
        "Script": [
            ["ObjectID", "LLUUID"],
            ["ItemID", "LLUUID"],
            ["Running", "BOOL"]
        ]
    }
registerMessage("SetScriptRunning", SetScriptRunning)

class ScriptReset(message.baseMessage):
    id = 246
    freq = 2
    trusted = False
    zero_coded = False
    blocks = [
        ("AgentData", 1),
        ("Script", 1)
    ]
    structure = {
        "AgentData": [
            ["AgentID", "LLUUID"],
            ["SessionID", "LLUUID"]
        ],
        "Script": [
            ["ObjectID", "LLUUID"],
            ["ItemID", "LLUUID"]
        ]
    }
registerMessage("ScriptReset", ScriptReset)

class ScriptSensorRequest(message.baseMessage):
    id = 247
    freq = 2
    trusted = True
    zero_coded = True
    blocks = [
        ("Requester", 1)
    ]
    structure = {
        "Requester": [
            ["SourceID", "LLUUID"],
            ["RequestID", "LLUUID"],
            ["SearchID", "LLUUID"],
            ["SearchPos", "LLVector3"],
            ["SearchDir", "LLQuaternion"],
            ["SearchName", "Variable1"],
            ["Type", "S32"],
            ["Range", "F32"],
            ["Arc", "F32"],
            ["RegionHandle", "U64"],
            ["SearchRegions", "U8"]
        ]
    }
registerMessage("ScriptSensorRequest", ScriptSensorRequest)

class ScriptSensorReply(message.baseMessage):
    id = 248
    freq = 2
    trusted = True
    zero_coded = True
    blocks = [
        ("Requester", 1),
        ("SensedData", 0)
    ]
    structure = {
        "Requester": [
            ["SourceID", "LLUUID"]
        ],
        "SensedData": [
            ["ObjectID", "LLUUID"],
            ["OwnerID", "LLUUID"],
            ["GroupID", "LLUUID"],
            ["Position", "LLVector3"],
            ["Velocity", "LLVector3"],
            ["Rotation", "LLQuaternion"],
            ["Name", "Variable1"],
            ["Type", "S32"],
            ["Range", "F32"]
        ]
    }
registerMessage("ScriptSensorReply", ScriptSensorReply)

class CompleteAgentMovement(message.baseMessage):
    id = 249
    freq = 2
    trusted = False
    zero_coded = False
    blocks = [
        ("AgentData", 1)
    ]
    structure = {
        "AgentData": [
            ["AgentID", "LLUUID"],
            ["SessionID", "LLUUID"],
            ["CircuitCode", "U32"]
        ]
    }
registerMessage("CompleteAgentMovement", CompleteAgentMovement)

class AgentMovementComplete(message.baseMessage):
    id = 250
    freq = 2
    trusted = False
    zero_coded = False
    blocks = [
        ("AgentData", 1),
        ("Data", 1),
        ("SimData", 1)
    ]
    structure = {
        "AgentData": [
            ["AgentID", "LLUUID"],
            ["SessionID", "LLUUID"]
        ],
        "Data": [
            ["Position", "LLVector3"],
            ["LookAt", "LLVector3"],
            ["RegionHandle", "U64"],
            ["Timestamp", "U32"]
        ],
        "SimData": [
            ["ChannelVersion", "Variable2"]
        ]
    }
registerMessage("AgentMovementComplete", AgentMovementComplete)

class DataServerLogout(message.baseMessage):
    id = 251
    freq = 2
    trusted = True
    zero_coded = False
    blocks = [
        ("UserData", 1)
    ]
    structure = {
        "UserData": [
            ["AgentID", "LLUUID"],
            ["ViewerIP", "IPADDR"],
            ["Disconnect", "BOOL"],
            ["SessionID", "LLUUID"]
        ]
    }
registerMessage("DataServerLogout", DataServerLogout)

class LogoutRequest(message.baseMessage):
    id = 252
    freq = 2
    trusted = False
    zero_coded = False
    blocks = [
        ("AgentData", 1)
    ]
    structure = {
        "AgentData": [
            ["AgentID", "LLUUID"],
            ["SessionID", "LLUUID"]
        ]
    }
registerMessage("LogoutRequest", LogoutRequest)

class LogoutReply(message.baseMessage):
    id = 253
    freq = 2
    trusted = True
    zero_coded = True
    blocks = [
        ("AgentData", 1),
        ("InventoryData", 0)
    ]
    structure = {
        "AgentData": [
            ["AgentID", "LLUUID"],
            ["SessionID", "LLUUID"]
        ],
        "InventoryData": [
            ["ItemID", "LLUUID"]
        ]
    }
registerMessage("LogoutReply", LogoutReply)

class ImprovedInstantMessage(message.baseMessage):
    id = 254
    freq = 2
    trusted = False
    zero_coded = True
    blocks = [
        ("AgentData", 1),
        ("MessageBlock", 1)
    ]
    structure = {
        "AgentData": [
            ["AgentID", "LLUUID"],
            ["SessionID", "LLUUID"]
        ],
        "MessageBlock": [
            ["FromGroup", "BOOL"],
            ["ToAgentID", "LLUUID"],
            ["ParentEstateID", "U32"],
            ["RegionID", "LLUUID"],
            ["Position", "LLVector3"],
            ["Offline", "U8"],
            ["Dialog", "U8"],
            ["ID", "LLUUID"],
            ["Timestamp", "U32"],
            ["FromAgentName", "Variable1"],
            ["Message", "Variable2"],
            ["BinaryBucket", "Variable2"]
        ]
    }
registerMessage("ImprovedInstantMessage", ImprovedInstantMessage)

class RetrieveInstantMessages(message.baseMessage):
    id = 255
    freq = 2
    trusted = False
    zero_coded = False
    blocks = [
        ("AgentData", 1)
    ]
    structure = {
        "AgentData": [
            ["AgentID", "LLUUID"],
            ["SessionID", "LLUUID"]
        ]
    }
registerMessage("RetrieveInstantMessages", RetrieveInstantMessages)

class FindAgent(message.baseMessage):
    id = 256
    freq = 2
    trusted = False
    zero_coded = False
    blocks = [
        ("AgentBlock", 1),
        ("LocationBlock", 0)
    ]
    structure = {
        "AgentBlock": [
            ["Hunter", "LLUUID"],
            ["Prey", "LLUUID"],
            ["SpaceIP", "IPADDR"]
        ],
        "LocationBlock": [
            ["GlobalX", "F64"],
            ["GlobalY", "F64"]
        ]
    }
registerMessage("FindAgent", FindAgent)

class RequestGodlikePowers(message.baseMessage):
    id = 257
    freq = 2
    trusted = False
    zero_coded = False
    blocks = [
        ("AgentData", 1),
        ("RequestBlock", 1)
    ]
    structure = {
        "AgentData": [
            ["AgentID", "LLUUID"],
            ["SessionID", "LLUUID"]
        ],
        "RequestBlock": [
            ["Godlike", "BOOL"],
            ["Token", "LLUUID"]
        ]
    }
registerMessage("RequestGodlikePowers", RequestGodlikePowers)

class GrantGodlikePowers(message.baseMessage):
    id = 258
    freq = 2
    trusted = True
    zero_coded = False
    blocks = [
        ("AgentData", 1),
        ("GrantData", 1)
    ]
    structure = {
        "AgentData": [
            ["AgentID", "LLUUID"],
            ["SessionID", "LLUUID"]
        ],
        "GrantData": [
            ["GodLevel", "U8"],
            ["Token", "LLUUID"]
        ]
    }
registerMessage("GrantGodlikePowers", GrantGodlikePowers)

class GodlikeMessage(message.baseMessage):
    id = 259
    freq = 2
    trusted = False
    zero_coded = True
    blocks = [
        ("AgentData", 1),
        ("MethodData", 1),
        ("ParamList", 0)
    ]
    structure = {
        "AgentData": [
            ["AgentID", "LLUUID"],
            ["SessionID", "LLUUID"],
            ["TransactionID", "LLUUID"]
        ],
        "MethodData": [
            ["Method", "Variable1"],
            ["Invoice", "LLUUID"]
        ],
        "ParamList": [
            ["Parameter", "Variable1"]
        ]
    }
registerMessage("GodlikeMessage", GodlikeMessage)

class EstateOwnerMessage(message.baseMessage):
    id = 260
    freq = 2
    trusted = False
    zero_coded = True
    blocks = [
        ("AgentData", 1),
        ("MethodData", 1),
        ("ParamList", 0)
    ]
    structure = {
        "AgentData": [
            ["AgentID", "LLUUID"],
            ["SessionID", "LLUUID"],
            ["TransactionID", "LLUUID"]
        ],
        "MethodData": [
            ["Method", "Variable1"],
            ["Invoice", "LLUUID"]
        ],
        "ParamList": [
            ["Parameter", "Variable1"]
        ]
    }
registerMessage("EstateOwnerMessage", EstateOwnerMessage)

class GenericMessage(message.baseMessage):
    id = 261
    freq = 2
    trusted = False
    zero_coded = True
    blocks = [
        ("AgentData", 1),
        ("MethodData", 1),
        ("ParamList", 0)
    ]
    structure = {
        "AgentData": [
            ["AgentID", "LLUUID"],
            ["SessionID", "LLUUID"],
            ["TransactionID", "LLUUID"]
        ],
        "MethodData": [
            ["Method", "Variable1"],
            ["Invoice", "LLUUID"]
        ],
        "ParamList": [
            ["Parameter", "Variable1"]
        ]
    }
registerMessage("GenericMessage", GenericMessage)

class MuteListRequest(message.baseMessage):
    id = 262
    freq = 2
    trusted = False
    zero_coded = False
    blocks = [
        ("AgentData", 1),
        ("MuteData", 1)
    ]
    structure = {
        "AgentData": [
            ["AgentID", "LLUUID"],
            ["SessionID", "LLUUID"]
        ],
        "MuteData": [
            ["MuteCRC", "U32"]
        ]
    }
registerMessage("MuteListRequest", MuteListRequest)

class UpdateMuteListEntry(message.baseMessage):
    id = 263
    freq = 2
    trusted = False
    zero_coded = False
    blocks = [
        ("AgentData", 1),
        ("MuteData", 1)
    ]
    structure = {
        "AgentData": [
            ["AgentID", "LLUUID"],
            ["SessionID", "LLUUID"]
        ],
        "MuteData": [
            ["MuteID", "LLUUID"],
            ["MuteName", "Variable1"],
            ["MuteType", "S32"],
            ["MuteFlags", "U32"]
        ]
    }
registerMessage("UpdateMuteListEntry", UpdateMuteListEntry)

class RemoveMuteListEntry(message.baseMessage):
    id = 264
    freq = 2
    trusted = False
    zero_coded = False
    blocks = [
        ("AgentData", 1),
        ("MuteData", 1)
    ]
    structure = {
        "AgentData": [
            ["AgentID", "LLUUID"],
            ["SessionID", "LLUUID"]
        ],
        "MuteData": [
            ["MuteID", "LLUUID"],
            ["MuteName", "Variable1"]
        ]
    }
registerMessage("RemoveMuteListEntry", RemoveMuteListEntry)

class CopyInventoryFromNotecard(message.baseMessage):
    id = 265
    freq = 2
    trusted = False
    zero_coded = True
    blocks = [
        ("AgentData", 1),
        ("NotecardData", 1),
        ("InventoryData", 0)
    ]
    structure = {
        "AgentData": [
            ["AgentID", "LLUUID"],
            ["SessionID", "LLUUID"]
        ],
        "NotecardData": [
            ["NotecardItemID", "LLUUID"],
            ["ObjectID", "LLUUID"]
        ],
        "InventoryData": [
            ["ItemID", "LLUUID"],
            ["FolderID", "LLUUID"]
        ]
    }
registerMessage("CopyInventoryFromNotecard", CopyInventoryFromNotecard)

class UpdateInventoryItem(message.baseMessage):
    id = 266
    freq = 2
    trusted = False
    zero_coded = True
    blocks = [
        ("AgentData", 1),
        ("InventoryData", 0)
    ]
    structure = {
        "AgentData": [
            ["AgentID", "LLUUID"],
            ["SessionID", "LLUUID"],
            ["TransactionID", "LLUUID"]
        ],
        "InventoryData": [
            ["ItemID", "LLUUID"],
            ["FolderID", "LLUUID"],
            ["CallbackID", "U32"],
            ["CreatorID", "LLUUID"],
            ["OwnerID", "LLUUID"],
            ["GroupID", "LLUUID"],
            ["BaseMask", "U32"],
            ["OwnerMask", "U32"],
            ["GroupMask", "U32"],
            ["EveryoneMask", "U32"],
            ["NextOwnerMask", "U32"],
            ["GroupOwned", "BOOL"],
            ["TransactionID", "LLUUID"],
            ["Type", "S8"],
            ["InvType", "S8"],
            ["Flags", "U32"],
            ["SaleType", "U8"],
            ["SalePrice", "S32"],
            ["Name", "Variable1"],
            ["Description", "Variable1"],
            ["CreationDate", "S32"],
            ["CRC", "U32"]
        ]
    }
registerMessage("UpdateInventoryItem", UpdateInventoryItem)

class UpdateCreateInventoryItem(message.baseMessage):
    id = 267
    freq = 2
    trusted = True
    zero_coded = True
    blocks = [
        ("AgentData", 1),
        ("InventoryData", 0)
    ]
    structure = {
        "AgentData": [
            ["AgentID", "LLUUID"],
            ["SimApproved", "BOOL"],
            ["TransactionID", "LLUUID"]
        ],
        "InventoryData": [
            ["ItemID", "LLUUID"],
            ["FolderID", "LLUUID"],
            ["CallbackID", "U32"],
            ["CreatorID", "LLUUID"],
            ["OwnerID", "LLUUID"],
            ["GroupID", "LLUUID"],
            ["BaseMask", "U32"],
            ["OwnerMask", "U32"],
            ["GroupMask", "U32"],
            ["EveryoneMask", "U32"],
            ["NextOwnerMask", "U32"],
            ["GroupOwned", "BOOL"],
            ["AssetID", "LLUUID"],
            ["Type", "S8"],
            ["InvType", "S8"],
            ["Flags", "U32"],
            ["SaleType", "U8"],
            ["SalePrice", "S32"],
            ["Name", "Variable1"],
            ["Description", "Variable1"],
            ["CreationDate", "S32"],
            ["CRC", "U32"]
        ]
    }
registerMessage("UpdateCreateInventoryItem", UpdateCreateInventoryItem)

class MoveInventoryItem(message.baseMessage):
    id = 268
    freq = 2
    trusted = False
    zero_coded = True
    blocks = [
        ("AgentData", 1),
        ("InventoryData", 0)
    ]
    structure = {
        "AgentData": [
            ["AgentID", "LLUUID"],
            ["SessionID", "LLUUID"],
            ["Stamp", "BOOL"]
        ],
        "InventoryData": [
            ["ItemID", "LLUUID"],
            ["FolderID", "LLUUID"],
            ["NewName", "Variable1"]
        ]
    }
registerMessage("MoveInventoryItem", MoveInventoryItem)

class CopyInventoryItem(message.baseMessage):
    id = 269
    freq = 2
    trusted = False
    zero_coded = True
    blocks = [
        ("AgentData", 1),
        ("InventoryData", 0)
    ]
    structure = {
        "AgentData": [
            ["AgentID", "LLUUID"],
            ["SessionID", "LLUUID"]
        ],
        "InventoryData": [
            ["CallbackID", "U32"],
            ["OldAgentID", "LLUUID"],
            ["OldItemID", "LLUUID"],
            ["NewFolderID", "LLUUID"],
            ["NewName", "Variable1"]
        ]
    }
registerMessage("CopyInventoryItem", CopyInventoryItem)

class RemoveInventoryItem(message.baseMessage):
    id = 270
    freq = 2
    trusted = False
    zero_coded = False
    blocks = [
        ("AgentData", 1),
        ("InventoryData", 0)
    ]
    structure = {
        "AgentData": [
            ["AgentID", "LLUUID"],
            ["SessionID", "LLUUID"]
        ],
        "InventoryData": [
            ["ItemID", "LLUUID"]
        ]
    }
registerMessage("RemoveInventoryItem", RemoveInventoryItem)

class ChangeInventoryItemFlags(message.baseMessage):
    id = 271
    freq = 2
    trusted = False
    zero_coded = False
    blocks = [
        ("AgentData", 1),
        ("InventoryData", 0)
    ]
    structure = {
        "AgentData": [
            ["AgentID", "LLUUID"],
            ["SessionID", "LLUUID"]
        ],
        "InventoryData": [
            ["ItemID", "LLUUID"],
            ["Flags", "U32"]
        ]
    }
registerMessage("ChangeInventoryItemFlags", ChangeInventoryItemFlags)

class SaveAssetIntoInventory(message.baseMessage):
    id = 272
    freq = 2
    trusted = True
    zero_coded = False
    blocks = [
        ("AgentData", 1),
        ("InventoryData", 1)
    ]
    structure = {
        "AgentData": [
            ["AgentID", "LLUUID"]
        ],
        "InventoryData": [
            ["ItemID", "LLUUID"],
            ["NewAssetID", "LLUUID"]
        ]
    }
registerMessage("SaveAssetIntoInventory", SaveAssetIntoInventory)

class CreateInventoryFolder(message.baseMessage):
    id = 273
    freq = 2
    trusted = False
    zero_coded = False
    blocks = [
        ("AgentData", 1),
        ("FolderData", 1)
    ]
    structure = {
        "AgentData": [
            ["AgentID", "LLUUID"],
            ["SessionID", "LLUUID"]
        ],
        "FolderData": [
            ["FolderID", "LLUUID"],
            ["ParentID", "LLUUID"],
            ["Type", "S8"],
            ["Name", "Variable1"]
        ]
    }
registerMessage("CreateInventoryFolder", CreateInventoryFolder)

class UpdateInventoryFolder(message.baseMessage):
    id = 274
    freq = 2
    trusted = False
    zero_coded = False
    blocks = [
        ("AgentData", 1),
        ("FolderData", 0)
    ]
    structure = {
        "AgentData": [
            ["AgentID", "LLUUID"],
            ["SessionID", "LLUUID"]
        ],
        "FolderData": [
            ["FolderID", "LLUUID"],
            ["ParentID", "LLUUID"],
            ["Type", "S8"],
            ["Name", "Variable1"]
        ]
    }
registerMessage("UpdateInventoryFolder", UpdateInventoryFolder)

class MoveInventoryFolder(message.baseMessage):
    id = 275
    freq = 2
    trusted = False
    zero_coded = True
    blocks = [
        ("AgentData", 1),
        ("InventoryData", 0)
    ]
    structure = {
        "AgentData": [
            ["AgentID", "LLUUID"],
            ["SessionID", "LLUUID"],
            ["Stamp", "BOOL"]
        ],
        "InventoryData": [
            ["FolderID", "LLUUID"],
            ["ParentID", "LLUUID"]
        ]
    }
registerMessage("MoveInventoryFolder", MoveInventoryFolder)

class RemoveInventoryFolder(message.baseMessage):
    id = 276
    freq = 2
    trusted = False
    zero_coded = False
    blocks = [
        ("AgentData", 1),
        ("FolderData", 0)
    ]
    structure = {
        "AgentData": [
            ["AgentID", "LLUUID"],
            ["SessionID", "LLUUID"]
        ],
        "FolderData": [
            ["FolderID", "LLUUID"]
        ]
    }
registerMessage("RemoveInventoryFolder", RemoveInventoryFolder)

class FetchInventoryDescendents(message.baseMessage):
    id = 277
    freq = 2
    trusted = False
    zero_coded = True
    blocks = [
        ("AgentData", 1),
        ("InventoryData", 1)
    ]
    structure = {
        "AgentData": [
            ["AgentID", "LLUUID"],
            ["SessionID", "LLUUID"]
        ],
        "InventoryData": [
            ["FolderID", "LLUUID"],
            ["OwnerID", "LLUUID"],
            ["SortOrder", "S32"],
            ["FetchFolders", "BOOL"],
            ["FetchItems", "BOOL"]
        ]
    }
registerMessage("FetchInventoryDescendents", FetchInventoryDescendents)

class InventoryDescendents(message.baseMessage):
    id = 278
    freq = 2
    trusted = True
    zero_coded = True
    blocks = [
        ("AgentData", 1),
        ("FolderData", 0),
        ("ItemData", 0)
    ]
    structure = {
        "AgentData": [
            ["AgentID", "LLUUID"],
            ["FolderID", "LLUUID"],
            ["OwnerID", "LLUUID"],
            ["Version", "S32"],
            ["Descendents", "S32"]
        ],
        "FolderData": [
            ["FolderID", "LLUUID"],
            ["ParentID", "LLUUID"],
            ["Type", "S8"],
            ["Name", "Variable1"]
        ],
        "ItemData": [
            ["ItemID", "LLUUID"],
            ["FolderID", "LLUUID"],
            ["CreatorID", "LLUUID"],
            ["OwnerID", "LLUUID"],
            ["GroupID", "LLUUID"],
            ["BaseMask", "U32"],
            ["OwnerMask", "U32"],
            ["GroupMask", "U32"],
            ["EveryoneMask", "U32"],
            ["NextOwnerMask", "U32"],
            ["GroupOwned", "BOOL"],
            ["AssetID", "LLUUID"],
            ["Type", "S8"],
            ["InvType", "S8"],
            ["Flags", "U32"],
            ["SaleType", "U8"],
            ["SalePrice", "S32"],
            ["Name", "Variable1"],
            ["Description", "Variable1"],
            ["CreationDate", "S32"],
            ["CRC", "U32"]
        ]
    }
registerMessage("InventoryDescendents", InventoryDescendents)

class FetchInventory(message.baseMessage):
    id = 279
    freq = 2
    trusted = False
    zero_coded = True
    blocks = [
        ("AgentData", 1),
        ("InventoryData", 0)
    ]
    structure = {
        "AgentData": [
            ["AgentID", "LLUUID"],
            ["SessionID", "LLUUID"]
        ],
        "InventoryData": [
            ["OwnerID", "LLUUID"],
            ["ItemID", "LLUUID"]
        ]
    }
registerMessage("FetchInventory", FetchInventory)

class FetchInventoryReply(message.baseMessage):
    id = 280
    freq = 2
    trusted = True
    zero_coded = True
    blocks = [
        ("AgentData", 1),
        ("InventoryData", 0)
    ]
    structure = {
        "AgentData": [
            ["AgentID", "LLUUID"]
        ],
        "InventoryData": [
            ["ItemID", "LLUUID"],
            ["FolderID", "LLUUID"],
            ["CreatorID", "LLUUID"],
            ["OwnerID", "LLUUID"],
            ["GroupID", "LLUUID"],
            ["BaseMask", "U32"],
            ["OwnerMask", "U32"],
            ["GroupMask", "U32"],
            ["EveryoneMask", "U32"],
            ["NextOwnerMask", "U32"],
            ["GroupOwned", "BOOL"],
            ["AssetID", "LLUUID"],
            ["Type", "S8"],
            ["InvType", "S8"],
            ["Flags", "U32"],
            ["SaleType", "U8"],
            ["SalePrice", "S32"],
            ["Name", "Variable1"],
            ["Description", "Variable1"],
            ["CreationDate", "S32"],
            ["CRC", "U32"]
        ]
    }
registerMessage("FetchInventoryReply", FetchInventoryReply)

class BulkUpdateInventory(message.baseMessage):
    id = 281
    freq = 2
    trusted = True
    zero_coded = True
    blocks = [
        ("AgentData", 1),
        ("FolderData", 0),
        ("ItemData", 0)
    ]
    structure = {
        "AgentData": [
            ["AgentID", "LLUUID"],
            ["TransactionID", "LLUUID"]
        ],
        "FolderData": [
            ["FolderID", "LLUUID"],
            ["ParentID", "LLUUID"],
            ["Type", "S8"],
            ["Name", "Variable1"]
        ],
        "ItemData": [
            ["ItemID", "LLUUID"],
            ["CallbackID", "U32"],
            ["FolderID", "LLUUID"],
            ["CreatorID", "LLUUID"],
            ["OwnerID", "LLUUID"],
            ["GroupID", "LLUUID"],
            ["BaseMask", "U32"],
            ["OwnerMask", "U32"],
            ["GroupMask", "U32"],
            ["EveryoneMask", "U32"],
            ["NextOwnerMask", "U32"],
            ["GroupOwned", "BOOL"],
            ["AssetID", "LLUUID"],
            ["Type", "S8"],
            ["InvType", "S8"],
            ["Flags", "U32"],
            ["SaleType", "U8"],
            ["SalePrice", "S32"],
            ["Name", "Variable1"],
            ["Description", "Variable1"],
            ["CreationDate", "S32"],
            ["CRC", "U32"]
        ]
    }
registerMessage("BulkUpdateInventory", BulkUpdateInventory)

class RequestInventoryAsset(message.baseMessage):
    id = 282
    freq = 2
    trusted = True
    zero_coded = False
    blocks = [
        ("QueryData", 1)
    ]
    structure = {
        "QueryData": [
            ["QueryID", "LLUUID"],
            ["AgentID", "LLUUID"],
            ["OwnerID", "LLUUID"],
            ["ItemID", "LLUUID"]
        ]
    }
registerMessage("RequestInventoryAsset", RequestInventoryAsset)

class InventoryAssetResponse(message.baseMessage):
    id = 283
    freq = 2
    trusted = True
    zero_coded = False
    blocks = [
        ("QueryData", 1)
    ]
    structure = {
        "QueryData": [
            ["QueryID", "LLUUID"],
            ["AssetID", "LLUUID"],
            ["IsReadable", "BOOL"]
        ]
    }
registerMessage("InventoryAssetResponse", InventoryAssetResponse)

class RemoveInventoryObjects(message.baseMessage):
    id = 284
    freq = 2
    trusted = False
    zero_coded = False
    blocks = [
        ("AgentData", 1),
        ("FolderData", 0),
        ("ItemData", 0)
    ]
    structure = {
        "AgentData": [
            ["AgentID", "LLUUID"],
            ["SessionID", "LLUUID"]
        ],
        "FolderData": [
            ["FolderID", "LLUUID"]
        ],
        "ItemData": [
            ["ItemID", "LLUUID"]
        ]
    }
registerMessage("RemoveInventoryObjects", RemoveInventoryObjects)

class PurgeInventoryDescendents(message.baseMessage):
    id = 285
    freq = 2
    trusted = False
    zero_coded = True
    blocks = [
        ("AgentData", 1),
        ("InventoryData", 1)
    ]
    structure = {
        "AgentData": [
            ["AgentID", "LLUUID"],
            ["SessionID", "LLUUID"]
        ],
        "InventoryData": [
            ["FolderID", "LLUUID"]
        ]
    }
registerMessage("PurgeInventoryDescendents", PurgeInventoryDescendents)

class UpdateTaskInventory(message.baseMessage):
    id = 286
    freq = 2
    trusted = False
    zero_coded = True
    blocks = [
        ("AgentData", 1),
        ("UpdateData", 1),
        ("InventoryData", 1)
    ]
    structure = {
        "AgentData": [
            ["AgentID", "LLUUID"],
            ["SessionID", "LLUUID"]
        ],
        "UpdateData": [
            ["LocalID", "U32"],
            ["Key", "U8"]
        ],
        "InventoryData": [
            ["ItemID", "LLUUID"],
            ["FolderID", "LLUUID"],
            ["CreatorID", "LLUUID"],
            ["OwnerID", "LLUUID"],
            ["GroupID", "LLUUID"],
            ["BaseMask", "U32"],
            ["OwnerMask", "U32"],
            ["GroupMask", "U32"],
            ["EveryoneMask", "U32"],
            ["NextOwnerMask", "U32"],
            ["GroupOwned", "BOOL"],
            ["TransactionID", "LLUUID"],
            ["Type", "S8"],
            ["InvType", "S8"],
            ["Flags", "U32"],
            ["SaleType", "U8"],
            ["SalePrice", "S32"],
            ["Name", "Variable1"],
            ["Description", "Variable1"],
            ["CreationDate", "S32"],
            ["CRC", "U32"]
        ]
    }
registerMessage("UpdateTaskInventory", UpdateTaskInventory)

class RemoveTaskInventory(message.baseMessage):
    id = 287
    freq = 2
    trusted = False
    zero_coded = True
    blocks = [
        ("AgentData", 1),
        ("InventoryData", 1)
    ]
    structure = {
        "AgentData": [
            ["AgentID", "LLUUID"],
            ["SessionID", "LLUUID"]
        ],
        "InventoryData": [
            ["LocalID", "U32"],
            ["ItemID", "LLUUID"]
        ]
    }
registerMessage("RemoveTaskInventory", RemoveTaskInventory)

class MoveTaskInventory(message.baseMessage):
    id = 288
    freq = 2
    trusted = False
    zero_coded = False
    blocks = [
        ("AgentData", 1),
        ("InventoryData", 1)
    ]
    structure = {
        "AgentData": [
            ["AgentID", "LLUUID"],
            ["SessionID", "LLUUID"],
            ["FolderID", "LLUUID"]
        ],
        "InventoryData": [
            ["LocalID", "U32"],
            ["ItemID", "LLUUID"]
        ]
    }
registerMessage("MoveTaskInventory", MoveTaskInventory)

class RequestTaskInventory(message.baseMessage):
    id = 289
    freq = 2
    trusted = False
    zero_coded = False
    blocks = [
        ("AgentData", 1),
        ("InventoryData", 1)
    ]
    structure = {
        "AgentData": [
            ["AgentID", "LLUUID"],
            ["SessionID", "LLUUID"]
        ],
        "InventoryData": [
            ["LocalID", "U32"]
        ]
    }
registerMessage("RequestTaskInventory", RequestTaskInventory)

class ReplyTaskInventory(message.baseMessage):
    id = 290
    freq = 2
    trusted = True
    zero_coded = True
    blocks = [
        ("InventoryData", 1)
    ]
    structure = {
        "InventoryData": [
            ["TaskID", "LLUUID"],
            ["Serial", "S16"],
            ["Filename", "Variable1"]
        ]
    }
registerMessage("ReplyTaskInventory", ReplyTaskInventory)

class DeRezObject(message.baseMessage):
    id = 291
    freq = 2
    trusted = False
    zero_coded = True
    blocks = [
        ("AgentData", 1),
        ("AgentBlock", 1),
        ("ObjectData", 0)
    ]
    structure = {
        "AgentData": [
            ["AgentID", "LLUUID"],
            ["SessionID", "LLUUID"]
        ],
        "AgentBlock": [
            ["GroupID", "LLUUID"],
            ["Destination", "U8"],
            ["DestinationID", "LLUUID"],
            ["TransactionID", "LLUUID"],
            ["PacketCount", "U8"],
            ["PacketNumber", "U8"]
        ],
        "ObjectData": [
            ["ObjectLocalID", "U32"]
        ]
    }
registerMessage("DeRezObject", DeRezObject)

class DeRezAck(message.baseMessage):
    id = 292
    freq = 2
    trusted = True
    zero_coded = False
    blocks = [
        ("TransactionData", 1)
    ]
    structure = {
        "TransactionData": [
            ["TransactionID", "LLUUID"],
            ["Success", "BOOL"]
        ]
    }
registerMessage("DeRezAck", DeRezAck)

class RezObject(message.baseMessage):
    id = 293
    freq = 2
    trusted = False
    zero_coded = True
    blocks = [
        ("AgentData", 1),
        ("RezData", 1),
        ("InventoryData", 1)
    ]
    structure = {
        "AgentData": [
            ["AgentID", "LLUUID"],
            ["SessionID", "LLUUID"],
            ["GroupID", "LLUUID"]
        ],
        "RezData": [
            ["FromTaskID", "LLUUID"],
            ["BypassRaycast", "U8"],
            ["RayStart", "LLVector3"],
            ["RayEnd", "LLVector3"],
            ["RayTargetID", "LLUUID"],
            ["RayEndIsIntersection", "BOOL"],
            ["RezSelected", "BOOL"],
            ["RemoveItem", "BOOL"],
            ["ItemFlags", "U32"],
            ["GroupMask", "U32"],
            ["EveryoneMask", "U32"],
            ["NextOwnerMask", "U32"]
        ],
        "InventoryData": [
            ["ItemID", "LLUUID"],
            ["FolderID", "LLUUID"],
            ["CreatorID", "LLUUID"],
            ["OwnerID", "LLUUID"],
            ["GroupID", "LLUUID"],
            ["BaseMask", "U32"],
            ["OwnerMask", "U32"],
            ["GroupMask", "U32"],
            ["EveryoneMask", "U32"],
            ["NextOwnerMask", "U32"],
            ["GroupOwned", "BOOL"],
            ["TransactionID", "LLUUID"],
            ["Type", "S8"],
            ["InvType", "S8"],
            ["Flags", "U32"],
            ["SaleType", "U8"],
            ["SalePrice", "S32"],
            ["Name", "Variable1"],
            ["Description", "Variable1"],
            ["CreationDate", "S32"],
            ["CRC", "U32"]
        ]
    }
registerMessage("RezObject", RezObject)

class RezObjectFromNotecard(message.baseMessage):
    id = 294
    freq = 2
    trusted = False
    zero_coded = True
    blocks = [
        ("AgentData", 1),
        ("RezData", 1),
        ("NotecardData", 1),
        ("InventoryData", 0)
    ]
    structure = {
        "AgentData": [
            ["AgentID", "LLUUID"],
            ["SessionID", "LLUUID"],
            ["GroupID", "LLUUID"]
        ],
        "RezData": [
            ["FromTaskID", "LLUUID"],
            ["BypassRaycast", "U8"],
            ["RayStart", "LLVector3"],
            ["RayEnd", "LLVector3"],
            ["RayTargetID", "LLUUID"],
            ["RayEndIsIntersection", "BOOL"],
            ["RezSelected", "BOOL"],
            ["RemoveItem", "BOOL"],
            ["ItemFlags", "U32"],
            ["GroupMask", "U32"],
            ["EveryoneMask", "U32"],
            ["NextOwnerMask", "U32"]
        ],
        "NotecardData": [
            ["NotecardItemID", "LLUUID"],
            ["ObjectID", "LLUUID"]
        ],
        "InventoryData": [
            ["ItemID", "LLUUID"]
        ]
    }
registerMessage("RezObjectFromNotecard", RezObjectFromNotecard)

class TransferInventory(message.baseMessage):
    id = 295
    freq = 2
    trusted = True
    zero_coded = True
    blocks = [
        ("InfoBlock", 1),
        ("InventoryBlock", 0)
    ]
    structure = {
        "InfoBlock": [
            ["SourceID", "LLUUID"],
            ["DestID", "LLUUID"],
            ["TransactionID", "LLUUID"]
        ],
        "InventoryBlock": [
            ["InventoryID", "LLUUID"],
            ["Type", "S8"]
        ]
    }
registerMessage("TransferInventory", TransferInventory)

class TransferInventoryAck(message.baseMessage):
    id = 296
    freq = 2
    trusted = True
    zero_coded = True
    blocks = [
        ("InfoBlock", 1)
    ]
    structure = {
        "InfoBlock": [
            ["TransactionID", "LLUUID"],
            ["InventoryID", "LLUUID"]
        ]
    }
registerMessage("TransferInventoryAck", TransferInventoryAck)

class AcceptFriendship(message.baseMessage):
    id = 297
    freq = 2
    trusted = False
    zero_coded = False
    blocks = [
        ("AgentData", 1),
        ("TransactionBlock", 1),
        ("FolderData", 0)
    ]
    structure = {
        "AgentData": [
            ["AgentID", "LLUUID"],
            ["SessionID", "LLUUID"]
        ],
        "TransactionBlock": [
            ["TransactionID", "LLUUID"]
        ],
        "FolderData": [
            ["FolderID", "LLUUID"]
        ]
    }
registerMessage("AcceptFriendship", AcceptFriendship)

class DeclineFriendship(message.baseMessage):
    id = 298
    freq = 2
    trusted = False
    zero_coded = False
    blocks = [
        ("AgentData", 1),
        ("TransactionBlock", 1)
    ]
    structure = {
        "AgentData": [
            ["AgentID", "LLUUID"],
            ["SessionID", "LLUUID"]
        ],
        "TransactionBlock": [
            ["TransactionID", "LLUUID"]
        ]
    }
registerMessage("DeclineFriendship", DeclineFriendship)

class FormFriendship(message.baseMessage):
    id = 299
    freq = 2
    trusted = True
    zero_coded = False
    blocks = [
        ("AgentBlock", 1)
    ]
    structure = {
        "AgentBlock": [
            ["SourceID", "LLUUID"],
            ["DestID", "LLUUID"]
        ]
    }
registerMessage("FormFriendship", FormFriendship)

class TerminateFriendship(message.baseMessage):
    id = 300
    freq = 2
    trusted = False
    zero_coded = False
    blocks = [
        ("AgentData", 1),
        ("ExBlock", 1)
    ]
    structure = {
        "AgentData": [
            ["AgentID", "LLUUID"],
            ["SessionID", "LLUUID"]
        ],
        "ExBlock": [
            ["OtherID", "LLUUID"]
        ]
    }
registerMessage("TerminateFriendship", TerminateFriendship)

class OfferCallingCard(message.baseMessage):
    id = 301
    freq = 2
    trusted = False
    zero_coded = False
    blocks = [
        ("AgentData", 1),
        ("AgentBlock", 1)
    ]
    structure = {
        "AgentData": [
            ["AgentID", "LLUUID"],
            ["SessionID", "LLUUID"]
        ],
        "AgentBlock": [
            ["DestID", "LLUUID"],
            ["TransactionID", "LLUUID"]
        ]
    }
registerMessage("OfferCallingCard", OfferCallingCard)

class AcceptCallingCard(message.baseMessage):
    id = 302
    freq = 2
    trusted = False
    zero_coded = False
    blocks = [
        ("AgentData", 1),
        ("TransactionBlock", 1),
        ("FolderData", 0)
    ]
    structure = {
        "AgentData": [
            ["AgentID", "LLUUID"],
            ["SessionID", "LLUUID"]
        ],
        "TransactionBlock": [
            ["TransactionID", "LLUUID"]
        ],
        "FolderData": [
            ["FolderID", "LLUUID"]
        ]
    }
registerMessage("AcceptCallingCard", AcceptCallingCard)

class DeclineCallingCard(message.baseMessage):
    id = 303
    freq = 2
    trusted = False
    zero_coded = False
    blocks = [
        ("AgentData", 1),
        ("TransactionBlock", 1)
    ]
    structure = {
        "AgentData": [
            ["AgentID", "LLUUID"],
            ["SessionID", "LLUUID"]
        ],
        "TransactionBlock": [
            ["TransactionID", "LLUUID"]
        ]
    }
registerMessage("DeclineCallingCard", DeclineCallingCard)

class RezScript(message.baseMessage):
    id = 304
    freq = 2
    trusted = False
    zero_coded = True
    blocks = [
        ("AgentData", 1),
        ("UpdateBlock", 1),
        ("InventoryBlock", 1)
    ]
    structure = {
        "AgentData": [
            ["AgentID", "LLUUID"],
            ["SessionID", "LLUUID"],
            ["GroupID", "LLUUID"]
        ],
        "UpdateBlock": [
            ["ObjectLocalID", "U32"],
            ["Enabled", "BOOL"]
        ],
        "InventoryBlock": [
            ["ItemID", "LLUUID"],
            ["FolderID", "LLUUID"],
            ["CreatorID", "LLUUID"],
            ["OwnerID", "LLUUID"],
            ["GroupID", "LLUUID"],
            ["BaseMask", "U32"],
            ["OwnerMask", "U32"],
            ["GroupMask", "U32"],
            ["EveryoneMask", "U32"],
            ["NextOwnerMask", "U32"],
            ["GroupOwned", "BOOL"],
            ["TransactionID", "LLUUID"],
            ["Type", "S8"],
            ["InvType", "S8"],
            ["Flags", "U32"],
            ["SaleType", "U8"],
            ["SalePrice", "S32"],
            ["Name", "Variable1"],
            ["Description", "Variable1"],
            ["CreationDate", "S32"],
            ["CRC", "U32"]
        ]
    }
registerMessage("RezScript", RezScript)

class CreateInventoryItem(message.baseMessage):
    id = 305
    freq = 2
    trusted = False
    zero_coded = True
    blocks = [
        ("AgentData", 1),
        ("InventoryBlock", 1)
    ]
    structure = {
        "AgentData": [
            ["AgentID", "LLUUID"],
            ["SessionID", "LLUUID"]
        ],
        "InventoryBlock": [
            ["CallbackID", "U32"],
            ["FolderID", "LLUUID"],
            ["TransactionID", "LLUUID"],
            ["NextOwnerMask", "U32"],
            ["Type", "S8"],
            ["InvType", "S8"],
            ["WearableType", "U8"],
            ["Name", "Variable1"],
            ["Description", "Variable1"]
        ]
    }
registerMessage("CreateInventoryItem", CreateInventoryItem)

class CreateLandmarkForEvent(message.baseMessage):
    id = 306
    freq = 2
    trusted = False
    zero_coded = True
    blocks = [
        ("AgentData", 1),
        ("EventData", 1),
        ("InventoryBlock", 1)
    ]
    structure = {
        "AgentData": [
            ["AgentID", "LLUUID"],
            ["SessionID", "LLUUID"]
        ],
        "EventData": [
            ["EventID", "U32"]
        ],
        "InventoryBlock": [
            ["FolderID", "LLUUID"],
            ["Name", "Variable1"]
        ]
    }
registerMessage("CreateLandmarkForEvent", CreateLandmarkForEvent)

class EventLocationRequest(message.baseMessage):
    id = 307
    freq = 2
    trusted = True
    zero_coded = True
    blocks = [
        ("QueryData", 1),
        ("EventData", 1)
    ]
    structure = {
        "QueryData": [
            ["QueryID", "LLUUID"]
        ],
        "EventData": [
            ["EventID", "U32"]
        ]
    }
registerMessage("EventLocationRequest", EventLocationRequest)

class EventLocationReply(message.baseMessage):
    id = 308
    freq = 2
    trusted = True
    zero_coded = True
    blocks = [
        ("QueryData", 1),
        ("EventData", 1)
    ]
    structure = {
        "QueryData": [
            ["QueryID", "LLUUID"]
        ],
        "EventData": [
            ["Success", "BOOL"],
            ["RegionID", "LLUUID"],
            ["RegionPos", "LLVector3"]
        ]
    }
registerMessage("EventLocationReply", EventLocationReply)

class RegionHandleRequest(message.baseMessage):
    id = 309
    freq = 2
    trusted = False
    zero_coded = False
    blocks = [
        ("RequestBlock", 1)
    ]
    structure = {
        "RequestBlock": [
            ["RegionID", "LLUUID"]
        ]
    }
registerMessage("RegionHandleRequest", RegionHandleRequest)

class RegionIDAndHandleReply(message.baseMessage):
    id = 310
    freq = 2
    trusted = True
    zero_coded = False
    blocks = [
        ("ReplyBlock", 1)
    ]
    structure = {
        "ReplyBlock": [
            ["RegionID", "LLUUID"],
            ["RegionHandle", "U64"]
        ]
    }
registerMessage("RegionIDAndHandleReply", RegionIDAndHandleReply)

class MoneyTransferRequest(message.baseMessage):
    id = 311
    freq = 2
    trusted = False
    zero_coded = True
    blocks = [
        ("AgentData", 1),
        ("MoneyData", 1)
    ]
    structure = {
        "AgentData": [
            ["AgentID", "LLUUID"],
            ["SessionID", "LLUUID"]
        ],
        "MoneyData": [
            ["SourceID", "LLUUID"],
            ["DestID", "LLUUID"],
            ["Flags", "U8"],
            ["Amount", "S32"],
            ["AggregatePermNextOwner", "U8"],
            ["AggregatePermInventory", "U8"],
            ["TransactionType", "S32"],
            ["Description", "Variable1"]
        ]
    }
registerMessage("MoneyTransferRequest", MoneyTransferRequest)

class MoneyTransferBackend(message.baseMessage):
    id = 312
    freq = 2
    trusted = True
    zero_coded = True
    blocks = [
        ("MoneyData", 1)
    ]
    structure = {
        "MoneyData": [
            ["TransactionID", "LLUUID"],
            ["TransactionTime", "U32"],
            ["SourceID", "LLUUID"],
            ["DestID", "LLUUID"],
            ["Flags", "U8"],
            ["Amount", "S32"],
            ["AggregatePermNextOwner", "U8"],
            ["AggregatePermInventory", "U8"],
            ["TransactionType", "S32"],
            ["RegionID", "LLUUID"],
            ["GridX", "U32"],
            ["GridY", "U32"],
            ["Description", "Variable1"]
        ]
    }
registerMessage("MoneyTransferBackend", MoneyTransferBackend)

class MoneyBalanceRequest(message.baseMessage):
    id = 313
    freq = 2
    trusted = False
    zero_coded = True
    blocks = [
        ("AgentData", 1),
        ("MoneyData", 1)
    ]
    structure = {
        "AgentData": [
            ["AgentID", "LLUUID"],
            ["SessionID", "LLUUID"]
        ],
        "MoneyData": [
            ["TransactionID", "LLUUID"]
        ]
    }
registerMessage("MoneyBalanceRequest", MoneyBalanceRequest)

class MoneyBalanceReply(message.baseMessage):
    id = 314
    freq = 2
    trusted = True
    zero_coded = True
    blocks = [
        ("MoneyData", 1),
        ("TransactionInfo", 1)
    ]
    structure = {
        "MoneyData": [
            ["AgentID", "LLUUID"],
            ["TransactionID", "LLUUID"],
            ["TransactionSuccess", "BOOL"],
            ["MoneyBalance", "S32"],
            ["SquareMetersCredit", "S32"],
            ["SquareMetersCommitted", "S32"],
            ["Description", "Variable1"]
        ],
        "TransactionInfo": [
            ["TransactionType", "S32"],
            ["SourceID", "LLUUID"],
            ["IsSourceGroup", "BOOL"],
            ["DestID", "LLUUID"],
            ["IsDestGroup", "BOOL"],
            ["Amount", "S32"],
            ["ItemDescription", "Variable1"]
        ]
    }
registerMessage("MoneyBalanceReply", MoneyBalanceReply)

class RoutedMoneyBalanceReply(message.baseMessage):
    id = 315
    freq = 2
    trusted = True
    zero_coded = True
    blocks = [
        ("TargetBlock", 1),
        ("MoneyData", 1),
        ("TransactionInfo", 1)
    ]
    structure = {
        "TargetBlock": [
            ["TargetIP", "IPADDR"],
            ["TargetPort", "IPPORT"]
        ],
        "MoneyData": [
            ["AgentID", "LLUUID"],
            ["TransactionID", "LLUUID"],
            ["TransactionSuccess", "BOOL"],
            ["MoneyBalance", "S32"],
            ["SquareMetersCredit", "S32"],
            ["SquareMetersCommitted", "S32"],
            ["Description", "Variable1"]
        ],
        "TransactionInfo": [
            ["TransactionType", "S32"],
            ["SourceID", "LLUUID"],
            ["IsSourceGroup", "BOOL"],
            ["DestID", "LLUUID"],
            ["IsDestGroup", "BOOL"],
            ["Amount", "S32"],
            ["ItemDescription", "Variable1"]
        ]
    }
registerMessage("RoutedMoneyBalanceReply", RoutedMoneyBalanceReply)

class ActivateGestures(message.baseMessage):
    id = 316
    freq = 2
    trusted = False
    zero_coded = False
    blocks = [
        ("AgentData", 1),
        ("Data", 0)
    ]
    structure = {
        "AgentData": [
            ["AgentID", "LLUUID"],
            ["SessionID", "LLUUID"],
            ["Flags", "U32"]
        ],
        "Data": [
            ["ItemID", "LLUUID"],
            ["AssetID", "LLUUID"],
            ["GestureFlags", "U32"]
        ]
    }
registerMessage("ActivateGestures", ActivateGestures)

class DeactivateGestures(message.baseMessage):
    id = 317
    freq = 2
    trusted = False
    zero_coded = False
    blocks = [
        ("AgentData", 1),
        ("Data", 0)
    ]
    structure = {
        "AgentData": [
            ["AgentID", "LLUUID"],
            ["SessionID", "LLUUID"],
            ["Flags", "U32"]
        ],
        "Data": [
            ["ItemID", "LLUUID"],
            ["GestureFlags", "U32"]
        ]
    }
registerMessage("DeactivateGestures", DeactivateGestures)

class MuteListUpdate(message.baseMessage):
    id = 318
    freq = 2
    trusted = True
    zero_coded = False
    blocks = [
        ("MuteData", 1)
    ]
    structure = {
        "MuteData": [
            ["AgentID", "LLUUID"],
            ["Filename", "Variable1"]
        ]
    }
registerMessage("MuteListUpdate", MuteListUpdate)

class UseCachedMuteList(message.baseMessage):
    id = 319
    freq = 2
    trusted = False
    zero_coded = False
    blocks = [
        ("AgentData", 1)
    ]
    structure = {
        "AgentData": [
            ["AgentID", "LLUUID"]
        ]
    }
registerMessage("UseCachedMuteList", UseCachedMuteList)

class GrantUserRights(message.baseMessage):
    id = 320
    freq = 2
    trusted = False
    zero_coded = False
    blocks = [
        ("AgentData", 1),
        ("Rights", 0)
    ]
    structure = {
        "AgentData": [
            ["AgentID", "LLUUID"],
            ["SessionID", "LLUUID"]
        ],
        "Rights": [
            ["AgentRelated", "LLUUID"],
            ["RelatedRights", "S32"]
        ]
    }
registerMessage("GrantUserRights", GrantUserRights)

class ChangeUserRights(message.baseMessage):
    id = 321
    freq = 2
    trusted = True
    zero_coded = False
    blocks = [
        ("AgentData", 1),
        ("Rights", 0)
    ]
    structure = {
        "AgentData": [
            ["AgentID", "LLUUID"]
        ],
        "Rights": [
            ["AgentRelated", "LLUUID"],
            ["RelatedRights", "S32"]
        ]
    }
registerMessage("ChangeUserRights", ChangeUserRights)

class OnlineNotification(message.baseMessage):
    id = 322
    freq = 2
    trusted = True
    zero_coded = False
    blocks = [
        ("AgentBlock", 0)
    ]
    structure = {
        "AgentBlock": [
            ["AgentID", "LLUUID"]
        ]
    }
registerMessage("OnlineNotification", OnlineNotification)

class OfflineNotification(message.baseMessage):
    id = 323
    freq = 2
    trusted = True
    zero_coded = False
    blocks = [
        ("AgentBlock", 0)
    ]
    structure = {
        "AgentBlock": [
            ["AgentID", "LLUUID"]
        ]
    }
registerMessage("OfflineNotification", OfflineNotification)

class SetStartLocationRequest(message.baseMessage):
    id = 324
    freq = 2
    trusted = False
    zero_coded = True
    blocks = [
        ("AgentData", 1),
        ("StartLocationData", 1)
    ]
    structure = {
        "AgentData": [
            ["AgentID", "LLUUID"],
            ["SessionID", "LLUUID"]
        ],
        "StartLocationData": [
            ["SimName", "Variable1"],
            ["LocationID", "U32"],
            ["LocationPos", "LLVector3"],
            ["LocationLookAt", "LLVector3"]
        ]
    }
registerMessage("SetStartLocationRequest", SetStartLocationRequest)

class SetStartLocation(message.baseMessage):
    id = 325
    freq = 2
    trusted = True
    zero_coded = True
    blocks = [
        ("StartLocationData", 1)
    ]
    structure = {
        "StartLocationData": [
            ["AgentID", "LLUUID"],
            ["RegionID", "LLUUID"],
            ["LocationID", "U32"],
            ["RegionHandle", "U64"],
            ["LocationPos", "LLVector3"],
            ["LocationLookAt", "LLVector3"]
        ]
    }
registerMessage("SetStartLocation", SetStartLocation)

class NetTest(message.baseMessage):
    id = 326
    freq = 2
    trusted = False
    zero_coded = False
    blocks = [
        ("NetBlock", 1)
    ]
    structure = {
        "NetBlock": [
            ["Port", "IPPORT"]
        ]
    }
registerMessage("NetTest", NetTest)

class SetCPURatio(message.baseMessage):
    id = 327
    freq = 2
    trusted = False
    zero_coded = False
    blocks = [
        ("Data", 1)
    ]
    structure = {
        "Data": [
            ["Ratio", "U8"]
        ]
    }
registerMessage("SetCPURatio", SetCPURatio)

class SimCrashed(message.baseMessage):
    id = 328
    freq = 2
    trusted = False
    zero_coded = False
    blocks = [
        ("Data", 1),
        ("Users", 0)
    ]
    structure = {
        "Data": [
            ["RegionX", "U32"],
            ["RegionY", "U32"]
        ],
        "Users": [
            ["AgentID", "LLUUID"]
        ]
    }
registerMessage("SimCrashed", SimCrashed)

class NameValuePair(message.baseMessage):
    id = 329
    freq = 2
    trusted = True
    zero_coded = False
    blocks = [
        ("TaskData", 1),
        ("NameValueData", 0)
    ]
    structure = {
        "TaskData": [
            ["ID", "LLUUID"]
        ],
        "NameValueData": [
            ["NVPair", "Variable2"]
        ]
    }
registerMessage("NameValuePair", NameValuePair)

class RemoveNameValuePair(message.baseMessage):
    id = 330
    freq = 2
    trusted = True
    zero_coded = False
    blocks = [
        ("TaskData", 1),
        ("NameValueData", 0)
    ]
    structure = {
        "TaskData": [
            ["ID", "LLUUID"]
        ],
        "NameValueData": [
            ["NVPair", "Variable2"]
        ]
    }
registerMessage("RemoveNameValuePair", RemoveNameValuePair)

class UpdateAttachment(message.baseMessage):
    id = 331
    freq = 2
    trusted = True
    zero_coded = True
    blocks = [
        ("AgentData", 1),
        ("AttachmentBlock", 1),
        ("OperationData", 1),
        ("InventoryData", 1)
    ]
    structure = {
        "AgentData": [
            ["AgentID", "LLUUID"],
            ["SessionID", "LLUUID"]
        ],
        "AttachmentBlock": [
            ["AttachmentPoint", "U8"]
        ],
        "OperationData": [
            ["AddItem", "BOOL"],
            ["UseExistingAsset", "BOOL"]
        ],
        "InventoryData": [
            ["ItemID", "LLUUID"],
            ["FolderID", "LLUUID"],
            ["CreatorID", "LLUUID"],
            ["OwnerID", "LLUUID"],
            ["GroupID", "LLUUID"],
            ["BaseMask", "U32"],
            ["OwnerMask", "U32"],
            ["GroupMask", "U32"],
            ["EveryoneMask", "U32"],
            ["NextOwnerMask", "U32"],
            ["GroupOwned", "BOOL"],
            ["AssetID", "LLUUID"],
            ["Type", "S8"],
            ["InvType", "S8"],
            ["Flags", "U32"],
            ["SaleType", "U8"],
            ["SalePrice", "S32"],
            ["Name", "Variable1"],
            ["Description", "Variable1"],
            ["CreationDate", "S32"],
            ["CRC", "U32"]
        ]
    }
registerMessage("UpdateAttachment", UpdateAttachment)

class RemoveAttachment(message.baseMessage):
    id = 332
    freq = 2
    trusted = False
    zero_coded = False
    blocks = [
        ("AgentData", 1),
        ("AttachmentBlock", 1)
    ]
    structure = {
        "AgentData": [
            ["AgentID", "LLUUID"],
            ["SessionID", "LLUUID"]
        ],
        "AttachmentBlock": [
            ["AttachmentPoint", "U8"],
            ["ItemID", "LLUUID"]
        ]
    }
registerMessage("RemoveAttachment", RemoveAttachment)

class SoundTrigger(message.baseMessage):
    id = 29
    freq = 0
    trusted = False
    zero_coded = False
    blocks = [
        ("SoundData", 1)
    ]
    structure = {
        "SoundData": [
            ["SoundID", "LLUUID"],
            ["OwnerID", "LLUUID"],
            ["ObjectID", "LLUUID"],
            ["ParentID", "LLUUID"],
            ["Handle", "U64"],
            ["Position", "LLVector3"],
            ["Gain", "F32"]
        ]
    }
registerMessage("SoundTrigger", SoundTrigger)

class AttachedSound(message.baseMessage):
    id = 13
    freq = 1
    trusted = True
    zero_coded = False
    blocks = [
        ("DataBlock", 1)
    ]
    structure = {
        "DataBlock": [
            ["SoundID", "LLUUID"],
            ["ObjectID", "LLUUID"],
            ["OwnerID", "LLUUID"],
            ["Gain", "F32"],
            ["Flags", "U8"]
        ]
    }
registerMessage("AttachedSound", AttachedSound)

class AttachedSoundGainChange(message.baseMessage):
    id = 14
    freq = 1
    trusted = True
    zero_coded = False
    blocks = [
        ("DataBlock", 1)
    ]
    structure = {
        "DataBlock": [
            ["ObjectID", "LLUUID"],
            ["Gain", "F32"]
        ]
    }
registerMessage("AttachedSoundGainChange", AttachedSoundGainChange)

class PreloadSound(message.baseMessage):
    id = 15
    freq = 1
    trusted = True
    zero_coded = False
    blocks = [
        ("DataBlock", 0)
    ]
    structure = {
        "DataBlock": [
            ["ObjectID", "LLUUID"],
            ["OwnerID", "LLUUID"],
            ["SoundID", "LLUUID"]
        ]
    }
registerMessage("PreloadSound", PreloadSound)

class AssetUploadRequest(message.baseMessage):
    id = 333
    freq = 2
    trusted = False
    zero_coded = False
    blocks = [
        ("AssetBlock", 1)
    ]
    structure = {
        "AssetBlock": [
            ["TransactionID", "LLUUID"],
            ["Type", "S8"],
            ["Tempfile", "BOOL"],
            ["StoreLocal", "BOOL"],
            ["AssetData", "Variable2"]
        ]
    }
registerMessage("AssetUploadRequest", AssetUploadRequest)

class AssetUploadComplete(message.baseMessage):
    id = 334
    freq = 2
    trusted = False
    zero_coded = False
    blocks = [
        ("AssetBlock", 1)
    ]
    structure = {
        "AssetBlock": [
            ["UUID", "LLUUID"],
            ["Type", "S8"],
            ["Success", "BOOL"]
        ]
    }
registerMessage("AssetUploadComplete", AssetUploadComplete)

class EmailMessageRequest(message.baseMessage):
    id = 335
    freq = 2
    trusted = True
    zero_coded = False
    blocks = [
        ("DataBlock", 1)
    ]
    structure = {
        "DataBlock": [
            ["ObjectID", "LLUUID"],
            ["FromAddress", "Variable1"],
            ["Subject", "Variable1"]
        ]
    }
registerMessage("EmailMessageRequest", EmailMessageRequest)

class EmailMessageReply(message.baseMessage):
    id = 336
    freq = 2
    trusted = True
    zero_coded = False
    blocks = [
        ("DataBlock", 1)
    ]
    structure = {
        "DataBlock": [
            ["ObjectID", "LLUUID"],
            ["More", "U32"],
            ["Time", "U32"],
            ["FromAddress", "Variable1"],
            ["Subject", "Variable1"],
            ["Data", "Variable2"],
            ["MailFilter", "Variable1"]
        ]
    }
registerMessage("EmailMessageReply", EmailMessageReply)

class InternalScriptMail(message.baseMessage):
    id = 16
    freq = 1
    trusted = True
    zero_coded = False
    blocks = [
        ("DataBlock", 1)
    ]
    structure = {
        "DataBlock": [
            ["From", "Variable1"],
            ["To", "LLUUID"],
            ["Subject", "Variable1"],
            ["Body", "Variable2"]
        ]
    }
registerMessage("InternalScriptMail", InternalScriptMail)

class ScriptDataRequest(message.baseMessage):
    id = 337
    freq = 2
    trusted = True
    zero_coded = False
    blocks = [
        ("DataBlock", 0)
    ]
    structure = {
        "DataBlock": [
            ["Hash", "U64"],
            ["RequestType", "S8"],
            ["Request", "Variable2"]
        ]
    }
registerMessage("ScriptDataRequest", ScriptDataRequest)

class ScriptDataReply(message.baseMessage):
    id = 338
    freq = 2
    trusted = True
    zero_coded = False
    blocks = [
        ("DataBlock", 0)
    ]
    structure = {
        "DataBlock": [
            ["Hash", "U64"],
            ["Reply", "Variable2"]
        ]
    }
registerMessage("ScriptDataReply", ScriptDataReply)

class CreateGroupRequest(message.baseMessage):
    id = 339
    freq = 2
    trusted = False
    zero_coded = True
    blocks = [
        ("AgentData", 1),
        ("GroupData", 1)
    ]
    structure = {
        "AgentData": [
            ["AgentID", "LLUUID"],
            ["SessionID", "LLUUID"]
        ],
        "GroupData": [
            ["Name", "Variable1"],
            ["Charter", "Variable2"],
            ["ShowInList", "BOOL"],
            ["InsigniaID", "LLUUID"],
            ["MembershipFee", "S32"],
            ["OpenEnrollment", "BOOL"],
            ["AllowPublish", "BOOL"],
            ["MaturePublish", "BOOL"]
        ]
    }
registerMessage("CreateGroupRequest", CreateGroupRequest)

class CreateGroupReply(message.baseMessage):
    id = 340
    freq = 2
    trusted = True
    zero_coded = False
    blocks = [
        ("AgentData", 1),
        ("ReplyData", 1)
    ]
    structure = {
        "AgentData": [
            ["AgentID", "LLUUID"]
        ],
        "ReplyData": [
            ["GroupID", "LLUUID"],
            ["Success", "BOOL"],
            ["Message", "Variable1"]
        ]
    }
registerMessage("CreateGroupReply", CreateGroupReply)

class UpdateGroupInfo(message.baseMessage):
    id = 341
    freq = 2
    trusted = False
    zero_coded = True
    blocks = [
        ("AgentData", 1),
        ("GroupData", 1)
    ]
    structure = {
        "AgentData": [
            ["AgentID", "LLUUID"],
            ["SessionID", "LLUUID"]
        ],
        "GroupData": [
            ["GroupID", "LLUUID"],
            ["Charter", "Variable2"],
            ["ShowInList", "BOOL"],
            ["InsigniaID", "LLUUID"],
            ["MembershipFee", "S32"],
            ["OpenEnrollment", "BOOL"],
            ["AllowPublish", "BOOL"],
            ["MaturePublish", "BOOL"]
        ]
    }
registerMessage("UpdateGroupInfo", UpdateGroupInfo)

class GroupRoleChanges(message.baseMessage):
    id = 342
    freq = 2
    trusted = False
    zero_coded = False
    blocks = [
        ("AgentData", 1),
        ("RoleChange", 0)
    ]
    structure = {
        "AgentData": [
            ["AgentID", "LLUUID"],
            ["SessionID", "LLUUID"],
            ["GroupID", "LLUUID"]
        ],
        "RoleChange": [
            ["RoleID", "LLUUID"],
            ["MemberID", "LLUUID"],
            ["Change", "U32"]
        ]
    }
registerMessage("GroupRoleChanges", GroupRoleChanges)

class JoinGroupRequest(message.baseMessage):
    id = 343
    freq = 2
    trusted = False
    zero_coded = True
    blocks = [
        ("AgentData", 1),
        ("GroupData", 1)
    ]
    structure = {
        "AgentData": [
            ["AgentID", "LLUUID"],
            ["SessionID", "LLUUID"]
        ],
        "GroupData": [
            ["GroupID", "LLUUID"]
        ]
    }
registerMessage("JoinGroupRequest", JoinGroupRequest)

class JoinGroupReply(message.baseMessage):
    id = 344
    freq = 2
    trusted = True
    zero_coded = False
    blocks = [
        ("AgentData", 1),
        ("GroupData", 1)
    ]
    structure = {
        "AgentData": [
            ["AgentID", "LLUUID"]
        ],
        "GroupData": [
            ["GroupID", "LLUUID"],
            ["Success", "BOOL"]
        ]
    }
registerMessage("JoinGroupReply", JoinGroupReply)

class EjectGroupMemberRequest(message.baseMessage):
    id = 345
    freq = 2
    trusted = False
    zero_coded = False
    blocks = [
        ("AgentData", 1),
        ("GroupData", 1),
        ("EjectData", 0)
    ]
    structure = {
        "AgentData": [
            ["AgentID", "LLUUID"],
            ["SessionID", "LLUUID"]
        ],
        "GroupData": [
            ["GroupID", "LLUUID"]
        ],
        "EjectData": [
            ["EjecteeID", "LLUUID"]
        ]
    }
registerMessage("EjectGroupMemberRequest", EjectGroupMemberRequest)

class EjectGroupMemberReply(message.baseMessage):
    id = 346
    freq = 2
    trusted = True
    zero_coded = False
    blocks = [
        ("AgentData", 1),
        ("GroupData", 1),
        ("EjectData", 1)
    ]
    structure = {
        "AgentData": [
            ["AgentID", "LLUUID"]
        ],
        "GroupData": [
            ["GroupID", "LLUUID"]
        ],
        "EjectData": [
            ["Success", "BOOL"]
        ]
    }
registerMessage("EjectGroupMemberReply", EjectGroupMemberReply)

class LeaveGroupRequest(message.baseMessage):
    id = 347
    freq = 2
    trusted = False
    zero_coded = False
    blocks = [
        ("AgentData", 1),
        ("GroupData", 1)
    ]
    structure = {
        "AgentData": [
            ["AgentID", "LLUUID"],
            ["SessionID", "LLUUID"]
        ],
        "GroupData": [
            ["GroupID", "LLUUID"]
        ]
    }
registerMessage("LeaveGroupRequest", LeaveGroupRequest)

class LeaveGroupReply(message.baseMessage):
    id = 348
    freq = 2
    trusted = True
    zero_coded = False
    blocks = [
        ("AgentData", 1),
        ("GroupData", 1)
    ]
    structure = {
        "AgentData": [
            ["AgentID", "LLUUID"]
        ],
        "GroupData": [
            ["GroupID", "LLUUID"],
            ["Success", "BOOL"]
        ]
    }
registerMessage("LeaveGroupReply", LeaveGroupReply)

class InviteGroupRequest(message.baseMessage):
    id = 349
    freq = 2
    trusted = False
    zero_coded = False
    blocks = [
        ("AgentData", 1),
        ("GroupData", 1),
        ("InviteData", 0)
    ]
    structure = {
        "AgentData": [
            ["AgentID", "LLUUID"],
            ["SessionID", "LLUUID"]
        ],
        "GroupData": [
            ["GroupID", "LLUUID"]
        ],
        "InviteData": [
            ["InviteeID", "LLUUID"],
            ["RoleID", "LLUUID"]
        ]
    }
registerMessage("InviteGroupRequest", InviteGroupRequest)

class InviteGroupResponse(message.baseMessage):
    id = 350
    freq = 2
    trusted = True
    zero_coded = False
    blocks = [
        ("InviteData", 1)
    ]
    structure = {
        "InviteData": [
            ["AgentID", "LLUUID"],
            ["InviteeID", "LLUUID"],
            ["GroupID", "LLUUID"],
            ["RoleID", "LLUUID"],
            ["MembershipFee", "S32"]
        ]
    }
registerMessage("InviteGroupResponse", InviteGroupResponse)

class GroupProfileRequest(message.baseMessage):
    id = 351
    freq = 2
    trusted = False
    zero_coded = False
    blocks = [
        ("AgentData", 1),
        ("GroupData", 1)
    ]
    structure = {
        "AgentData": [
            ["AgentID", "LLUUID"],
            ["SessionID", "LLUUID"]
        ],
        "GroupData": [
            ["GroupID", "LLUUID"]
        ]
    }
registerMessage("GroupProfileRequest", GroupProfileRequest)

class GroupProfileReply(message.baseMessage):
    id = 352
    freq = 2
    trusted = True
    zero_coded = True
    blocks = [
        ("AgentData", 1),
        ("GroupData", 1)
    ]
    structure = {
        "AgentData": [
            ["AgentID", "LLUUID"]
        ],
        "GroupData": [
            ["GroupID", "LLUUID"],
            ["Name", "Variable1"],
            ["Charter", "Variable2"],
            ["ShowInList", "BOOL"],
            ["MemberTitle", "Variable1"],
            ["PowersMask", "U64"],
            ["InsigniaID", "LLUUID"],
            ["FounderID", "LLUUID"],
            ["MembershipFee", "S32"],
            ["OpenEnrollment", "BOOL"],
            ["Money", "S32"],
            ["GroupMembershipCount", "S32"],
            ["GroupRolesCount", "S32"],
            ["AllowPublish", "BOOL"],
            ["MaturePublish", "BOOL"],
            ["OwnerRole", "LLUUID"]
        ]
    }
registerMessage("GroupProfileReply", GroupProfileReply)

class GroupAccountSummaryRequest(message.baseMessage):
    id = 353
    freq = 2
    trusted = False
    zero_coded = True
    blocks = [
        ("AgentData", 1),
        ("MoneyData", 1)
    ]
    structure = {
        "AgentData": [
            ["AgentID", "LLUUID"],
            ["SessionID", "LLUUID"],
            ["GroupID", "LLUUID"]
        ],
        "MoneyData": [
            ["RequestID", "LLUUID"],
            ["IntervalDays", "S32"],
            ["CurrentInterval", "S32"]
        ]
    }
registerMessage("GroupAccountSummaryRequest", GroupAccountSummaryRequest)

class GroupAccountSummaryReply(message.baseMessage):
    id = 354
    freq = 2
    trusted = True
    zero_coded = True
    blocks = [
        ("AgentData", 1),
        ("MoneyData", 1)
    ]
    structure = {
        "AgentData": [
            ["AgentID", "LLUUID"],
            ["GroupID", "LLUUID"]
        ],
        "MoneyData": [
            ["RequestID", "LLUUID"],
            ["IntervalDays", "S32"],
            ["CurrentInterval", "S32"],
            ["StartDate", "Variable1"],
            ["Balance", "S32"],
            ["TotalCredits", "S32"],
            ["TotalDebits", "S32"],
            ["ObjectTaxCurrent", "S32"],
            ["LightTaxCurrent", "S32"],
            ["LandTaxCurrent", "S32"],
            ["GroupTaxCurrent", "S32"],
            ["ParcelDirFeeCurrent", "S32"],
            ["ObjectTaxEstimate", "S32"],
            ["LightTaxEstimate", "S32"],
            ["LandTaxEstimate", "S32"],
            ["GroupTaxEstimate", "S32"],
            ["ParcelDirFeeEstimate", "S32"],
            ["NonExemptMembers", "S32"],
            ["LastTaxDate", "Variable1"],
            ["TaxDate", "Variable1"]
        ]
    }
registerMessage("GroupAccountSummaryReply", GroupAccountSummaryReply)

class GroupAccountDetailsRequest(message.baseMessage):
    id = 355
    freq = 2
    trusted = False
    zero_coded = True
    blocks = [
        ("AgentData", 1),
        ("MoneyData", 1)
    ]
    structure = {
        "AgentData": [
            ["AgentID", "LLUUID"],
            ["SessionID", "LLUUID"],
            ["GroupID", "LLUUID"]
        ],
        "MoneyData": [
            ["RequestID", "LLUUID"],
            ["IntervalDays", "S32"],
            ["CurrentInterval", "S32"]
        ]
    }
registerMessage("GroupAccountDetailsRequest", GroupAccountDetailsRequest)

class GroupAccountDetailsReply(message.baseMessage):
    id = 356
    freq = 2
    trusted = True
    zero_coded = True
    blocks = [
        ("AgentData", 1),
        ("MoneyData", 1),
        ("HistoryData", 0)
    ]
    structure = {
        "AgentData": [
            ["AgentID", "LLUUID"],
            ["GroupID", "LLUUID"]
        ],
        "MoneyData": [
            ["RequestID", "LLUUID"],
            ["IntervalDays", "S32"],
            ["CurrentInterval", "S32"],
            ["StartDate", "Variable1"]
        ],
        "HistoryData": [
            ["Description", "Variable1"],
            ["Amount", "S32"]
        ]
    }
registerMessage("GroupAccountDetailsReply", GroupAccountDetailsReply)

class GroupAccountTransactionsRequest(message.baseMessage):
    id = 357
    freq = 2
    trusted = False
    zero_coded = True
    blocks = [
        ("AgentData", 1),
        ("MoneyData", 1)
    ]
    structure = {
        "AgentData": [
            ["AgentID", "LLUUID"],
            ["SessionID", "LLUUID"],
            ["GroupID", "LLUUID"]
        ],
        "MoneyData": [
            ["RequestID", "LLUUID"],
            ["IntervalDays", "S32"],
            ["CurrentInterval", "S32"]
        ]
    }
registerMessage("GroupAccountTransactionsRequest", GroupAccountTransactionsRequest)

class GroupAccountTransactionsReply(message.baseMessage):
    id = 358
    freq = 2
    trusted = True
    zero_coded = True
    blocks = [
        ("AgentData", 1),
        ("MoneyData", 1),
        ("HistoryData", 0)
    ]
    structure = {
        "AgentData": [
            ["AgentID", "LLUUID"],
            ["GroupID", "LLUUID"]
        ],
        "MoneyData": [
            ["RequestID", "LLUUID"],
            ["IntervalDays", "S32"],
            ["CurrentInterval", "S32"],
            ["StartDate", "Variable1"]
        ],
        "HistoryData": [
            ["Time", "Variable1"],
            ["User", "Variable1"],
            ["Type", "S32"],
            ["Item", "Variable1"],
            ["Amount", "S32"]
        ]
    }
registerMessage("GroupAccountTransactionsReply", GroupAccountTransactionsReply)

class GroupActiveProposalsRequest(message.baseMessage):
    id = 359
    freq = 2
    trusted = False
    zero_coded = False
    blocks = [
        ("AgentData", 1),
        ("GroupData", 1),
        ("TransactionData", 1)
    ]
    structure = {
        "AgentData": [
            ["AgentID", "LLUUID"],
            ["SessionID", "LLUUID"]
        ],
        "GroupData": [
            ["GroupID", "LLUUID"]
        ],
        "TransactionData": [
            ["TransactionID", "LLUUID"]
        ]
    }
registerMessage("GroupActiveProposalsRequest", GroupActiveProposalsRequest)

class GroupActiveProposalItemReply(message.baseMessage):
    id = 360
    freq = 2
    trusted = True
    zero_coded = True
    blocks = [
        ("AgentData", 1),
        ("TransactionData", 1),
        ("ProposalData", 0)
    ]
    structure = {
        "AgentData": [
            ["AgentID", "LLUUID"],
            ["GroupID", "LLUUID"]
        ],
        "TransactionData": [
            ["TransactionID", "LLUUID"],
            ["TotalNumItems", "U32"]
        ],
        "ProposalData": [
            ["VoteID", "LLUUID"],
            ["VoteInitiator", "LLUUID"],
            ["TerseDateID", "Variable1"],
            ["StartDateTime", "Variable1"],
            ["EndDateTime", "Variable1"],
            ["AlreadyVoted", "BOOL"],
            ["VoteCast", "Variable1"],
            ["Majority", "F32"],
            ["Quorum", "S32"],
            ["ProposalText", "Variable1"]
        ]
    }
registerMessage("GroupActiveProposalItemReply", GroupActiveProposalItemReply)

class GroupVoteHistoryRequest(message.baseMessage):
    id = 361
    freq = 2
    trusted = False
    zero_coded = False
    blocks = [
        ("AgentData", 1),
        ("GroupData", 1),
        ("TransactionData", 1)
    ]
    structure = {
        "AgentData": [
            ["AgentID", "LLUUID"],
            ["SessionID", "LLUUID"]
        ],
        "GroupData": [
            ["GroupID", "LLUUID"]
        ],
        "TransactionData": [
            ["TransactionID", "LLUUID"]
        ]
    }
registerMessage("GroupVoteHistoryRequest", GroupVoteHistoryRequest)

class GroupVoteHistoryItemReply(message.baseMessage):
    id = 362
    freq = 2
    trusted = True
    zero_coded = True
    blocks = [
        ("AgentData", 1),
        ("TransactionData", 1),
        ("HistoryItemData", 1),
        ("VoteItem", 0)
    ]
    structure = {
        "AgentData": [
            ["AgentID", "LLUUID"],
            ["GroupID", "LLUUID"]
        ],
        "TransactionData": [
            ["TransactionID", "LLUUID"],
            ["TotalNumItems", "U32"]
        ],
        "HistoryItemData": [
            ["VoteID", "LLUUID"],
            ["TerseDateID", "Variable1"],
            ["StartDateTime", "Variable1"],
            ["EndDateTime", "Variable1"],
            ["VoteInitiator", "LLUUID"],
            ["VoteType", "Variable1"],
            ["VoteResult", "Variable1"],
            ["Majority", "F32"],
            ["Quorum", "S32"],
            ["ProposalText", "Variable2"]
        ],
        "VoteItem": [
            ["CandidateID", "LLUUID"],
            ["VoteCast", "Variable1"],
            ["NumVotes", "S32"]
        ]
    }
registerMessage("GroupVoteHistoryItemReply", GroupVoteHistoryItemReply)

class StartGroupProposal(message.baseMessage):
    id = 363
    freq = 2
    trusted = False
    zero_coded = True
    blocks = [
        ("AgentData", 1),
        ("ProposalData", 1)
    ]
    structure = {
        "AgentData": [
            ["AgentID", "LLUUID"],
            ["SessionID", "LLUUID"]
        ],
        "ProposalData": [
            ["GroupID", "LLUUID"],
            ["Quorum", "S32"],
            ["Majority", "F32"],
            ["Duration", "S32"],
            ["ProposalText", "Variable1"]
        ]
    }
registerMessage("StartGroupProposal", StartGroupProposal)

class GroupProposalBallot(message.baseMessage):
    id = 364
    freq = 2
    trusted = False
    zero_coded = False
    blocks = [
        ("AgentData", 1),
        ("ProposalData", 1)
    ]
    structure = {
        "AgentData": [
            ["AgentID", "LLUUID"],
            ["SessionID", "LLUUID"]
        ],
        "ProposalData": [
            ["ProposalID", "LLUUID"],
            ["GroupID", "LLUUID"],
            ["VoteCast", "Variable1"]
        ]
    }
registerMessage("GroupProposalBallot", GroupProposalBallot)

class TallyVotes(message.baseMessage):
    id = 365
    freq = 2
    trusted = True
    zero_coded = False
    blocks = [

    ]
    structure = {

    }
registerMessage("TallyVotes", TallyVotes)

class GroupMembersRequest(message.baseMessage):
    id = 366
    freq = 2
    trusted = False
    zero_coded = False
    blocks = [
        ("AgentData", 1),
        ("GroupData", 1)
    ]
    structure = {
        "AgentData": [
            ["AgentID", "LLUUID"],
            ["SessionID", "LLUUID"]
        ],
        "GroupData": [
            ["GroupID", "LLUUID"],
            ["RequestID", "LLUUID"]
        ]
    }
registerMessage("GroupMembersRequest", GroupMembersRequest)

class GroupMembersReply(message.baseMessage):
    id = 367
    freq = 2
    trusted = True
    zero_coded = True
    blocks = [
        ("AgentData", 1),
        ("GroupData", 1),
        ("MemberData", 0)
    ]
    structure = {
        "AgentData": [
            ["AgentID", "LLUUID"]
        ],
        "GroupData": [
            ["GroupID", "LLUUID"],
            ["RequestID", "LLUUID"],
            ["MemberCount", "S32"]
        ],
        "MemberData": [
            ["AgentID", "LLUUID"],
            ["Contribution", "S32"],
            ["OnlineStatus", "Variable1"],
            ["AgentPowers", "U64"],
            ["Title", "Variable1"],
            ["IsOwner", "BOOL"]
        ]
    }
registerMessage("GroupMembersReply", GroupMembersReply)

class ActivateGroup(message.baseMessage):
    id = 368
    freq = 2
    trusted = False
    zero_coded = True
    blocks = [
        ("AgentData", 1)
    ]
    structure = {
        "AgentData": [
            ["AgentID", "LLUUID"],
            ["SessionID", "LLUUID"],
            ["GroupID", "LLUUID"]
        ]
    }
registerMessage("ActivateGroup", ActivateGroup)

class SetGroupContribution(message.baseMessage):
    id = 369
    freq = 2
    trusted = False
    zero_coded = False
    blocks = [
        ("AgentData", 1),
        ("Data", 1)
    ]
    structure = {
        "AgentData": [
            ["AgentID", "LLUUID"],
            ["SessionID", "LLUUID"]
        ],
        "Data": [
            ["GroupID", "LLUUID"],
            ["Contribution", "S32"]
        ]
    }
registerMessage("SetGroupContribution", SetGroupContribution)

class SetGroupAcceptNotices(message.baseMessage):
    id = 370
    freq = 2
    trusted = False
    zero_coded = False
    blocks = [
        ("AgentData", 1),
        ("Data", 1),
        ("NewData", 1)
    ]
    structure = {
        "AgentData": [
            ["AgentID", "LLUUID"],
            ["SessionID", "LLUUID"]
        ],
        "Data": [
            ["GroupID", "LLUUID"],
            ["AcceptNotices", "BOOL"]
        ],
        "NewData": [
            ["ListInProfile", "BOOL"]
        ]
    }
registerMessage("SetGroupAcceptNotices", SetGroupAcceptNotices)

class GroupRoleDataRequest(message.baseMessage):
    id = 371
    freq = 2
    trusted = False
    zero_coded = False
    blocks = [
        ("AgentData", 1),
        ("GroupData", 1)
    ]
    structure = {
        "AgentData": [
            ["AgentID", "LLUUID"],
            ["SessionID", "LLUUID"]
        ],
        "GroupData": [
            ["GroupID", "LLUUID"],
            ["RequestID", "LLUUID"]
        ]
    }
registerMessage("GroupRoleDataRequest", GroupRoleDataRequest)

class GroupRoleDataReply(message.baseMessage):
    id = 372
    freq = 2
    trusted = True
    zero_coded = False
    blocks = [
        ("AgentData", 1),
        ("GroupData", 1),
        ("RoleData", 0)
    ]
    structure = {
        "AgentData": [
            ["AgentID", "LLUUID"]
        ],
        "GroupData": [
            ["GroupID", "LLUUID"],
            ["RequestID", "LLUUID"],
            ["RoleCount", "S32"]
        ],
        "RoleData": [
            ["RoleID", "LLUUID"],
            ["Name", "Variable1"],
            ["Title", "Variable1"],
            ["Description", "Variable1"],
            ["Powers", "U64"],
            ["Members", "U32"]
        ]
    }
registerMessage("GroupRoleDataReply", GroupRoleDataReply)

class GroupRoleMembersRequest(message.baseMessage):
    id = 373
    freq = 2
    trusted = False
    zero_coded = False
    blocks = [
        ("AgentData", 1),
        ("GroupData", 1)
    ]
    structure = {
        "AgentData": [
            ["AgentID", "LLUUID"],
            ["SessionID", "LLUUID"]
        ],
        "GroupData": [
            ["GroupID", "LLUUID"],
            ["RequestID", "LLUUID"]
        ]
    }
registerMessage("GroupRoleMembersRequest", GroupRoleMembersRequest)

class GroupRoleMembersReply(message.baseMessage):
    id = 374
    freq = 2
    trusted = True
    zero_coded = False
    blocks = [
        ("AgentData", 1),
        ("MemberData", 0)
    ]
    structure = {
        "AgentData": [
            ["AgentID", "LLUUID"],
            ["GroupID", "LLUUID"],
            ["RequestID", "LLUUID"],
            ["TotalPairs", "U32"]
        ],
        "MemberData": [
            ["RoleID", "LLUUID"],
            ["MemberID", "LLUUID"]
        ]
    }
registerMessage("GroupRoleMembersReply", GroupRoleMembersReply)

class GroupTitlesRequest(message.baseMessage):
    id = 375
    freq = 2
    trusted = False
    zero_coded = False
    blocks = [
        ("AgentData", 1)
    ]
    structure = {
        "AgentData": [
            ["AgentID", "LLUUID"],
            ["SessionID", "LLUUID"],
            ["GroupID", "LLUUID"],
            ["RequestID", "LLUUID"]
        ]
    }
registerMessage("GroupTitlesRequest", GroupTitlesRequest)

class GroupTitlesReply(message.baseMessage):
    id = 376
    freq = 2
    trusted = True
    zero_coded = True
    blocks = [
        ("AgentData", 1),
        ("GroupData", 0)
    ]
    structure = {
        "AgentData": [
            ["AgentID", "LLUUID"],
            ["GroupID", "LLUUID"],
            ["RequestID", "LLUUID"]
        ],
        "GroupData": [
            ["Title", "Variable1"],
            ["RoleID", "LLUUID"],
            ["Selected", "BOOL"]
        ]
    }
registerMessage("GroupTitlesReply", GroupTitlesReply)

class GroupTitleUpdate(message.baseMessage):
    id = 377
    freq = 2
    trusted = False
    zero_coded = False
    blocks = [
        ("AgentData", 1)
    ]
    structure = {
        "AgentData": [
            ["AgentID", "LLUUID"],
            ["SessionID", "LLUUID"],
            ["GroupID", "LLUUID"],
            ["TitleRoleID", "LLUUID"]
        ]
    }
registerMessage("GroupTitleUpdate", GroupTitleUpdate)

class GroupRoleUpdate(message.baseMessage):
    id = 378
    freq = 2
    trusted = False
    zero_coded = False
    blocks = [
        ("AgentData", 1),
        ("RoleData", 0)
    ]
    structure = {
        "AgentData": [
            ["AgentID", "LLUUID"],
            ["SessionID", "LLUUID"],
            ["GroupID", "LLUUID"]
        ],
        "RoleData": [
            ["RoleID", "LLUUID"],
            ["Name", "Variable1"],
            ["Description", "Variable1"],
            ["Title", "Variable1"],
            ["Powers", "U64"],
            ["UpdateType", "U8"]
        ]
    }
registerMessage("GroupRoleUpdate", GroupRoleUpdate)

class LiveHelpGroupRequest(message.baseMessage):
    id = 379
    freq = 2
    trusted = True
    zero_coded = False
    blocks = [
        ("RequestData", 1)
    ]
    structure = {
        "RequestData": [
            ["RequestID", "LLUUID"],
            ["AgentID", "LLUUID"]
        ]
    }
registerMessage("LiveHelpGroupRequest", LiveHelpGroupRequest)

class LiveHelpGroupReply(message.baseMessage):
    id = 380
    freq = 2
    trusted = True
    zero_coded = False
    blocks = [
        ("ReplyData", 1)
    ]
    structure = {
        "ReplyData": [
            ["RequestID", "LLUUID"],
            ["GroupID", "LLUUID"],
            ["Selection", "Variable1"]
        ]
    }
registerMessage("LiveHelpGroupReply", LiveHelpGroupReply)

class AgentWearablesRequest(message.baseMessage):
    id = 381
    freq = 2
    trusted = False
    zero_coded = False
    blocks = [
        ("AgentData", 1)
    ]
    structure = {
        "AgentData": [
            ["AgentID", "LLUUID"],
            ["SessionID", "LLUUID"]
        ]
    }
registerMessage("AgentWearablesRequest", AgentWearablesRequest)

class AgentWearablesUpdate(message.baseMessage):
    id = 382
    freq = 2
    trusted = True
    zero_coded = True
    blocks = [
        ("AgentData", 1),
        ("WearableData", 0)
    ]
    structure = {
        "AgentData": [
            ["AgentID", "LLUUID"],
            ["SessionID", "LLUUID"],
            ["SerialNum", "U32"]
        ],
        "WearableData": [
            ["ItemID", "LLUUID"],
            ["AssetID", "LLUUID"],
            ["WearableType", "U8"]
        ]
    }
registerMessage("AgentWearablesUpdate", AgentWearablesUpdate)

class AgentIsNowWearing(message.baseMessage):
    id = 383
    freq = 2
    trusted = False
    zero_coded = True
    blocks = [
        ("AgentData", 1),
        ("WearableData", 0)
    ]
    structure = {
        "AgentData": [
            ["AgentID", "LLUUID"],
            ["SessionID", "LLUUID"]
        ],
        "WearableData": [
            ["ItemID", "LLUUID"],
            ["WearableType", "U8"]
        ]
    }
registerMessage("AgentIsNowWearing", AgentIsNowWearing)

class AgentCachedTexture(message.baseMessage):
    id = 384
    freq = 2
    trusted = False
    zero_coded = False
    blocks = [
        ("AgentData", 1),
        ("WearableData", 0)
    ]
    structure = {
        "AgentData": [
            ["AgentID", "LLUUID"],
            ["SessionID", "LLUUID"],
            ["SerialNum", "S32"]
        ],
        "WearableData": [
            ["ID", "LLUUID"],
            ["TextureIndex", "U8"]
        ]
    }
registerMessage("AgentCachedTexture", AgentCachedTexture)

class AgentCachedTextureResponse(message.baseMessage):
    id = 385
    freq = 2
    trusted = True
    zero_coded = False
    blocks = [
        ("AgentData", 1),
        ("WearableData", 0)
    ]
    structure = {
        "AgentData": [
            ["AgentID", "LLUUID"],
            ["SessionID", "LLUUID"],
            ["SerialNum", "S32"]
        ],
        "WearableData": [
            ["TextureID", "LLUUID"],
            ["TextureIndex", "U8"],
            ["HostName", "Variable1"]
        ]
    }
registerMessage("AgentCachedTextureResponse", AgentCachedTextureResponse)

class AgentDataUpdateRequest(message.baseMessage):
    id = 386
    freq = 2
    trusted = False
    zero_coded = False
    blocks = [
        ("AgentData", 1)
    ]
    structure = {
        "AgentData": [
            ["AgentID", "LLUUID"],
            ["SessionID", "LLUUID"]
        ]
    }
registerMessage("AgentDataUpdateRequest", AgentDataUpdateRequest)

class AgentDataUpdate(message.baseMessage):
    id = 387
    freq = 2
    trusted = True
    zero_coded = True
    blocks = [
        ("AgentData", 1)
    ]
    structure = {
        "AgentData": [
            ["AgentID", "LLUUID"],
            ["FirstName", "Variable1"],
            ["LastName", "Variable1"],
            ["GroupTitle", "Variable1"],
            ["ActiveGroupID", "LLUUID"],
            ["GroupPowers", "U64"],
            ["GroupName", "Variable1"]
        ]
    }
registerMessage("AgentDataUpdate", AgentDataUpdate)

class GroupDataUpdate(message.baseMessage):
    id = 388
    freq = 2
    trusted = True
    zero_coded = True
    blocks = [
        ("AgentGroupData", 0)
    ]
    structure = {
        "AgentGroupData": [
            ["AgentID", "LLUUID"],
            ["GroupID", "LLUUID"],
            ["AgentPowers", "U64"],
            ["GroupTitle", "Variable1"]
        ]
    }
registerMessage("GroupDataUpdate", GroupDataUpdate)

class AgentGroupDataUpdate(message.baseMessage):
    id = 389
    freq = 2
    trusted = True
    zero_coded = True
    blocks = [
        ("AgentData", 1),
        ("GroupData", 0)
    ]
    structure = {
        "AgentData": [
            ["AgentID", "LLUUID"]
        ],
        "GroupData": [
            ["GroupID", "LLUUID"],
            ["GroupPowers", "U64"],
            ["AcceptNotices", "BOOL"],
            ["GroupInsigniaID", "LLUUID"],
            ["Contribution", "S32"],
            ["GroupName", "Variable1"]
        ]
    }
registerMessage("AgentGroupDataUpdate", AgentGroupDataUpdate)

class AgentDropGroup(message.baseMessage):
    id = 390
    freq = 2
    trusted = True
    zero_coded = True
    blocks = [
        ("AgentData", 1)
    ]
    structure = {
        "AgentData": [
            ["AgentID", "LLUUID"],
            ["GroupID", "LLUUID"]
        ]
    }
registerMessage("AgentDropGroup", AgentDropGroup)

class LogTextMessage(message.baseMessage):
    id = 391
    freq = 2
    trusted = True
    zero_coded = True
    blocks = [
        ("DataBlock", 0)
    ]
    structure = {
        "DataBlock": [
            ["FromAgentId", "LLUUID"],
            ["ToAgentId", "LLUUID"],
            ["GlobalX", "F64"],
            ["GlobalY", "F64"],
            ["Time", "U32"],
            ["Message", "Variable2"]
        ]
    }
registerMessage("LogTextMessage", LogTextMessage)

class ViewerEffect(message.baseMessage):
    id = 17
    freq = 1
    trusted = False
    zero_coded = True
    blocks = [
        ("AgentData", 1),
        ("Effect", 0)
    ]
    structure = {
        "AgentData": [
            ["AgentID", "LLUUID"],
            ["SessionID", "LLUUID"]
        ],
        "Effect": [
            ["ID", "LLUUID"],
            ["AgentID", "LLUUID"],
            ["Type", "U8"],
            ["Duration", "F32"],
            ["Color", "Fixed"],
            ["TypeData", "Variable1"]
        ]
    }
registerMessage("ViewerEffect", ViewerEffect)

class CreateTrustedCircuit(message.baseMessage):
    id = 392
    freq = 2
    trusted = False
    zero_coded = False
    blocks = [
        ("DataBlock", 1)
    ]
    structure = {
        "DataBlock": [
            ["EndPointID", "LLUUID"],
            ["Digest", "Fixed"]
        ]
    }
registerMessage("CreateTrustedCircuit", CreateTrustedCircuit)

class DenyTrustedCircuit(message.baseMessage):
    id = 393
    freq = 2
    trusted = False
    zero_coded = False
    blocks = [
        ("DataBlock", 1)
    ]
    structure = {
        "DataBlock": [
            ["EndPointID", "LLUUID"]
        ]
    }
registerMessage("DenyTrustedCircuit", DenyTrustedCircuit)

class RequestTrustedCircuit(message.baseMessage):
    id = 394
    freq = 2
    trusted = True
    zero_coded = False
    blocks = [

    ]
    structure = {

    }
registerMessage("RequestTrustedCircuit", RequestTrustedCircuit)

class RezSingleAttachmentFromInv(message.baseMessage):
    id = 395
    freq = 2
    trusted = False
    zero_coded = True
    blocks = [
        ("AgentData", 1),
        ("ObjectData", 1)
    ]
    structure = {
        "AgentData": [
            ["AgentID", "LLUUID"],
            ["SessionID", "LLUUID"]
        ],
        "ObjectData": [
            ["ItemID", "LLUUID"],
            ["OwnerID", "LLUUID"],
            ["AttachmentPt", "U8"],
            ["ItemFlags", "U32"],
            ["GroupMask", "U32"],
            ["EveryoneMask", "U32"],
            ["NextOwnerMask", "U32"],
            ["Name", "Variable1"],
            ["Description", "Variable1"]
        ]
    }
registerMessage("RezSingleAttachmentFromInv", RezSingleAttachmentFromInv)

class RezMultipleAttachmentsFromInv(message.baseMessage):
    id = 396
    freq = 2
    trusted = False
    zero_coded = True
    blocks = [
        ("AgentData", 1),
        ("HeaderData", 1),
        ("ObjectData", 0)
    ]
    structure = {
        "AgentData": [
            ["AgentID", "LLUUID"],
            ["SessionID", "LLUUID"]
        ],
        "HeaderData": [
            ["CompoundMsgID", "LLUUID"],
            ["TotalObjects", "U8"],
            ["FirstDetachAll", "BOOL"]
        ],
        "ObjectData": [
            ["ItemID", "LLUUID"],
            ["OwnerID", "LLUUID"],
            ["AttachmentPt", "U8"],
            ["ItemFlags", "U32"],
            ["GroupMask", "U32"],
            ["EveryoneMask", "U32"],
            ["NextOwnerMask", "U32"],
            ["Name", "Variable1"],
            ["Description", "Variable1"]
        ]
    }
registerMessage("RezMultipleAttachmentsFromInv", RezMultipleAttachmentsFromInv)

class DetachAttachmentIntoInv(message.baseMessage):
    id = 397
    freq = 2
    trusted = False
    zero_coded = False
    blocks = [
        ("ObjectData", 1)
    ]
    structure = {
        "ObjectData": [
            ["AgentID", "LLUUID"],
            ["ItemID", "LLUUID"]
        ]
    }
registerMessage("DetachAttachmentIntoInv", DetachAttachmentIntoInv)

class CreateNewOutfitAttachments(message.baseMessage):
    id = 398
    freq = 2
    trusted = False
    zero_coded = False
    blocks = [
        ("AgentData", 1),
        ("HeaderData", 1),
        ("ObjectData", 0)
    ]
    structure = {
        "AgentData": [
            ["AgentID", "LLUUID"],
            ["SessionID", "LLUUID"]
        ],
        "HeaderData": [
            ["NewFolderID", "LLUUID"]
        ],
        "ObjectData": [
            ["OldItemID", "LLUUID"],
            ["OldFolderID", "LLUUID"]
        ]
    }
registerMessage("CreateNewOutfitAttachments", CreateNewOutfitAttachments)

class UserInfoRequest(message.baseMessage):
    id = 399
    freq = 2
    trusted = False
    zero_coded = False
    blocks = [
        ("AgentData", 1)
    ]
    structure = {
        "AgentData": [
            ["AgentID", "LLUUID"],
            ["SessionID", "LLUUID"]
        ]
    }
registerMessage("UserInfoRequest", UserInfoRequest)

class UserInfoReply(message.baseMessage):
    id = 400
    freq = 2
    trusted = False
    zero_coded = False
    blocks = [
        ("AgentData", 1),
        ("UserData", 1)
    ]
    structure = {
        "AgentData": [
            ["AgentID", "LLUUID"]
        ],
        "UserData": [
            ["IMViaEMail", "BOOL"],
            ["DirectoryVisibility", "Variable1"],
            ["EMail", "Variable2"]
        ]
    }
registerMessage("UserInfoReply", UserInfoReply)

class UpdateUserInfo(message.baseMessage):
    id = 401
    freq = 2
    trusted = False
    zero_coded = False
    blocks = [
        ("AgentData", 1),
        ("UserData", 1)
    ]
    structure = {
        "AgentData": [
            ["AgentID", "LLUUID"],
            ["SessionID", "LLUUID"]
        ],
        "UserData": [
            ["IMViaEMail", "BOOL"],
            ["DirectoryVisibility", "Variable1"]
        ]
    }
registerMessage("UpdateUserInfo", UpdateUserInfo)

class ParcelRename(message.baseMessage):
    id = 402
    freq = 2
    trusted = True
    zero_coded = False
    blocks = [
        ("ParcelData", 0)
    ]
    structure = {
        "ParcelData": [
            ["ParcelID", "LLUUID"],
            ["NewName", "Variable1"]
        ]
    }
registerMessage("ParcelRename", ParcelRename)

class InitiateDownload(message.baseMessage):
    id = 403
    freq = 2
    trusted = False
    zero_coded = False
    blocks = [
        ("AgentData", 1),
        ("FileData", 1)
    ]
    structure = {
        "AgentData": [
            ["AgentID", "LLUUID"]
        ],
        "FileData": [
            ["SimFilename", "Variable1"],
            ["ViewerFilename", "Variable1"]
        ]
    }
registerMessage("InitiateDownload", InitiateDownload)

class SystemMessage(message.baseMessage):
    id = 404
    freq = 2
    trusted = True
    zero_coded = True
    blocks = [
        ("MethodData", 1),
        ("ParamList", 0)
    ]
    structure = {
        "MethodData": [
            ["Method", "Variable1"],
            ["Invoice", "LLUUID"],
            ["Digest", "Fixed"]
        ],
        "ParamList": [
            ["Parameter", "Variable1"]
        ]
    }
registerMessage("SystemMessage", SystemMessage)

class MapLayerRequest(message.baseMessage):
    id = 405
    freq = 2
    trusted = False
    zero_coded = False
    blocks = [
        ("AgentData", 1)
    ]
    structure = {
        "AgentData": [
            ["AgentID", "LLUUID"],
            ["SessionID", "LLUUID"],
            ["Flags", "U32"],
            ["EstateID", "U32"],
            ["Godlike", "BOOL"]
        ]
    }
registerMessage("MapLayerRequest", MapLayerRequest)

class MapLayerReply(message.baseMessage):
    id = 406
    freq = 2
    trusted = True
    zero_coded = False
    blocks = [
        ("AgentData", 1),
        ("LayerData", 0)
    ]
    structure = {
        "AgentData": [
            ["AgentID", "LLUUID"],
            ["Flags", "U32"]
        ],
        "LayerData": [
            ["Left", "U32"],
            ["Right", "U32"],
            ["Top", "U32"],
            ["Bottom", "U32"],
            ["ImageID", "LLUUID"]
        ]
    }
registerMessage("MapLayerReply", MapLayerReply)

class MapBlockRequest(message.baseMessage):
    id = 407
    freq = 2
    trusted = False
    zero_coded = False
    blocks = [
        ("AgentData", 1),
        ("PositionData", 1)
    ]
    structure = {
        "AgentData": [
            ["AgentID", "LLUUID"],
            ["SessionID", "LLUUID"],
            ["Flags", "U32"],
            ["EstateID", "U32"],
            ["Godlike", "BOOL"]
        ],
        "PositionData": [
            ["MinX", "U16"],
            ["MaxX", "U16"],
            ["MinY", "U16"],
            ["MaxY", "U16"]
        ]
    }
registerMessage("MapBlockRequest", MapBlockRequest)

class MapNameRequest(message.baseMessage):
    id = 408
    freq = 2
    trusted = False
    zero_coded = False
    blocks = [
        ("AgentData", 1),
        ("NameData", 1)
    ]
    structure = {
        "AgentData": [
            ["AgentID", "LLUUID"],
            ["SessionID", "LLUUID"],
            ["Flags", "U32"],
            ["EstateID", "U32"],
            ["Godlike", "BOOL"]
        ],
        "NameData": [
            ["Name", "Variable1"]
        ]
    }
registerMessage("MapNameRequest", MapNameRequest)

class MapBlockReply(message.baseMessage):
    id = 409
    freq = 2
    trusted = True
    zero_coded = False
    blocks = [
        ("AgentData", 1),
        ("Data", 0)
    ]
    structure = {
        "AgentData": [
            ["AgentID", "LLUUID"],
            ["Flags", "U32"]
        ],
        "Data": [
            ["X", "U16"],
            ["Y", "U16"],
            ["Name", "Variable1"],
            ["Access", "U8"],
            ["RegionFlags", "U32"],
            ["WaterHeight", "U8"],
            ["Agents", "U8"],
            ["MapImageID", "LLUUID"]
        ]
    }
registerMessage("MapBlockReply", MapBlockReply)

class MapItemRequest(message.baseMessage):
    id = 410
    freq = 2
    trusted = False
    zero_coded = False
    blocks = [
        ("AgentData", 1),
        ("RequestData", 1)
    ]
    structure = {
        "AgentData": [
            ["AgentID", "LLUUID"],
            ["SessionID", "LLUUID"],
            ["Flags", "U32"],
            ["EstateID", "U32"],
            ["Godlike", "BOOL"]
        ],
        "RequestData": [
            ["ItemType", "U32"],
            ["RegionHandle", "U64"]
        ]
    }
registerMessage("MapItemRequest", MapItemRequest)

class MapItemReply(message.baseMessage):
    id = 411
    freq = 2
    trusted = True
    zero_coded = False
    blocks = [
        ("AgentData", 1),
        ("RequestData", 1),
        ("Data", 0)
    ]
    structure = {
        "AgentData": [
            ["AgentID", "LLUUID"],
            ["Flags", "U32"]
        ],
        "RequestData": [
            ["ItemType", "U32"]
        ],
        "Data": [
            ["X", "U32"],
            ["Y", "U32"],
            ["ID", "LLUUID"],
            ["Extra", "S32"],
            ["Extra2", "S32"],
            ["Name", "Variable1"]
        ]
    }
registerMessage("MapItemReply", MapItemReply)

class SendPostcard(message.baseMessage):
    id = 412
    freq = 2
    trusted = False
    zero_coded = False
    blocks = [
        ("AgentData", 1)
    ]
    structure = {
        "AgentData": [
            ["AgentID", "LLUUID"],
            ["SessionID", "LLUUID"],
            ["AssetID", "LLUUID"],
            ["PosGlobal", "LLVector3d"],
            ["To", "Variable1"],
            ["From", "Variable1"],
            ["Name", "Variable1"],
            ["Subject", "Variable1"],
            ["Msg", "Variable2"],
            ["AllowPublish", "BOOL"],
            ["MaturePublish", "BOOL"]
        ]
    }
registerMessage("SendPostcard", SendPostcard)

class RpcChannelRequest(message.baseMessage):
    id = 413
    freq = 2
    trusted = True
    zero_coded = False
    blocks = [
        ("DataBlock", 1)
    ]
    structure = {
        "DataBlock": [
            ["GridX", "U32"],
            ["GridY", "U32"],
            ["TaskID", "LLUUID"],
            ["ItemID", "LLUUID"]
        ]
    }
registerMessage("RpcChannelRequest", RpcChannelRequest)

class RpcChannelReply(message.baseMessage):
    id = 414
    freq = 2
    trusted = True
    zero_coded = False
    blocks = [
        ("DataBlock", 1)
    ]
    structure = {
        "DataBlock": [
            ["TaskID", "LLUUID"],
            ["ItemID", "LLUUID"],
            ["ChannelID", "LLUUID"]
        ]
    }
registerMessage("RpcChannelReply", RpcChannelReply)

class RpcScriptRequestInbound(message.baseMessage):
    id = 415
    freq = 2
    trusted = False
    zero_coded = False
    blocks = [
        ("TargetBlock", 1),
        ("DataBlock", 1)
    ]
    structure = {
        "TargetBlock": [
            ["GridX", "U32"],
            ["GridY", "U32"]
        ],
        "DataBlock": [
            ["TaskID", "LLUUID"],
            ["ItemID", "LLUUID"],
            ["ChannelID", "LLUUID"],
            ["IntValue", "U32"],
            ["StringValue", "Variable2"]
        ]
    }
registerMessage("RpcScriptRequestInbound", RpcScriptRequestInbound)

class RpcScriptRequestInboundForward(message.baseMessage):
    id = 416
    freq = 2
    trusted = True
    zero_coded = False
    blocks = [
        ("DataBlock", 1)
    ]
    structure = {
        "DataBlock": [
            ["RPCServerIP", "IPADDR"],
            ["RPCServerPort", "IPPORT"],
            ["TaskID", "LLUUID"],
            ["ItemID", "LLUUID"],
            ["ChannelID", "LLUUID"],
            ["IntValue", "U32"],
            ["StringValue", "Variable2"]
        ]
    }
registerMessage("RpcScriptRequestInboundForward", RpcScriptRequestInboundForward)

class RpcScriptReplyInbound(message.baseMessage):
    id = 417
    freq = 2
    trusted = False
    zero_coded = False
    blocks = [
        ("DataBlock", 1)
    ]
    structure = {
        "DataBlock": [
            ["TaskID", "LLUUID"],
            ["ItemID", "LLUUID"],
            ["ChannelID", "LLUUID"],
            ["IntValue", "U32"],
            ["StringValue", "Variable2"]
        ]
    }
registerMessage("RpcScriptReplyInbound", RpcScriptReplyInbound)

class ScriptMailRegistration(message.baseMessage):
    id = 418
    freq = 2
    trusted = True
    zero_coded = False
    blocks = [
        ("DataBlock", 1)
    ]
    structure = {
        "DataBlock": [
            ["TargetIP", "Variable1"],
            ["TargetPort", "IPPORT"],
            ["TaskID", "LLUUID"],
            ["Flags", "U32"]
        ]
    }
registerMessage("ScriptMailRegistration", ScriptMailRegistration)

class ParcelMediaCommandMessage(message.baseMessage):
    id = 419
    freq = 2
    trusted = True
    zero_coded = False
    blocks = [
        ("CommandBlock", 1)
    ]
    structure = {
        "CommandBlock": [
            ["Flags", "U32"],
            ["Command", "U32"],
            ["Time", "F32"]
        ]
    }
registerMessage("ParcelMediaCommandMessage", ParcelMediaCommandMessage)

class ParcelMediaUpdate(message.baseMessage):
    id = 420
    freq = 2
    trusted = True
    zero_coded = False
    blocks = [
        ("DataBlock", 1),
        ("DataBlockExtended", 1)
    ]
    structure = {
        "DataBlock": [
            ["MediaURL", "Variable1"],
            ["MediaID", "LLUUID"],
            ["MediaAutoScale", "U8"]
        ],
        "DataBlockExtended": [
            ["MediaType", "Variable1"],
            ["MediaDesc", "Variable1"],
            ["MediaWidth", "S32"],
            ["MediaHeight", "S32"],
            ["MediaLoop", "U8"]
        ]
    }
registerMessage("ParcelMediaUpdate", ParcelMediaUpdate)

class LandStatRequest(message.baseMessage):
    id = 421
    freq = 2
    trusted = False
    zero_coded = False
    blocks = [
        ("AgentData", 1),
        ("RequestData", 1)
    ]
    structure = {
        "AgentData": [
            ["AgentID", "LLUUID"],
            ["SessionID", "LLUUID"]
        ],
        "RequestData": [
            ["ReportType", "U32"],
            ["RequestFlags", "U32"],
            ["Filter", "Variable1"],
            ["ParcelLocalID", "S32"]
        ]
    }
registerMessage("LandStatRequest", LandStatRequest)

class LandStatReply(message.baseMessage):
    id = 422
    freq = 2
    trusted = True
    zero_coded = False
    blocks = [
        ("RequestData", 1),
        ("ReportData", 0)
    ]
    structure = {
        "RequestData": [
            ["ReportType", "U32"],
            ["RequestFlags", "U32"],
            ["TotalObjectCount", "U32"]
        ],
        "ReportData": [
            ["TaskLocalID", "U32"],
            ["TaskID", "LLUUID"],
            ["LocationX", "F32"],
            ["LocationY", "F32"],
            ["LocationZ", "F32"],
            ["Score", "F32"],
            ["TaskName", "Variable1"],
            ["OwnerName", "Variable1"]
        ]
    }
registerMessage("LandStatReply", LandStatReply)

class Error(message.baseMessage):
    id = 423
    freq = 2
    trusted = False
    zero_coded = True
    blocks = [
        ("AgentData", 1),
        ("Data", 1)
    ]
    structure = {
        "AgentData": [
            ["AgentID", "LLUUID"]
        ],
        "Data": [
            ["Code", "S32"],
            ["Token", "Variable1"],
            ["ID", "LLUUID"],
            ["System", "Variable1"],
            ["Message", "Variable2"],
            ["Data", "Variable2"]
        ]
    }
registerMessage("Error", Error)

class ObjectIncludeInSearch(message.baseMessage):
    id = 424
    freq = 2
    trusted = False
    zero_coded = False
    blocks = [
        ("AgentData", 1),
        ("ObjectData", 0)
    ]
    structure = {
        "AgentData": [
            ["AgentID", "LLUUID"],
            ["SessionID", "LLUUID"]
        ],
        "ObjectData": [
            ["ObjectLocalID", "U32"],
            ["IncludeInSearch", "BOOL"]
        ]
    }
registerMessage("ObjectIncludeInSearch", ObjectIncludeInSearch)

class RezRestoreToWorld(message.baseMessage):
    id = 425
    freq = 2
    trusted = False
    zero_coded = False
    blocks = [
        ("AgentData", 1),
        ("InventoryData", 1)
    ]
    structure = {
        "AgentData": [
            ["AgentID", "LLUUID"],
            ["SessionID", "LLUUID"]
        ],
        "InventoryData": [
            ["ItemID", "LLUUID"],
            ["FolderID", "LLUUID"],
            ["CreatorID", "LLUUID"],
            ["OwnerID", "LLUUID"],
            ["GroupID", "LLUUID"],
            ["BaseMask", "U32"],
            ["OwnerMask", "U32"],
            ["GroupMask", "U32"],
            ["EveryoneMask", "U32"],
            ["NextOwnerMask", "U32"],
            ["GroupOwned", "BOOL"],
            ["TransactionID", "LLUUID"],
            ["Type", "S8"],
            ["InvType", "S8"],
            ["Flags", "U32"],
            ["SaleType", "U8"],
            ["SalePrice", "S32"],
            ["Name", "Variable1"],
            ["Description", "Variable1"],
            ["CreationDate", "S32"],
            ["CRC", "U32"]
        ]
    }
registerMessage("RezRestoreToWorld", RezRestoreToWorld)

class LinkInventoryItem(message.baseMessage):
    id = 426
    freq = 2
    trusted = False
    zero_coded = True
    blocks = [
        ("AgentData", 1),
        ("InventoryBlock", 1)
    ]
    structure = {
        "AgentData": [
            ["AgentID", "LLUUID"],
            ["SessionID", "LLUUID"]
        ],
        "InventoryBlock": [
            ["CallbackID", "U32"],
            ["FolderID", "LLUUID"],
            ["TransactionID", "LLUUID"],
            ["OldItemID", "LLUUID"],
            ["Type", "S8"],
            ["InvType", "S8"],
            ["Name", "Variable1"],
            ["Description", "Variable1"]
        ]
    }
registerMessage("LinkInventoryItem", LinkInventoryItem)

