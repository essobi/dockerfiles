FROM java:8  
MAINTAINER Ludwig Strale Wiren  
  
RUN apt-get update  
RUN apt-get install -y maven  
  
WORKDIR /code  
  
ADD pom.xml /code/pom.xml  
RUN ["mvn", "dependency:resolve"]  
RUN ["mvn", "verify"]  
  
ADD src /code/src  
RUN ["mvn", "package"]  
  
EXPOSE 4567  
CMD ["/usr/lib/jvm/java-8-openjdk-amd64/bin/java", "-jar", "target/sparktest-
jar-with-dependencies.jar"]  

