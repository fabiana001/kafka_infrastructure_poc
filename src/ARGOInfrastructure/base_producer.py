from confluent_kafka import avro
from confluent_kafka.avro import AvroProducer
import logging

class GenericKafkaError(Exception):
    pass


class KafkaKeyboardInterrupt(Exception):
    pass


class KafkaValueError(Exception):
    pass


class BaseProducer(object):

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(threadName)-12.12s] [%(levelname)-5.5s]  %(message)s",
        handlers=[
            logging.FileHandler("example.log"),
            logging.StreamHandler()
        ])

    def __init__(self,
                 avro_schema_path,
                 bootsrap_servers='localhost:29092',
                 schema_registry='http://localhost:8081',
                 topic_subscribe='quickstart-elastic-news'):
        # remember if you are running this code outside docker set bootstrap.servers = 'localhost:29092' and 'schema.registry.url'= 'http://localhost:8081',
        # otherwise set bootstrap.servers = 'kafka:9092' and 'schema.registry.url'= 'http://schema-registry:8081'
        # "debug":"all",
        self.conf = {
            'schema.registry.url': schema_registry,
            'bootstrap.servers': bootsrap_servers
        }
        self.SCHEMA = avro.loads(open(avro_schema_path, "r").read())
        self.topic_subscribe = topic_subscribe
        self.logger = logging.getLogger(__name__)

    def _on_delivery(self, err, msg, obj):
        """
            Handle delivery reports served from producer.poll.
            This callback takes an extra argument, obj.
            This allows the original contents to be included for debugging purposes.
        """
        if err is not None:
            self.logger.error('Message {} delivery failed for user with error {}'.format(obj, err))

    def __enter__(self):
        self.avroProducer = AvroProducer(self.conf, default_value_schema=self.SCHEMA)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.avroProducer.flush()

    def send_message(self, record):
        try:
            self.avroProducer.produce(topic=self.topic_subscribe,
                                      value=record,
                                      callback=lambda err, msg, obj=record: self._on_delivery(err, msg, obj))

            self.avroProducer.poll(30)

        except KeyboardInterrupt as e:
            raise KafkaKeyboardInterrupt(e)
        except ValueError as e:
            raise KafkaValueError("Invalid input {}" % e)
        except Exception as e:
            #raise GenericKafkaError(e)
            raise Exception(e)

    def __repr__(self):
        return '%s(%r)' % (self.__class__.__name__, self.bootsrap_servers)

    @staticmethod
    def test():
        from faker import Faker

        avro_schema_path = "../avro/sensor_reading.avsc"
        topic_subscribe = "test-elasticsearch-sink"
        with BaseProducer(avro_schema_path=avro_schema_path, topic_subscribe=topic_subscribe) as prod:
            gen = Faker()

            for i in range(100):
                message = {"id": gen.uuid4(),
                           "lat": float(gen.latitude()),
                           "lon": float(gen.longitude()),
                           "val": gen.pyint()}

                prod.send_message(message)
        print("Messages correctly sent to kafka broker")
        print("topic: {0}, schema_path: {1}".format(topic_subscribe, avro_schema_path))

if __name__ == '__main__':
    BaseProducer.test()
