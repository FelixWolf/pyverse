class TestMessage(message.baseMessage):
    name = "TestMessage"
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
registerMessage(TestMessage)

class PacketAck(message.baseMessage):
    name = "PacketAck"
    id = 4294967291
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
registerMessage(PacketAck)

class OpenCircuit(message.baseMessage):
    name = "OpenCircuit"
    id = 4294967292
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
registerMessage(OpenCircuit)

class CloseCircuit(message.baseMessage):
    name = "CloseCircuit"
    id = 4294967293
    freq = 3
    trusted = False
    zero_coded = False
    blocks = [

    ]
    structure = {

    }
registerMessage(CloseCircuit)

class StartPingCheck(message.baseMessage):
    name = "StartPingCheck"
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
registerMessage(StartPingCheck)

class CompletePingCheck(message.baseMessage):
    name = "CompletePingCheck"
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
registerMessage(CompletePingCheck)

class AddCircuitCode(message.baseMessage):
    name = "AddCircuitCode"
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
registerMessage(AddCircuitCode)

class UseCircuitCode(message.baseMessage):
    name = "UseCircuitCode"
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
registerMessage(UseCircuitCode)

class NeighborList(message.baseMessage):
    name = "NeighborList"
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
registerMessage(NeighborList)

class AvatarTextureUpdate(message.baseMessage):
    name = "AvatarTextureUpdate"
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
registerMessage(AvatarTextureUpdate)

class SimulatorMapUpdate(message.baseMessage):
    name = "SimulatorMapUpdate"
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
registerMessage(SimulatorMapUpdate)

class SimulatorSetMap(message.baseMessage):
    name = "SimulatorSetMap"
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
registerMessage(SimulatorSetMap)

class SubscribeLoad(message.baseMessage):
    name = "SubscribeLoad"
    id = 7
    freq = 2
    trusted = True
    zero_coded = False
    blocks = [

    ]
    structure = {

    }
registerMessage(SubscribeLoad)

class UnsubscribeLoad(message.baseMessage):
    name = "UnsubscribeLoad"
    id = 8
    freq = 2
    trusted = True
    zero_coded = False
    blocks = [

    ]
    structure = {

    }
registerMessage(UnsubscribeLoad)

class SimulatorReady(message.baseMessage):
    name = "SimulatorReady"
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
registerMessage(SimulatorReady)

class TelehubInfo(message.baseMessage):
    name = "TelehubInfo"
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
registerMessage(TelehubInfo)

class SimulatorPresentAtLocation(message.baseMessage):
    name = "SimulatorPresentAtLocation"
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
registerMessage(SimulatorPresentAtLocation)

class SimulatorLoad(message.baseMessage):
    name = "SimulatorLoad"
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
registerMessage(SimulatorLoad)

class SimulatorShutdownRequest(message.baseMessage):
    name = "SimulatorShutdownRequest"
    id = 13
    freq = 2
    trusted = True
    zero_coded = False
    blocks = [

    ]
    structure = {

    }
registerMessage(SimulatorShutdownRequest)

class RegionPresenceRequestByRegionID(message.baseMessage):
    name = "RegionPresenceRequestByRegionID"
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
registerMessage(RegionPresenceRequestByRegionID)

class RegionPresenceRequestByHandle(message.baseMessage):
    name = "RegionPresenceRequestByHandle"
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
registerMessage(RegionPresenceRequestByHandle)

class RegionPresenceResponse(message.baseMessage):
    name = "RegionPresenceResponse"
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
registerMessage(RegionPresenceResponse)

class UpdateSimulator(message.baseMessage):
    name = "UpdateSimulator"
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
registerMessage(UpdateSimulator)

class LogDwellTime(message.baseMessage):
    name = "LogDwellTime"
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
registerMessage(LogDwellTime)

class FeatureDisabled(message.baseMessage):
    name = "FeatureDisabled"
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
registerMessage(FeatureDisabled)

class LogFailedMoneyTransaction(message.baseMessage):
    name = "LogFailedMoneyTransaction"
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
registerMessage(LogFailedMoneyTransaction)

class UserReportInternal(message.baseMessage):
    name = "UserReportInternal"
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
registerMessage(UserReportInternal)

class SetSimStatusInDatabase(message.baseMessage):
    name = "SetSimStatusInDatabase"
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
registerMessage(SetSimStatusInDatabase)

class SetSimPresenceInDatabase(message.baseMessage):
    name = "SetSimPresenceInDatabase"
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
registerMessage(SetSimPresenceInDatabase)

class EconomyDataRequest(message.baseMessage):
    name = "EconomyDataRequest"
    id = 24
    freq = 2
    trusted = False
    zero_coded = False
    blocks = [

    ]
    structure = {

    }
registerMessage(EconomyDataRequest)

class EconomyData(message.baseMessage):
    name = "EconomyData"
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
registerMessage(EconomyData)

class AvatarPickerRequest(message.baseMessage):
    name = "AvatarPickerRequest"
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
registerMessage(AvatarPickerRequest)

class AvatarPickerRequestBackend(message.baseMessage):
    name = "AvatarPickerRequestBackend"
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
registerMessage(AvatarPickerRequestBackend)

class AvatarPickerReply(message.baseMessage):
    name = "AvatarPickerReply"
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
registerMessage(AvatarPickerReply)

class PlacesQuery(message.baseMessage):
    name = "PlacesQuery"
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
registerMessage(PlacesQuery)

class PlacesReply(message.baseMessage):
    name = "PlacesReply"
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
registerMessage(PlacesReply)

class DirFindQuery(message.baseMessage):
    name = "DirFindQuery"
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
registerMessage(DirFindQuery)

class DirFindQueryBackend(message.baseMessage):
    name = "DirFindQueryBackend"
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
registerMessage(DirFindQueryBackend)

class DirPlacesQuery(message.baseMessage):
    name = "DirPlacesQuery"
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
registerMessage(DirPlacesQuery)

class DirPlacesQueryBackend(message.baseMessage):
    name = "DirPlacesQueryBackend"
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
registerMessage(DirPlacesQueryBackend)

class DirPlacesReply(message.baseMessage):
    name = "DirPlacesReply"
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
registerMessage(DirPlacesReply)

class DirPeopleReply(message.baseMessage):
    name = "DirPeopleReply"
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
registerMessage(DirPeopleReply)

class DirEventsReply(message.baseMessage):
    name = "DirEventsReply"
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
registerMessage(DirEventsReply)

class DirGroupsReply(message.baseMessage):
    name = "DirGroupsReply"
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
registerMessage(DirGroupsReply)

class DirClassifiedQuery(message.baseMessage):
    name = "DirClassifiedQuery"
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
registerMessage(DirClassifiedQuery)

class DirClassifiedQueryBackend(message.baseMessage):
    name = "DirClassifiedQueryBackend"
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
registerMessage(DirClassifiedQueryBackend)

class DirClassifiedReply(message.baseMessage):
    name = "DirClassifiedReply"
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
registerMessage(DirClassifiedReply)

class AvatarClassifiedReply(message.baseMessage):
    name = "AvatarClassifiedReply"
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
registerMessage(AvatarClassifiedReply)

class ClassifiedInfoRequest(message.baseMessage):
    name = "ClassifiedInfoRequest"
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
registerMessage(ClassifiedInfoRequest)

class ClassifiedInfoReply(message.baseMessage):
    name = "ClassifiedInfoReply"
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
registerMessage(ClassifiedInfoReply)

class ClassifiedInfoUpdate(message.baseMessage):
    name = "ClassifiedInfoUpdate"
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
registerMessage(ClassifiedInfoUpdate)

class ClassifiedDelete(message.baseMessage):
    name = "ClassifiedDelete"
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
registerMessage(ClassifiedDelete)

class ClassifiedGodDelete(message.baseMessage):
    name = "ClassifiedGodDelete"
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
registerMessage(ClassifiedGodDelete)

class DirLandQuery(message.baseMessage):
    name = "DirLandQuery"
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
registerMessage(DirLandQuery)

