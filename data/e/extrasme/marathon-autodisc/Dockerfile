FROM mesosphere/marathon  
MAINTAINER tech@extrasme.com  
  
RUN apt-get update && apt-get install jq  
  
ENV ZK_IMAGE_NAME=zookeeper-autodisc ZK_PORT=2181 REGISTRATOR=registrator
ETCD_PORT=4001  
EXPOSE 8080  
ADD *sh /marathon/  
RUN chmod +x /marathon/*.sh  
  
ENTRYPOINT ["./discovery.sh"]  

