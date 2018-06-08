FROM mustardgrain/base:latest  
  
MAINTAINER Kirk True <kirk@mustardgrain.com>  
  
CMD ["/sbin/my_init"]  
  
ENV REDIS_VERSION 2.8.19  
ENV REDIS_URL http://download.redis.io/releases/redis-$REDIS_VERSION.tar.gz  
ENV REDIS_HOME /opt/redis-$REDIS_VERSION  
  
RUN cd /opt && /usr/bin/curl -L -s $REDIS_URL | tar xz && \  
apt-get update && apt-get install -y \  
gcc \  
make && \  
cd $REDIS_HOME && \  
make  
  
COPY . /src  
  
RUN mkdir -p /etc/service/redis && cp /src/run /etc/service/redis  
  
WORKDIR $REDIS_HOME  
  
EXPOSE 6379  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  