class DirLandQueryBackend(message.baseMessage):
    name = "DirLandQueryBackend"
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
registerMessage(DirLandQueryBackend)

class DirLandReply(message.baseMessage):
    name = "DirLandReply"
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
registerMessage(DirLandReply)

class DirPopularQuery(message.baseMessage):
    name = "DirPopularQuery"
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
registerMessage(DirPopularQuery)

class DirPopularQueryBackend(message.baseMessage):
    name = "DirPopularQueryBackend"
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
registerMessage(DirPopularQueryBackend)

class DirPopularReply(message.baseMessage):
    name = "DirPopularReply"
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
registerMessage(DirPopularReply)

class ParcelInfoRequest(message.baseMessage):
    name = "ParcelInfoRequest"
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
registerMessage(ParcelInfoRequest)

class ParcelInfoReply(message.baseMessage):
    name = "ParcelInfoReply"
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
registerMessage(ParcelInfoReply)

class ParcelObjectOwnersRequest(message.baseMessage):
    name = "ParcelObjectOwnersRequest"
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
registerMessage(ParcelObjectOwnersRequest)

class ParcelObjectOwnersReply(message.baseMessage):
    name = "ParcelObjectOwnersReply"
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
registerMessage(ParcelObjectOwnersReply)

class GroupNoticesListRequest(message.baseMessage):
    name = "GroupNoticesListRequest"
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
registerMessage(GroupNoticesListRequest)

class GroupNoticesListReply(message.baseMessage):
    name = "GroupNoticesListReply"
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
registerMessage(GroupNoticesListReply)

class GroupNoticeRequest(message.baseMessage):
    name = "GroupNoticeRequest"
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
registerMessage(GroupNoticeRequest)

class GroupNoticeAdd(message.baseMessage):
    name = "GroupNoticeAdd"
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
registerMessage(GroupNoticeAdd)

class TeleportRequest(message.baseMessage):
    name = "TeleportRequest"
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
registerMessage(TeleportRequest)

class TeleportLocationRequest(message.baseMessage):
    name = "TeleportLocationRequest"
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
registerMessage(TeleportLocationRequest)

class TeleportLocal(message.baseMessage):
    name = "TeleportLocal"
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
registerMessage(TeleportLocal)

class TeleportLandmarkRequest(message.baseMessage):
    name = "TeleportLandmarkRequest"
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
registerMessage(TeleportLandmarkRequest)

class TeleportProgress(message.baseMessage):
    name = "TeleportProgress"
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
registerMessage(TeleportProgress)

class DataHomeLocationRequest(message.baseMessage):
    name = "DataHomeLocationRequest"
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
registerMessage(DataHomeLocationRequest)

class DataHomeLocationReply(message.baseMessage):
    name = "DataHomeLocationReply"
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
registerMessage(DataHomeLocationReply)

class TeleportFinish(message.baseMessage):
    name = "TeleportFinish"
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
registerMessage(TeleportFinish)

class StartLure(message.baseMessage):
    name = "StartLure"
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
registerMessage(StartLure)

class TeleportLureRequest(message.baseMessage):
    name = "TeleportLureRequest"
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
registerMessage(TeleportLureRequest)

class TeleportCancel(message.baseMessage):
    name = "TeleportCancel"
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
registerMessage(TeleportCancel)

class TeleportStart(message.baseMessage):
    name = "TeleportStart"
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
registerMessage(TeleportStart)

class TeleportFailed(message.baseMessage):
    name = "TeleportFailed"
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
registerMessage(TeleportFailed)

class Undo(message.baseMessage):
    name = "Undo"
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
registerMessage(Undo)

class Redo(message.baseMessage):
    name = "Redo"
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
registerMessage(Redo)

class UndoLand(message.baseMessage):
    name = "UndoLand"
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
registerMessage(UndoLand)

class AgentPause(message.baseMessage):
    name = "AgentPause"
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
registerMessage(AgentPause)

class AgentResume(message.baseMessage):
    name = "AgentResume"
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
registerMessage(AgentResume)

class AgentUpdate(message.baseMessage):
    name = "AgentUpdate"
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
registerMessage(AgentUpdate)

class ChatFromViewer(message.baseMessage):
    name = "ChatFromViewer"
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
registerMessage(ChatFromViewer)

class AgentThrottle(message.baseMessage):
    name = "AgentThrottle"
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
registerMessage(AgentThrottle)

class AgentFOV(message.baseMessage):
    name = "AgentFOV"
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
registerMessage(AgentFOV)

class AgentHeightWidth(message.baseMessage):
    name = "AgentHeightWidth"
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
registerMessage(AgentHeightWidth)

class AgentSetAppearance(message.baseMessage):
    name = "AgentSetAppearance"
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
registerMessage(AgentSetAppearance)

class AgentAnimation(message.baseMessage):
    name = "AgentAnimation"
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
registerMessage(AgentAnimation)

class AgentRequestSit(message.baseMessage):
    name = "AgentRequestSit"
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
registerMessage(AgentRequestSit)

class AgentSit(message.baseMessage):
    name = "AgentSit"
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
registerMessage(AgentSit)

class AgentQuitCopy(message.baseMessage):
    name = "AgentQuitCopy"
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
registerMessage(AgentQuitCopy)

class RequestImage(message.baseMessage):
    name = "RequestImage"
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
registerMessage(RequestImage)

class ImageNotInDatabase(message.baseMessage):
    name = "ImageNotInDatabase"
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
registerMessage(ImageNotInDatabase)

class RebakeAvatarTextures(message.baseMessage):
    name = "RebakeAvatarTextures"
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
registerMessage(RebakeAvatarTextures)

class SetAlwaysRun(message.baseMessage):
    name = "SetAlwaysRun"
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
registerMessage(SetAlwaysRun)

class ObjectAdd(message.baseMessage):
    name = "ObjectAdd"
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
registerMessage(ObjectAdd)

class ObjectDelete(message.baseMessage):
    name = "ObjectDelete"
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
registerMessage(ObjectDelete)

class ObjectDuplicate(message.baseMessage):
    name = "ObjectDuplicate"
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
registerMessage(ObjectDuplicate)

class ObjectDuplicateOnRay(message.baseMessage):
    name = "ObjectDuplicateOnRay"
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
registerMessage(ObjectDuplicateOnRay)

class MultipleObjectUpdate(message.baseMessage):
    name = "MultipleObjectUpdate"
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
registerMessage(MultipleObjectUpdate)

class RequestMultipleObjects(message.baseMessage):
    name = "RequestMultipleObjects"
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
registerMessage(RequestMultipleObjects)

class ObjectPosition(message.baseMessage):
    name = "ObjectPosition"
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
registerMessage(ObjectPosition)

class ObjectScale(message.baseMessage):
    name = "ObjectScale"
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
registerMessage(ObjectScale)

class ObjectRotation(message.baseMessage):
    name = "ObjectRotation"
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
registerMessage(ObjectRotation)

class ObjectFlagUpdate(message.baseMessage):
    name = "ObjectFlagUpdate"
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
registerMessage(ObjectFlagUpdate)

class ObjectClickAction(message.baseMessage):
    name = "ObjectClickAction"
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
registerMessage(ObjectClickAction)

class ObjectImage(message.baseMessage):
    name = "ObjectImage"
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
registerMessage(ObjectImage)

class ObjectMaterial(message.baseMessage):
    name = "ObjectMaterial"
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
registerMessage(ObjectMaterial)

class ObjectShape(message.baseMessage):
    name = "ObjectShape"
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
registerMessage(ObjectShape)

class ObjectExtraParams(message.baseMessage):
    name = "ObjectExtraParams"
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
registerMessage(ObjectExtraParams)

class ObjectOwner(message.baseMessage):
    name = "ObjectOwner"
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
registerMessage(ObjectOwner)

class ObjectGroup(message.baseMessage):
    name = "ObjectGroup"
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
registerMessage(ObjectGroup)

class ObjectBuy(message.baseMessage):
    name = "ObjectBuy"
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
registerMessage(ObjectBuy)

