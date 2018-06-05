FROM ubuntu:14.04  
RUN apt-get update -qq && \  
apt-get install -y -qq curl  
  
RUN curl -L
https://github.com/coreos/etcd/releases/download/v2.0.0/etcd-v2.0.0-linux-
amd64.tar.gz -o /tmp/etcd-v2.0.0-linux-amd64.tar.gz && \  
cd /tmp/ && tar xfv /tmp/etcd-v2.0.0-linux-amd64.tar.gz && \  
mv /tmp/etcd-v2.0.0-linux-amd64/etcdctl /usr/local/bin/etcdctl  
  
COPY service.sh /service.sh  
RUN chmod +x /service.sh  
  
CMD ["/service.sh"]

