# file: Dockerfile (git checkout step-02)  
FROM openjdk:8u121-jdk-alpine  
  
WORKDIR /build-env  
ADD . /build-env  
RUN ./gradlew build  
  
RUN mkdir -p /app  
RUN cp /build-env/build/libs/teamstaffer-service-1.0.0-SNAPSHOT.jar
/app/teamstaffer-service.jar  
RUN rm -rf /build-env  
  
EXPOSE 8080  
CMD java -jar /app/teamstaffer-service.jar

