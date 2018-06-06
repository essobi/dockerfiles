FROM alpine/git as clone  
WORKDIR /app  
  
RUN git clone https://github.com/lbennardis/iot-kafka-cassandra-spark.git  
  
FROM maven:3.5-jdk-8-alpine as build  
WORKDIR /app  
COPY \--from=clone /app/iot-kafka-cassandra-spark /app  
RUN mvn install  
  
FROM openjdk:8-jre-alpine  
WORKDIR /app  

