FROM java:8  
# mount to /tmp  
VOLUME /tmp  
  
# Install maven  
RUN apt-get update  
RUN apt-get install -y maven  
  
# Prepare by downloading dependencies  
ADD pom.xml /pom.xml  
RUN ["mvn", "dependency:resolve"]  
  
# Adding source, compile and package into a fat jar  
ADD src /src  
RUN ["mvn", "package"]  
  
EXPOSE 8090  
ENV JAVA_OPTS=""  
CMD ["/usr/lib/jvm/java-8-openjdk-amd64/bin/java", "-jar",
"target/demo-0.0.1-SNAPSHOT.jar"]

