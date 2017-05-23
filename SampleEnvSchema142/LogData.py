# automatically generated, do not modify

# namespace: 

import flatbuffers

class LogData(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsLogData(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = LogData()
        x.Init(buf, n + offset)
        return x


    # LogData
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # LogData
    def SourceName(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return ""

    # LogData
    def ValueType(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint8Flags, o + self._tab.Pos)
        return 0

    # LogData
    def Value(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            from flatbuffers.table import Table
            obj = Table(bytearray(), 0)
            self._tab.Union(obj, o)
            return obj
        return None

    # LogData
    def Timestamp(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint64Flags, o + self._tab.Pos)
        return 0

    # LogData
    def FwdinfoType(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint8Flags, o + self._tab.Pos)
        return 0

    # LogData
    def Fwdinfo(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            from flatbuffers.table import Table
            obj = Table(bytearray(), 0)
            self._tab.Union(obj, o)
            return obj
        return None

def LogDataStart(builder): builder.StartObject(6)
def LogDataAddSourceName(builder, sourceName): builder.PrependUOffsetTRelativeSlot(0, flatbuffers.number_types.UOffsetTFlags.py_type(sourceName), 0)
def LogDataAddValueType(builder, valueType): builder.PrependUint8Slot(1, valueType, 0)
def LogDataAddValue(builder, value): builder.PrependUOffsetTRelativeSlot(2, flatbuffers.number_types.UOffsetTFlags.py_type(value), 0)
def LogDataAddTimestamp(builder, timestamp): builder.PrependUint64Slot(3, timestamp, 0)
def LogDataAddFwdinfoType(builder, fwdinfoType): builder.PrependUint8Slot(4, fwdinfoType, 0)
def LogDataAddFwdinfo(builder, fwdinfo): builder.PrependUOffsetTRelativeSlot(5, flatbuffers.number_types.UOffsetTFlags.py_type(fwdinfo), 0)
def LogDataEnd(builder): return builder.EndObject()
