FROM turbulent/heap-base:3.0.0  
MAINTAINER Benoit Beausejour <b@turbulent.ca>  
  
ENV heap-redis 3.0.0  
# Install packages  
ENV DEBIAN_FRONTEND noninteractive  
RUN add-apt-repository ppa:chris-lea/redis-server  
RUN apt-get update && \  
apt-get -y install redis-server=3:3.2.9-2chl1~xenial1 && \  
rm -rf /var/lib/apt/lists/*  
  
ADD redis.conf.tmpl /systpl/  
ADD run-redis.sh /run-redis.sh  
ADD make-backup.sh.tmpl /systpl/  
  
ENV VAR_REDIS_DATABASES=16 \  
VAR_REDIS_DBFILENAME="dump.rdb" \  
VAR_REDIS_AOF="no" \  
VAR_REDIS_AOF_FILENAME="appendonly.aof" \  
VAR_REDIS_TCP_KEEPALIVE="60"  
RUN mkdir -p /vol/logs && chown heap:root /vol/logs  
RUN mkdir -p /vol/database && chown heap:root /vol/database  
VOLUME ["/vol/logs", "/vol/database"]  
  
CMD ["/run-redis.sh"]  