class BuyObjectInventory(message.baseMessage):
    name = "BuyObjectInventory"
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
registerMessage(BuyObjectInventory)

class DerezContainer(message.baseMessage):
    name = "DerezContainer"
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
registerMessage(DerezContainer)

class ObjectPermissions(message.baseMessage):
    name = "ObjectPermissions"
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
registerMessage(ObjectPermissions)

class ObjectSaleInfo(message.baseMessage):
    name = "ObjectSaleInfo"
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
registerMessage(ObjectSaleInfo)

class ObjectName(message.baseMessage):
    name = "ObjectName"
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
registerMessage(ObjectName)

class ObjectDescription(message.baseMessage):
    name = "ObjectDescription"
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
registerMessage(ObjectDescription)

class ObjectCategory(message.baseMessage):
    name = "ObjectCategory"
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
registerMessage(ObjectCategory)

class ObjectSelect(message.baseMessage):
    name = "ObjectSelect"
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
registerMessage(ObjectSelect)

class ObjectDeselect(message.baseMessage):
    name = "ObjectDeselect"
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
registerMessage(ObjectDeselect)

class ObjectAttach(message.baseMessage):
    name = "ObjectAttach"
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
registerMessage(ObjectAttach)

class ObjectDetach(message.baseMessage):
    name = "ObjectDetach"
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
registerMessage(ObjectDetach)

class ObjectDrop(message.baseMessage):
    name = "ObjectDrop"
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
registerMessage(ObjectDrop)

class ObjectLink(message.baseMessage):
    name = "ObjectLink"
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
registerMessage(ObjectLink)

class ObjectDelink(message.baseMessage):
    name = "ObjectDelink"
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
registerMessage(ObjectDelink)

class ObjectGrab(message.baseMessage):
    name = "ObjectGrab"
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
registerMessage(ObjectGrab)

class ObjectGrabUpdate(message.baseMessage):
    name = "ObjectGrabUpdate"
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
registerMessage(ObjectGrabUpdate)

class ObjectDeGrab(message.baseMessage):
    name = "ObjectDeGrab"
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
registerMessage(ObjectDeGrab)

class ObjectSpinStart(message.baseMessage):
    name = "ObjectSpinStart"
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
registerMessage(ObjectSpinStart)

class ObjectSpinUpdate(message.baseMessage):
    name = "ObjectSpinUpdate"
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
registerMessage(ObjectSpinUpdate)

class ObjectSpinStop(message.baseMessage):
    name = "ObjectSpinStop"
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
registerMessage(ObjectSpinStop)

class ObjectExportSelected(message.baseMessage):
    name = "ObjectExportSelected"
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
registerMessage(ObjectExportSelected)

class ModifyLand(message.baseMessage):
    name = "ModifyLand"
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
registerMessage(ModifyLand)

class VelocityInterpolateOn(message.baseMessage):
    name = "VelocityInterpolateOn"
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
registerMessage(VelocityInterpolateOn)

class VelocityInterpolateOff(message.baseMessage):
    name = "VelocityInterpolateOff"
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
registerMessage(VelocityInterpolateOff)

class StateSave(message.baseMessage):
    name = "StateSave"
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
registerMessage(StateSave)

class ReportAutosaveCrash(message.baseMessage):
    name = "ReportAutosaveCrash"
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
registerMessage(ReportAutosaveCrash)

class SimWideDeletes(message.baseMessage):
    name = "SimWideDeletes"
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
registerMessage(SimWideDeletes)

class RequestObjectPropertiesFamily(message.baseMessage):
    name = "RequestObjectPropertiesFamily"
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
registerMessage(RequestObjectPropertiesFamily)

class TrackAgent(message.baseMessage):
    name = "TrackAgent"
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
registerMessage(TrackAgent)

class ViewerStats(message.baseMessage):
    name = "ViewerStats"
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
registerMessage(ViewerStats)

class ScriptAnswerYes(message.baseMessage):
    name = "ScriptAnswerYes"
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
registerMessage(ScriptAnswerYes)

class UserReport(message.baseMessage):
    name = "UserReport"
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
registerMessage(UserReport)

class AlertMessage(message.baseMessage):
    name = "AlertMessage"
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
registerMessage(AlertMessage)

class AgentAlertMessage(message.baseMessage):
    name = "AgentAlertMessage"
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
registerMessage(AgentAlertMessage)

class MeanCollisionAlert(message.baseMessage):
    name = "MeanCollisionAlert"
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
registerMessage(MeanCollisionAlert)

class ViewerFrozenMessage(message.baseMessage):
    name = "ViewerFrozenMessage"
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
registerMessage(ViewerFrozenMessage)

class HealthMessage(message.baseMessage):
    name = "HealthMessage"
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
registerMessage(HealthMessage)

class ChatFromSimulator(message.baseMessage):
    name = "ChatFromSimulator"
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
registerMessage(ChatFromSimulator)

class SimStats(message.baseMessage):
    name = "SimStats"
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
registerMessage(SimStats)

class RequestRegionInfo(message.baseMessage):
    name = "RequestRegionInfo"
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
registerMessage(RequestRegionInfo)

class RegionInfo(message.baseMessage):
    name = "RegionInfo"
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
registerMessage(RegionInfo)

class GodUpdateRegionInfo(message.baseMessage):
    name = "GodUpdateRegionInfo"
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
registerMessage(GodUpdateRegionInfo)

class NearestLandingRegionRequest(message.baseMessage):
    name = "NearestLandingRegionRequest"
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
registerMessage(NearestLandingRegionRequest)

class NearestLandingRegionReply(message.baseMessage):
    name = "NearestLandingRegionReply"
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
registerMessage(NearestLandingRegionReply)

class NearestLandingRegionUpdated(message.baseMessage):
    name = "NearestLandingRegionUpdated"
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
registerMessage(NearestLandingRegionUpdated)

class TeleportLandingStatusChanged(message.baseMessage):
    name = "TeleportLandingStatusChanged"
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
registerMessage(TeleportLandingStatusChanged)

class RegionHandshake(message.baseMessage):
    name = "RegionHandshake"
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
registerMessage(RegionHandshake)

class RegionHandshakeReply(message.baseMessage):
    name = "RegionHandshakeReply"
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
registerMessage(RegionHandshakeReply)

class CoarseLocationUpdate(message.baseMessage):
    name = "CoarseLocationUpdate"
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
registerMessage(CoarseLocationUpdate)

class ImageData(message.baseMessage):
    name = "ImageData"
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
registerMessage(ImageData)

class ImagePacket(message.baseMessage):
    name = "ImagePacket"
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
registerMessage(ImagePacket)

class LayerData(message.baseMessage):
    name = "LayerData"
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
registerMessage(LayerData)

class ObjectUpdate(message.baseMessage):
    name = "ObjectUpdate"
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
registerMessage(ObjectUpdate)

class ObjectUpdateCompressed(message.baseMessage):
    name = "ObjectUpdateCompressed"
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
registerMessage(ObjectUpdateCompressed)

class ObjectUpdateCached(message.baseMessage):
    name = "ObjectUpdateCached"
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
registerMessage(ObjectUpdateCached)

class ImprovedTerseObjectUpdate(message.baseMessage):
    name = "ImprovedTerseObjectUpdate"
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
registerMessage(ImprovedTerseObjectUpdate)

class KillObject(message.baseMessage):
    name = "KillObject"
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
registerMessage(KillObject)

class CrossedRegion(message.baseMessage):
    name = "CrossedRegion"
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
registerMessage(CrossedRegion)

class SimulatorViewerTimeMessage(message.baseMessage):
    name = "SimulatorViewerTimeMessage"
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
registerMessage(SimulatorViewerTimeMessage)

class EnableSimulator(message.baseMessage):
    name = "EnableSimulator"
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
registerMessage(EnableSimulator)

class DisableSimulator(message.baseMessage):
    name = "DisableSimulator"
    id = 152
    freq = 2
    trusted = True
    zero_coded = False
    blocks = [

    ]
    structure = {

    }
registerMessage(DisableSimulator)

