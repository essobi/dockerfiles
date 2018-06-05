FROM java:openjdk-8-jre  
  
ENV DEBIAN_FRONTEND noninteractive  
ENV SCALA_VERSION 2.11  
ENV KAFKA_VERSION 0.9.0.1  
ENV ZOOKEEPER_VERSION 3.4.6  
ENV KAFKA_PORT 9092  
ENV KAFKA_HOME /opt/kafka_"$SCALA_VERSION"-"$KAFKA_VERSION"  
ENV ZOOKEEPER_HOME /opt/zookeeper-"$ZOOKEEPER_VERSION"  
ENV KAFKA_LOGLEVEL DEBUG  
  
ENV NUM_PARTITIONS 1  
ENV REPLICATION_FACTOR 1  
ENV LEADER_REBALANCE_CHECK_INTERVAL 10  
# Install Kafka, Zookeeper and other needed things  
RUN apt-get update && \  
apt-get install -y dnsutils nano && \  
rm -rf /var/lib/apt/lists/* && \  
apt-get clean && \  
wget -q
http://mirror.reverse.net/pub/apache/zookeeper/zookeeper-"$ZOOKEEPER_VERSION"/zookeeper-"$ZOOKEEPER_VERSION".tar.gz
-O /tmp/zookeeper-"$ZOOKEEPER_VERSION".tgz && \  
tar xfz /tmp/zookeeper-"$ZOOKEEPER_VERSION".tgz -C /opt && \  
rm /tmp/zookeeper-"$ZOOKEEPER_VERSION".tgz && \  
wget -q
http://apache.mirrors.spacedump.net/kafka/"$KAFKA_VERSION"/kafka_"$SCALA_VERSION"-"$KAFKA_VERSION".tgz
-O /tmp/kafka_"$SCALA_VERSION"-"$KAFKA_VERSION".tgz && \  
tar xfz /tmp/kafka_"$SCALA_VERSION"-"$KAFKA_VERSION".tgz -C /opt && \  
rm /tmp/kafka_"$SCALA_VERSION"-"$KAFKA_VERSION".tgz && \  
rm -rf $KAFKA_HOME/bin/windows/ && \  
mv "${ZOOKEEPER_HOME}"/conf/zoo_sample.cfg "${ZOOKEEPER_HOME}"/conf/zoo.cfg  
  
ADD server.properties $KAFKA_HOME/config/  
  
ADD entrypoint.sh /  
RUN chmod +x /entrypoint.sh  
  
# 2181 is zookeeper, 9092 is kafka  
EXPOSE 2181 9092  
ENTRYPOINT ["/entrypoint.sh"]  
CMD ["kafka"]  

