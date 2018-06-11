FROM alpine  
MAINTAINER Walker Lee <walkerlee.tw@gmail.com>  
  
ARG ETCD_VER=3.0.7  
RUN apk -U --no-cache add ca-certificates && \  
apk --no-cache add openssl && \  
wget -qO-
https://github.com/coreos/etcd/releases/download/v$ETCD_VER/etcd-v$ETCD_VER-
linux-amd64.tar.gz | tar zxf - -C /tmp && \  
mv /tmp/etcd-v$ETCD_VER-linux-amd64/etcd /usr/local/bin && \  
apk del --purge openssl && \  
rm -rf /tmp/etcd-v$ETCD_VER* /var/cache/apk/*  
  
EXPOSE 2379 2380 4001 7001  
ENTRYPOINT ["/usr/local/bin/etcd"]  

