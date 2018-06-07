FROM alpine:3.3  
  
ENV VERSION_ETCD=2.3.3 \  
GOPATH=/tmp  
  
RUN apk \--update \--no-cache upgrade && \  
apk add \--update \--no-cache curl git && \  
apk add \--update \--no-cache \--repository
http://alpine.gliderlabs.com/alpine/edge/community go && \  
  
curl -sSL
https://github.com/coreos/etcd/releases/download/v${VERSION_ETCD}/etcd-v${VERSION_ETCD}-linux-
amd64.tar.gz \  
| tar xfz - -C /tmp && \  
  
mv /tmp/etcd-v${VERSION_ETCD}-linux-amd64/etcd /usr/bin/etcd && \  
  
go get -u -v -t github.com/tleyden/etcd-discovery/... && \  
mv $GOPATH/bin/* /usr/bin && \  
  
rm -rf /tmp/* && \  
apk del git go && \  
  
addgroup etcdisco && \  
adduser -D -g "" -s /bin/sh -G etcdisco etcdisco  
  
USER etcdisco  
WORKDIR /home/etcdisco  
  
CMD ash  

