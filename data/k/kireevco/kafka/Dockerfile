  
FROM java:openjdk-8-jre  
  
MAINTAINER Dmitry Kireev <dmitry@kireev.co>  
  
# Kafka and Zookeeper  
ENV DEBIAN_FRONTEND noninteractive  
ENV SCALA_VERSION 2.11  
ENV KAFKA_VERSION 0.10.0.0  
ENV KAFKA_HOME /opt/kafka_"$SCALA_VERSION"-"$KAFKA_VERSION"  
# Install Kafka, Zookeeper and other needed things  
RUN apt-get update && \  
apt-get install -y zookeeper wget supervisor dnsutils && \  
rm -rf /var/lib/apt/lists/* && \  
apt-get clean && \  
wget -q
http://apache.mirrors.spacedump.net/kafka/"$KAFKA_VERSION"/kafka_"$SCALA_VERSION"-"$KAFKA_VERSION".tgz
-O /tmp/kafka_"$SCALA_VERSION"-"$KAFKA_VERSION".tgz && \  
tar xfz /tmp/kafka_"$SCALA_VERSION"-"$KAFKA_VERSION".tgz -C /opt && \  
rm /tmp/kafka_"$SCALA_VERSION"-"$KAFKA_VERSION".tgz  
  
ADD scripts/start-kafka.sh /usr/bin/start-kafka.sh  
# Supervisor config  
ADD config/supervisord.conf /etc/supervisor/  
ADD config/server.properties ${KAFKA_HOME}/config/server.properties  
ADD config/zoo.cfg /etc/zookeeper/conf/zoo.cfg  
  
EXPOSE 2181 9092  
CMD ["supervisord", "-c", "/etc/supervisor/supervisord.conf"]

