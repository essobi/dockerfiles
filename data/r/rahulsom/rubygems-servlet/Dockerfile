FROM maven:3-jdk-8-alpine  
MAINTAINER Rahul Somasunderam  
  
RUN apk update && apk add git  
WORKDIR /  
RUN git clone https://github.com/torquebox/rubygems-servlets  
  
WORKDIR /rubygems-servlets  
RUN mvn package  
EXPOSE 8989  
CMD mvn jetty:run

