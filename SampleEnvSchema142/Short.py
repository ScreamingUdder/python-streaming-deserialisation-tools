# automatically generated, do not modify

# namespace: 

import flatbuffers

class Short(object):
    __slots__ = ['_tab']

    # Short
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # Short
    def Value(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int16Flags, o + self._tab.Pos)
        return 0

def ShortStart(builder): builder.StartObject(1)
def ShortAddValue(builder, value): builder.PrependInt16Slot(0, value, 0)
def ShortEnd(builder): return builder.EndObject()
