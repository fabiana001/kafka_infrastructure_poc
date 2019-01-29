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
