FROM java:8  
#Install maven  
RUN apt-get update  
RUN apt-get install -y maven  
  
WORKDIR /build  
  
# Dependencies  
ADD pom.xml /build/pom.xml  
ADD profiles/ /build/profiles  
RUN ["mvn", "dependency:resolve"]  
RUN ["mvn", "verify"]  
  
# Compile and package jar  
ADD src /build/src  
ADD cert /build/cert  
  
RUN ["mvn", "package"]  
  
EXPOSE 4567  
CMD ["mvn", "exec:java"]  

