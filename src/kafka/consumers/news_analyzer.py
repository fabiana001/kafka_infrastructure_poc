from kafka.consumers.base_consumer import BaseConsumer
from kafka.consumers.base_producer import BaseProducer
import nerdalidator.nerdalidator as nd
import logging
import traceback
import time

class NewsAnalyzer(object):

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(threadName)-12.12s] [%(levelname)-5.5s]  %(message)s",
        handlers=[
            logging.FileHandler("example.log"),
            logging.StreamHandler()
        ])

    def __init__(self,
                 es_avro_schema_path,
                 language_model="en",
                 bootsrap_servers='localhost:29092',
                 schema_registry='http://localhost:8081',
                 mysql_topic_subscribe='quickstart-jdbc-PRO_clip_repository',
                 es_topic_subscribe="test-elasticsearch-sink"
                 ):

        self.logger = logging.getLogger(__name__)

        self.logger.info("Initializing model")
        self.model = nd.NERTagger(lang=language_model)
        self.logger.info("Model initialized")
        self.bootsrap_servers = bootsrap_servers
        self.schema_registry = schema_registry
        self.mysql_topic_subscribe = mysql_topic_subscribe
        self.es_avro_schema_path = es_avro_schema_path
        self.es_topic_subscribe = es_topic_subscribe

    def _from_timestamp_to_long(self, ts):
        return int(ts.timestamp())

    def _convert_ts_fields(self, ts_fields, dict):
        """
        :param ts_fields: list of ts fields
        :param dict: dictionary containing data to convert
        :return:
        """
        new_dict = dict
        for f in ts_fields:
            new_dict[f] = self._from_timestamp_to_long(dict[f])
        return new_dict

    def run(self):
        with BaseConsumer(self.bootsrap_servers,
                          self.schema_registry,
                          self.mysql_topic_subscribe) as cons, \
                BaseProducer(self.es_avro_schema_path,
                             self.bootsrap_servers,
                             self.schema_registry,
                             self.es_topic_subscribe) as prod:
            while True:
                try:
                    message = cons.process_message()
                    if message and message.value()["text"]:
                        data = message.value()
                        text = data["text"]
                        dict_loc = self.model.validate_loc(text)
                        converted_data = self._convert_ts_fields(["insertdate", "pubDate"], data)

                        converted_data["locations"] = dict_loc
                        prod.send_message(converted_data)
                except Exception as e:
                    str = "[{}] partition:{}, offset:{}, traceback:{},  ".format(self.__class__.__name__,
                                                                                 message.topic(),
                                                                                 message.partition(),
                                                                                 traceback.format_exc())
                    self.logger.info(str)




if __name__ == '__main__':
    news_analyzer = NewsAnalyzer(es_avro_schema_path="../avro/es_news.avsc", es_topic_subscribe="genero_news")
    news_analyzer.run()
