# automatically generated, do not modify

# namespace: 

import flatbuffers

class Int(object):
    __slots__ = ['_tab']

    # Int
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # Int
    def Value(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

def IntStart(builder): builder.StartObject(1)
def IntAddValue(builder, value): builder.PrependInt32Slot(0, value, 0)
def IntEnd(builder): return builder.EndObject()
