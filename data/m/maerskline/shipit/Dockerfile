# Dockerfile for Ship-IT Backend  
FROM maven:3.5.0-jdk-8  
RUN mkdir -p /usr/src/app  
RUN mkdir -p /usr/src/app/loadfinder-backend  
  
ADD pom.xml /usr/src/app  
  
WORKDIR /usr/src/app/loadfinder-backend  
ADD ./loadfinder-backend /usr/src/app/loadfinder-backend  
  
RUN mvn clean  
RUN mvn package  
  
RUN cp target/loadfinder-backend-0.0.1-SNAPSHOT.jar .  
  
EXPOSE 8080  
HEALTHCHECK \--start-period=2m --interval=5m --timeout=10s CMD curl -f
http://localhost:8080/api/home/status || exit 1  
  
CMD [ "mvn", "spring-boot:run" ]

