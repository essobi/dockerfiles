############################################################  
# Dockerfile to build Recipe Management Service  
# Based on openjdk:8  
############################################################  
  
FROM openjdk:8  
  
MAINTAINER Erik Hage <ehage4@gmail.com>  
  
ENV TERM xterm  
  
VOLUME /tmp  
  
RUN mkdir -p /usr/src/app  
WORKDIR /usr/src/app  
  
ADD /target/rms-0.0.1-SNAPSHOT.jar rms_app.jar  
  
#Install text editor nano  
RUN ["apt-get", "update"]  
RUN ["apt-get", "install", "-y", "nano"]  
  
RUN sh -c 'touch /rms_app.jar'  
  
EXPOSE 3002

