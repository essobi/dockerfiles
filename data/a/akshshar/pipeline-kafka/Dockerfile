# Kafka and Zookeeper  
FROM java:openjdk-8-jre  
Maintainer akshshar  
  
ENV DEBIAN_FRONTEND noninteractive  
ENV SCALA_VERSION 2.11  
ENV KAFKA_VERSION 0.10.1.0  
ENV KAFKA_HOME /opt/kafka_"$SCALA_VERSION"-"$KAFKA_VERSION"  
ENV PIPELINE_DOCKER_DIR "bigmuddy-network-telemetry-pipeline/docker/"  
ENV KAFKA_DIR "docker-kafka/kafka"  
# Install Kafka, Zookeeper and other needed things  
RUN apt-get update && \  
apt-get install -y zookeeper wget supervisor dnsutils iproute2 python-pip && \  
rm -rf /var/lib/apt/lists/* && \  
apt-get clean && \  
wget -q
http://apache.mirrors.spacedump.net/kafka/"$KAFKA_VERSION"/kafka_"$SCALA_VERSION"-"$KAFKA_VERSION".tgz
-O /tmp/kafka_"$SCALA_VERSION"-"$KAFKA_VERSION".tgz && \  
tar xfz /tmp/kafka_"$SCALA_VERSION"-"$KAFKA_VERSION".tgz -C /opt && \  
rm /tmp/kafka_"$SCALA_VERSION"-"$KAFKA_VERSION".tgz  
  
RUN pip install --upgrade pip  
RUN pip install kafka-python  
ADD start-kafka.sh /usr/bin/start-kafka.sh  
  
# Supervisor config  
ADD $KAFKA_DIR/supervisor/kafka.conf $KAFKA_DIR/supervisor/zookeeper.conf
supervisor/pipeline.conf /etc/supervisor/conf.d/  
  
# Stage default configuration, metrics spec and example setup  
ADD $PIPELINE_DOCKER_DIR/pipeline.conf /data/pipeline.conf  
ADD $PIPELINE_DOCKER_DIR/metrics.json /data/metrics.json  
ADD $PIPELINE_DOCKER_DIR/metrics_gpb.json /data/metrics_gpb.json  
ADD $PIPELINE_DOCKER_DIR/pipeline /pipeline  
  
VOLUME ["/data"]  
  
# Set up an entry for localhost in /etc/hosts, used by kafka and pipeline  
RUN echo "127.0.0.1 localhost" > /etc/hosts  
  
# 2181 is zookeeper, 9092 is kafka, 5958 is pipeline (udp), 5432 is
pipeline(tcp)  
EXPOSE 2181 9092 5958 5432  
CMD ["supervisord", "-n"]  

