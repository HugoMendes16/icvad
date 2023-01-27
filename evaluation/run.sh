docker network create hugoslave

docker run --network=hugoslave --name planner -d planner

docker run --network=hugoslave -e ADRESS=http://worker -e PORT=8080 --name worker -d worker
docker run --network=hugoslave -e ADRESS=http://worker1 --name worker1 -e PORT=8081 -d worker
docker run --network=hugoslave -e ADRESS=http://worker2 --name worker2 -e PORT=8082 -d worker

