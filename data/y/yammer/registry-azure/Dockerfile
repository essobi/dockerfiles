FROM registry:0.9.0  
MAINTAINER Brian Morton "bmorton@yammer-inc.com"  
RUN apt-get -y update && apt-get -y install libffi-dev libssl-dev  
RUN pip install docker-registry-driver-azureblob  
  
# Install etcd client  
ENV ETCD_VERSION v2.0.8  
ADD
https://github.com/coreos/etcd/releases/download/${ETCD_VERSION}/etcd-${ETCD_VERSION}-linux-
amd64.tar.gz /tmp/  
RUN tar -xvzf /tmp/etcd-${ETCD_VERSION}-linux-amd64.tar.gz -C /tmp  
RUN mv /tmp/etcd-${ETCD_VERSION}-linux-amd64/etcdctl /bin/etcdctl  
RUN rm -rf /tmp/*  
  
ADD env /env  
RUN chmod +x /env  
ENTRYPOINT ["/env"]  
CMD ["docker-registry"]  

