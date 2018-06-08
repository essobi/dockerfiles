FROM quay.io/falkonry/openjdk:8-jre-alpine  
  
COPY start.sh /  
  
ENV KAFKA_VERSION=0.10.1.0 \  
SCALA_VERSION=2.11  
#Install Kafka  
RUN \  
mkdir -p /opt/falkonry/confluent && \  
apk --update add wget && \  
cd /tmp && \  
wget -O confluent.zip http://packages.confluent.io/archive/3.1/confluent-
oss-3.1.1-2.11.zip && \  
unzip confluent.zip && \  
rm -rf confluent.zip && \  
cp -rf confluent-3.1.1/* /opt/falkonry/confluent/ && \  
apk del wget && \  
rm -rf \  
/tmp/* \  
/var/cache/apk/*  
  
VOLUME /tmp/kafka-logs  
  
EXPOSE 2181 9092 8081 8082  
ENTRYPOINT ["/start.sh"]

