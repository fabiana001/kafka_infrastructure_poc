#!/usr/bin/env python2
from faker import Faker
from confluent_kafka import avro
from confluent_kafka.avro import AvroProducer

TOPIC = 'sensor-readings'
SCHEMA = avro.loads(open("/src/wallaroo/sensor_reading.avsc", "r").read())
conf = {
    'bootstrap.servers': 'kafka:9092',
    'schema.registry.url': 'http://schema-registry:8081'
    }

def main():
    #source = KafkaProducer(bootstrap_servers=KAFKA)
    producer = AvroProducer(conf, default_value_schema=SCHEMA)
    print("Producing user records to topic {}. ^c to exit.".format(TOPIC))

    gen = Faker()
    loop(producer, gen)

def loop(producer, gen):
    while True:
        try:
            record = random_sensor_reading(gen)

            # The message passed to the delivery callback will already be serialized.
            # To aid in debugging we provide the original object to the delivery callback.
            #producer.produce(topic=TOPIC, value=record, callback=lambda err, msg, obj=record: on_delivery(err, msg, obj))
            producer.produce(topic=TOPIC, value=record,
                             callback=lambda err, msg, obj=record: on_delivery(err, msg, obj))

            # Serve on_delivery callbacks from previous asynchronous produce()
            producer.poll(0)
        except KeyboardInterrupt:
            break
        except ValueError as error:
            print("Invalid input, discarding record...")
            #print(error)
            continue

    print("\nFlushing records...")
    producer.flush()

def on_delivery(err, msg, obj):
    """
        Handle delivery reports served from producer.poll.
        This callback takes an extra argument, obj.
        This allows the original contents to be included for debugging purposes.
    """
    if err is not None:
        print('Message {} delivery failed for user with error {}'.format(obj, err))
    #else:
    #    print('Message {} successfully produced to {} [{}] at offset {}'.format(
    #        obj, msg.topic(), msg.partition(), msg.offset()))


def random_sensor_reading(gen=Faker()):
    return {"id": gen.uuid4(),
            "lat": float(gen.latitude()),
            "lon": float(gen.longitude()),
            "val": gen.pyint()}

if __name__ == '__main__':
    main()
