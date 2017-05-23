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
        from SampleEnvSchema142.Int import Int as Int

        ans = LogData.LogData.GetRootAsLogData(buf, 0)

        name = ans.SourceName()
        ts = ans.Timestamp()

        if ans.ValueType() == Value.Int:
            value = Int()
            value.Init(ans.Value().Bytes, ans.Value().Pos)

        return {"name": name, "value": value.Value(), "timestamp": ts}
