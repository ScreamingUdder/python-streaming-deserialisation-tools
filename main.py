from sample_env_deserialisation import SampleEnvDeserialiser142 as Deserialiser
from kafka_data_fetcher import KafkaDataFetcher


BROKERS = ["tenten:9092", "sakura:9092"]
TOPIC_NAME = "forwarder_test"

buf = KafkaDataFetcher.fetch_data(BROKERS, TOPIC_NAME)

print Deserialiser.deserialise_sample_env_data(buf)

