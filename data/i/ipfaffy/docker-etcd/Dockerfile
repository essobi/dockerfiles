FROM ubuntu:16.04  
LABEL maintainer "mike@mikepfaffroth.com"  
  
WORKDIR "/vulcan"  
  
RUN apt-get update &&\  
apt-get -y install curl tar &&\  
curl -L
"https://github.com/coreos/etcd/releases/download/v2.0.9/etcd-v2.0.9-linux-
amd64.tar.gz" -o etcd-v2.0.9-linux-amd64.tar.gz &&\  
tar xzvf etcd-v2.0.9-linux-amd64.tar.gz &&\  
mv etcd-v2.0.9-linux-amd64/etcd /usr/local/bin/etcd &&\  
mv etcd-v2.0.9-linux-amd64/etcdctl /usr/local/bin/etcdctl &&\  
rm -rf ./etcd-v2.0.9-linux-amd64 &&\  
rm -rf ./etcd-v2.0.9-linux-amd64.tar.gz &&\  
apt-get remove --purge -y $BUILD_PACKAGES $(apt-mark showauto) &&\  
rm -rf /var/lib/apt/lists/*  
  
ENTRYPOINT ["/usr/local/bin/etcd"]  

