FROM oberthur/docker-ubuntu:16.04  
MAINTAINER Tomasz Arendt <tomasz.arendt@idemia.com>  
  
ENV _ETCD_VERSION=v3.2.8  
RUN curl -LO
https://github.com/coreos/etcd/releases/download/$_ETCD_VERSION/etcd-$_ETCD_VERSION-
linux-amd64.tar.gz && \  
tar xzvf etcd-$_ETCD_VERSION-linux-amd64.tar.gz && \  
mv etcd-$_ETCD_VERSION-linux-amd64/etcd* /bin/ && \  
rm -Rf etcd-$_ETCD_VERSION-linux-amd64*  
  
CMD ["/bin/etcd"]  

