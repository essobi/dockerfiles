FROM maven:3.2.5-jdk-8  
WORKDIR /code  
  
ADD pom.xml /code/pom.xml  
RUN ["mvn", "dependency:resolve"]  
  
ADD src /code/src  
RUN ["mvn","-DskipTests=true", "package"]  
  
EXPOSE 8080  
CMD ["java", "-Xmx8G", "-jar", "target/evacuation-web-app-0.1-SNAPSHOT.jar"]  

