# Producing info into Kakfa
from confluent_kafka.avro import AvroConsumer
from confluent_kafka import KafkaError
import logging
import time
from confluent_kafka.cimpl import TopicPartition


class KafkaPartitionError(Exception):
    pass


class GenericKafkaError(Exception):
    pass


class BaseConsumer(object):

    def __init__(self, bootsrap_servers='localhost:29092',
                 schema_registry='http://localhost:8081',
                 topic_subscribe='quickstart-jdbc-PRO_clip_repository'):
        # remember if you are running this code outside docker set bootstrap.servers = 'localhost:29092' and 'schema.registry.url'= 'http://localhost:8081',
        # otherwise set bootstrap.servers = 'kafka:9092' and 'schema.registry.url'= 'http://schema-registry:8081'
        # "debug":"all",

        genero_consumer_id = "genero_consumer_{}".format(int(time.time()))

        self.conf = {
            'schema.registry.url': schema_registry,
            'bootstrap.servers': bootsrap_servers,
            'group.id': genero_consumer_id,
            'auto.offset.reset': 'beginning',
            #'enable.auto.commit': True,
            #'enable.auto.offset.store': False,
            'socket.timeout.ms': 60000,
            'session.timeout.ms': 60000}

        self.topic_subscribe = topic_subscribe

        logging.basicConfig(
            level=logging.INFO,
            format="%(asctime)s [%(threadName)-12.12s] [%(levelname)-5.5s]  %(message)s",
            handlers=[
                logging.FileHandler("example.log"),
                logging.StreamHandler()
            ])
        self.logger = logging.getLogger(__name__)

        self.avroConsumer = AvroConsumer(config=self.conf)
        self.avroConsumer.subscribe(topics=[self.topic_subscribe])

    def __enter__(self):
        #self.avroConsumer = AvroConsumer(config=self.conf)
        #self.avroConsumer.subscribe(topics=[self.topic_subscribe])

        #self.tp = TopicPartition(topic=self.topic_subscribe, partition=0, offset=0)

        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.avroConsumer.close()

    def process_message(self):
        """
        :return: message object with deserialized key and value as dict objects
        :rtype: Message
        """
        try:
            msg = self.avroConsumer.poll(0)
            if msg:
                if not msg.error():
                    return msg
                elif msg.error().code() == KafkaError._PARTITION_EOF:
                    self.logger.info('[{0}] End of partition reached {1}/{2}'.format(self.__class__.__name__, msg.topic(), msg.partition()))
                else:
                    raise GenericKafkaError(msg.error())
        except Exception as e:
            raise GenericKafkaError(e)

    def __repr__(self):
        return '%s(%r)' % (self.__class__.__name__, self.conf)

    @staticmethod
    def test():
        with BaseConsumer(topic_subscribe='pippo') as cons:
            while True:
                message = cons.process_message()
                if message:
                    print(message.value())


if __name__ == '__main__':
    import nerdalidator.nerdalidator as nd
    try:
        #BaseConsumer.test()
        print("Initializing model")
        #model = nd.NERTagger()
        print("Starting consuming")
        with BaseConsumer() as cons:
            while True:
                message = cons.process_message()
                if message and message.value()["text"]:
                    data = message.value()
                    #print(message.value())
                    text = data["text"]
                    date = data["insertdate"]
                    print("\nTEXT : \t", text)
                    print("\nDATE : \t", date)
                    print(message.offset())
                    print(message.partition())
                    #dict_loc = model.validate_loc(text)
                    #print(dict_loc)

    except KeyboardInterrupt as e:
        print("Consumed stopped due KeyboardInterrupt")

