FROM ubuntu:16.04  
MAINTAINER Matteo Crippa @ghego20  
  
# Env  
ENV HOME /root  
ENV WORK_DIR /root/node  
  
# Set WORKDIR  
WORKDIR ${WORK_DIR}  
  
# Set Volume  
VOLUME ${WORK_DIR}  
  
# Update distro  
RUN apt-get update  
RUN apt-get upgrade -y  
RUN apt-get install -y wget  
RUN apt-get install -y curl  
RUN apt-get install -y vim  
RUN apt-get install -y git  
RUN apt-get install build-essential -y  
RUN apt-get autoremove -y  
RUN apt-get autoclean -y  
RUN apt-get clean -y  
  
# Install NodeJS  
RUN wget -qO- https://deb.nodesource.com/setup_7.x | sh  
RUN apt-get update  
RUN apt-get install nodejs -y  
  
# Install libjs  
RUN apt-get install libjpeg-turbo8 -y  
RUN apt-get install libjpeg-turbo8-dev -y  
RUN apt-get install giflib-tools -y  
RUN apt-get install libpng16-16 -y  
RUN apt-get install libpng16-dev -y  

