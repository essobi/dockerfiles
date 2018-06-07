FROM maven:3-jdk-8  
MAINTAINER Erlend Kristiansen, erlendk@mesan.no, Mesan AS  
  
COPY pom.xml /tmp/pom.xml  
  
WORKDIR /tmp  
  
RUN mvn dependency:go-offline  
  
COPY . /opt/fangerepo  
  
WORKDIR /opt/fangerepo  
  
# Would like to truly "go offline", but it simply doesn't work  
RUN mvn package  
  
EXPOSE 8080  
CMD ["/usr/lib/jvm/java-8-openjdk-amd64/jre/bin/java", "-jar",
"target/persistering.fangerepo-0.0.1-SNAPSHOT.jar", "server",
"fangerepo_docker.yml"]  

