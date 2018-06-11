# Redis for Debian jessie  
#  
# URL: https://github.com/William-Yeh/docker-redis  
#  
# Reference: https://github.com/dockerfile/redis  
#  
# Version 0.4  
#  
# pull base image  
FROM debian:jessie  
MAINTAINER William Yeh <william.pjyeh@gmail.com>  
  
ENV VER 2.8.19  
ENV TARBALL http://download.redis.io/releases/redis-$VER.tar.gz  
  
  
RUN apt-get update && \  
\  
echo "==> Install curl and helper tools..." && \  
DEBIAN_FRONTEND=noninteractive apt-get install -y curl make gcc && \  
\  
\  
\  
echo "==> Download, compile, and install..." && \  
cd /tmp && \  
curl -L $TARBALL -o redis.tar.gz && \  
tar xvzf redis.tar.gz && \  
cd redis-$VER && \  
make && \  
make install && \  
\  
\  
echo "==> Copy default configuration..." && \  
cp -f src/redis-sentinel /usr/local/bin && \  
mkdir -p /etc/redis && \  
cp -f *.conf /etc/redis && \  
rm -rf /tmp/redis* && \  
\  
\  
echo "==> Configure for Dockerized version of Redis..." && \  
sed -i 's/^\\(bind .*\\)$/#\1/' /etc/redis/redis.conf && \  
sed -i 's/^\\(daemonize .*\\)$/#\1/' /etc/redis/redis.conf && \  
sed -i 's/^\\(logfile .*\\)$/#\1/' /etc/redis/redis.conf && \  
sed -i 's/^\\(dir .*\\)$/dir \/data/' /etc/redis/redis.conf && \  
\  
\  
echo "==> Clean up..." && \  
apt-get remove -y --auto-remove curl make gcc && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
# configure Redis  
VOLUME [ "/data", "/etc/redis" ]  
  
#sed -i 's/^\\(dir .*\\)$/dir \/var\/lib\/redis/' /etc/redis/redis.conf  
# Redis port.  
EXPOSE 6379  
# for convenience  
ENV PATH /opt:$PATH  
COPY usage.sh /opt/  
COPY start /opt/  
COPY client /opt/  
COPY benchmark /opt/  
RUN date '+%Y-%m-%dT%H:%M:%S%:z' > /var/log/DOCKER_BUILD_TIME  
  
# Define default command.  
CMD ["usage.sh"]  

