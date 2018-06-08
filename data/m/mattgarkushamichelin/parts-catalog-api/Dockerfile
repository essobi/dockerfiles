FROM maven:3.5.0-jdk-8  
WORKDIR /app  
#copy the directoy over  
COPY . /app  
  
#build with maven, get a jar  
RUN mvn package -Dmaven.test.skip=true  
  
EXPOSE 8080  
#now run that jar  
CMD ["/usr/bin/java", "-jar", "target/app.jar"]  

