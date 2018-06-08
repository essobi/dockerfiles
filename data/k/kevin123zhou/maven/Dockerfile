#!Dockerfile  
FROM maven:3.5.0-jdk-8-alpine  
  
RUN mkdir -p /usr/src/app  
VOLUME /usr/src/app  
WORKDIR /usr/src/app  
  
CMD ["mvn","install"]

