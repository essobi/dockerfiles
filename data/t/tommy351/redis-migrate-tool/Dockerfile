FROM debian:jessie  
  
MAINTAINER Tommy Chen <tommy351@gmail.com>  
  
ENV BUILD_PACKAGES "build-essential git automake libtool autoconf bzip2"  
ENV RUNTIME_PACKAGES "ca-certificates"  
RUN apt-get update -y && \  
apt-get install -y --no-install-recommends --no-install-suggests
$BUILD_PACKAGES $RUNTIME_PACKAGES && \  
git clone https://github.com/vipshop/redis-migrate-tool.git && \  
cd redis-migrate-tool && \  
autoreconf -fvi && \  
./configure && \  
make && \  
cd .. && \  
mv redis-migrate-tool/src/redis-migrate-tool /usr/local/bin && \  
apt-get remove --purge -y $BUILD_PACKAGES && \  
apt-get autoremove -y && \  
rm -rf /var/lib/apt/lists/* redis-migrate-tool  
  
CMD ["redis-migrate-tool"]  

