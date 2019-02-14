from codec import deserialize
from collections import namedtuple
import wallaroo

def application_setup(args):
    ab = wallaroo.ApplicationBuilder("Avro example app")
    ab.new_pipeline("avro example pipeline",
                    wallaroo.DefaultKafkaSourceCLIParser(decoder))
    ab.to(extract_value)
    ab.to_sink(wallaroo.DefaultKafkaSinkCLIParser(encoder))
    return ab.build()

@wallaroo.computation(name="extract reading value")
def extract_value(reading):
    print(reading)
    return reading[u'val']

@wallaroo.decoder(header_length=4, length_fmt=">I")
def decoder(data):
    return deserialize(data)

@wallaroo.encoder
def encoder(val):
    return (str(val), None, None)
