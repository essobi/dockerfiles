FROM maven:3.5.2-jdk-8-slim AS build  
  
WORKDIR /usr/src/app  
  
COPY maven-docker-build-settings.xml $MAVEN_CONFIG/settings.xml  
  
COPY pom.xml .  
  
RUN mkdir -p src/main/java src/test/java  
  
RUN mvn package  
  
COPY src src  
  
RUN mvn package  
  
RUN cp target/kafka-topic-client-1.0-SNAPSHOT-jar-with-dependencies.jar kafka-
topic-client.jar  
  
# This cleanup will probably not reduce image size as the layers have already
been produced  
RUN mvn clean && rm -Rf /m2-build-repository && rm $MAVEN_CONFIG/settings.xml  
  
FROM
yolean/java@sha256:06dabfc8cacd0687c8f52c52afd650444fb6d4a8e0b85f68557e6e7a5c71667c  
  
WORKDIR /usr/src/app  
  
COPY \--from=build /usr/src/app/kafka-topic-client.jar kafka-topic-client.jar  
  
ENV ZOOKEEPER_CONNECT "zookeeper:2181"  
ENV TOPIC_NAME "build-contract-test"  
ENV RESET_TOPIC false  
ENV NUM_PARTITIONS 1  
ENV NUM_REPLICAS 1  
ENV NUM_CREATE_RETRIES 5  
ENTRYPOINT ["java", "-jar", "kafka-topic-client.jar"]  
  

