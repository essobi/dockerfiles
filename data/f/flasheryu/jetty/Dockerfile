FROM maven  
  
# Install maven  
#RUN apt-get -y update  
#RUN apt-get install -y maven  
#RUN mkdir -p /root/.m2/repository  
#COPY repository/ /root/.m2/repository/  
WORKDIR /code  
  
# Prepare by downloading dependencies  
ADD pom.xml /code/pom.xml  
RUN ["mvn", "dependency:resolve"]  
RUN ["mvn", "verify"]  
  
# Adding source, compile and package into a fat jar  
#ADD hello-world-0.1-SNAPSHOT-jar-with-dependencies.jar /code/hello-
world-0.1-SNAPSHOT-jar-with-dependencies.jar  
ADD src /code/src  
RUN ["mvn", "package"]  
  
EXPOSE 8080  
CMD ["java", "-jar", "target/hello-world-0.1-SNAPSHOT-jar-with-
dependencies.jar"]

