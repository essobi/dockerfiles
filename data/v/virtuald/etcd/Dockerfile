  
FROM radial/busyboxplus  
MAINTAINER Dustin Spicuzza <dustin@virtualroadside.com>  
  
RUN mkdir /download && cd /download && (curl -L
https://github.com/coreos/etcd/releases/download/v0.4.6/etcd-v0.4.6-linux-
amd64.tar.gz | gunzip | tar -xf -) && cp */etcd /usr/bin && cd / && rm -rf
/download  
  
ENTRYPOINT ["/usr/bin/etcd"]  
  
EXPOSE 4001 7001  

