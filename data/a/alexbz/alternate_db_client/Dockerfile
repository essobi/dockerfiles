FROM openjdk:8-jdk-alpine  
VOLUME /tmp  
ARG JAR_FILE  
COPY ${JAR_FILE} db_client_app.jar  
ENTRYPOINT
["java","-Djava.security.egd=file:/dev/./urandom","-jar","/db_client_app.jar"]

