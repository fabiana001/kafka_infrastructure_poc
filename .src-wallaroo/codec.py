from avro.io import DatumReader, DatumWriter
from avro.io import BinaryDecoder, BinaryEncoder
from io import StringIO
import avro.schema
import unittest

SCHEMA = avro.schema.Parse(open("/src/wallaroo/fabiana_kafka/sensor_reading.avsc", "r").read())
def deserialize(thing):
    reader = DatumReader(writers_schema=SCHEMA, readers_schema=SCHEMA)
    buf = StringIO(thing)
    data = reader.read(BinaryDecoder(buf))
    buf.close()
    return data

def serialize(thing):
    writer = DatumWriter(SCHEMA)
    buf = StringIO()
    writer.write(thing, BinaryEncoder(buf))
    v = buf.getvalue()
    buf.close()
    return v

class Tests(unittest.TestCase):
    READING = {u"id": u"1",
               u"lat": 23.2,
               u"lon": -50.9,
               u"val": 2345}

    def test_serialize_deserialize(self):
        p = self.READING
        q = deserialize(serialize(p))
        self.assertEqual(p['id'], q['id'])
        self.assertEqual(p['val'], q['val'])
        self.assertAlmostEqual(p['lon'], q['lon'], places=5)
        self.assertAlmostEqual(p['lat'], q['lat'], places=5)
