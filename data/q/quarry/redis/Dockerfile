FROM ubuntu:12.04  
  
# Update package repository  
RUN echo "deb http://archive.ubuntu.com/ubuntu precise main universe
multiverse" > /etc/apt/sources.list  
RUN apt-get update  
RUN apt-get upgrade -y  
  
RUN apt-get install -y python-software-properties  
  
# Init latest redis-server  
RUN add-apt-repository -y ppa:chris-lea/redis-server  
RUN apt-get update  
RUN apt-get install -y redis-server  
  
# we create this for the redis data so it is commong across services  
RUN mkdir -p /data/db  
  
ADD ./redis.conf /etc/redis.conf  
  
ENTRYPOINT ["/usr/bin/redis-server", "/etc/redis.conf"]

