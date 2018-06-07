# Build:  
# docker build -t learnshiva/redis:latest .  
#  
# Create:  
# docker create -it -p 6379:6379 --name container-redis learnshiva/redis  
#  
# Start:  
# docker start container-redis  
#  
# Connect with redis client  
# docker exec -it container-redis redis-cli  
#  
# Connect bash  
# docker exec -it container-redis bash  
  
FROM ubuntu:latest  
MAINTAINER Siva <learn.shiva@gmail.com>  
RUN apt-get update && apt-get install -y redis-server  
EXPOSE 6379  
ENTRYPOINT ["/usr/bin/redis-server"]  

