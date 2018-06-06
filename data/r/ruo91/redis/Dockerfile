#  
# Dockerfile - Redis  
#  
FROM ubuntu:14.04  
MAINTAINER Yongbok Kim <ruo91@yongbok.net>  
  
# Last Package Update & Install  
RUN apt-get update ; apt-get install -y curl build-essential supervisor  
  
# Redis  
ENV SRC_DIR /opt  
ENV REDIS_VERSION stable  
RUN cd $SRC_DIR && curl -LO
http://download.redis.io/releases/redis-$REDIS_VERSION.tar.gz \  
&& tar xzf redis-$REDIS_VERSION.tar.gz && mv redis-$REDIS_VERSION redis && cd
redis && make \  
&& ln -s $SRC_DIR/redis/src/redis-cli /usr/sbin/redis-cli \  
&& ln -s $SRC_DIR/redis/src/redis-server /usr/sbin/redis-server \  
&& rm -f $SRC_DIR/redis-$REDIS_VERSION.tar.gz  
  
# Add in the /etc/redis directory  
RUN mkdir /etc/redis  
ADD conf/redis.conf /etc/redis/redis.conf  
  
# Unset ENV  
RUN unset SRC_DIR REDIS_VERSION  
  
# Sysctl  
RUN echo 'vm.overcommit_memory = 1' >> /etc/sysctl.conf  
  
# Supervisor  
RUN mkdir -p /var/log/supervisor  
ADD conf/supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
  
# Port  
EXPOSE 6379  
# Daemon  
CMD ["/usr/bin/supervisord"]  

