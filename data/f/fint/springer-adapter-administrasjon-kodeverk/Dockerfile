FROM gradle:4.2.1-jdk8-alpine as builder  
USER root  
COPY . .  
RUN gradle --no-daemon build  
  
FROM openjdk:8-jre-alpine  
COPY \--from=builder /home/gradle/build/libs/fint-springer-adapter-
administrasjon-kodeverk-*.jar /data/app.jar  
CMD ["java", "-jar", "/data/app.jar"]

