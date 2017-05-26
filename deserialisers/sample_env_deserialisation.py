class SampleEnvDeserialiser142(object):
    """
    Deserialisation for sample environment data encoded with the f142 schema.
    """

    @staticmethod
    def deserialise_data(buf):
        """
        Extract sample environment data from FlatBuffers encoded data.

        :param buf: the FlatBuffers data buffer as a bytearray
        :return: a dictionary containing the relevant information
        """
        import SampleEnvSchema142.LogData as LogData
        from SampleEnvSchema142.Value import Value
        from SampleEnvSchema142.Int import Int
        from SampleEnvSchema142.Double import Double

        ans = LogData.LogData.GetRootAsLogData(buf, 0)

        data = dict()
        data['name'] = ans.SourceName()
        data['timestamp'] = ans.Timestamp()

        if ans.ValueType() == Value.Int:
            value = Int()
            value.Init(ans.Value().Bytes, ans.Value().Pos)
            data['value'] = value.Value()
        elif ans.ValueType() == Value.Double:
            value = Double()
            value.Init(ans.Value().Bytes, ans.Value().Pos)
            data['value'] = value.Value()
        else:
            raise TypeError("Could not handle the value type")

        return data
