FROM maven:3.3.9-jdk-8  
ADD rest-web-app /  
RUN mvn package  
  
EXPOSE 8080  
ENTRYPOINT ["java", "-jar", "target/rest-web-app-1.0.0-swarm.jar"]  

