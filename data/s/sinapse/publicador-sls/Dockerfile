FROM openjdk:8-jdk-alpine  
COPY publicador/SLEngineService.jar /SLEngineService.jar  
VOLUME /tmp  
WORKDIR /  
EXPOSE 8080  
CMD ["java", "-Djava.security.egd=file:/dev/./urandom", "-jar",
"SLEngineService.jar"]

