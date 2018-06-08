FROM project42/ruby-alpine:latest  
MAINTAINER Jordan Clark jordan.clark@esu10.org  
  
COPY container-files /  
  
RUN apk add --no-cache ruby-json && \  
cd /usr/local && \  
wget
https://gobuilder.me/get/github.com/coreos/etcd/etcdctl/etcdctl_master_linux-
amd64.zip && \  
unzip etcdctl_master_linux-amd64.zip && \  
rm etcdctl_master_linux-amd64.zip && \  
ln -s /usr/local/etcdctl/etcdctl /usr/local/bin/ && \  
wget https://github.com/thejordanclark/etcd-glueops/archive/master.zip && \  
unzip master.zip && \  
mv etcd-glueops-master etcd-glueops && \  
rm master.zip && \  
cd etcd-glueops && \  
bundle install  
  
ENTRYPOINT ["/config/bootstrap.sh"]  
  

