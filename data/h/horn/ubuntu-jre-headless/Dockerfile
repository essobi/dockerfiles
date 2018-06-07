FROM ubuntu:trusty  
  
MAINTAINER David Weber  
  
# Helper to add deb file source  
RUN apt-get update -y  
RUN apt-get install software-properties-common -y  
RUN add-apt-repository ppa:openjdk-r/ppa  
RUN apt-get update -y  
RUN apt-get upgrade -y  
RUN apt-get install -y openjdk-8-jre-headless  
  
# The current Open-JDK java 8 has an error in its script...  
ADD cacerts /etc/ssl/certs/java/  
  

