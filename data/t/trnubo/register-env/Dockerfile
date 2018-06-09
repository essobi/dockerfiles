FROM alpine:latest  
  
MAINTAINER Tim Robinson <tim@panubo.com>  
  
ENV ETCD_VERSION 2.0.11  
RUN apk update && \  
apk add wget tar ca-certificates && \  
wget -q -O -
https://github.com/coreos/etcd/releases/download/v${ETCD_VERSION}/etcd-v${ETCD_VERSION}-linux-
amd64.tar.gz | tar -C /usr/local/bin --strip-components 1 -zxf -
etcd-v${ETCD_VERSION}-linux-amd64/etcdctl  
  
COPY run.sh run.sh  
  
CMD ["/run.sh"]  

