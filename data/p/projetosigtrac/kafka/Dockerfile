FROM java:8-jre  
MAINTAINER Luiz Coura <luizcoura@gmail.com>  
  
ENV KAFKA_VERSION 0.10.0.1  
ENV SCALA_VERSION 2.11  
# Download Kafka  
ADD
http://ftp.unicamp.br/pub/apache/kafka/${KAFKA_VERSION}/kafka_${SCALA_VERSION}-${KAFKA_VERSION}.tgz
/tmp/  
  
# Install Kafka  
RUN mkdir -p /usr/local/kafka \  
&& tar -zx -C /usr/local/kafka --strip-components=1 -f
/tmp/kafka_${SCALA_VERSION}-${KAFKA_VERSION}.tgz \  
&& rm -rf kafka_*  
  
# Add service config files  
ADD config /usr/local/kafka/config  
  
# Add Init Script  
ADD bin/kafka-start.sh /usr/local/kafka/bin/kafka-start.sh  
RUN chmod 755 /usr/local/kafka/bin/kafka-start.sh  
  
EXPOSE 9092  
CMD ["/usr/local/kafka/bin/kafka-start.sh"]

