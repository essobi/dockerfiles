FROM openjdk:8u111-jdk-alpine  
VOLUME /tmp  
ADD /target/rpp-campaign-0.1.0-SNAPSHOT.jar app.jar  
RUN bash -c 'touch /app.jar'  
ENTRYPOINT
["java","-Djava.security.egd=file:/dev/./urandom","-jar","/app.jar"]

