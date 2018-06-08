FROM java AS buildenv  
COPY app /spring-rest/app/  
WORKDIR /spring-rest/app  
RUN ["./mvnw", "-q", "clean", "package"]  
  
FROM openjdk:jre-alpine  
COPY \--from=buildenv /spring-rest/app/target/spring-data-rest-0.1.0.jar
/spring-data-rest.jar  
EXPOSE 8080  
CMD ["java", "-jar", "/spring-data-rest.jar"]  

