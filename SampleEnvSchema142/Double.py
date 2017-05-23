# automatically generated, do not modify

# namespace: 

import flatbuffers

class Double(object):
    __slots__ = ['_tab']

    # Double
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # Double
    def Value(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float64Flags, o + self._tab.Pos)
        return 0

def DoubleStart(builder): builder.StartObject(1)
def DoubleAddValue(builder, value): builder.PrependFloat64Slot(0, value, 0)
def DoubleEnd(builder): return builder.EndObject()
