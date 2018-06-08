FROM openjdk:8-jdk-alpine  
FROM maven:3.5.3-alpine  
ADD src /usr/local/reactivechat/src  
ADD pom.xml /usr/local/reactivechat/pom.xml  
WORKDIR /usr/local/reactivechat/  
RUN mvn package  
CMD ["java","-jar","target/ChatApp-0.0.1-SNAPSHOT.jar"]

