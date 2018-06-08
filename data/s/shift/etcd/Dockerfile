FROM scratch  
  
MAINTAINER Vincent Palmer <shift@someone.section.me>  
  
ADD etcd-v2.2.0-linux-amd64/etcd /etcd  
ADD etcd-v2.2.0-linux-amd64/etcdctl /etcdctl  
  
EXPOSE 2379/tcp  
EXPOSE 2380/tcp  
EXPOSE 7001/tcp  
EXPOSE 4001/tcp  
  
VOLUME /data  
VOLUME /wal  
  
CMD ["/etcd", "--data-dir", "/data", "--wal-dir", "/wal"]  

