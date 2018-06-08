FROM debian  
  
RUN apt-get update && \  
apt-get install curl dnsutils jq -yq && \  
curl -L
https://github.com/coreos/etcd/releases/download/v2.3.3/etcd-v2.3.3-linux-
amd64.tar.gz -o /tmp/etcd-v2.3.3-linux-amd64.tar.gz && \  
tar xzvf /tmp/etcd-v2.3.3-linux-amd64.tar.gz -C /tmp && \  
mv /tmp/etcd-v2.3.3-linux-amd64/etcd /usr/local/bin && \  
mv /tmp/etcd-v2.3.3-linux-amd64/etcdctl /usr/local/bin && \  
rm -rf /tmp/etcd* && \  
rm -rf /var/lib/apt/lists/*  
COPY run.sh /run.sh  
CMD /run.sh  

