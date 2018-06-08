FROM alpine:3.5  
ARG VERSION  
ENV VERSION=3.1.1  
RUN apk update && apk add ca-certificates wget && update-ca-certificates \  
&& wget
https://github.com/coreos/etcd/releases/download/v${VERSION}/etcd-v${VERSION}-linux-
amd64.tar.gz \  
&& tar zxvf etcd*.tar.gz \  
&& mv etcd-v${VERSION}-linux-amd64/etcd /usr/bin \  
&& mv etcd-v${VERSION}-linux-amd64/etcdctl /usr/bin \  
&& rm -r etcd*  
  
EXPOSE 2379 2380  
ENTRYPOINT ["/usr/bin/etcd"]  

