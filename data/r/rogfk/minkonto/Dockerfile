FROM node AS node  
WORKDIR /src/client  
COPY client .  
RUN yarn install && yarn build  
  
FROM gradle:jdk8-alpine as java  
USER root  
COPY . .  
COPY \--from=node /src/client/build/ src/main/resources/public/  
RUN gradle --no-daemon build  
  
  
FROM openjdk:8-jre-alpine  
COPY \--from=java /home/gradle/build/libs/minkonto*.jar /data/app.jar  
CMD ["java", "-jar", "/data/app.jar"]

