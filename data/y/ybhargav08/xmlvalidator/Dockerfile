FROM openjdk:8-jdk-alpine  
FROM maven:3.5.3-alpine  
ADD src /usr/local/xmlvalidator/src  
ADD pom.xml /usr/local/xmlvalidator/pom.xml  
WORKDIR /usr/local/xmlvalidator/  
RUN mvn package  
CMD ["java","-jar","target/UIXmlValidator-0.0.1-SNAPSHOT.jar"]

