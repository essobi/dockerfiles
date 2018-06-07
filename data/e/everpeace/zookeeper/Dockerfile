# it is derived from alpine:3.4  
FROM java:openjdk-8-jre-alpine  
  
MAINTAINER Shingo Omura <everpeace@gmail.com>  
  
ARG VERSION=3.4.5  
LABEL name="zookeeper" version=$VERSION  
  
USER root  
EXPOSE 2181 2888 3888  
RUN mkdir -p /opt && \  
apk add --no-cache wget bash \  
&& wget -q -O -
https://archive.apache.org/dist/zookeeper/zookeeper-${VERSION}/zookeeper-${VERSION}.tar.gz
| tar -xzf - -C /opt \  
&& mv /opt/zookeeper-${VERSION} /opt/zookeeper \  
&& cp /opt/zookeeper/conf/zoo_sample.cfg /opt/zookeeper/conf/zoo.cfg \  
&& mkdir -p /opt/zookeeper/{data,log}  
  
WORKDIR /opt/zookeeper  
VOLUME ["/opt/zookeeper/conf", "/opt/zookeeper/data", "/opt/zookeeper/log"]  
  
COPY config-and-run.sh ./bin/  
COPY zoo.cfg ./conf/  
  
CMD ["/opt/zookeeper/bin/config-and-run.sh"]  

