# automatically generated, do not modify

# namespace: 

import flatbuffers

class Byte(object):
    __slots__ = ['_tab']

    # Byte
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # Byte
    def Value(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int8Flags, o + self._tab.Pos)
        return 0

def ByteStart(builder): builder.StartObject(1)
def ByteAddValue(builder, value): builder.PrependInt8Slot(0, value, 0)
def ByteEnd(builder): return builder.EndObject()
