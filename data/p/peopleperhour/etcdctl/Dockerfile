FROM gliderlabs/alpine:3.1  
MAINTAINER Panagiotis Moustafellos <pmoust@peopleperhour.com>  
  
ENV VERSION 2.0.13  
ENV ETCD_ENDPOINT 127.0.0.1:4001  
RUN apk-install curl && \  
curl -LOks
https://github.com/coreos/etcd/releases/download/v${VERSION}/etcd-v${VERSION}-linux-
amd64.tar.gz && \  
tar zxvf etcd-v${VERSION}-linux-amd64.tar.gz && \  
cp etcd-v${VERSION}-linux-amd64/etcdctl /etcdctl && \  
rm -rf etcd-v* && \  
chmod +x /etcdctl  
  
ENTRYPOINT ["/etcdctl"]  

