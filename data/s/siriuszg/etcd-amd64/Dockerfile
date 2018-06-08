  
FROM alpine:latest  
  
ENV ETCD_VERSION 3.1.8  
RUN apk upgrade libssl1.0 --update-cache \  
&& apk add wget ca-certificates \  
&& wget -O etcd-v${ETCD_VERSION}-linux-amd64.tar.gz
https://github.com/coreos/etcd/releases/download/v${ETCD_VERSION}/etcd-v${ETCD_VERSION}-linux-
amd64.tar.gz \  
&& tar zxvf etcd-v${ETCD_VERSION}-linux-amd64.tar.gz \  
&& rm etcd-v${ETCD_VERSION}-linux-amd64.tar.gz \  
&& mv etcd-v${ETCD_VERSION}-linux-amd64/etcd* /usr/local/bin/ \  
&& rm -r etcd-v${ETCD_VERSION}-linux-amd64 \  
&& mkdir -p /var/etcd/ \  
&& mkdir -p /var/lib/etcd/  
  
WORKDIR /usr/local/bin/  
  
EXPOSE 2379 2380  
ENTRYPOINT ["etcd"]

