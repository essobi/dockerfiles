FROM alpine:latest  
MAINTAINER pangpanglab <pangpanglab@p2shop.cn>  
  
ENV ETCD_VERSION 3.1.3  
RUN apk add --update ca-certificates openssl tar \  
&& wget
https://github.com/coreos/etcd/releases/download/v${ETCD_VERSION}/etcd-v${ETCD_VERSION}-linux-
amd64.tar.gz \  
&& tar xzvf etcd-v${ETCD_VERSION}-linux-amd64.tar.gz \  
&& mv etcd-v${ETCD_VERSION}-linux-amd64/etcd* /bin/ \  
&& apk del --purge tar openssl \  
&& rm -Rf etcd-v${ETCD_VERSION}-linux-amd64* /var/cache/apk/*  
  
VOLUME /data  
EXPOSE 2379 2380 4001 7001  
ENTRYPOINT ["/bin/etcd"]

