FROM debian:jessie  
MAINTAINER Andrea Usuelli (andreausu@gmail.com)  
  
ADD . /usr/src/app  
  
RUN apt-get update && apt-get -y install curl && \  
curl -L -O
https://github.com/coreos/etcd/releases/download/v2.2.2/etcd-v2.2.2-linux-
amd64.tar.gz && \  
tar xzvf etcd-v2.2.2-linux-amd64.tar.gz && \  
cd etcd-v2.2.2-linux-amd64 && \  
chmod +x etcdctl && \  
cp etcdctl /usr/bin && \  
cd .. && \  
rm -rf etcd-v2.2.2-linux-amd64* && \  
curl -L -O
https://github.com/coreos/fleet/releases/download/v0.11.5/fleet-v0.11.5-linux-
amd64.tar.gz && \  
tar xzvf fleet-v0.11.5-linux-amd64.tar.gz && \  
cd fleet-v0.11.5-linux-amd64 && \  
chmod +x fleetctl && \  
cp fleetctl /usr/bin && \  
cd .. && \  
rm -rf fleet-v0.11.5-linux-amd64* && \  
apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
CMD /bin/bash /usr/src/app/rebalance-services.sh  

