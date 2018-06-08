# This is a Dockerfile to build a riakcs storage system image.  
FROM buildpack-deps:trusty-curl  
MAINTAINER Mengz <mz@dasudian.com>  
  
ENV DEBIAN_FRONTEND="noninteractive" \  
RIAK_VERSION="2.1.3-1" \  
RIAKCS_VERSION="2.1.1-1" \  
STANCHION_VERSION="2.1.1-1" \  
RIAK_CONFIG="/etc/riak/riak.conf" \  
RIAKCS_CONFIG="/etc/riak-cs/riak-cs.conf" \  
STANCHION_CONFIG="/etc/stanchion/stanchion.conf" \  
STANCHION_NODE="yes" \  
ADMIN_USER="admin" \  
ADMIN_EMAIL="admin@maildomain.com"  
# Docker control environment  
# NODE_HOST="127.0.0.1" for cluster deployment  
# ROOT_HOST="s3.amazonaws.com"  
# ADMIN_KEY=""  
# ADMIN_SECRET=""  
# PRIMARY_NOTE_HOST  
# Setup the repositories  
RUN curl -fsSL
https://packagecloud.io/install/repositories/basho/riak/script.deb.sh | sudo
bash && \  
curl -s
https://packagecloud.io/install/repositories/basho/stanchion/script.deb.sh |
sudo bash && \  
curl -s https://packagecloud.io/install/repositories/basho/riak-
cs/script.deb.sh | sudo bash  
  
RUN apt-get update && \  
apt-get install --no-install-recommends -y --force-yes supervisor
riak=$RIAK_VERSION stanchion=$STANCHION_VERSION riak-cs=$RIAKCS_VERSION && \  
mkdir -p /var/log/supervisor && \  
locale-gen en_US en_US.UTF-8 && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
RUN sed -ri "s|^listener.http.internal = .*|listener.http.internal =
0.0.0.0:8098|" $RIAK_CONFIG && \  
sed -ri "s|^listener.protobuf.internal = .*|listener.protobuf.internal =
0.0.0.0:8087|" $RIAK_CONFIG && \  
sed -ri "s|^listener = .*|listener = 0.0.0.0:8085|" $STANCHION_CONFIG && \  
sed -ri "s|^listener = .*|listener = 0.0.0.0:8080|" $RIAKCS_CONFIG && \  
sed -ri "s|^distributed_cookie = .*|distributed_cookie = riak-cs|"
$RIAK_CONFIG && \  
sed -ri "s|^distributed_cookie = .*|distributed_cookie = riak-cs|"
$RIAKCS_CONFIG && \  
sed -ri "s|^distributed_cookie = .*|distributed_cookie = riak-cs|"
$STANCHION_CONFIG && \  
sed -ri "s|^storage_backend = .*|buckets.default.allow_mult = true|"
$RIAK_CONFIG && \  
sed -ri "s|^admin.key = .*|admin.key = admin-key\nadmin.secret = admin-
secret|" $RIAKCS_CONFIG && \  
sed -ri "s|^admin.key = .*|admin.key = admin-key\nadmin.secret = admin-
secret|" $STANCHION_CONFIG  
  
COPY riak-advanced.config /etc/riak/advanced.config  
COPY supervisord-init.conf /etc/supervisor/conf.d/  
COPY supervisord-riakcs.conf /etc/supervisor/conf.d/  
COPY supervisord-riak.conf /etc/supervisor/conf.d/  
COPY supervisord-stanchion.conf /etc/supervisor/conf.d/  
COPY docker-entrypoint.sh /entrypoint  
COPY init-riakcs.sh /init-riakcs  
  
EXPOSE 8098 8080  
VOLUME ["/var/lib/riak"]  
  
ENTRYPOINT ["/entrypoint"]  
CMD ["supervisord"]  

