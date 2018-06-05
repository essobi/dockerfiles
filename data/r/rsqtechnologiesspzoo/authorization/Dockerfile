FROM gradle:4.6.0-jdk8-alpine as builder  
COPY . /home/gradle/project  
WORKDIR /home/gradle/project  
USER root  
RUN gradle bootRepackage  
  
FROM develar/java:latest  
COPY \--from=builder /home/gradle/project/build/libs/project-0.10.0.jar
/app.jar  
ENTRYPOINT exec java -Djava.security.egd=file:/dev/./urandom
-Dfile.encoding=UTF-8 -jar $JAVA_OPTS /app.jar  
  

