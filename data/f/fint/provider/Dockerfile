FROM gradle:4.2.1-jdk8-alpine as builder  
USER root  
COPY . .  
RUN gradle --no-daemon build  
  
FROM openjdk:8-jre-alpine  
COPY \--from=builder /home/gradle/build/deps/external/*.jar /data/  
COPY \--from=builder /home/gradle/build/deps/fint/*.jar /data/  
COPY \--from=builder /home/gradle/build/libs/fint-provider-*.jar /data/fint-
provider.jar  
CMD ["java", "-jar", "/data/fint-provider.jar"]  

