FROM ubuntu:14.04  
RUN apt-get update && apt-get install -y maven openjdk-7-jre openjdk-7-jdk  
  
WORKDIR /tmp/  
  
run mkdir src  
  
COPY src ./src/  
COPY pom.xml ./  
  
CMD mvn package  

