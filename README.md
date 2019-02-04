# Genero Stack Docker Compose
This project runs an example of a simple news pipeline. Data are initially stored on mysql and after the pipeline enriched data are store on ElasticSearch.

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

## Run all services
The following script run all required docker containers.

```bash
> chmod +x launch_demo.sh
> ./launch_demo.sh
```
Moreover it create a Kafka MYSQL connector which put data from Mysql to Kafka. Configurations are defined in the file _./docker/kafka/quickstart-jdbc-source.json_.


## Load news
### Dump few news from a remote database
``` bash
> mysqldump --single-transaction --column-statistics=0 --user=$user --password=$password --host=$mysql_hostname $mysql_database --tables $mysql_table --where="language IN ('IT', 'it-IT') and pubDate = '2019-01-15';" > dump_2019_01_15.sql
```

### Load news on the local mysql instance

```bash
> docker exec quickstart-mysql sh -c "mysql -uconfluent -pconfluent connect_test < /dbscript/dump_2019_01_15.sql"
```

## Show news
```bash
> docker exec schema-registry kafka-avro-console-consumer --bootstrap-server kafka:9092 --topic quickstart-jdbc-PRO_clip_repository --from-beginning --max-messages 10
```

## Refereneces
[1][kafka-stack-docker-compos](https://github.com/simplesteph/kafka-stack-docker-compose)
