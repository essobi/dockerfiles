FROM java:openjdk-8-jre-alpine  
  
RUN mkdir -p /data /logs /opt/zookeeper  
RUN wget -q -O - https://s3-us-west-2.amazonaws.com/usw2-relateiq-build-
resources/zookeeper-3.3.5.tar.gz \  
| tar -xzf - -C /opt \  
&& mv /opt/zookeeper-3.3.5/* /opt/zookeeper  
  
VOLUME [ "/data", "/logs" ]  
  
EXPOSE 2181  
CMD ["/opt/zookeeper/bin/zkServer.sh", "start-foreground"]  
  
ADD zoo.cfg /opt/zookeeper/conf/zoo.cfg  
ADD log4j.properties /opt/zookeeper/conf/log4j.properties  

