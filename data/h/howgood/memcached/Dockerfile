# howgood/memcached:latest  
FROM debian:jessie  
  
# Install build needs  
RUN apt-get update && \  
apt-get install -y \  
build-essential \  
libevent-dev \  
curl && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* && \  
apt-get autoremove -y  
  
# Download and install memcached  
RUN mkdir /tmp/memcached && \  
cd /tmp/memcached && \  
curl -SL "http://memcached.org/latest" | tar zx --strip-components=1 && \  
./configure && \  
make && \  
make install && \  
cd / && \  
rm -Rf /tmp/memcached*  
  
# The default memcached port  
EXPOSE 11211  
ENTRYPOINT ["/usr/local/bin/memcached"]  
CMD ["-u", "root", "-v"]  

