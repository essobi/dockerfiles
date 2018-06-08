FROM java:8  
WORKDIR /code  
  
# Install maven  
RUN apt-get update  
RUN apt-get install -y maven  
  
# Prepare by downloading dependencies  
ADD pom.xml /code/pom.xml  
#RUN ["mvn", "dependency:resolve"]  
ADD src /code/src  
RUN ["mvn", "package"]  
  
EXPOSE 8080  
CMD ["/usr/lib/jvm/java-8-openjdk-amd64/bin/java", "-jar", "target/sigma-ms-
user-1.0.0.jar"]  
  
#ADD target/sigma-ms-user-1.0.0.jar app.jar  
#ENV JAVA_OPTS=""  
#ENTRYPOINT exec java $JAVA_OPTS -Djava.security.egd=file:/dev/./urandom -jar
/app.jar

