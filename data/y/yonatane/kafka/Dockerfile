FROM openjdk:8u151-jre-alpine3.7  
  
ENV KAFKA_VERSION=1.1.0 KAFKA_SCALA_VERSION=2.11  
ENV KAFKA_RELEASE_ARCHIVE kafka_${KAFKA_SCALA_VERSION}-${KAFKA_VERSION}.tgz  
  
# Download Kafka binary distribution  
RUN mkdir /kafka /kafka/data /kafka/logs && \  
apk --no-cache add bash curl && \  
curl -sS
http://www.us.apache.org/dist/kafka/${KAFKA_VERSION}/${KAFKA_RELEASE_ARCHIVE}
| \  
tar -zxf - -C /kafka && \  
mv /kafka/kafka_* /kafka/dist && \  
apk --no-cache del curl  

