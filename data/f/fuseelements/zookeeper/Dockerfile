FROM anapsix/alpine-java:8_server-jre  
  
MAINTAINER Jon Buffington <jon@fuseelements.com>  
  
# Add data for docker inspect.  
LABEL name="zookeeper" version="3.4.9" jre_version="8"  
  
ENV ZOOKEEPER_VERSION="3.4.9"  
RUN mkdir -p /opt && \  
wget -q -O -
http://www.gtlib.gatech.edu/pub/apache/zookeeper/zookeeper-$ZOOKEEPER_VERSION/zookeeper-$ZOOKEEPER_VERSION.tar.gz
| tar -zxf - -C /tmp && \  
mkdir -p /opt/zookeeper-$ZOOKEEPER_VERSION && \  
ln -s /opt/zookeeper-$ZOOKEEPER_VERSION /opt/zookeeper && \  
cd /tmp/zookeeper-$ZOOKEEPER_VERSION && \  
mv ./bin ./conf ./lib ./zookeeper-$ZOOKEEPER_VERSION.jar /opt/zookeeper/ && \  
mv /opt/zookeeper/conf/zoo_sample.cfg /opt/zookeeper/conf/zoo.cfg && \  
sed -i -r 's|#autopurge|autopurge|g' /opt/zookeeper/conf/zoo.cfg && \  
mkdir -p /tmp/zookeeper && \  
sed -i -r 's|#(log4j.appender.ROLLINGFILE.MaxBackupIndex.*)|\1|g'
/opt/zookeeper/conf/log4j.properties && \  
rm -rf /tmp/zookeeper-$ZOOKEEPER_VERSION  
  
# client port (2188/tcp), peer connection port (2888/tcp), leader election
port (3888/tcp)  
EXPOSE 2181 2888 3888  
WORKDIR /opt/zookeeper  
  
VOLUME ["/tmp/zookeeper"] # dataDir=/tmp/zookeeper  
  
ENTRYPOINT ["/opt/zookeeper/bin/zkServer.sh"]  
  
CMD ["start-foreground"]  

