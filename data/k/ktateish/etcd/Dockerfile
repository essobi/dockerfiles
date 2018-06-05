FROM alpine:latest  
  
ADD etcd /  
ADD etcdctl /  
VOLUME ["/data", "/certs"]  
WORKDIR /data  
  
EXPOSE 2379 2380  
CMD ["/etcd"]  

