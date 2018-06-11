FROM openjdk:8-jdk-alpine  
VOLUME /tmp  
ARG JAR_FILE  
ADD ${JAR_FILE} gs-spring-boot-docker-0.1.0.jar.jar  
ENTRYPOINT
["java","-Djava.security.egd=file:/dev/./urandom","-jar","/app.jar"]

