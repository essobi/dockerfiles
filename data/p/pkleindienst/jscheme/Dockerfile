FROM maven:3.5-alpine as builder  
COPY . /jscheme  
WORKDIR /jscheme  
RUN mvn clean package -Dmaven.test.skip=true && \  
mv ./target/JScheme-*-jar-with-dependencies.jar ./target/jscheme.jar  
  
FROM openjdk:8-jre-alpine  
MAINTAINER patrick.kleindienst  
COPY \--from=builder /jscheme/target/jscheme.jar .  
ENTRYPOINT ["java", "-jar", "jscheme.jar"]  

