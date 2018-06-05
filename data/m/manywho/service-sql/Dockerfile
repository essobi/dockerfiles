FROM maven:3-jdk-8-alpine  
  
RUN mkdir -p /usr/src/app  
WORKDIR /usr/src/app  
  
ADD . /usr/src/app  
  
RUN mvn install -DskipTests=true  
  
EXPOSE 8080  
CMD ["java", "-Xmx600m", "-jar", "/usr/src/app/target/sql-2.0-SNAPSHOT.jar"]  

