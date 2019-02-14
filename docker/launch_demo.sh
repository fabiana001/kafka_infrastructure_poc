cd ./dbs
docker-compose down
sleep 10
cd ../kafka
docker-compose down
sleep 10

docker-compose  up -d
sleep 10
cd ../dbs
docker-compose up -d
sleep 10

cd ../kafka
chmod +x ./setup.sh
./setup.sh

# Check all is up
sleep 10
# Check status db connector
printf "\nCheck status of mysql connector\n\t"
res=$(curl http://localhost:8083/connectors/quickstart-timestamp-jdbc-source/status)
echo $res
#printf "\nCheck status of elastic connector\n\t"
#res=$(curl http://localhost:8083/connectors/quickstart-elasticsearch-sink/status)
#echo $res

printf "\nCheck mysql-connector topics are correctly created:\n\t"
res=$(curl "http://localhost:8082/topics/docker-connect-offsets")
printf "$res\n\t"
res=$(curl "http://localhost:8082/topics/docker-connect-config")
printf "$res\n\t"
res=$(curl "http://localhost:8082/topics/docker-connect-status")
printf "$res\n\t"

printf "\nPrint first 1 row from mysql table:\n \t"
res=$(docker exec quickstart-mysql sh -c "mysql -uconfluent -pconfluent -hquickstart-mysql connect_test  -Bse 'select * from PRO_clip_repository limit 1;'")
echo $res

printf "\n Print elastic news"
res=$(curl -XGET 'http://localhost:9200/genero_news/_search?pretty')
echo $res