class ConfirmEnableSimulator(message.baseMessage):
    name = "ConfirmEnableSimulator"
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
registerMessage(ConfirmEnableSimulator)

class TransferRequest(message.baseMessage):
    name = "TransferRequest"
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
registerMessage(TransferRequest)

class TransferInfo(message.baseMessage):
    name = "TransferInfo"
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
registerMessage(TransferInfo)

class TransferPacket(message.baseMessage):
    name = "TransferPacket"
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
registerMessage(TransferPacket)

class TransferAbort(message.baseMessage):
    name = "TransferAbort"
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
registerMessage(TransferAbort)

class RequestXfer(message.baseMessage):
    name = "RequestXfer"
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
registerMessage(RequestXfer)

class SendXferPacket(message.baseMessage):
    name = "SendXferPacket"
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
registerMessage(SendXferPacket)

class ConfirmXferPacket(message.baseMessage):
    name = "ConfirmXferPacket"
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
registerMessage(ConfirmXferPacket)

class AbortXfer(message.baseMessage):
    name = "AbortXfer"
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
registerMessage(AbortXfer)

class AvatarAnimation(message.baseMessage):
    name = "AvatarAnimation"
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
registerMessage(AvatarAnimation)

class AvatarAppearance(message.baseMessage):
    name = "AvatarAppearance"
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
registerMessage(AvatarAppearance)

class AvatarSitResponse(message.baseMessage):
    name = "AvatarSitResponse"
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
registerMessage(AvatarSitResponse)

class SetFollowCamProperties(message.baseMessage):
    name = "SetFollowCamProperties"
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
registerMessage(SetFollowCamProperties)

class ClearFollowCamProperties(message.baseMessage):
    name = "ClearFollowCamProperties"
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
registerMessage(ClearFollowCamProperties)

class CameraConstraint(message.baseMessage):
    name = "CameraConstraint"
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
registerMessage(CameraConstraint)

class ObjectProperties(message.baseMessage):
    name = "ObjectProperties"
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
registerMessage(ObjectProperties)

class ObjectPropertiesFamily(message.baseMessage):
    name = "ObjectPropertiesFamily"
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
registerMessage(ObjectPropertiesFamily)

class RequestPayPrice(message.baseMessage):
    name = "RequestPayPrice"
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
registerMessage(RequestPayPrice)

class PayPriceReply(message.baseMessage):
    name = "PayPriceReply"
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
registerMessage(PayPriceReply)

class KickUser(message.baseMessage):
    name = "KickUser"
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
registerMessage(KickUser)

class KickUserAck(message.baseMessage):
    name = "KickUserAck"
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
registerMessage(KickUserAck)

class GodKickUser(message.baseMessage):
    name = "GodKickUser"
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
registerMessage(GodKickUser)

class SystemKickUser(message.baseMessage):
    name = "SystemKickUser"
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
registerMessage(SystemKickUser)

class EjectUser(message.baseMessage):
    name = "EjectUser"
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
registerMessage(EjectUser)

class FreezeUser(message.baseMessage):
    name = "FreezeUser"
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
registerMessage(FreezeUser)

class AvatarPropertiesRequest(message.baseMessage):
    name = "AvatarPropertiesRequest"
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
registerMessage(AvatarPropertiesRequest)

class AvatarPropertiesRequestBackend(message.baseMessage):
    name = "AvatarPropertiesRequestBackend"
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
registerMessage(AvatarPropertiesRequestBackend)

class AvatarPropertiesReply(message.baseMessage):
    name = "AvatarPropertiesReply"
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
registerMessage(AvatarPropertiesReply)

class AvatarInterestsReply(message.baseMessage):
    name = "AvatarInterestsReply"
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
registerMessage(AvatarInterestsReply)

class AvatarGroupsReply(message.baseMessage):
    name = "AvatarGroupsReply"
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
registerMessage(AvatarGroupsReply)

class AvatarPropertiesUpdate(message.baseMessage):
    name = "AvatarPropertiesUpdate"
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
registerMessage(AvatarPropertiesUpdate)

class AvatarInterestsUpdate(message.baseMessage):
    name = "AvatarInterestsUpdate"
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
registerMessage(AvatarInterestsUpdate)

class AvatarNotesReply(message.baseMessage):
    name = "AvatarNotesReply"
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
registerMessage(AvatarNotesReply)

class AvatarNotesUpdate(message.baseMessage):
    name = "AvatarNotesUpdate"
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
registerMessage(AvatarNotesUpdate)

class AvatarPicksReply(message.baseMessage):
    name = "AvatarPicksReply"
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
registerMessage(AvatarPicksReply)

class EventInfoRequest(message.baseMessage):
    name = "EventInfoRequest"
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
registerMessage(EventInfoRequest)

class EventInfoReply(message.baseMessage):
    name = "EventInfoReply"
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
registerMessage(EventInfoReply)

class EventNotificationAddRequest(message.baseMessage):
    name = "EventNotificationAddRequest"
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
registerMessage(EventNotificationAddRequest)

class EventNotificationRemoveRequest(message.baseMessage):
    name = "EventNotificationRemoveRequest"
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
registerMessage(EventNotificationRemoveRequest)

class EventGodDelete(message.baseMessage):
    name = "EventGodDelete"
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
registerMessage(EventGodDelete)

class PickInfoReply(message.baseMessage):
    name = "PickInfoReply"
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
registerMessage(PickInfoReply)

class PickInfoUpdate(message.baseMessage):
    name = "PickInfoUpdate"
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
registerMessage(PickInfoUpdate)

class PickDelete(message.baseMessage):
    name = "PickDelete"
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
registerMessage(PickDelete)

class PickGodDelete(message.baseMessage):
    name = "PickGodDelete"
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
registerMessage(PickGodDelete)

class ScriptQuestion(message.baseMessage):
    name = "ScriptQuestion"
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
registerMessage(ScriptQuestion)

class ScriptControlChange(message.baseMessage):
    name = "ScriptControlChange"
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
registerMessage(ScriptControlChange)

class ScriptDialog(message.baseMessage):
    name = "ScriptDialog"
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
registerMessage(ScriptDialog)

class ScriptDialogReply(message.baseMessage):
    name = "ScriptDialogReply"
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
registerMessage(ScriptDialogReply)

class ForceScriptControlRelease(message.baseMessage):
    name = "ForceScriptControlRelease"
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
registerMessage(ForceScriptControlRelease)

class RevokePermissions(message.baseMessage):
    name = "RevokePermissions"
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
registerMessage(RevokePermissions)

class LoadURL(message.baseMessage):
    name = "LoadURL"
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
registerMessage(LoadURL)

class ScriptTeleportRequest(message.baseMessage):
    name = "ScriptTeleportRequest"
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
registerMessage(ScriptTeleportRequest)

class ParcelOverlay(message.baseMessage):
    name = "ParcelOverlay"
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
registerMessage(ParcelOverlay)

class ParcelPropertiesRequest(message.baseMessage):
    name = "ParcelPropertiesRequest"
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
registerMessage(ParcelPropertiesRequest)

class ParcelPropertiesRequestByID(message.baseMessage):
    name = "ParcelPropertiesRequestByID"
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
registerMessage(ParcelPropertiesRequestByID)

class ParcelProperties(message.baseMessage):
    name = "ParcelProperties"
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
registerMessage(ParcelProperties)

class ParcelPropertiesUpdate(message.baseMessage):
    name = "ParcelPropertiesUpdate"
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
registerMessage(ParcelPropertiesUpdate)

class ParcelReturnObjects(message.baseMessage):
    name = "ParcelReturnObjects"
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
registerMessage(ParcelReturnObjects)

class ParcelSetOtherCleanTime(message.baseMessage):
    name = "ParcelSetOtherCleanTime"
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
registerMessage(ParcelSetOtherCleanTime)

class ParcelDisableObjects(message.baseMessage):
    name = "ParcelDisableObjects"
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
registerMessage(ParcelDisableObjects)

class ParcelSelectObjects(message.baseMessage):
    name = "ParcelSelectObjects"
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
registerMessage(ParcelSelectObjects)

