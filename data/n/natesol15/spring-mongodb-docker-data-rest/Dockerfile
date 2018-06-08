#FROM frolvlad/alpine-oraclejdk8:slim  
#FROM java:8  
#RUN sh -c 'touch $SPRING_JAR'  
#Add /test.txt /  
#ADD /spring-mongodb-docker-data-rest-0.1.0.jar /  
#ENTRYPOINT
["java","-Dspring.data.mongodb.uri=mongodb://mongodb/micros","-Djava.security.egd=file:/dev/./urandom","-jar","$SPRING_JAR"]  
#ENTRYPOINT
["java","-Dspring.data.mongodb.uri=mongodb://mongodb/micros","-Djava.security.egd=file:/dev/./urandom","-jar","spring-
mongodb-docker-data-rest-0.1.0.jar"]  
FROM java:8  
# Install maven to build project  
FROM maven:3-jdk-8  
WORKDIR /app  
  
# Add POM and source  
ADD pom.xml /app/pom.xml  
ADD src /app/src  
  
# Build the app  
RUN ["mvn", "clean", "package"]  
  
# Run the app  
#RUN bash -c 'touch /app/target/spring-mongodb-docker-data-rest-0.1.0.jar'  
ENTRYPOINT
["java","-Dspring.data.mongodb.uri=mongodb://mongodb/micros","-Djava.security.egd=file:/dev/./urandom","-jar","/app/target/spring-
mongodb-docker-data-rest-0.1.0.jar"]  

