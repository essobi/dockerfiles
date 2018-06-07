FROM maven  
ADD pom.xml /app/  
ADD src/ /app/src/  
WORKDIR /app/  
RUN mvn package  
EXPOSE 8080  
CMD ["java","-Djava.security.egd=file:/dev/./urandom","-jar","target/spring-
boot-sample-tomcat-1.1.5.RELEASE.jar"]  
  

