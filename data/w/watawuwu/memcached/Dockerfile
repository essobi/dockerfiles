FROM watawuwu/debian:jessie  
  
RUN groupadd -r memcache && useradd -r -g memcache memcache  
  
ENV MEMCACHED_VERSION 1.4.21-1.1  
RUN apt-get update && \  
apt-get install -y memcached=${MEMCACHED_VERSION} \--no-install-recommends &&
\  
rm /etc/memcached.conf && \  
rm /etc/init.d/memcached && \  
mkdir -p /var/log/memcached && \  
chown memcache:memcache /var/log/memcached && \  
rm -rf /var/lib/apt/lists/*  
  
ADD launch.sh /usr/local/bin/launch.sh  
  
EXPOSE 11211  
ADD memcached /etc/memcached  
ADD init.d/memcached /etc/init.d/memcached  
ADD launch.sh /usr/local/bin/launch.sh  
  
CMD ["/usr/local/bin/launch.sh"]  

