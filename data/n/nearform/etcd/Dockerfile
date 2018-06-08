FROM alpine:3.6  
LABEL name "Docker ETCD"  
LABEL version "1.0.0"  
LABEL maintainer "Alex Knol <alex.knol@nearform.com>"  
  
ARG ETCD_VERSION=3.2.11  
RUN mkdir /etcd && \  
chgrp -R 0 /etcd && \  
chmod -R g=u /etcd && \  
cd /etcd && \  
chmod u+s /bin/ping && \  
apk add --update ca-certificates openssl tar drill && \  
wget
https://github.com/coreos/etcd/releases/download/v${ETCD_VERSION}/etcd-v${ETCD_VERSION}-linux-
amd64.tar.gz && \  
tar xzvf etcd-v${ETCD_VERSION}-linux-amd64.tar.gz && \  
mv etcd-v${ETCD_VERSION}-linux-amd64/etcd* /bin/ && \  
apk del --purge tar openssl && \  
rm -Rf etcd-v${ETCD_VERSION}-linux-amd64* /var/cache/apk/*  
  
RUN chmod g=u /etc/passwd  
  
USER 1001  
VOLUME /data  
  
EXPOSE 2379 2380  

