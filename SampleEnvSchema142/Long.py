# automatically generated, do not modify

# namespace: 

import flatbuffers

class Long(object):
    __slots__ = ['_tab']

    # Long
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # Long
    def Value(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

def LongStart(builder): builder.StartObject(1)
def LongAddValue(builder, value): builder.PrependInt64Slot(0, value, 0)
def LongEnd(builder): return builder.EndObject()
