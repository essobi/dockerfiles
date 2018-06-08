FROM maven:3.5  
WORKDIR /code  
  
# Prepare by downloading dependencies  
ADD pom.xml /code/pom.xml  
RUN ["mvn", "dependency:resolve"]  
RUN ["mvn", "verify"]  
  
# Adding source, compile and package into a fat jar  
ADD src /code/src  
RUN ["mvn", "package"]  
  
EXPOSE 80  
CMD ["/usr/lib/jvm/java-8-openjdk-amd64/bin/java", "-jar",
"target/sparkexample-jar-with-dependencies.jar"]  

