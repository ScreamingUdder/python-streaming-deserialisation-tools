# automatically generated, do not modify

# namespace: 

import flatbuffers

class ArrayInt(object):
    __slots__ = ['_tab']

    # ArrayInt
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # ArrayInt
    def Value(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Int32Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 4))
        return 0

    # ArrayInt
    def ValueLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

def ArrayIntStart(builder): builder.StartObject(1)
def ArrayIntAddValue(builder, value): builder.PrependUOffsetTRelativeSlot(0, flatbuffers.number_types.UOffsetTFlags.py_type(value), 0)
def ArrayIntStartValueVector(builder, numElems): return builder.StartVector(4, numElems, 4)
def ArrayIntEnd(builder): return builder.EndObject()
