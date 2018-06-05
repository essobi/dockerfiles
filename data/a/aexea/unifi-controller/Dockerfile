FROM debian:jessie  
MAINTAINER Aexea Carpentry  
  
RUN apt-get update && apt-get install -y wget openjdk-7-jre-headless binutils
mongodb-server jsvc unzip  
RUN mkdir -p /opt  
WORKDIR /opt  
RUN wget https://www.ubnt.com/downloads/unifi/5.3.8/UniFi.unix.zip  
RUN unzip UniFi.unix.zip  
WORKDIR /opt/UniFi  
  
EXPOSE 8443 8080  
CMD ["java", "-jar", "lib/ace.jar", "start"]  

