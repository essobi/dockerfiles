FROM ubuntu:16.04  
ENV DEBIAN_FRONTEND noninteractive  
ENV TERM xterm  
  
# Add repository PPA php 7.1  
RUN apt-get update && \  
apt-get install -y software-properties-common && \  
apt-get install -y build-essential make  
  
RUN DEBIAN_FRONTEND=noninteractive \  
apt-get update && \  
apt-get install -y language-pack-en-base &&\  
export LC_ALL=en_US.UTF-8 && \  
export LANG=en_US.UTF-8  
  
RUN DEBIAN_FRONTEND=noninteractive LC_ALL=en_US.UTF-8 add-apt-repository
ppa:ondrej/php  
  
# Update the package repository and Install base packages  
RUN apt-get update && apt-get upgrade --yes && \  
apt-get install --yes nano wget curl git  
  
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
sed -i 's/^\\(logfile .*\\)$/# \1/' /etc/redis/redis.conf && \  
sed -i -e "s/protected-mode yes/protected-mode no/g" /etc/redis/redis.conf  
  
# Define mountable directories.  
VOLUME ["/data"]  
  
# Define working directory.  
WORKDIR /data  
  
# Define default command.  
CMD ["redis-server", "/etc/redis/redis.conf"]  
  
# Expose ports.  
EXPOSE 6379

