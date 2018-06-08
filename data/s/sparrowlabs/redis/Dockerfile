FROM ubuntu:12.04  
MAINTAINER Oliver Letterer <oliver.letterer@sparrow-labs.de>  
  
RUN apt-get update  
RUN apt-get upgrade -y  
  
RUN apt-get install -y wget make build-essential && apt-get clean  
# RUN groupadd -r redis && useradd -r -g redis redis  
ENV REDIS_VERSION 2.8.13  
RUN mkdir -p /usr/src/redis && \  
wget http://download.redis.io/releases/redis-$REDIS_VERSION.tar.gz && \  
tar -xzf redis-$REDIS_VERSION.tar.gz -C /usr/src/redis --strip-components=1 &&
\  
rm redis-$REDIS_VERSION.tar.gz && \  
make -C /usr/src/redis && \  
make -C /usr/src/redis install && \  
rm -r /usr/src/redis  
  
ADD redis.conf /etc/redis.conf  
RUN mkdir /data  
# RUN mkdir /data && chown redis:redis /data  
WORKDIR /data  
  
# USER redis  
EXPOSE 6379  
CMD [ "/usr/local/bin/redis-server", "/etc/redis.conf" ]  

