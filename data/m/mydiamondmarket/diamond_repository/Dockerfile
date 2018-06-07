FROM openjdk:8-jdk-alpine  
VOLUME /tmp  
ARG JAR_FILE  
ADD ${JAR_FILE} diamonds-0.0.1-SNAPSHOT.jar  
ENTRYPOINT
["java","-Djava.security.egd=file:/dev/./urandom","-jar","/diamonds-0.0.1-SNAPSHOT.jar"]

