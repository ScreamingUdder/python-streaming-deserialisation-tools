# automatically generated, do not modify

# namespace: 

import flatbuffers

class ArrayULong(object):
    __slots__ = ['_tab']

    # ArrayULong
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # ArrayULong
    def Value(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Uint64Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 8))
        return 0

    # ArrayULong
    def ValueLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

def ArrayULongStart(builder): builder.StartObject(1)
def ArrayULongAddValue(builder, value): builder.PrependUOffsetTRelativeSlot(0, flatbuffers.number_types.UOffsetTFlags.py_type(value), 0)
def ArrayULongStartValueVector(builder, numElems): return builder.StartVector(8, numElems, 8)
def ArrayULongEnd(builder): return builder.EndObject()
