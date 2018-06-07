FROM golang:latest  
MAINTAINER Liam Galvin <liam.galvin@switchconcepts.com>  
  
RUN apt-get update  
RUN apt-get install -y dejavu-* pulseaudio  
RUN wget https://dl.google.com/linux/direct/google-chrome-
beta_current_amd64.deb  
RUN dpkg -i google-chrome*.deb || apt-get install -f -y  
  

