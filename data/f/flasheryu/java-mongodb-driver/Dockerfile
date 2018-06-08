FROM maven  
  
# Install maven  
#RUN apt-get -y update  
#RUN apt-get install -y maven  
RUN mkdir -p /root/.m2/repository  
COPY repository/ /root/.m2/repository/  
  
WORKDIR /code  
  
# Prepare by downloading dependencies  
ADD pom.xml /code/pom.xml  
ADD startup.properties /code/startup.properties  
#RUN ["mvn", "dependency:resolve"]  
#RUN ["mvn", "verify"]  
# Adding source, compile and package into a fat jar  
#ADD java-mongo-0.0.1-SNAPSHOT-jar-with-dependencies.jar /code/java-
mongo-0.0.1-SNAPSHOT-jar-with-dependencies.jar  
ADD src /code/src  
RUN ["mvn", "package"]  
  
#EXPOSE 8080  
CMD ["java", "-jar", "target/java-mongo-0.0.1-SNAPSHOT-jar-with-
dependencies.jar"]

