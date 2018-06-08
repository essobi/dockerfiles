#FROM maven:3.5.2-jdk-8  
#VOLUME /root/.m2  
#WORKDIR /repo  
#ADD . /repo  
#RUN mvn --settings ./settings.xml clean package  
FROM vinacex/vinacex:profile-initial as build  
WORKDIR /repo  
ADD . /repo  
RUN mvn --settings ./settings.xml clean package  
  
FROM openjdk:8-jdk-alpine  
VOLUME /tmp  
COPY \--from=build /repo/service/target/profile-service-1.0-SNAPSHOT.jar
app.jar  
ENTRYPOINT ["java", "-Djava.security.egd=file:/dev/./urandom", "-jar",
"/app.jar", "--spring.profiles.active=production"]  

