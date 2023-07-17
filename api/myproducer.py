from time import sleep
import re
from kafka import KafkaProducer,KafkaConsumer
import json

def publish_message(producer_instance, topic_name, key, value):
    try:
        key_bytes = bytes(key, encoding='utf-8')
        value_str = json.dumps(value)  # Serialize dictionary to JSON string
        value_bytes = bytes(value_str, encoding='utf-8')
        producer_instance.send(topic_name, key=key_bytes, value=value_bytes)
        producer_instance.flush()
        print('Message published successfully.')
      
    except Exception as ex:
        print('Exception in publishing message')
        print(str(ex))


def connect_kafka_producer(bs):
    _producer = None
    try:
        _producer = KafkaProducer(bootstrap_servers=bs, api_version=(0, 10))
    except Exception as ex:
        print('Exception while connecting Kafka')
        print(str(ex))
    finally:
        return _producer

