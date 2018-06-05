FROM openjdk:8-jdk-alpine  
VOLUME /tmp  
ADD app.jar app.jar  
USER user  
EXPOSE 8080  
ENTRYPOINT
["java","-Djava.security.egd=file:/dev/./urandom","-jar","/app.jar"]

