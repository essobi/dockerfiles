From centos:7  
# Install make & gcc for building redis  
RUN yum update -y && yum install -y gcc make && yum clean all  
  
# Install Redis  
RUN cd /tmp && \  
curl -O http://download.redis.io/releases/redis-3.0.6.tar.gz && \  
tar zxfv redis-3.0.6.tar.gz && \  
cd redis-3.0.6 && \  
make && \  
make install && \  
mkdir -p /etc/redis /data/redis && \  
cp -f redis.conf /etc/redis && \  
rm -rf /tmp/redis*  
  
EXPOSE 6379  
CMD ["redis-server", "/etc/redis/redis.conf"]

