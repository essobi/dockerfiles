FROM maven:3.5-jdk-8-alpine as build  
WORKDIR /app  
COPY . /app  
RUN mvn install  
  
FROM maven:3.5-jdk-8-alpine  
WORKDIR /app  
COPY \--from=build /app/target/caller-service-1.0.0-SNAPSHOT.jar app/caller-
service-1.0.0-SNAPSHOT.jar  
EXPOSE 8090  
ENTRYPOINT
["java","-Djava.security.egd=file:/dev/./urandom","-jar","app/caller-
service-1.0.0-SNAPSHOT.jar"]

