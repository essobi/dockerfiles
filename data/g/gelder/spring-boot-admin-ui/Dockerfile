FROM java:8-jre-alpine  
  
EXPOSE 8080  
### Add microservice artifact  
COPY build/docker/spring-boot-admin-ui-*.jar /opt/spring-boot-admin-ui.jar  
  
WORKDIR /opt  
ENTRYPOINT ["java", "-jar", "spring-boot-admin-ui.jar"]

