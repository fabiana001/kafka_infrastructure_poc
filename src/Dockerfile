FROM python:3.7.0-slim

ARG LIBRDKAFKA_VER="0.9.1-1"

RUN mkdir /usr/kafka \
    && mkdir /usr/kafka/avro \
    && mkdir /usr/kafka/consumers

ADD ./kafka/consumers /usr/kafka/consumers
ADD ./avro/news.avsc /usr/kafka/news.avsc
ADD ./news_generator.py /usr/kafka/news_generator.py

WORKDIR /usr

RUN apt-get update && \
    apt-get install -y \
      unzip \
      wget \
      git \
      gcc \
      g++ \
      make

RUN wget https://github.com/edenhill/librdkafka/archive/debian/$LIBRDKAFKA_VER.zip && \
    unzip $LIBRDKAFKA_VER.zip && \
    rm $LIBRDKAFKA_VER.zip && \
    ls && \
    cd librdkafka-debian-$LIBRDKAFKA_VER && \
    ./configure && \
    make && \
    make install && \
    cd ..


RUN pip install confluent-kafka \
    && pip install confluent-kafka[avro] \
    && pip install avro-gen

WORKDIR /usr/kafka

RUN python news_generator.py -a news.avsc -o ./avro/

CMD ["/bin/bash"]
