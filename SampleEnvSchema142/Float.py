# automatically generated, do not modify

# namespace: 

import flatbuffers

class Float(object):
    __slots__ = ['_tab']

    # Float
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # Float
    def Value(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0

def FloatStart(builder): builder.StartObject(1)
def FloatAddValue(builder, value): builder.PrependFloat32Slot(0, value, 0)
def FloatEnd(builder): return builder.EndObject()
