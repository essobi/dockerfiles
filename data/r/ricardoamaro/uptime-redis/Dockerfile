FROM ricardoamaro/uptime-base:latest  
  
MAINTAINER Ricardo Amaro <ricardo.amaro_at_acquia.com>  
ENV DEBIAN_FRONTEND noninteractive  
  
# Install Redis.  
RUN \  
cd /tmp && \  
wget http://download.redis.io/redis-stable.tar.gz && \  
tar xvzf redis-stable.tar.gz && \  
cd redis-stable && \  
make && \  
make install && \  
cp -f src/redis-sentinel /usr/local/bin && \  
mkdir -p /etc/redis && \  
cp -f *.conf /etc/redis && \  
rm -rf /tmp/redis-stable* && \  
sed -i 's/^\\(bind .*\\)$/# \1/' /etc/redis/redis.conf && \  
sed -i 's/^\\(daemonize .*\\)$/# \1/' /etc/redis/redis.conf && \  
sed -i 's/^\\(dir .*\\)$/# \1\ndir \/data/' /etc/redis/redis.conf && \  
sed -i 's/^\\(logfile .*\\)$/# \1/' /etc/redis/redis.conf  
  
VOLUME ["/data"]  
WORKDIR /data  
CMD ["redis-server", "/etc/redis/redis.conf"]  
EXPOSE 6379  

