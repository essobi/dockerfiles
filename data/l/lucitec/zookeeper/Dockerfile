FROM lucitec/base-java8  
MAINTAINER Lucitec  
  
ENV ZK_HOME /opt/zookeeper-3.4.6  
RUN wget -q -O -
http://apache.mirrors.pair.com/zookeeper/zookeeper-3.4.6/zookeeper-3.4.6.tar.gz
| tar -xzf - -C /opt  
RUN cp $ZK_HOME/conf/zoo_sample.cfg $ZK_HOME/conf/zoo.cfg  
RUN mkdir -p /tmp/zookeeper  
  
EXPOSE 2181 2888 3888  
WORKDIR /opt/zookeeper-3.4.6  
  
# Disabled because of https://issues.apache.org/jira/browse/KAFKA-1029  
# VOLUME ["/opt/zookeeper-3.4.6/conf", "/tmp/zookeeper"]  
CMD ["/opt/zookeeper-3.4.6/bin/zkServer.sh", "start-foreground"]  

