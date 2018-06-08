FROM secondriver/base-os:v1.0  
MAINTAINER secondriver <secondriver@yeah.net>  
  
RUN echo 'Redis 3.x version' && \  
cd /tmp && \  
wget http://download.redis.io/releases/redis-3.0.3.tar.gz && \  
tar xvzf redis-3.0.3.tar.gz && \  
cd redis-3.0.3 && \  
make && \  
cp -f src/redis-sentinel /usr/local/bin && \  
cp -f src/redis-server /usr/local/bin && \  
cp -f src/redis-cli /usr/local/bin && \  
cp -f src/redis-check-dump /usr/local/bin && \  
cp -f src/redis-check-aof /usr/local/bin && \  
cp -f src/redis-benchmark /usr/local/bin && \  
mkdir -p /etc/redis && \  
cp -f *.conf /etc/redis && \  
rm -rf /tmp/redis-3.0.3 && \  
sed -i 's/^\\(bind .*\\)$/# \1/' /etc/redis/redis.conf && \  
sed -i 's/^\\(daemonize .*\\)$/# \1/' /etc/redis/redis.conf && \  
sed -i 's/^\\(dir .*\\)$/# \1\ndir \/data/' /etc/redis/redis.conf && \  
sed -i 's/^\\(logfile .*\\)$/# \1/' /etc/redis/redis.conf  
  
ENV REDIS_DATA /data  
  
VOLUME ${REDIS_DATA}  
  
WORKDIR ${REDIS_DATA}  
  
EXPOSE 6379  
CMD ["redis-server", "/etc/redis/redis.conf"]

