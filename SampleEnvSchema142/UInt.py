# automatically generated, do not modify

# namespace: 

import flatbuffers

class UInt(object):
    __slots__ = ['_tab']

    # UInt
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # UInt
    def Value(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, o + self._tab.Pos)
        return 0

def UIntStart(builder): builder.StartObject(1)
def UIntAddValue(builder, value): builder.PrependUint32Slot(0, value, 0)
def UIntEnd(builder): return builder.EndObject()
