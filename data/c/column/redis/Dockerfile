FROM column/base:v1  
  
MAINTAINER Column Fang <column.fang@gmail.com>  
  
COPY files /  
  
RUN \  
# Install build tools & openresty dependencies  
apt-get update && \  
apt-get install -y build-essential && \  
  
# Download redis souce  
curl -L http://download.redis.io/releases/redis-3.2.8.tar.gz >
/tmp/redis.tar.gz && \  
tar xzvf /tmp/redis.tar.gz -C /tmp && \  
  
# Install redis  
cd /tmp/redis*/ && \  
make && \  
make install && \  
mkdir -p /usr/local/etc/redis && \  
cp redis.conf sentinel.conf /usr/local/etc/redis && \  
  
# Cleanup  
apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
EXPOSE 6379  

