# Genero Infrastructure

## Stack version
- Python 3
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

## Genero Workflow

The following figure show the workflow of Genero Infrastructure.

![](https://github.com/fabiana001/wallaroo_kafka_example/blob/master/imgs/genero_workflow.png)
1. Data is initially stored in a mysql database and daily updated;
2. Each time new data is inserted or updated in the database, the Kafka Connect component polls it on a Kafka queue (on topic **). We set as polling strategy *timestamp* on the dataset attribute *insertdate* (for more information see [here](https://docs.confluent.io/current/connect/kafka-connect-jdbc/source-connector/source_config_options.html)).
3. The Genero component enriches input data with other information and sends it on another Kafka queue (on topic *news_genero*);
4. Finally the Kafka Connect component sends data having topic *news_genero* in the Elastic database.

## Run Genero with Docker

The following commands run dockers with a mysql server with 200 data record, an ElasticSearch server, Kafka and Kafka connector
```bash
> $ cd ./genero_infrastructure_poc/docker
> $ chmod +x launch_demo.sh
> $ ./launch_demo.sh
```
For running the Genero component:
```bash
> cd ./genero_infrastructure_poc/src
> python -m ./consumers/news_analyzer
```

## Genero Interfaces
