FROM ubuntu:latest  
  
MAINTAINER Lyray  
  
RUN apt-get update  
RUN apt-get install default-jre -y  
RUN apt-get install default-jdk -y  
RUN apt-get install maven -y  
  
COPY pom.xml /xiuxiu/  
  
COPY src/ /xiuxiu/src/  
  
WORKDIR /xiuxiu/  
  
RUN mvn package  
  
EXPOSE 8080  
CMD
["java","-Djava.security.egd=file:/dev/./urandom","-jar","target/xiuxiu-0.0.1-SNAPSHOT.jar"]

