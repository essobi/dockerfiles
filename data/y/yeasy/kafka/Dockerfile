# Kafka image  
# github.com/yeasy/docker-kafka  
# KAFKA_HOME=/opt/kafka  
# Add $KAFKA_HOME/bin to the $PATH.  
# workdir is set to $KAFKA_HOME  
FROM anapsix/alpine-java:8  
MAINTAINER <yeasy@github.com>  
  
ENV KAFKA_VERSION=0.11.0.1 \  
SCALA_VERSION=2.12  
ENV KAFKA_PKG=kafka_${SCALA_VERSION}-${KAFKA_VERSION}  
ENV KAFKA_HOME=/opt/kafka  
ENV PATH=$PATH:${KAFKA_HOME}/bin  
  
RUN wget http://www-us.apache.org/dist/kafka/${KAFKA_VERSION}/${KAFKA_PKG}.tgz
\  
&& tar xzf ${KAFKA_PKG}.tgz -C /opt \  
&& mv /opt/${KAFKA_PKG} ${KAFKA_HOME}  
  
COPY scripts/* /tmp/  
  
WORKDIR $KAFKA_HOME  
  
# Start a zk service for the kafka to use  
#CMD ["bash", "/tmp/start_zk.sh"]  
# Start a kafka service  
CMD ["bash", "/tmp/start_kafka.sh"]  

