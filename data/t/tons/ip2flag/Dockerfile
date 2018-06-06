FROM openjdk:8-jdk-alpine as builder  
WORKDIR /app  
ADD . /app  
RUN ./gradlew -DskipTests clean bootJar  
  
FROM openjdk:8-jre-alpine  
WORKDIR /app  
COPY \--from=builder /app/build/libs/*-SNAPSHOT.jar .  
CMD java -jar *.jar  

