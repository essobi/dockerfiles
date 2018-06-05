# Kafka and Zookeeper  
FROM ubuntu:14.04  
MAINTAINER Andreas Fritzler <andreas.fritzler@gmail.com>  
  
RUN apt-get -y update  
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y --force-yes software-
properties-common python-software-properties  
RUN apt-add-repository -y ppa:webupd8team/java  
RUN apt-get -y update  
RUN /bin/echo debconf shared/accepted-oracle-license-v1-1 select true |
/usr/bin/debconf-set-selections  
RUN DEBIAN_FRONTEND=noninteractive apt-get -y install oracle-java8-installer
oracle-java8-set-default  
  
ENV DEBIAN_FRONTEND noninteractive  
ENV SCALA_VERSION 2.11  
ENV KAFKA_VERSION 0.8.2.1  
ENV KAFKA_HOME /opt/kafka_"$SCALA_VERSION"-"$KAFKA_VERSION"  
# Install Kafka, Zookeeper and other needed things  
RUN apt-get update && \  
apt-get install -y zookeeper wget supervisor dnsutils netcat-openbsd && \  
rm -rf /var/lib/apt/lists/* && \  
apt-get clean  
  
RUN wget -q
http://apache.mirrors.spacedump.net/kafka/"$KAFKA_VERSION"/kafka_"$SCALA_VERSION"-"$KAFKA_VERSION".tgz
-O /tmp/kafka_"$SCALA_VERSION"-"$KAFKA_VERSION".tgz && \  
tar xfz /tmp/kafka_"$SCALA_VERSION"-"$KAFKA_VERSION".tgz -C /opt && \  
rm /tmp/kafka_"$SCALA_VERSION"-"$KAFKA_VERSION".tgz  
  
ADD scripts/start-kafka.sh /usr/bin/start-kafka.sh  
ADD scripts/kafkaStarter.jar /kafkaStarter.jar  
Add scripts/runKafkaStarter.sh /runKafkaStarter.sh  
  
# Supervisor config  
ADD supervisor/kafka.conf /etc/supervisor/conf.d/kafka.conf  
ADD supervisor/zookeeper.conf /etc/supervisor/conf.d/zookeeper.conf  
  
# 2181 is zookeeper, 9092 is kafka  
EXPOSE 2181 9092 8085  
CMD ["./runKafkaStarter.sh"]  

