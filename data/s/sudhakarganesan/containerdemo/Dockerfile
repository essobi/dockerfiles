FROM openjdk:8-jdk-alpine  
VOLUME /tmp  
EXPOSE 8080  
ARG JAR_FILE  
COPY ${JAR_FILE} demo1.0.jar  
ENTRYPOINT
["java","-Djava.security.egd=file:/dev/./urandom","-jar","/demo1.0.jar"]  

