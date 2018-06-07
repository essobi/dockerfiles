FROM extrasme/mesos-slave-docker  
MAINTAINER tech@extrasme.com  
  
RUN apt-get update && apt-get install jq  
  
ENV ZK_IMAGE_NAME=zookeeper-autodisc QUORUM=2 ZK_PORT=2181
REGISTRATOR=registrator ETCD_PORT=4001  
ADD *sh /mesos/  
RUN chmod +x /mesos/*.sh  
  
ENTRYPOINT ["./discovery.sh"]  

