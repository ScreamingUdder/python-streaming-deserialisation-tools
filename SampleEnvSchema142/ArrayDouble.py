# automatically generated, do not modify

# namespace: 

import flatbuffers

class ArrayDouble(object):
    __slots__ = ['_tab']

    # ArrayDouble
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # ArrayDouble
    def Value(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Float64Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 8))
        return 0

    # ArrayDouble
    def ValueLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

def ArrayDoubleStart(builder): builder.StartObject(1)
def ArrayDoubleAddValue(builder, value): builder.PrependUOffsetTRelativeSlot(0, flatbuffers.number_types.UOffsetTFlags.py_type(value), 0)
def ArrayDoubleStartValueVector(builder, numElems): return builder.StartVector(8, numElems, 8)
def ArrayDoubleEnd(builder): return builder.EndObject()