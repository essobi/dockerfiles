FROM maven:3-jdk-8-alpine  
  
ADD . /app  
  
# Build & clean  
RUN cd /app && \  
mvn package && \  
mv target/*.jar /app/app.jar && \  
rm -rf target src $MAVEN_CONFIG/repository  
  
EXPOSE 8080  
ENTRYPOINT ["/usr/bin/java", "-jar", "/app/app.jar" ]  

