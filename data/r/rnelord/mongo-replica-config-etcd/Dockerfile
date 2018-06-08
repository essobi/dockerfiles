FROM mongo:3  
ENV NEXTRUN_WAIT_TIME 3  
ENV MONGO_MIN_NODES=3  
ENV ETCDCTL_VERSION=v2.2.0  
RUN curl -L
https://github.com/coreos/etcd/releases/download/$ETCDCTL_VERSION/etcd-$ETCDCTL_VERSION-
linux-amd64.tar.gz -o /tmp/etcd-$ETCDCTL_VERSION-linux-amd64.tar.gz \  
&& cd /tmp && tar xzvf etcd-$ETCDCTL_VERSION-linux-amd64.tar.gz \  
&& cd etcd-$ETCDCTL_VERSION-linux-amd64 \  
&& cp etcdctl /usr/local/bin \  
&& chmod +x /usr/local/bin \  
&& cd / && rm -rf /tmp/etcd-$ETCDCTL_VERSION/*  
  
COPY rs-config.sh /rs-config.sh  
COPY entrypoint.sh /entrypoint.sh  
RUN chmod +x /entrypoint.sh /rs-config.sh  
  
ENTRYPOINT ["/entrypoint.sh"]  

