FROM maven:3.3-jdk-8  
EXPOSE 8080  
RUN ["mkdir","/opt/cornea"]  
  
ADD . /opt/cornea/  
  
WORKDIR /opt/cornea  
  
RUN mvn install  
  
ENTRYPOINT ["java", "-jar", "target/cornea-0.1-SNAPSHOT.jar", "--
spring.config.location=classpath:/application.production.properties"]  

