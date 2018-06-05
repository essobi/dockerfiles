FROM cassandra:3  
ENV ETCD_VERSION v3.1.6  
RUN DOWNLOAD_URL=https://github.com/coreos/etcd/releases/download \  
&& apt-get update && apt-get install -y curl && rm -rf /var/lib/apt/lists/* \  
&& curl -L ${DOWNLOAD_URL}/${ETCD_VERSION}/etcd-${ETCD_VERSION}-linux-
amd64.tar.gz -o /tmp/etcd-${ETCD_VERSION}-linux-amd64.tar.gz \  
&& mkdir -p /tmp/etcd-${ETCD_VERSION} \  
&& tar xzvf /tmp/etcd-${ETCD_VERSION}-linux-amd64.tar.gz -C
/tmp/etcd-${ETCD_VERSION} \--strip-components=1 \  
&& cp /tmp/etcd-${ETCD_VERSION}/etcdctl /bin \  
&& rm -rf /tmp/etcd-${ETCD_VERSION}  
  
COPY cassandra-env.sh /etc/cassandra/cassandra-env.sh  
COPY docker-entrypoint.sh /arhea/docker-entrypoint.sh  
  
RUN chmod +x /arhea/docker-entrypoint.sh  
  
ENTRYPOINT ["/arhea/docker-entrypoint.sh"]  
  
CMD ["cassandra", "-f"]  

