docker network create hugoslave


docker run --network=hugoslave -e ADRESS=http://worker --name worker -d worker
docker run --network=hugoslave -e ADRESS=http://worker1 --name worker1 -d worker
docker run --network=hugoslave -e ADRESS=http://worker2 --name worker2 -d worker
sleep(1)
docker run --network=hugoslave --name planner -d planner
