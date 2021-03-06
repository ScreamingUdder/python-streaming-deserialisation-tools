# automatically generated, do not modify

# namespace: 

import flatbuffers

class EventMessage(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsEventMessage(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = EventMessage()
        x.Init(buf, n + offset)
        return x


    # EventMessage
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # EventMessage
    def SourceName(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return ""

    # EventMessage
    def MessageId(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint64Flags, o + self._tab.Pos)
        return 0

    # EventMessage
    def PulseTime(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint64Flags, o + self._tab.Pos)
        return 0

    # EventMessage
    def TimeOfFlight(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 4))
        return 0

    # EventMessage
    def TimeOfFlightLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # EventMessage
    def DetectorId(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 4))
        return 0

    # EventMessage
    def DetectorIdLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # EventMessage
    def FacilitySpecificDataType(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint8Flags, o + self._tab.Pos)
        return 0

    # EventMessage
    def FacilitySpecificData(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            from flatbuffers.table import Table
            obj = Table(bytearray(), 0)
            self._tab.Union(obj, o)
            return obj
        return None

def EventMessageStart(builder): builder.StartObject(7)
def EventMessageAddSourceName(builder, sourceName): builder.PrependUOffsetTRelativeSlot(0, flatbuffers.number_types.UOffsetTFlags.py_type(sourceName), 0)
def EventMessageAddMessageId(builder, messageId): builder.PrependUint64Slot(1, messageId, 0)
def EventMessageAddPulseTime(builder, pulseTime): builder.PrependUint64Slot(2, pulseTime, 0)
def EventMessageAddTimeOfFlight(builder, timeOfFlight): builder.PrependUOffsetTRelativeSlot(3, flatbuffers.number_types.UOffsetTFlags.py_type(timeOfFlight), 0)
def EventMessageStartTimeOfFlightVector(builder, numElems): return builder.StartVector(4, numElems, 4)
def EventMessageAddDetectorId(builder, detectorId): builder.PrependUOffsetTRelativeSlot(4, flatbuffers.number_types.UOffsetTFlags.py_type(detectorId), 0)
def EventMessageStartDetectorIdVector(builder, numElems): return builder.StartVector(4, numElems, 4)
def EventMessageAddFacilitySpecificDataType(builder, facilitySpecificDataType): builder.PrependUint8Slot(5, facilitySpecificDataType, 0)
def EventMessageAddFacilitySpecificData(builder, facilitySpecificData): builder.PrependUOffsetTRelativeSlot(6, flatbuffers.number_types.UOffsetTFlags.py_type(facilitySpecificData), 0)
def EventMessageEnd(builder): return builder.EndObject()
