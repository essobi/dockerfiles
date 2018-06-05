# Spoke Dockerfile for etcd  
FROM radial/spoke-base:latest  
MAINTAINER Brian Clements <radial@brianclements.net>  
  
# Install packages  
ENV DEBIAN_FRONTEND noninteractive  
RUN apt-get -q update && apt-get -qyV install \  
curl &&\  
apt-get clean  
  
ENV VERSION v0.4.6  
WORKDIR /opt  
RUN curl -L
https://github.com/coreos/etcd/releases/download/$VERSION/etcd-$VERSION-linux-
amd64.tar.gz \  
-o etcd-$VERSION-linux-amd64.tar.gz  
RUN tar xzvf etcd-$VERSION-linux-amd64.tar.gz  
RUN ln -s /opt/etcd-$VERSION-linux-amd64/etcd /usr/local/bin/etcd &&\  
ln -s /opt/etcd-$VERSION-linux-amd64/etcdctl /usr/local/bin/etcdctl  
  
# Configure Spoke behavior  
ENV SPOKE_NAME etcd  
ENV SPOKE_CMD etcdctl  
  
COPY /entrypoint.sh /entrypoint.sh  
  
EXPOSE 4001 7001  