class EstateCovenantRequest(message.baseMessage):
    name = "EstateCovenantRequest"
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
registerMessage(EstateCovenantRequest)

class EstateCovenantReply(message.baseMessage):
    name = "EstateCovenantReply"
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
registerMessage(EstateCovenantReply)

class ForceObjectSelect(message.baseMessage):
    name = "ForceObjectSelect"
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
registerMessage(ForceObjectSelect)

class ParcelBuyPass(message.baseMessage):
    name = "ParcelBuyPass"
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
registerMessage(ParcelBuyPass)

class ParcelDeedToGroup(message.baseMessage):
    name = "ParcelDeedToGroup"
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
registerMessage(ParcelDeedToGroup)

class ParcelReclaim(message.baseMessage):
    name = "ParcelReclaim"
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
registerMessage(ParcelReclaim)

class ParcelClaim(message.baseMessage):
    name = "ParcelClaim"
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
registerMessage(ParcelClaim)

class ParcelJoin(message.baseMessage):
    name = "ParcelJoin"
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
registerMessage(ParcelJoin)

class ParcelDivide(message.baseMessage):
    name = "ParcelDivide"
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
registerMessage(ParcelDivide)

class ParcelRelease(message.baseMessage):
    name = "ParcelRelease"
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
registerMessage(ParcelRelease)

class ParcelBuy(message.baseMessage):
    name = "ParcelBuy"
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
registerMessage(ParcelBuy)

class ParcelGodForceOwner(message.baseMessage):
    name = "ParcelGodForceOwner"
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
registerMessage(ParcelGodForceOwner)

class ParcelAccessListRequest(message.baseMessage):
    name = "ParcelAccessListRequest"
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
registerMessage(ParcelAccessListRequest)

class ParcelAccessListReply(message.baseMessage):
    name = "ParcelAccessListReply"
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
registerMessage(ParcelAccessListReply)

class ParcelAccessListUpdate(message.baseMessage):
    name = "ParcelAccessListUpdate"
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
registerMessage(ParcelAccessListUpdate)

class ParcelDwellRequest(message.baseMessage):
    name = "ParcelDwellRequest"
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
registerMessage(ParcelDwellRequest)

class ParcelDwellReply(message.baseMessage):
    name = "ParcelDwellReply"
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
registerMessage(ParcelDwellReply)

class RequestParcelTransfer(message.baseMessage):
    name = "RequestParcelTransfer"
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
registerMessage(RequestParcelTransfer)

class UpdateParcel(message.baseMessage):
    name = "UpdateParcel"
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
registerMessage(UpdateParcel)

class RemoveParcel(message.baseMessage):
    name = "RemoveParcel"
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
registerMessage(RemoveParcel)

class MergeParcel(message.baseMessage):
    name = "MergeParcel"
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
registerMessage(MergeParcel)

class LogParcelChanges(message.baseMessage):
    name = "LogParcelChanges"
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
registerMessage(LogParcelChanges)

class CheckParcelSales(message.baseMessage):
    name = "CheckParcelSales"
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
registerMessage(CheckParcelSales)

class ParcelSales(message.baseMessage):
    name = "ParcelSales"
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
registerMessage(ParcelSales)

class ParcelGodMarkAsContent(message.baseMessage):
    name = "ParcelGodMarkAsContent"
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
registerMessage(ParcelGodMarkAsContent)

class ViewerStartAuction(message.baseMessage):
    name = "ViewerStartAuction"
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
registerMessage(ViewerStartAuction)

class StartAuction(message.baseMessage):
    name = "StartAuction"
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
registerMessage(StartAuction)

class ConfirmAuctionStart(message.baseMessage):
    name = "ConfirmAuctionStart"
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
registerMessage(ConfirmAuctionStart)

class CompleteAuction(message.baseMessage):
    name = "CompleteAuction"
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
registerMessage(CompleteAuction)

class CancelAuction(message.baseMessage):
    name = "CancelAuction"
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
registerMessage(CancelAuction)

class CheckParcelAuctions(message.baseMessage):
    name = "CheckParcelAuctions"
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
registerMessage(CheckParcelAuctions)

class ParcelAuctions(message.baseMessage):
    name = "ParcelAuctions"
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
registerMessage(ParcelAuctions)

class UUIDNameRequest(message.baseMessage):
    name = "UUIDNameRequest"
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
registerMessage(UUIDNameRequest)

class UUIDNameReply(message.baseMessage):
    name = "UUIDNameReply"
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
registerMessage(UUIDNameReply)

class UUIDGroupNameRequest(message.baseMessage):
    name = "UUIDGroupNameRequest"
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
registerMessage(UUIDGroupNameRequest)

class UUIDGroupNameReply(message.baseMessage):
    name = "UUIDGroupNameReply"
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
registerMessage(UUIDGroupNameReply)

class ChatPass(message.baseMessage):
    name = "ChatPass"
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
registerMessage(ChatPass)

class EdgeDataPacket(message.baseMessage):
    name = "EdgeDataPacket"
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
registerMessage(EdgeDataPacket)

class SimStatus(message.baseMessage):
    name = "SimStatus"
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
registerMessage(SimStatus)

class ChildAgentUpdate(message.baseMessage):
    name = "ChildAgentUpdate"
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
registerMessage(ChildAgentUpdate)

class ChildAgentAlive(message.baseMessage):
    name = "ChildAgentAlive"
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
registerMessage(ChildAgentAlive)

class ChildAgentPositionUpdate(message.baseMessage):
    name = "ChildAgentPositionUpdate"
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
registerMessage(ChildAgentPositionUpdate)

class ChildAgentDying(message.baseMessage):
    name = "ChildAgentDying"
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
registerMessage(ChildAgentDying)

class ChildAgentUnknown(message.baseMessage):
    name = "ChildAgentUnknown"
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
registerMessage(ChildAgentUnknown)

class AtomicPassObject(message.baseMessage):
    name = "AtomicPassObject"
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
registerMessage(AtomicPassObject)

class KillChildAgents(message.baseMessage):
    name = "KillChildAgents"
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
registerMessage(KillChildAgents)

class GetScriptRunning(message.baseMessage):
    name = "GetScriptRunning"
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
registerMessage(GetScriptRunning)

class ScriptRunningReply(message.baseMessage):
    name = "ScriptRunningReply"
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
registerMessage(ScriptRunningReply)

class SetScriptRunning(message.baseMessage):
    name = "SetScriptRunning"
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
registerMessage(SetScriptRunning)

class ScriptReset(message.baseMessage):
    name = "ScriptReset"
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
registerMessage(ScriptReset)

class ScriptSensorRequest(message.baseMessage):
    name = "ScriptSensorRequest"
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
registerMessage(ScriptSensorRequest)

class ScriptSensorReply(message.baseMessage):
    name = "ScriptSensorReply"
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
registerMessage(ScriptSensorReply)

class CompleteAgentMovement(message.baseMessage):
    name = "CompleteAgentMovement"
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
registerMessage(CompleteAgentMovement)

class AgentMovementComplete(message.baseMessage):
    name = "AgentMovementComplete"
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
registerMessage(AgentMovementComplete)

class DataServerLogout(message.baseMessage):
    name = "DataServerLogout"
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
registerMessage(DataServerLogout)

class LogoutRequest(message.baseMessage):
    name = "LogoutRequest"
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
registerMessage(LogoutRequest)

class LogoutReply(message.baseMessage):
    name = "LogoutReply"
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
registerMessage(LogoutReply)

class ImprovedInstantMessage(message.baseMessage):
    name = "ImprovedInstantMessage"
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
registerMessage(ImprovedInstantMessage)

class RetrieveInstantMessages(message.baseMessage):
    name = "RetrieveInstantMessages"
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
registerMessage(RetrieveInstantMessages)

class FindAgent(message.baseMessage):
    name = "FindAgent"
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
registerMessage(FindAgent)

class RequestGodlikePowers(message.baseMessage):
    name = "RequestGodlikePowers"
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
registerMessage(RequestGodlikePowers)

