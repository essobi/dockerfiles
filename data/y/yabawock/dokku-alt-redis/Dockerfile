FROM phusion/baseimage:0.9.17  
MAINTAINER Morton Jonuschat <m.jonuschat@mojocode.de>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
# Install dependencies  
RUN apt-get update && \  
apt-get dist-upgrade -y && \  
apt-get -qy --no-install-recommends --fix-missing --force-yes install wget
strace lsof netcat build-essential && \  
update-locale LANG=en_US.UTF-8 LANGUAGE=en_US.UTF-8 LC_ALL=en_US.UTF-8 && \  
cd /tmp && \  
wget http://download.redis.io/releases/redis-3.0.4.tar.gz && \  
tar xvzf redis-3.0.4.tar.gz && \  
cd redis-3.0.4 && \  
make && make install && \  
mkdir -p /etc/redis /var/lib/redis && \  
rm -rf /tmp/redis-3.0.4* && \  
apt-get remove build-essential -y && \  
apt-get clean && \  
apt-get autoremove -y  
  
# Disable SSH  
RUN rm -rf /etc/service/sshd /etc/my_init.d/00_regen_ssh_host_keys.sh  
  
# Service: redis-server  
RUN mkdir -p /etc/service/redis-server/log/main  
ADD configs/redis.conf /etc/redis/redis.conf  
ADD runit/redis-server /etc/service/redis-server/run  
ADD runit/log /etc/service/redis-server/log/run  

