# automatically generated, do not modify

# namespace: 

import flatbuffers

class UShort(object):
    __slots__ = ['_tab']

    # UShort
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # UShort
    def Value(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint16Flags, o + self._tab.Pos)
        return 0

def UShortStart(builder): builder.StartObject(1)
def UShortAddValue(builder, value): builder.PrependUint16Slot(0, value, 0)
def UShortEnd(builder): return builder.EndObject()
