FROM java:openjdk-8  
EXPOSE 8080  
WORKDIR /stallevent  
  
COPY dist/stallevent-gate-service-0.3.0.jar /stallevent/service.jar  
COPY dist/application.properties /stallevent/application.properties  
COPY dist/stallevent-keystore.p12 /stallevent/stallevent-keystore.p12  
  
ENTRYPOINT ["java", "-jar", "/stallevent/service.jar", "--db.url=${SQL_URL}"]  
  

