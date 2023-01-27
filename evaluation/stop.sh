#docker stop worker worker1 worker2 worker2 worker2 worker2 worker2 planner
#docker rm worker worker1 worker2 planner
for i in {1..30}; do docker stop worker$i ; done
docker stop planner
for i in {1..30}; do docker rm worker$i ; done
docker rm planner
docker network rm hugoslave