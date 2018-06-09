FROM java:8  
#FROM maven:latest  
MAINTAINER Sonam Samdupkhangsar <sonamhava@gmail.com>  
  
RUN apt-get update  
RUN apt-get install -y maven  
  
WORKDIR /code  
  
#Prepare by downloading dependencies  
ADD pom.xml /code/pom.xml  
RUN ["mvn", "dependency:resolve"]  
RUN ["mvn", "verify"]  
  
#Adding source, compile and package into a fat jar  
ADD src /code/src  
  
RUN ["mvn", "clean"]  
RUN ["mvn", "install", "-Dmaven.test.skip=true"]  
  
RUN mkdir webapps  
  
CMD ["cp"] ["/code/target/note-1.0.war", "/usr/local/tomcat/webapps/"]  

