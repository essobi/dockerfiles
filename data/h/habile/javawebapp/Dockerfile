FROM java:8  
# Install maven  
RUN apt-get update  
RUN apt-get install -y maven  
  
# Prepare by downloading dependencies  
ADD pom.xml /pom.xml  
RUN ["mvn", "dependency:resolve"]  
RUN ["mvn", "verify"]  
  
# Adding source, compile and package into a fat jar  
ADD src /src  
  
RUN ["mvn", "package"]  
  

