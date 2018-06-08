FROM java:7  
MAINTAINER Kurt Greiner  
  
ENV ZK_VERSION 3.4.7  
RUN wget -qO-
http://ftp.unicamp.br/pub/apache/zookeeper/zookeeper-${ZK_VERSION}/zookeeper-${ZK_VERSION}.tar.gz
| tar xzf - -C /opt  
RUN mv /opt/zookeeper-${ZK_VERSION} /opt/zookeeper && cp
/opt/zookeeper/conf/zoo_sample.cfg /opt/zookeeper/conf/zoo.cfg  
RUN mkdir -p /tmp/zookeeper  
  
EXPOSE 2181  
WORKDIR /opt/zookeeper  
  
VOLUME ["/opt/zookeeper/conf", "/tmp/zookeeper"]  
  
ENTRYPOINT ["/opt/zookeeper/bin/zkServer.sh"]  
CMD ["start-foreground"]  

