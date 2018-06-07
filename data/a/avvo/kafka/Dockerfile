FROM ubuntu:trusty  
  
MAINTAINER Wurstmeister  
  
RUN apt-get update; apt-get install -y unzip openjdk-6-jdk wget git docker.io  
  
ENV SCALA_VERSION=2.9.1  
ENV KAFKA_VERSION=0.8.2.1  
RUN wget -q
http://apache.claz.org/kafka/${KAFKA_VERSION}/kafka_${SCALA_VERSION}-${KAFKA_VERSION}.tgz
-O /tmp/kafka_${SCALA_VERSION}-${KAFKA_VERSION}.tgz  
RUN tar xfz /tmp/kafka_${SCALA_VERSION}-${KAFKA_VERSION}.tgz -C /opt  
  
VOLUME ["/kafka"]  
  
ENV KAFKA_HOME /opt/kafka_${SCALA_VERSION}-${KAFKA_VERSION}  
ADD start-kafka.sh /usr/bin/start-kafka.sh  
ADD broker-list.sh /usr/bin/broker-list.sh  
CMD start-kafka.sh  

