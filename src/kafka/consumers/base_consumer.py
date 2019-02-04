#Producing info into Kakfa
from confluent_kafka.avro import AvroConsumer
from confluent_kafka import KafkaError
from confluent_kafka.avro.serializer import SerializerError
import random
import time

#Set producer
conf = {'bootstrap.servers': 'kafka:9092',
        'group.id': 'pippo_supplier_groups',
        'auto.offset.reset': 'beginning',
        'schema.registry.url': 'http://schema-registry:8081'}


avroConsumer = AvroConsumer(config=conf)

topics_subsribe = ['quickstart-jdbc-PRO_clip_repository']

#Consume values
avroConsumer.subscribe(topics=topics_subsribe)

print("Starting consumer for topic quickstart-jdbc-PRO_clip_repository")
running = True
while running:
    try:
        #Get message
        msg = avroConsumer.poll(30)
        if msg:

            #If message is not error, then print message
            if not msg.error():
                print("Message is : ", msg.value())
                time.sleep(4)
                countries = ["it", "us", "sp", "tk", "gb", "gr", "po"]
                print(random.sample(countries, 5))

            #If not EOF partition error, print error
            elif msg.error().code() != KafkaError._PARTITION_EOF:
                print("Error is ", msg.error())
                running = False

    except SerializerError as e:
        print("Message serialization failed for %s : %s" % (msg, e))
        running = False
    except Exception as e:
        print(e)
        running = False

avroConsumer.close()
print("Consumer stopped")
