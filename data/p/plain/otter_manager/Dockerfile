FROM openjdk:8-jre-alpine  
MAINTAINER lw6c@qq.com  
RUN apk add --no-cache ca-certificates wget file bash && update-ca-
certificates  
RUN mkdir manager && cd manager && wget
https://github.com/alibaba/otter/releases/download/otter-4.2.13/manager.deployer-4.2.13.tar.gz
&& tar -xzf manager.deployer-4.2.13.tar.gz && rm
manager.deployer-4.2.13.tar.gz  
RUN sed -i s/"-server -Xms2048m -Xmx3072m -Xmn1024m"/"-server -Xms32m
-Xmx3072m"/g /manager/bin/startup.sh && sed -i s/"-server -Xms1024m -Xmx1024m
-XX:NewSize=256m -XX:MaxNewSize=256m"/"-server -Xms32m -Xmx1024m"/g
/manager/bin/startup.sh  
  
ARG MIRROR=http://apache.mirrors.pair.com  
ARG VERSION=3.4.10  
LABEL name="zookeeper" version=$VERSION  
RUN mkdir -p /opt/zookeeper \  
&& wget -q -O - $MIRROR/zookeeper/zookeeper-$VERSION/zookeeper-$VERSION.tar.gz
\  
| tar -xzC /opt/zookeeper --strip-components=1 \  
&& cp /opt/zookeeper/conf/zoo_sample.cfg /opt/zookeeper/conf/zoo.cfg \  
&& sed -ri 's/(dataDir).*/\1=\/zkdata/' /opt/zookeeper/conf/zoo.cfg \  
&& mkdir -p /zkdata  
  
RUN apk add -U tzdata  
ADD docker-entrypoint.sh /  
RUN chmod +x docker-entrypoint.sh  
ENTRYPOINT ["/docker-entrypoint.sh"]

