# automatically generated, do not modify

# namespace: 

import flatbuffers

class UByte(object):
    __slots__ = ['_tab']

    # UByte
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # UByte
    def Value(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint8Flags, o + self._tab.Pos)
        return 0

def UByteStart(builder): builder.StartObject(1)
def UByteAddValue(builder, value): builder.PrependUint8Slot(0, value, 0)
def UByteEnd(builder): return builder.EndObject()
