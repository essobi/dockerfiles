# Version 1.0.0  
FROM ubuntu:16.04  
MAINTAINER Ovidiu Dan <contact@ovidiudan.com>  
  
RUN apt-get update && apt-get -y install \  
openjdk-8-jdk \  
openjdk-8-jre \  
unzip \  
wget  
  
WORKDIR /home  
RUN wget -O carrot2-dcs.zip
https://github.com/carrot2/carrot2/releases/download/release%2F3.12.0/carrot2-dcs-3.12.0.zip  
RUN unzip carrot2-dcs.zip  
  
EXPOSE 8080  
WORKDIR /home/carrot2-dcs-3.12.0  
CMD ./dcs.sh  
  

