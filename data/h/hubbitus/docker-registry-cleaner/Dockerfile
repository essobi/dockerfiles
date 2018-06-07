# Multi-stage build https://docs.docker.com/develop/develop-images/multistage-
build/#use-multi-stage-builds  
# 1) stage. Builder image  
#FROM openjdk:10-slim as builder  
FROM openjdk:8-jre-alpine as builder  
  
COPY . /build  
WORKDIR /build  
ENV GRADLE_USER_HOME=./.gradle  
RUN ./gradlew --no-daemon fatJar -S && ./gradlew check --rerun-tasks  
RUN ls /build/build/libs/*  
  
# 2 stage. Final application  
FROM openjdk:8-jre-alpine  
LABEL MAINTAINER="Pavel Alexeev <Pahan@Hubbitus.info>"  
COPY \--from=builder /build/build/libs/*.jar /app/docker-registry-cleaner.jar  
ENTRYPOINT ["java", "-jar", "/app/docker-registry-cleaner.jar"]  

