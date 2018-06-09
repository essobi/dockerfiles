FROM ubuntu:trusty  
MAINTAINER Kristian Drucker  
  
RUN apt-get update  
RUN apt-get upgrade -y  
RUN apt-get install -y openjdk-7-jre wget  
  
WORKDIR /tmp  
  
RUN wget http://subsonic.org/download/subsonic-6.0.deb  
RUN dpkg -i subsonic-6.0.deb  
  
EXPOSE 4040  
CMD ['ping 127.0.0.1']  

