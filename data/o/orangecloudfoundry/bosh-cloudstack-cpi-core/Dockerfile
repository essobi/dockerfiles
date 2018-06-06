FROM maven:3.3-jdk-8  
ADD src/ src/  
ADD pom.xml pom.xml  
RUN mvn clean install -DskipTests=true  
RUN mv /target/cloudstack-cpi-core-0.0.1-SNAPSHOT.jar app.jar  
RUN sh -c 'touch /app.jar'  
ENV PORT 8080  
EXPOSE 8080  
ENTRYPOINT
["java","-Djava.security.egd=file:/dev/./urandom","-jar","/app.jar"]  

