# automatically generated, do not modify

# namespace: 

import flatbuffers

class ArrayUByte(object):
    __slots__ = ['_tab']

    # ArrayUByte
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # ArrayUByte
    def Value(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Uint8Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 1))
        return 0

    # ArrayUByte
    def ValueLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

def ArrayUByteStart(builder): builder.StartObject(1)
def ArrayUByteAddValue(builder, value): builder.PrependUOffsetTRelativeSlot(0, flatbuffers.number_types.UOffsetTFlags.py_type(value), 0)
def ArrayUByteStartValueVector(builder, numElems): return builder.StartVector(1, numElems, 1)
def ArrayUByteEnd(builder): return builder.EndObject()
