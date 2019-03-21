#!/usr/bin/env bash

# create topics
printf "Create kafka topics for mysql connector\n\t"
docker-compose exec kafka kafka-topics --create --topic docker-connect-status --partitions 1 --replication-factor 1 --if-not-exists --zookeeper zookeeper:2181
docker-compose exec kafka kafka-topics --create --topic docker-connect-config --partitions 1 --replication-factor 1 --if-not-exists --zookeeper zookeeper:2181
docker-compose exec kafka kafka-topics --create --topic docker-connect-offsets --partitions 1 --replication-factor 1 --if-not-exists --zookeeper zookeeper:2181

# show topic list
#docker-compose exec kafka kafka-topics --list --zookeeper zookeeper:2181

sleep 180
# Register mysql connector
printf "\nCreate mysql connector\n\t"
res=$(curl -X POST -H "Content-Type: application/json" --data @quickstart-timestamp-jdbc-source.json http://localhost:8083/connectors)
echo $res
sleep 10
printf "\nCreate elastic connector\n\t"
res=$(curl -X POST -H "Content-Type: application/json" --data @quickstart-elastic-sink.json http://localhost:8083/connectors)
echo $res


# Setup mysql database
printf "\nCreate table PRO_clip_repository and populate it with few news\n\t"
docker exec quickstart-mysql sh -c "mysql -uconfluent -pconfluent connect_test < /dbscript/dump_2019_01_15.sql"
