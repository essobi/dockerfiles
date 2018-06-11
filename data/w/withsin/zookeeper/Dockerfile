FROM alpine  
MAINTAINER withsin <withsin@gmail.com>  
  
ENV ZOO_VERSION=3.4.8  
RUN apk --no-cache add openjdk8-jre bash  
RUN mkdir /opt \  
&& wget -O -
http://archive.apache.org/dist/zookeeper/zookeeper-${ZOO_VERSION}/zookeeper-${ZOO_VERSION}.tar.gz
| tar zx -C /opt \  
&& ln -s /opt/zookeeper-${ZOO_VERSION} /opt/zookeeper \  
&& mkdir /opt/zookeeper/data \  
&& chown -R root:root /opt/zookeeper-${ZOO_VERSION} \  
&& mv /opt/zookeeper/conf/zoo_sample.cfg /opt/zookeeper/conf/zoo.cfg  
  
EXPOSE 2181 2888 3888  
CMD ["/opt/zookeeper/bin/zkServer.sh", "start-foreground"]  

