FROM alpine:latest  
  
LABEL name "Docker ETCD"  
LABEL version "1.0.0"  
LABEL maintainer "Lee Keitel <lfkeitel@usi.edu>"  
  
ARG ETCD_VERSION=3.1.0  
RUN apk add --update ca-certificates openssl tar drill && \  
wget
https://github.com/coreos/etcd/releases/download/v${ETCD_VERSION}/etcd-v${ETCD_VERSION}-linux-
amd64.tar.gz && \  
tar xzvf etcd-v${ETCD_VERSION}-linux-amd64.tar.gz && \  
mv etcd-v${ETCD_VERSION}-linux-amd64/etcd* /bin/ && \  
apk del --purge tar openssl && \  
rm -Rf etcd-v${ETCD_VERSION}-linux-amd64* /var/cache/apk/*  
  
ADD run.sh /bin/run.sh  
  
VOLUME /data  
  
EXPOSE 2379 2380  
ENTRYPOINT ["/bin/run.sh"]  

