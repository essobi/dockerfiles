FROM eatcode/openjdk8  
  
MAINTAINER Ayub Malik <ayub.malik@gmail.com>  
  
WORKDIR /opt  
  
ENV ZK_VERSION 3.4.8  
LABEL name="zookeeper" version="$ZK_VERSION"  
  
RUN wget -q -O -
http://apache.mirrors.pair.com/zookeeper/zookeeper-3.4.8/zookeeper-$ZK_VERSION.tar.gz
| tar -xzf - -C /opt \  
&& ln -s /opt/zookeeper-$ZK_VERSION /opt/zookeeper \  
&& cp /opt/zookeeper/conf/zoo_sample.cfg /opt/zookeeper/conf/zoo.cfg \  
&& mkdir -p /tmp/zookeeper  
  
ENV ZOOKEEPER_HOME /opt/zookeeper  
  
EXPOSE 2181 2888 3888  
WORKDIR /opt/zookeeper  
  
VOLUME ["/opt/zookeeper/conf", "/tmp/zookeeper"]  
  
ENTRYPOINT ["/opt/zookeeper/bin/zkServer.sh"]  
  
CMD ["start-foreground"]  
  

