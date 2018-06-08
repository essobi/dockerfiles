# This is a Dockerfile to build a riak database image.  
FROM buildpack-deps:trusty-curl  
MAINTAINER Mengz <mz@dasudian.com>  
  
ENV DEBIAN_FRONTEND="noninteractive" \  
RIAK_VERSION="2.1.4-1"  
# Docker ENV can be used to set riak configuration  
# STORAGE_BACKEND="bitcask/leveldb"  
# NODE_HOST="ip or hostname"  
# RIAK_SEARCH="off/on"  
# Setup the repository for riak  
RUN curl -fsSL
https://packagecloud.io/install/repositories/basho/riak/script.deb.sh | sudo
bash  
  
RUN apt-get update && \  
apt-get install --no-install-recommends -y --force-yes supervisor default-jre
riak=$RIAK_VERSION && \  
mkdir -p /var/log/supervisor && \  
locale-gen en_US en_US.UTF-8 && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
RUN sed -ri "s|listener.http.internal = 127.0.0.1:8098|listener.http.internal
= 0.0.0.0:8098|" /etc/riak/riak.conf && \  
sed -ri "s|listener.protobuf.internal =
127.0.0.1:8087|listener.protobuf.internal = 0.0.0.0:8087|" /etc/riak/riak.conf  
  
COPY supervisord-riak.conf /etc/supervisor/conf.d/supervisord-riak.conf  
COPY docker-entrypoint.sh /entrypoint.sh  
  
EXPOSE 8087 8098  
VOLUME ["/var/lib/riak"]  
  
ENTRYPOINT ["/entrypoint.sh"]  
CMD ["supervisord"]  

