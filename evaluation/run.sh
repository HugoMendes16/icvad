docker network create hugoslave


#docker run --network=hugoslave -e ADRESS=http://worker --name worker -d worker
#docker run --network=hugoslave -e ADRESS=http://worker1 --name worker1 -d worker
#docker run --network=hugoslave -e ADRESS=http://worker2 --name worker2 -d worker
#sleep 1
docker run --network=hugoslave --name planner -d planner

for i in {1..10}; do docker run  --network=hugoslave -e MULT=true -e ADD=true -e PLANNER=http://planner:3000 -e ADDRESS=http://worker$i --name worker$i -d worker; done

for i in {11..20}; do docker run  --network=hugoslave -e MULT=true -e ADD=false -e PLANNER=http://planner:3000 -e ADDRESS=http://worker$i --name worker$i -d worker; done

for i in {21..30}; do docker run  --network=hugoslave -e MULT=false -e ADD=true -e PLANNER=http://planner:3000 -e ADDRESS=http://worker$i --name worker$i -d worker; done