FROM openjdk:8-jre-alpine  
MAINTAINER Justin Plock <justin@plock.net>  
  
ARG MIRROR=http://apache.mirrors.pair.com  
ARG VERSION=3.4.8  
LABEL name="zookeeper" version=$VERSION  
  
RUN apk add --no-cache wget bash \  
&& mkdir /opt \  
&& wget -q -O - $MIRROR/zookeeper/zookeeper-$VERSION/zookeeper-$VERSION.tar.gz
| tar -xzf - -C /opt \  
&& mv /opt/zookeeper-$VERSION /opt/zookeeper \  
&& mkdir -p /tmp/zookeeper  
  
EXPOSE 2181 2888 3888  
WORKDIR /opt/zookeeper  
  
ENV tickTime=2000  
ENV dataDir=/tmp/zookeeper  
ENV dataLogDir=/tmp/zookeeper/log  
ENV clientPort=2181  
ENV initLimit=10  
ENV syncLimit=5  
VOLUME ["/opt/zookeeper/conf", "/tmp/zookeeper"]  
  
ADD entrypoint.sh entrypoint.sh  
RUN chmod +x entrypoint.sh  
  
ENTRYPOINT ["/opt/zookeeper/entrypoint.sh"]  

