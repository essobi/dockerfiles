FROM maven:alpine AS build  
  
WORKDIR /usr/src/app  
  
COPY src src  
COPY pom.xml pom.xml  
  
RUN mvn clean package  
  
FROM openjdk:jre-alpine  
  
EXPOSE 8080  
COPY \--from=build /usr/src/app/target/service-dummy.jar
/usr/src/app/target/service-dummy.jar  
  
CMD ["java", "-Xmx300m", "-jar", "/usr/src/app/target/service-dummy.jar"]  

