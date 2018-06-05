# Ideas from:  
# https://hackernoon.com/crafting-perfect-java-docker-build-flow-740f71638d63  
# Use official OpenJDK 8 runtime as base image  
FROM openjdk:8-jdk-alpine  
  
# Copy source code  
WORKDIR /broker-src  
COPY . /broker-src  
  
# Build "fat" JAR  
RUN apk update && \  
apk --no-cache add bash && \  
./gradlew shadowJar && \  
mv /broker-src/build/libs/cloud-broker-*-all.jar /cloud-broker.jar && \  
apk del bash && \  
rm -rf /broker-src/build && \  
rm -rf /root/.gradle && \  
rm -rf /var/cache/apk/*  
  
# Default environment variables  
ENV KAFKA_HOST kafka  
ENV KAFKA_PORT 9092  
ENV KAFKA_GROUP data-dev  
ENV KAFKA_TOPIC data-dev  
ENV REDIS_HOST redis  
ENV REDIS_PASSWORD ""  
ENV CASSANDRA_HOST cassandra  
ENV CASSANDRA_KEYSPACE streamr_dev  
  
# Run broker when container launches  
CMD java \  
-Dkafka.server=${KAFKA_HOST}:${KAFKA_PORT} \  
-Dkafka.group=${KAFKA_GROUP} \  
-Dkafka.topic=${KAFKA_TOPIC} \  
-Dredis.host=${REDIS_HOST} \  
-Dredis.password=${REDIS_PASSWORD} \  
-Dcassandra.host=${CASSANDRA_HOST} \  
-Dcassandra.keyspace=${CASSANDRA_KEYSPACE} \  
-jar /cloud-broker.jar  

