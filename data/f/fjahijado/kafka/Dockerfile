# Kafka and Zookeeper  
FROM openjdk:8-jre  
  
MAINTAINER Francisco Javier Ahijado (https://github.com/iCesofT)  
  
ENV DEBIAN_FRONTEND noninteractive  
ENV KAFKA_MIRROR http://www-eu.apache.org/dist/kafka  
ENV SCALA_VERSION 2.11  
ENV KAFKA_VERSION 0.11.0.2  
ENV KAFKA_HOME /opt/kafka_"$SCALA_VERSION"-"$KAFKA_VERSION"  
# Install Kafka, Zookeeper and other needed things  
RUN apt-get update \  
&& apt-get install -y zookeeper wget supervisor dnsutils \  
&& rm -rf /var/lib/apt/lists/* \  
&& apt-get clean \  
&& apt-get autoremove \  
&& wget -q
"$KAFKA_MIRROR"/"$KAFKA_VERSION"/kafka_"$SCALA_VERSION"-"$KAFKA_VERSION".tgz
-O /tmp/kafka_"$SCALA_VERSION"-"$KAFKA_VERSION".tgz \  
&& tar xfz /tmp/kafka_"$SCALA_VERSION"-"$KAFKA_VERSION".tgz -C /opt \  
&& rm /tmp/kafka_"$SCALA_VERSION"-"$KAFKA_VERSION".tgz  
  
COPY [ "scripts/start-kafka.sh", "/usr/bin/start-kafka.sh" ]  
  
# Supervisor config  
COPY [ "supervisor/kafka.conf", "supervisor/zookeeper.conf",
"/etc/supervisor/conf.d/" ]  
  
# 2181 is zookeeper, 9092 is kafka  
EXPOSE 2181 9092  
CMD ["supervisord", "-n"]  

