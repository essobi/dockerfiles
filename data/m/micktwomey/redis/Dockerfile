FROM ubuntu:14.04  
MAINTAINER Michael Twomey, mick@twomeylee.name  
  
ENV REDIS_VERSION 2.8.11  
# && apt-get upgrade -y \  
RUN apt-get update \  
&& apt-get install -y \  
curl \  
gcc \  
make \  
&& apt-get autoremove \  
&& curl http://download.redis.io/releases/redis-${REDIS_VERSION}.tar.gz >
/usr/src/redis-${REDIS_VERSION}.tar.gz \  
&& tar -C /usr/src -zxf /usr/src/redis-${REDIS_VERSION}.tar.gz \  
&& cd /usr/src/redis-${REDIS_VERSION} \  
&& make \  
&& make install \  
&& apt-get purge -y \  
curl \  
gcc \  
make \  
&& apt-get autoremove -y \  
&& apt-get clean  
  
ADD redis.conf /etc/redis/redis.conf  
  
VOLUME /redis/logs  
VOLUME /redis/db  
  
EXPOSE 6379  
CMD ["/etc/redis/redis.conf"]  
  
ENTRYPOINT ["/usr/local/bin/redis-server"]  

