# automatically generated, do not modify

# namespace: 

import flatbuffers

class ArrayUInt(object):
    __slots__ = ['_tab']

    # ArrayUInt
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # ArrayUInt
    def Value(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 4))
        return 0

    # ArrayUInt
    def ValueLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

def ArrayUIntStart(builder): builder.StartObject(1)
def ArrayUIntAddValue(builder, value): builder.PrependUOffsetTRelativeSlot(0, flatbuffers.number_types.UOffsetTFlags.py_type(value), 0)
def ArrayUIntStartValueVector(builder, numElems): return builder.StartVector(4, numElems, 4)
def ArrayUIntEnd(builder): return builder.EndObject()
