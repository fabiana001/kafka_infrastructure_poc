#!/usr/bin/env bash

# create topics
printf "Create kafka topics for mysql connector\n\t"
docker-compose exec kafka kafka-topics --create --topic docker-connect-status --partitions 1 --replication-factor 1 --if-not-exists --zookeeper zookeeper:2181
docker-compose exec kafka kafka-topics --create --topic docker-connect-config --partitions 1 --replication-factor 1 --if-not-exists --zookeeper zookeeper:2181
docker-compose exec kafka kafka-topics --create --topic docker-connect-offsets --partitions 1 --replication-factor 1 --if-not-exists --zookeeper zookeeper:2181

# show topic list
#docker-compose exec kafka kafka-topics --list --zookeeper zookeeper:2181

# Register mysql connector
printf "\nCreate mysql connector\n\t"
curl -X POST -H "Content-Type: application/json" --data @quickstart-jdbc-source.json http://localhost:8083/connectors

# Setup mysql database
printf "\nCreate table Test and populate it\n\t"
#docker exec quickstart-mysql mysql -uconfluent -pconfluent -hquickstart-mysql < /dbscript/setup.sql
docker exec quickstart-mysql sh -c "mysql -uconfluent -pconfluent -hquickstart-mysql connect_test < /dbscript/setup.sql"