class GrantGodlikePowers(message.baseMessage):
    name = "GrantGodlikePowers"
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
registerMessage(GrantGodlikePowers)

class GodlikeMessage(message.baseMessage):
    name = "GodlikeMessage"
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
registerMessage(GodlikeMessage)

class EstateOwnerMessage(message.baseMessage):
    name = "EstateOwnerMessage"
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
registerMessage(EstateOwnerMessage)

class GenericMessage(message.baseMessage):
    name = "GenericMessage"
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
registerMessage(GenericMessage)

class MuteListRequest(message.baseMessage):
    name = "MuteListRequest"
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
registerMessage(MuteListRequest)

class UpdateMuteListEntry(message.baseMessage):
    name = "UpdateMuteListEntry"
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
registerMessage(UpdateMuteListEntry)

class RemoveMuteListEntry(message.baseMessage):
    name = "RemoveMuteListEntry"
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
registerMessage(RemoveMuteListEntry)

class CopyInventoryFromNotecard(message.baseMessage):
    name = "CopyInventoryFromNotecard"
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
registerMessage(CopyInventoryFromNotecard)

class UpdateInventoryItem(message.baseMessage):
    name = "UpdateInventoryItem"
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
registerMessage(UpdateInventoryItem)

class UpdateCreateInventoryItem(message.baseMessage):
    name = "UpdateCreateInventoryItem"
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
registerMessage(UpdateCreateInventoryItem)

class MoveInventoryItem(message.baseMessage):
    name = "MoveInventoryItem"
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
registerMessage(MoveInventoryItem)

class CopyInventoryItem(message.baseMessage):
    name = "CopyInventoryItem"
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
registerMessage(CopyInventoryItem)

class RemoveInventoryItem(message.baseMessage):
    name = "RemoveInventoryItem"
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
registerMessage(RemoveInventoryItem)

class ChangeInventoryItemFlags(message.baseMessage):
    name = "ChangeInventoryItemFlags"
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
registerMessage(ChangeInventoryItemFlags)

class SaveAssetIntoInventory(message.baseMessage):
    name = "SaveAssetIntoInventory"
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
registerMessage(SaveAssetIntoInventory)

class CreateInventoryFolder(message.baseMessage):
    name = "CreateInventoryFolder"
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
registerMessage(CreateInventoryFolder)

class UpdateInventoryFolder(message.baseMessage):
    name = "UpdateInventoryFolder"
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
registerMessage(UpdateInventoryFolder)

class MoveInventoryFolder(message.baseMessage):
    name = "MoveInventoryFolder"
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
registerMessage(MoveInventoryFolder)

class RemoveInventoryFolder(message.baseMessage):
    name = "RemoveInventoryFolder"
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
registerMessage(RemoveInventoryFolder)

class FetchInventoryDescendents(message.baseMessage):
    name = "FetchInventoryDescendents"
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
registerMessage(FetchInventoryDescendents)

class InventoryDescendents(message.baseMessage):
    name = "InventoryDescendents"
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
registerMessage(InventoryDescendents)

class FetchInventory(message.baseMessage):
    name = "FetchInventory"
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
registerMessage(FetchInventory)

class FetchInventoryReply(message.baseMessage):
    name = "FetchInventoryReply"
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
registerMessage(FetchInventoryReply)

class BulkUpdateInventory(message.baseMessage):
    name = "BulkUpdateInventory"
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
registerMessage(BulkUpdateInventory)

class RequestInventoryAsset(message.baseMessage):
    name = "RequestInventoryAsset"
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
registerMessage(RequestInventoryAsset)

class InventoryAssetResponse(message.baseMessage):
    name = "InventoryAssetResponse"
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
registerMessage(InventoryAssetResponse)

class RemoveInventoryObjects(message.baseMessage):
    name = "RemoveInventoryObjects"
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
registerMessage(RemoveInventoryObjects)

class PurgeInventoryDescendents(message.baseMessage):
    name = "PurgeInventoryDescendents"
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
registerMessage(PurgeInventoryDescendents)

class UpdateTaskInventory(message.baseMessage):
    name = "UpdateTaskInventory"
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
registerMessage(UpdateTaskInventory)

class RemoveTaskInventory(message.baseMessage):
    name = "RemoveTaskInventory"
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
registerMessage(RemoveTaskInventory)

class MoveTaskInventory(message.baseMessage):
    name = "MoveTaskInventory"
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
registerMessage(MoveTaskInventory)

class RequestTaskInventory(message.baseMessage):
    name = "RequestTaskInventory"
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
registerMessage(RequestTaskInventory)

class ReplyTaskInventory(message.baseMessage):
    name = "ReplyTaskInventory"
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
registerMessage(ReplyTaskInventory)

class DeRezObject(message.baseMessage):
    name = "DeRezObject"
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
registerMessage(DeRezObject)

class DeRezAck(message.baseMessage):
    name = "DeRezAck"
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
registerMessage(DeRezAck)

class RezObject(message.baseMessage):
    name = "RezObject"
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
registerMessage(RezObject)

class RezObjectFromNotecard(message.baseMessage):
    name = "RezObjectFromNotecard"
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
registerMessage(RezObjectFromNotecard)

class TransferInventory(message.baseMessage):
    name = "TransferInventory"
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
registerMessage(TransferInventory)

class TransferInventoryAck(message.baseMessage):
    name = "TransferInventoryAck"
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
registerMessage(TransferInventoryAck)

class AcceptFriendship(message.baseMessage):
    name = "AcceptFriendship"
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
registerMessage(AcceptFriendship)

class DeclineFriendship(message.baseMessage):
    name = "DeclineFriendship"
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
registerMessage(DeclineFriendship)

class FormFriendship(message.baseMessage):
    name = "FormFriendship"
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
registerMessage(FormFriendship)

class TerminateFriendship(message.baseMessage):
    name = "TerminateFriendship"
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
registerMessage(TerminateFriendship)

class OfferCallingCard(message.baseMessage):
    name = "OfferCallingCard"
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
registerMessage(OfferCallingCard)

class AcceptCallingCard(message.baseMessage):
    name = "AcceptCallingCard"
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
registerMessage(AcceptCallingCard)

class DeclineCallingCard(message.baseMessage):
    name = "DeclineCallingCard"
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
registerMessage(DeclineCallingCard)

class RezScript(message.baseMessage):
    name = "RezScript"
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
registerMessage(RezScript)

class CreateInventoryItem(message.baseMessage):
    name = "CreateInventoryItem"
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
registerMessage(CreateInventoryItem)

class CreateLandmarkForEvent(message.baseMessage):
    name = "CreateLandmarkForEvent"
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
registerMessage(CreateLandmarkForEvent)

class EventLocationRequest(message.baseMessage):
    name = "EventLocationRequest"
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
registerMessage(EventLocationRequest)

class EventLocationReply(message.baseMessage):
    name = "EventLocationReply"
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
registerMessage(EventLocationReply)

class RegionHandleRequest(message.baseMessage):
    name = "RegionHandleRequest"
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
registerMessage(RegionHandleRequest)

class RegionIDAndHandleReply(message.baseMessage):
    name = "RegionIDAndHandleReply"
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
registerMessage(RegionIDAndHandleReply)

class MoneyTransferRequest(message.baseMessage):
    name = "MoneyTransferRequest"
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
registerMessage(MoneyTransferRequest)

class MoneyTransferBackend(message.baseMessage):
    name = "MoneyTransferBackend"
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
registerMessage(MoneyTransferBackend)

class MoneyBalanceRequest(message.baseMessage):
    name = "MoneyBalanceRequest"
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
registerMessage(MoneyBalanceRequest)

class MoneyBalanceReply(message.baseMessage):
    name = "MoneyBalanceReply"
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
registerMessage(MoneyBalanceReply)

class RoutedMoneyBalanceReply(message.baseMessage):
    name = "RoutedMoneyBalanceReply"
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
registerMessage(RoutedMoneyBalanceReply)

class ActivateGestures(message.baseMessage):
    name = "ActivateGestures"
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
registerMessage(ActivateGestures)

