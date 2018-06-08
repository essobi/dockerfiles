# Using Java 8 official image, based on Debian Jessie  
FROM java:8-jre  
MAINTAINER Artyom Artemiev <cptn.foxmk@gmail.com>  
  
# Download and install Apache Kafka  
ENV SCALA_VERSION 2.11  
ENV KAFKA_VERSION 0.8.2.2  
RUN wget -q -O /tmp/kafka.tar.gz http://apache-
mirror.rbc.ru/pub/apache/kafka/$KAFKA_VERSION/kafka_$SCALA_VERSION-$KAFKA_VERSION.tgz
\  
&& tar -xzf /tmp/kafka.tar.gz -C /opt \  
&& rm -f /tmp/kafka.tar.gz  
  
ADD entrypoint.sh /entrypoint.sh  
RUN chmod a+x /entrypoint.sh  
  
VOLUME [ "/var/lib/kafka" ]  
VOLUME [ "/var/log/kafka" ]  
  
# Default settings  
ENV KAFKA_HOME /opt/kafka_$SCALA_VERSION-$KAFKA_VERSION  
ENV KAFKA_LOG_DIR /var/log/kafka  
ENV KAFKA_CLIENT_PORT 9092  
ENV KAFKA_JMX_PORT 7203  
ENV ZOOKEEPER_CONNECTION_TIMEOUT 1000000  
#ENV KAFKA_CONFIG_TEMPLATE /opt/kafka/config/server.properties.template  
#CMD dockerize -template
$KAFKA_CONFIG_TEMPLATE:/opt/kafka/config/server.properties
/opt/kafka/bin/kafka-server-start.sh /opt/kafka/config/server.properties  
EXPOSE $KAFKA_CLIENT_PORT  
EXPOSE $KAFKA_JMX_PORT  
  
ENV PATH $KAFKA_HOME/bin:$PATH  
ENTRYPOINT [ "/entrypoint.sh" ]  
CMD [ "kafka-server-start.sh", "/server.properties" ]  
  

