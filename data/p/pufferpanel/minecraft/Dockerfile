# Dockerfile for running a Java based Minecraft server using pufferd.  
FROM openjdk:8-alpine  
  
RUN adduser -D -h /server pufferd  
WORKDIR /server  
  
RUN apk add \--no-cache \--virtual=.run-deps git  
# Add any additional commands here  
  
USER pufferd  
ENV HOME /server  

