FROM markusma/supervisord:ubuntu-trusty  
MAINTAINER Markus Mattinen <markus@gamma.fi>  
  
ENV DOCKERFILE_ETCD_VERSION 3.0.7  
RUN cd /tmp \  
&& curl -LO
https://github.com/coreos/etcd/releases/download/v$DOCKERFILE_ETCD_VERSION/etcd-v$DOCKERFILE_ETCD_VERSION-
linux-amd64.tar.gz \  
&& tar zxf etcd-v$DOCKERFILE_ETCD_VERSION-linux-amd64.tar.gz \  
&& cd etcd-v$DOCKERFILE_ETCD_VERSION-linux-amd64 \  
&& mv etcd etcdctl /usr/local/bin/ \  
&& cd / \  
&& rm -rf /tmp/etcd-v$DOCKERFILE_ETCD_VERSION-linux-amd64.tar.gz
/tmp/etcd-v$DOCKERFILE_ETCD_VERSION-linux-amd64  
  
ADD config/init /init  
ADD config/etc/supervisor/conf.d/etcd.conf /etc/supervisor/conf.d/etcd.conf  
  
EXPOSE 2379 2380 4001  
CMD ["/init"]  

