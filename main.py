from sample_env_deserialisation import SampleEnvDeserialiser142 as SampleEnvDeserialiser
from event_deserialisation import EventDeserialiser42 as EventDeserialiser
from kafka_data_fetcher import KafkaDataFetcher


BROKERS = ["tenten:9092", "sakura:9092"]
SE_TOPIC_NAME = "fewtestdata_sampleEnv"
EVENT_TOPIC_NAME = "fewtestdata_events"

# Get SE data
buf = KafkaDataFetcher.fetch_data(BROKERS, SE_TOPIC_NAME)
print SampleEnvDeserialiser.deserialise_data(buf)

# Get event data
buf = KafkaDataFetcher.fetch_data(BROKERS, EVENT_TOPIC_NAME)
print EventDeserialiser.deserialise_data(buf)
