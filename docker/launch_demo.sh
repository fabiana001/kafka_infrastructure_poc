cd ./mysql
docker-compose down
sleep 10
cd ../kafka
docker-compose down
sleep 10

docker-compose  up -d
sleep 10
cd ../mysql
docker-compose up -d
sleep 10

cd ../kafka
chmod +x ./setup.sh
./setup.sh

# Check all is up
sleep 10
# Check status mysql connector
printf "\nCheck status of mysql connector\n\t"
res=$(curl http://localhost:8083/connectors/quickstart-jdbc-source/status)
echo $res

printf "\nCheck mysql-connector topics are correctly created:\n\t"
res=$(curl "http://localhost:8082/topics/docker-connect-offsets")
printf "$res\n\t"
res=$(curl "http://localhost:8082/topics/docker-connect-config")
printf "$res\n\t"
res=$(curl "http://localhost:8082/topics/docker-connect-status")
printf "$res\n\t"

printf "\nPrint first 5 rows from mysql table:\n \t"
res=$(docker exec quickstart-mysql sh -c "mysql -uconfluent -pconfluent -hquickstart-mysql connect_test  -Bse 'select * from PRO_clip_repository limit 1;'")
echo $res
