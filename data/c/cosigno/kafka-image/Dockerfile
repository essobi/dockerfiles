# Kafka and Zookeeper  
FROM java:openjdk-8-jre  
  
ENV DEBIAN_FRONTEND noninteractive  
ENV SCALA_VERSION 2.11  
ENV KAFKA_VERSION 0.10.1.0  
ENV KAFKA_HOME /opt/kafka_"$SCALA_VERSION"-"$KAFKA_VERSION"  
# Install Kafka, Zookeeper and other needed things  
RUN wget -q
http://apache.mirrors.spacedump.net/kafka/"$KAFKA_VERSION"/kafka_"$SCALA_VERSION"-"$KAFKA_VERSION".tgz
-O /tmp/kafka_"$SCALA_VERSION"-"$KAFKA_VERSION".tgz && \  
tar xfz /tmp/kafka_"$SCALA_VERSION"-"$KAFKA_VERSION".tgz -C /opt && \  
rm /tmp/kafka_"$SCALA_VERSION"-"$KAFKA_VERSION".tgz  
  
ADD start-kafka.sh /usr/bin/start-kafka.sh  
  
WORKDIR $KAFKA_HOME  
EXPOSE 2181 9092  
CMD ["/usr/bin/start-kafka.sh"]  

