FROM openjdk:8-alpine  
  
# general needed stuff  
RUN apk update && \  
apk add curl openssh-client bash  
  
# install maven and project dependecies  
COPY pom.xml ./  
RUN apk add maven && \  
mvn dependency:go-offline  
  
# install postgres  
ENV PGDATA /var/lib/postgresql/data  
RUN apk add postgresql

