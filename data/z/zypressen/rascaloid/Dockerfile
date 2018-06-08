FROM maven:3.5.2-jdk-8 AS build  
  
RUN mkdir -p /rascaloid  
  
WORKDIR /rascaloid  
  
ADD ./ ./  
  
RUN mvn dependency:go-offline  
  
FROM openjdk:8-alpine  
  
COPY \--from=build /rascaloid/ /rascaloid/  
  
WORKDIR /rascaloid  
  
ENTRYPOINT ["java", "-cp", "rascaloid.jar:runtime/*",
"net.unit8.rascaloid.Main"]  
  

