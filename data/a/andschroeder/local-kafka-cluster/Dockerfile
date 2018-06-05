FROM anapsix/alpine-java  
  
MAINTAINER Andreas Schroeder, https://github.com/andreas-schroeder  
  
# Versions  
ARG scala_version=2.11  
ARG kafka_version=0.10.0.0  
# Fetch Kafka & Zookeeper tarfile from apache mirror & extract it to
/kafka_<versions-info>.  
RUN \  
echo "===> fetching Kafka..." && \  
wget -q
http://mirror.23media.de/apache/kafka/${kafka_version}/kafka_${scala_version}-${kafka_version}.tgz
-O /tmp/kafka.tgz && \  
\  
\  
echo "===> installing Kafka..." && \  
tar -C / -xzf /tmp/kafka.tgz && \  
ln -s /kafka_${scala_version}-${kafka_version} /kafka && \  
\  
\  
echo "===> clean up..." && \  
rm /tmp/kafka.tgz  
  
# Add Kafka & Zookeeper custom configurations.  
ADD files/config/server.properties files/config/zookeeper.properties
files/config/log4j.properties /kafka/config/  
  
# Add Kafka & Zookeeper start wrapper.  
ADD files/bin/start /kafka/bin/  
  
# Expose config volume.  
VOLUME /kafka/config  
  
# Expose Kafka data volume.  
VOLUME /var/lib/kafka  
  
# Kafka broker port.  
ENV kafka_ip=127.0.0.1  
# Kafka broker port.  
ENV kafka_port=9092  
# Default Kafka broker id  
ENV kafka_id=1  
# Define start wrapper as entrypoint.  
ENTRYPOINT [ "kafka/bin/start" ]  
  
# Define kafka as default command (the other option being "zookeeper").  
CMD [ "kafka" ]  

