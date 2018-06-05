FROM java:openjdk-8-jre-alpine  
  
MAINTAINER Shreyas Kulkarni <shyran at gmail>  
  
ARG MIRROR=http://apache.mirrors.pair.com  
ARG VERSION=3.4.9  
LABEL name="zookeeper" version=$VERSION  
  
RUN apk add --no-cache wget bash \  
&& mkdir /opt \  
&& wget -q -O - $MIRROR/zookeeper/zookeeper-$VERSION/zookeeper-$VERSION.tar.gz
| tar -xzf - -C /opt \  
&& mv /opt/zookeeper-$VERSION /opt/zookeeper \  
&& rm /opt/zookeeper/conf/zoo_sample.cfg \  
&& mkdir -p /opt/zookeeper/conf-helpers \  
&& mkdir -p /opt/zookeeper/data  
  
EXPOSE 2181 2888 3888  
WORKDIR /opt/zookeeper  
  
VOLUME ["/opt/zookeeper/conf", "/opt/zookeeper/data"]  
  
COPY ./conf-helpers/gen.zoo.cfg /opt/zookeeper/conf-helpers/gen.zoo.cfg  
HEALTHCHECK \--interval=5s --timeout=10s --retries=12 CMD
/opt/zookeeper/bin/zkServer.sh status  
  
COPY zookeeper-entrypoint.sh /zookeeper-entrypoint.sh  
RUN chmod a+x /zookeeper-entrypoint.sh  
ENTRYPOINT ["/zookeeper-entrypoint.sh"]  
  

