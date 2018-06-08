FROM pierophp/base:ubuntu_16_04  
MAINTAINER "Piero Giusti <pierophp@gmail.com>"  
# Base  
RUN apt-get update && \  
apt-get install -y build-essential tcl && \  
apt-get clean && rm -rf /var/lib/apt/lists/*  
# Redis  
RUN cd /tmp && \  
curl -O http://download.redis.io/redis-stable.tar.gz && \  
tar xzvf redis-stable.tar.gz && \  
cd redis-stable && \  
make && \  
make install && \  
mkdir /etc/redis  
  
# Redis User  
RUN adduser --system --group --no-create-home redis && \  
mkdir /var/lib/redis && \  
chown redis:redis /var/lib/redis && \  
chmod 770 /var/lib/redis  
# Supervisor  
RUN apt-get update && \  
apt-get install -y supervisor && \  
apt-get clean && rm -rf /var/lib/apt/lists/*  
  
ADD supervisor/redis.conf /etc/supervisor/conf.d/redis.conf  
ADD redis/redis.conf /etc/redis/redis.conf  
  
EXPOSE 6379  
  
CMD ["/usr/bin/supervisord", "--nodaemon", "-c",
"/etc/supervisor/supervisord.conf"]  