class DeactivateGestures(message.baseMessage):
    name = "DeactivateGestures"
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
registerMessage(DeactivateGestures)

class MuteListUpdate(message.baseMessage):
    name = "MuteListUpdate"
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
registerMessage(MuteListUpdate)

class UseCachedMuteList(message.baseMessage):
    name = "UseCachedMuteList"
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
registerMessage(UseCachedMuteList)

class GrantUserRights(message.baseMessage):
    name = "GrantUserRights"
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
registerMessage(GrantUserRights)

class ChangeUserRights(message.baseMessage):
    name = "ChangeUserRights"
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
registerMessage(ChangeUserRights)

class OnlineNotification(message.baseMessage):
    name = "OnlineNotification"
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
registerMessage(OnlineNotification)

class OfflineNotification(message.baseMessage):
    name = "OfflineNotification"
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
registerMessage(OfflineNotification)

class SetStartLocationRequest(message.baseMessage):
    name = "SetStartLocationRequest"
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
registerMessage(SetStartLocationRequest)

class SetStartLocation(message.baseMessage):
    name = "SetStartLocation"
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
registerMessage(SetStartLocation)

class NetTest(message.baseMessage):
    name = "NetTest"
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
registerMessage(NetTest)

class SetCPURatio(message.baseMessage):
    name = "SetCPURatio"
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
registerMessage(SetCPURatio)

class SimCrashed(message.baseMessage):
    name = "SimCrashed"
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
registerMessage(SimCrashed)

class NameValuePair(message.baseMessage):
    name = "NameValuePair"
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
registerMessage(NameValuePair)

class RemoveNameValuePair(message.baseMessage):
    name = "RemoveNameValuePair"
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
registerMessage(RemoveNameValuePair)

class UpdateAttachment(message.baseMessage):
    name = "UpdateAttachment"
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
registerMessage(UpdateAttachment)

class RemoveAttachment(message.baseMessage):
    name = "RemoveAttachment"
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
registerMessage(RemoveAttachment)

class SoundTrigger(message.baseMessage):
    name = "SoundTrigger"
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
registerMessage(SoundTrigger)

class AttachedSound(message.baseMessage):
    name = "AttachedSound"
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
registerMessage(AttachedSound)

class AttachedSoundGainChange(message.baseMessage):
    name = "AttachedSoundGainChange"
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
registerMessage(AttachedSoundGainChange)

class PreloadSound(message.baseMessage):
    name = "PreloadSound"
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
registerMessage(PreloadSound)

class AssetUploadRequest(message.baseMessage):
    name = "AssetUploadRequest"
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
registerMessage(AssetUploadRequest)

class AssetUploadComplete(message.baseMessage):
    name = "AssetUploadComplete"
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
registerMessage(AssetUploadComplete)

class EmailMessageRequest(message.baseMessage):
    name = "EmailMessageRequest"
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
registerMessage(EmailMessageRequest)

class EmailMessageReply(message.baseMessage):
    name = "EmailMessageReply"
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
registerMessage(EmailMessageReply)

class InternalScriptMail(message.baseMessage):
    name = "InternalScriptMail"
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
registerMessage(InternalScriptMail)

class ScriptDataRequest(message.baseMessage):
    name = "ScriptDataRequest"
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
registerMessage(ScriptDataRequest)

class ScriptDataReply(message.baseMessage):
    name = "ScriptDataReply"
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
registerMessage(ScriptDataReply)

class CreateGroupRequest(message.baseMessage):
    name = "CreateGroupRequest"
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
registerMessage(CreateGroupRequest)

class CreateGroupReply(message.baseMessage):
    name = "CreateGroupReply"
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
registerMessage(CreateGroupReply)

class UpdateGroupInfo(message.baseMessage):
    name = "UpdateGroupInfo"
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
registerMessage(UpdateGroupInfo)

class GroupRoleChanges(message.baseMessage):
    name = "GroupRoleChanges"
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
registerMessage(GroupRoleChanges)

class JoinGroupRequest(message.baseMessage):
    name = "JoinGroupRequest"
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
registerMessage(JoinGroupRequest)

class JoinGroupReply(message.baseMessage):
    name = "JoinGroupReply"
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
registerMessage(JoinGroupReply)

class EjectGroupMemberRequest(message.baseMessage):
    name = "EjectGroupMemberRequest"
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
registerMessage(EjectGroupMemberRequest)

class EjectGroupMemberReply(message.baseMessage):
    name = "EjectGroupMemberReply"
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
registerMessage(EjectGroupMemberReply)

class LeaveGroupRequest(message.baseMessage):
    name = "LeaveGroupRequest"
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
registerMessage(LeaveGroupRequest)

class LeaveGroupReply(message.baseMessage):
    name = "LeaveGroupReply"
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
registerMessage(LeaveGroupReply)

class InviteGroupRequest(message.baseMessage):
    name = "InviteGroupRequest"
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
registerMessage(InviteGroupRequest)

class InviteGroupResponse(message.baseMessage):
    name = "InviteGroupResponse"
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
registerMessage(InviteGroupResponse)

class GroupProfileRequest(message.baseMessage):
    name = "GroupProfileRequest"
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
registerMessage(GroupProfileRequest)

class GroupProfileReply(message.baseMessage):
    name = "GroupProfileReply"
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
registerMessage(GroupProfileReply)

class GroupAccountSummaryRequest(message.baseMessage):
    name = "GroupAccountSummaryRequest"
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
registerMessage(GroupAccountSummaryRequest)

class GroupAccountSummaryReply(message.baseMessage):
    name = "GroupAccountSummaryReply"
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
registerMessage(GroupAccountSummaryReply)

class GroupAccountDetailsRequest(message.baseMessage):
    name = "GroupAccountDetailsRequest"
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
registerMessage(GroupAccountDetailsRequest)

class GroupAccountDetailsReply(message.baseMessage):
    name = "GroupAccountDetailsReply"
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
registerMessage(GroupAccountDetailsReply)

class GroupAccountTransactionsRequest(message.baseMessage):
    name = "GroupAccountTransactionsRequest"
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
registerMessage(GroupAccountTransactionsRequest)

class GroupAccountTransactionsReply(message.baseMessage):
    name = "GroupAccountTransactionsReply"
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
registerMessage(GroupAccountTransactionsReply)

class GroupActiveProposalsRequest(message.baseMessage):
    name = "GroupActiveProposalsRequest"
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
registerMessage(GroupActiveProposalsRequest)

class GroupActiveProposalItemReply(message.baseMessage):
    name = "GroupActiveProposalItemReply"
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
registerMessage(GroupActiveProposalItemReply)

class GroupVoteHistoryRequest(message.baseMessage):
    name = "GroupVoteHistoryRequest"
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
registerMessage(GroupVoteHistoryRequest)

class GroupVoteHistoryItemReply(message.baseMessage):
    name = "GroupVoteHistoryItemReply"
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
registerMessage(GroupVoteHistoryItemReply)

class StartGroupProposal(message.baseMessage):
    name = "StartGroupProposal"
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
registerMessage(StartGroupProposal)

class GroupProposalBallot(message.baseMessage):
    name = "GroupProposalBallot"
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
registerMessage(GroupProposalBallot)

class TallyVotes(message.baseMessage):
    name = "TallyVotes"
    id = 365
    freq = 2
    trusted = True
    zero_coded = False
    blocks = [

    ]
    structure = {

    }
registerMessage(TallyVotes)

class GroupMembersRequest(message.baseMessage):
    name = "GroupMembersRequest"
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
registerMessage(GroupMembersRequest)

class GroupMembersReply(message.baseMessage):
    name = "GroupMembersReply"
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
registerMessage(GroupMembersReply)

class ActivateGroup(message.baseMessage):
    name = "ActivateGroup"
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
registerMessage(ActivateGroup)

class SetGroupContribution(message.baseMessage):
    name = "SetGroupContribution"
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
registerMessage(SetGroupContribution)

class SetGroupAcceptNotices(message.baseMessage):
    name = "SetGroupAcceptNotices"
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
registerMessage(SetGroupAcceptNotices)

