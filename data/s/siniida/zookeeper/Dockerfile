FROM alpine  
MAINTAINER siniida <sinpukyu@gmail.com>  
  
ENV ZOO_VERSION=3.4.6  
RUN apk --no-cache add openjdk8-jre bash \  
&& mkdir /opt \  
&& wget -O -
http://archive.apache.org/dist/zookeeper/zookeeper-${ZOO_VERSION}/zookeeper-${ZOO_VERSION}.tar.gz
| tar zx -C /opt \  
&& ln -s /opt/zookeeper-${ZOO_VERSION} /opt/zookeeper \  
&& mkdir /opt/zookeeper/data \  
&& chown -R root:root /opt/zookeeper-${ZOO_VERSION} \  
&& mv /opt/zookeeper/conf/zoo_sample.cfg /opt/zookeeper/conf/zoo.cfg \  
&& sed -i \  
-e 's/^\\(dataDir\\)=.*/\1=\/opt\/zookeeper\/data/g' \  
-e 's/^#\\(autopurge.snapRetainCount=.*\\)/\1/g' \  
-e 's/^#\\(autopurge.purgeInterval=.*\\)/\1/g' \  
/opt/zookeeper/conf/zoo.cfg  
  
ENV JAVA_HOME /usr/lib/jvm/default-jvm/jre  
  
EXPOSE 2181 2888 3888  
WORKDIR /opt/zookeeper  
  
ADD entry.sh /  
  
ENTRYPOINT ["/entry.sh"]  
CMD ["/opt/zookeeper/bin/zkServer.sh", "start-foreground"]  

