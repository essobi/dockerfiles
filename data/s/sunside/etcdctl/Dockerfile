FROM gliderlabs/alpine:3.2  
MAINTAINER Markus Mayer <awesome@wundercart.de>  
# Panagiotis Moustafellos <pmoust@peopleperhour.com>  
ENV VERSION 2.2.1  
ENV ETCDCTL_ENDPOINT 172.17.42.1:2379  
RUN apk-install curl && \  
curl -LOks
https://github.com/coreos/etcd/releases/download/v${VERSION}/etcd-v${VERSION}-linux-
amd64.tar.gz && \  
tar zxvf etcd-v${VERSION}-linux-amd64.tar.gz && \  
cp etcd-v${VERSION}-linux-amd64/etcdctl /usr/bin/etcdctl && \  
rm -rf etcd-v* && \  
chmod +x /usr/bin/etcdctl  
  

