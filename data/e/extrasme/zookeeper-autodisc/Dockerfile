FROM extrasme/zookeeper  
MAINTAINER tech@extrasme.com  
  
RUN apk --update add jq  
  
ADD discovery.sh /zookeeper/  
RUN chmod +x /zookeeper/*.sh  
  
ENV ETCD_PORT=4001 REGISTRATOR=registrator IMAGE_NAME=zookeeper-autodisc
PORT=2888 MINUS_COUNT=2  
CMD ["/zookeeper/discovery.sh"]  

