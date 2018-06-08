FROM rabbitmq:3.7.4-management  
  
ENV ETCD_BIN_VERSION=2.2.1  
  
RUN apt-get update -y && \  
apt-get install -y wget curl s3cmd && \  
wget -qO -
https://github.com/coreos/etcd/releases/download/v${ETCD_BIN_VERSION}/etcd-v${ETCD_BIN_VERSION}-linux-
amd64.tar.gz | \  
tar -xzf - -C /tmp && \  
mv /tmp/etcd-v${ETCD_BIN_VERSION}-linux-amd64/etcd /usr/local/bin && \  
rm -fr /tmp/etcd-v${ETCD_BIN_VERSION}-linux-amd64* && \  
apt-get autoremove -y wget && \  
apt-get clean && \  
  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* && \  
rabbitmq-plugins enable --offline \  
rabbitmq_consistent_hash_exchange \  
rabbitmq_federation \  
rabbitmq_federation_management \  
rabbitmq_shovel \  
rabbitmq_shovel_management \  
rabbitmq_peer_discovery_etcd  
  
ADD rabbitmq-wrapper.sh /usr/local/bin/rabbitmq-wrapper.sh  

