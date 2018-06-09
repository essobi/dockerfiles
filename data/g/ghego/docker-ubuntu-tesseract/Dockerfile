FROM ubuntu:16.04  
MAINTAINER Matteo Crippa @ghego20  
  
# Env  
ENV HOME /root  
ENV WORK_DIR /root/node  
  
# Set WORKDIR  
WORKDIR ${WORK_DIR}  
  
# Set Volume  
VOLUME ${WORK_DIR}  
  
# Update ubuntu  
RUN apt-get update  
RUN apt-get upgrade -y  
RUN apt-get install -y wget  
RUN apt-get install -y unzip  
RUN apt-get install -y vim  
RUN apt-get install -y git  
RUN apt-get install -y build-essential cmake  
RUN apt-get autoremove -y  
RUN apt-get autoclean -y  
RUN apt-get clean -y  
RUN apt-get install software-properties-common -y  
  
# Install NodeJS  
RUN wget -qO- https://deb.nodesource.com/setup_7.x | sh  
RUN apt-get update  
RUN apt-get install nodejs -y  
  
# Install Image libs  
RUN apt-get install -y zlib1g-dev libjpeg-dev libwebp-dev libpng-dev
libtiff5-dev libjasper-dev libopenexr-dev libgdal-dev  
  
# Install Tesseract  
RUN apt-get install -y tesseract-ocr tesseract-ocr-all  
RUN apt-get install -y imagemagick  
  

