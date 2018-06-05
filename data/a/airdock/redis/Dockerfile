# VERSION 1.0  
# AUTHOR: Jerome Guibert <jguibert@gmail.com>  
# DESCRIPTION: Redis Dockerfile  
# TO_BUILD: docker build --rm -t airdock/redis .  
# SOURCE: https://github.com/airdock-io/docker-redis  
# Pull base image.  
FROM airdock/base:jessie  
  
MAINTAINER Jerome Guibert <jguibert@gmail.com>  
  
ENV REDIS_VERSION 3.2.6  
# Install redis server from redis.io  
RUN apt-get update && apt-get install -y gcc make g++ build-essential
libc6-dev tcl git && \  
cd /tmp && mkdir -p /etc/redis /var/log/redis /var/lib/redis && \  
git clone https://github.com/antirez/redis.git && cd redis && \  
make && \  
make install && \  
cp redis.conf /etc/redis && \  
sed -i 's/^dir .*$/dir \/var\/lib\/redis/g' /etc/redis/redis.conf && \  
chown -R redis:redis /etc/redis /var/log/redis /var/lib/redis && \  
cd /tmp && \  
git clone https://github.com/antirez/neural-redis.git && cd neural-redis && \  
make generic && mkdir -p /usr/lib/neuralredis && cp neuralredis.so
/usr/lib/neuralredis && \  
echo "loadmodule /usr/lib/neuralredis/neuralredis.so" >> /etc/redis/redis.conf
&& \  
cd /root && \  
apt-get remove -y gcc make g++ build-essential libc6-dev tcl git && \  
apt-get autoremove -y && \  
/root/post-install  
  
# Data Folder  
VOLUME ["/var/lib/redis", "/var/log/redis"]  
  
# Expose ports.  
EXPOSE 6379  
# Define default command.  
CMD ["tini", "-g", "--", "gosu", "redis:redis", "/usr/local/bin/redis-server",
"/etc/redis/redis.conf"]  

