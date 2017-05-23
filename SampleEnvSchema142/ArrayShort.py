# automatically generated, do not modify

# namespace: 

import flatbuffers

class ArrayShort(object):
    __slots__ = ['_tab']

    # ArrayShort
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # ArrayShort
    def Value(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Int16Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 2))
        return 0

    # ArrayShort
    def ValueLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

def ArrayShortStart(builder): builder.StartObject(1)
def ArrayShortAddValue(builder, value): builder.PrependUOffsetTRelativeSlot(0, flatbuffers.number_types.UOffsetTFlags.py_type(value), 0)
def ArrayShortStartValueVector(builder, numElems): return builder.StartVector(2, numElems, 2)
def ArrayShortEnd(builder): return builder.EndObject()
