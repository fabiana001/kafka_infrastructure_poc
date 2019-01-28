## Run wallaroo container
First run a kafka container:
```bash
> cd docker
> docker-compose up -d
```
First check the network name of kafka and the other containers:

> docker network ls

Then run a wallaroo container:

```bash
docker run --rm -it --privileged -p 4000:4000 \
-v /Users/lanottef/git/test_wallaroo/wallaroo-src:/src/wallaroo \
-v /Users/lanottef/git/test_wallaroo/python-virtualenv-machida3:/src/python-virtualenv \
--name wally \
--net=docker_default \
wallaroo-labs-docker-wallaroolabs.bintray.io/release/wallaroo:0.6.1 -p python3
```
where `--net=docker_default` is the name of the network extracted through the `docker network ls` command.




2. Create the directory _wallaroo_kafka_project_:
``` bash
> mkdir wallaroo_kafka_project
> cd wallaroo_kafka_project
```

3. It contains the following files:
-  requirements.txt;
- app.py;
- generator.py;
- codec.py;
- sensor_reading.avsc

4. Install required dependencies:
``` bash
> pip install -r ./requirements.txt
```
5. Run the producer:
```bash
./generator.py
```

7. Run the consumer
``` bash
> machida3 --application-module app \
	--kafka_source_topic $(IN_TOPIC) \
	--kafka_source_brokers 127.0.0.1:9092 \
	--kafka_sink_topic $(OUT_TOPIC) \
	--kafka_sink_brokers 127.0.0.1:9092 \
	--kafka_sink_max_message_size 100000 \
	--kafka_sink_max_produce_buffer_ms 100 \
	--metrics 127.0.0.1:5001 \
	--control 127.0.0.1:12500 \
	--data 127.0.0.1:12501 \
	--external 127.0.0.1:5050 \
	--cluster-initializer --ponythreads=1 \
	--ponynoblock
```

8. From Kafka to ElasticSearch:
https://github.com/confluentinc/demo-scene/blob/master/ksql-atm-fraud-detection/docker-compose.yml
