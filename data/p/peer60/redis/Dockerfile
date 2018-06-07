FROM ubuntu:quantal  
MAINTAINER Jason Staten <jstaten@peer60.com>  
  
ADD sources.list /etc/apt/sources.list.d/peer60-redis.list  
RUN apt-get update \  
&& apt-get -y --force-yes install redis-server=2:2.8.2-1chl1~quantal1 \  
&& rm -rf /var/lib/apt/lists/* \  
&& apt-get clean  
ADD redis.conf /etc/redis/redis.conf  
  
USER redis  
  
EXPOSE 6379  
CMD /usr/bin/redis-server /etc/redis/redis.conf

