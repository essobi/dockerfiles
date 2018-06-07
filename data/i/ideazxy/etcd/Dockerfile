FROM golang  
  
MAINTAINER Yudi  
  
ADD etcd-v2.0.5-linux-amd64/etcd /bin/etcd  
  
EXPOSE 4001 7001 2379 2380  
VOLUME ["/data"]  
  
ENTRYPOINT ["/bin/etcd"]  
  
CMD ["--data-dir=/data", "--listen-client-
urls=http://0.0.0.0:2379,http://0.0.0.0:4001", "--listen-peer-
urls=http://0.0.0.0:2380,http://0.0.0.0:7001"]  

