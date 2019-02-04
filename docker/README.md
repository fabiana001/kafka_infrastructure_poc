##Stack version
- Zookeeper version: 3.4.9
- Kafka version: 2.1.0 (Confluent 5.1.0)
- Kafka Schema Registry: Confluent 5.1.0
- [Kafka Schema Registry UI: 0.9.4](https://github.com/Landoop/schema-registry-ui)
- Kafka Rest Proxy: Confluent 5.1.0
- [Kafka Topics UI: 0.9.4](https://github.com/Landoop/kafka-topics-ui)
- Kafka Connect: Confluent 5.1.0
- Kafka Connect UI: 0.9.4
- Zoonavigator: 0.5.1
- Mysql: 5.7

## Run all services
The following script ru

```bash
> chmod +x launch_demo.sh
> ./launch_demo.sh
```
## Run Kafka consumer

```bash
> docker build --no-cache -t simple_kafka_consumer .
> docker run -it simple_kafka_consumer
```
