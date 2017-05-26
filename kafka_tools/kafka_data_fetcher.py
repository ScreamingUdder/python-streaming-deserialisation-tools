from kafka import KafkaConsumer, TopicPartition


class KafkaDataFetcher(object):
    """
    Fetches data from kafka_tools.
    """

    @staticmethod
    def fetch_data(brokers, topic, offset=-1):
        """
        Fetch data from the specified broker(s) and topic.

        :param brokers: a list of brokers
        :param topic:  the topic name
        :param offset: the offset of the data to fetch (defaults to most recent value)
        :return: bytearray containing the data
        """
        topic = TopicPartition(topic, 0)

        consumer = KafkaConsumer(bootstrap_servers=brokers)
        consumer.assign([topic])

        if offset == -1:
            # Get most recent value
            consumer.seek_to_end(topic)
            end_pos = consumer.position(topic)
            consumer.seek(topic, end_pos - 1)
        else:
            consumer.seek(topic, offset)

        data = list()

        while len(data) == 0:
            data = consumer.poll()
        buf = bytearray(data[topic][0].value)

        consumer.close()

        return buf
