# Kafka and Zookeeper  
FROM java:openjdk-8-jre  
  
ENV DEBIAN_FRONTEND noninteractive  
ENV SCALA_VERSION 2.11  
ENV KAFKA_VERSION 0.10.1.0  
ENV KAFKA_HOME /opt/kafka_"$SCALA_VERSION"-"$KAFKA_VERSION"  
# Install Kafka, Zookeeper and other needed things  
RUN apt-get update && \  
apt-get install -y wget&& \  
rm -rf /var/lib/apt/lists/* && \  
apt-get clean && \  
wget -q http://mirrors.ae-
online.de/apache/kafka/"$KAFKA_VERSION"/kafka_"$SCALA_VERSION"-"$KAFKA_VERSION".tgz
-O /tmp/kafka_"$SCALA_VERSION"-"$KAFKA_VERSION".tgz && \  
tar xfz /tmp/kafka_"$SCALA_VERSION"-"$KAFKA_VERSION".tgz -C /opt && \  
mv /opt/kafka_"$SCALA_VERSION"-"$KAFKA_VERSION" /opt/kafka && \  
rm /tmp/kafka_"$SCALA_VERSION"-"$KAFKA_VERSION".tgz  
  
# 9092 is kafka  
EXPOSE 9092  
CMD ["/opt/kafka/bin/kafka-server-start.sh",
"/opt/kafka/config/server.properties"]  

