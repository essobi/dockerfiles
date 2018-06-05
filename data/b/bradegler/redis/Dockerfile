FROM bradegler/base-ubuntu  
MAINTAINER Brad Egler "begler@gmail.com"  
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
sed -i 's/^\\(bind .*\\)$/# \1/' /etc/redis/redis.conf && \  
sed -i 's/^\\(daemonize .*\\)$/# \1/' /etc/redis/redis.conf && \  
sed -i 's/^\\(dir .*\\)$/# \1\ndir \/data/' /etc/redis/redis.conf && \  
sed -i 's/^\\(logfile .*\\)$/# \1/' /etc/redis/redis.conf && \  
sed -i 's/appendonly no/appendonly yes/' /etc/redis/redis.conf  
  
# rm -rf /tmp/redis-stable* && \  
RUN echo "[program:redis]" > /etc/supervisor/conf.d/redis.conf && \  
echo "command = redis-server /etc/redis/redis.conf" >>
/etc/supervisor/conf.d/redis.conf && \  
echo "user = root" >> /etc/supervisor/conf.d/redis.conf && \  
echo "autostart = true" >> /etc/supervisor/conf.d/redis.conf  
  
# Define mountable directories.  
VOLUME ["/data"]  
  
# Define working directory.  
WORKDIR /data  
  
# Expose ports.  
EXPOSE 6379  
# Define default command.  
CMD ["/usr/bin/supervisord"]  

