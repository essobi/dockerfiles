FROM gregory90/java:1.7  
ENV ZK_VERSION 3.4.6  
RUN wget -q -O -
http://apache.mirrors.pair.com/zookeeper/zookeeper-$ZK_VERSION/zookeeper-$ZK_VERSION.tar.gz
| tar -xzf - -C /opt  
RUN mkdir -p /var/lib/zookeeper  
  
ENV JAVA_HOME /usr/lib/jvm/java-7-openjdk-amd64  
  
EXPOSE 2181 2888 3888  
WORKDIR /opt/zookeeper-3.4.6  
  
ADD zoo.cfg /opt/zookeeper-3.4.6/conf/zoo.cfg  
ADD run /opt/zookeeper-3.4.6/.docker/  
  
CMD ["/opt/zookeeper-3.4.6/.docker/run"]  
  