class GroupRoleDataRequest(message.baseMessage):
    name = "GroupRoleDataRequest"
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
registerMessage(GroupRoleDataRequest)

class GroupRoleDataReply(message.baseMessage):
    name = "GroupRoleDataReply"
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
registerMessage(GroupRoleDataReply)

class GroupRoleMembersRequest(message.baseMessage):
    name = "GroupRoleMembersRequest"
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
registerMessage(GroupRoleMembersRequest)

class GroupRoleMembersReply(message.baseMessage):
    name = "GroupRoleMembersReply"
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
registerMessage(GroupRoleMembersReply)

class GroupTitlesRequest(message.baseMessage):
    name = "GroupTitlesRequest"
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
registerMessage(GroupTitlesRequest)

class GroupTitlesReply(message.baseMessage):
    name = "GroupTitlesReply"
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
registerMessage(GroupTitlesReply)

class GroupTitleUpdate(message.baseMessage):
    name = "GroupTitleUpdate"
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
registerMessage(GroupTitleUpdate)

class GroupRoleUpdate(message.baseMessage):
    name = "GroupRoleUpdate"
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
registerMessage(GroupRoleUpdate)

class LiveHelpGroupRequest(message.baseMessage):
    name = "LiveHelpGroupRequest"
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
registerMessage(LiveHelpGroupRequest)

class LiveHelpGroupReply(message.baseMessage):
    name = "LiveHelpGroupReply"
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
registerMessage(LiveHelpGroupReply)

class AgentWearablesRequest(message.baseMessage):
    name = "AgentWearablesRequest"
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
registerMessage(AgentWearablesRequest)

class AgentWearablesUpdate(message.baseMessage):
    name = "AgentWearablesUpdate"
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
registerMessage(AgentWearablesUpdate)

class AgentIsNowWearing(message.baseMessage):
    name = "AgentIsNowWearing"
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
registerMessage(AgentIsNowWearing)

class AgentCachedTexture(message.baseMessage):
    name = "AgentCachedTexture"
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
registerMessage(AgentCachedTexture)

class AgentCachedTextureResponse(message.baseMessage):
    name = "AgentCachedTextureResponse"
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
registerMessage(AgentCachedTextureResponse)

class AgentDataUpdateRequest(message.baseMessage):
    name = "AgentDataUpdateRequest"
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
registerMessage(AgentDataUpdateRequest)

class AgentDataUpdate(message.baseMessage):
    name = "AgentDataUpdate"
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
registerMessage(AgentDataUpdate)

class GroupDataUpdate(message.baseMessage):
    name = "GroupDataUpdate"
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
registerMessage(GroupDataUpdate)

class AgentGroupDataUpdate(message.baseMessage):
    name = "AgentGroupDataUpdate"
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
registerMessage(AgentGroupDataUpdate)

class AgentDropGroup(message.baseMessage):
    name = "AgentDropGroup"
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
registerMessage(AgentDropGroup)

class LogTextMessage(message.baseMessage):
    name = "LogTextMessage"
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
registerMessage(LogTextMessage)

class ViewerEffect(message.baseMessage):
    name = "ViewerEffect"
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
registerMessage(ViewerEffect)

class CreateTrustedCircuit(message.baseMessage):
    name = "CreateTrustedCircuit"
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
registerMessage(CreateTrustedCircuit)

class DenyTrustedCircuit(message.baseMessage):
    name = "DenyTrustedCircuit"
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
registerMessage(DenyTrustedCircuit)

class RequestTrustedCircuit(message.baseMessage):
    name = "RequestTrustedCircuit"
    id = 394
    freq = 2
    trusted = True
    zero_coded = False
    blocks = [

    ]
    structure = {

    }
registerMessage(RequestTrustedCircuit)

class RezSingleAttachmentFromInv(message.baseMessage):
    name = "RezSingleAttachmentFromInv"
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
registerMessage(RezSingleAttachmentFromInv)

class RezMultipleAttachmentsFromInv(message.baseMessage):
    name = "RezMultipleAttachmentsFromInv"
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
registerMessage(RezMultipleAttachmentsFromInv)

class DetachAttachmentIntoInv(message.baseMessage):
    name = "DetachAttachmentIntoInv"
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
registerMessage(DetachAttachmentIntoInv)

class CreateNewOutfitAttachments(message.baseMessage):
    name = "CreateNewOutfitAttachments"
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
registerMessage(CreateNewOutfitAttachments)

class UserInfoRequest(message.baseMessage):
    name = "UserInfoRequest"
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
registerMessage(UserInfoRequest)

class UserInfoReply(message.baseMessage):
    name = "UserInfoReply"
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
registerMessage(UserInfoReply)

class UpdateUserInfo(message.baseMessage):
    name = "UpdateUserInfo"
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
registerMessage(UpdateUserInfo)

class ParcelRename(message.baseMessage):
    name = "ParcelRename"
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
registerMessage(ParcelRename)

class InitiateDownload(message.baseMessage):
    name = "InitiateDownload"
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
registerMessage(InitiateDownload)

class SystemMessage(message.baseMessage):
    name = "SystemMessage"
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
registerMessage(SystemMessage)

class MapLayerRequest(message.baseMessage):
    name = "MapLayerRequest"
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
registerMessage(MapLayerRequest)

class MapLayerReply(message.baseMessage):
    name = "MapLayerReply"
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
registerMessage(MapLayerReply)

class MapBlockRequest(message.baseMessage):
    name = "MapBlockRequest"
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
registerMessage(MapBlockRequest)

class MapNameRequest(message.baseMessage):
    name = "MapNameRequest"
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
registerMessage(MapNameRequest)

class MapBlockReply(message.baseMessage):
    name = "MapBlockReply"
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
registerMessage(MapBlockReply)

class MapItemRequest(message.baseMessage):
    name = "MapItemRequest"
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
registerMessage(MapItemRequest)

class MapItemReply(message.baseMessage):
    name = "MapItemReply"
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
registerMessage(MapItemReply)

class SendPostcard(message.baseMessage):
    name = "SendPostcard"
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
registerMessage(SendPostcard)

class RpcChannelRequest(message.baseMessage):
    name = "RpcChannelRequest"
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
registerMessage(RpcChannelRequest)

class RpcChannelReply(message.baseMessage):
    name = "RpcChannelReply"
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
registerMessage(RpcChannelReply)

class RpcScriptRequestInbound(message.baseMessage):
    name = "RpcScriptRequestInbound"
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
registerMessage(RpcScriptRequestInbound)

class RpcScriptRequestInboundForward(message.baseMessage):
    name = "RpcScriptRequestInboundForward"
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
registerMessage(RpcScriptRequestInboundForward)

class RpcScriptReplyInbound(message.baseMessage):
    name = "RpcScriptReplyInbound"
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
registerMessage(RpcScriptReplyInbound)

class ScriptMailRegistration(message.baseMessage):
    name = "ScriptMailRegistration"
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
registerMessage(ScriptMailRegistration)

class ParcelMediaCommandMessage(message.baseMessage):
    name = "ParcelMediaCommandMessage"
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
registerMessage(ParcelMediaCommandMessage)

class ParcelMediaUpdate(message.baseMessage):
    name = "ParcelMediaUpdate"
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
registerMessage(ParcelMediaUpdate)

class LandStatRequest(message.baseMessage):
    name = "LandStatRequest"
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
registerMessage(LandStatRequest)

class LandStatReply(message.baseMessage):
    name = "LandStatReply"
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
registerMessage(LandStatReply)

class Error(message.baseMessage):
    name = "Error"
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
registerMessage(Error)

class ObjectIncludeInSearch(message.baseMessage):
    name = "ObjectIncludeInSearch"
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
registerMessage(ObjectIncludeInSearch)

class RezRestoreToWorld(message.baseMessage):
    name = "RezRestoreToWorld"
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
registerMessage(RezRestoreToWorld)

class LinkInventoryItem(message.baseMessage):
    name = "LinkInventoryItem"
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
registerMessage(LinkInventoryItem)

