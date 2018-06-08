FROM java:openjdk-8-jre-alpine  
  
ARG MIRROR=http://apache.mirrors.pair.com  
ARG VERSION=3.5.2-alpha  
  
LABEL name="zookeeper" version=$VERSION  
  
RUN apk add --no-cache wget bash \  
&& wget -q -O - $MIRROR/zookeeper/zookeeper-$VERSION/zookeeper-$VERSION.tar.gz
| tar -xzf - -C /etc \  
&& mv /etc/zookeeper-$VERSION /etc/zookeeper  
  
WORKDIR /etc/zookeeper  
  
EXPOSE 2181 2888 3888  
VOLUME ["/var/lib/zookeeper", "/var/log/zookeeper"]  
  
ADD ./zk-init.sh /zk-init.sh  
  
ENTRYPOINT ["/zk-init.sh"]  

