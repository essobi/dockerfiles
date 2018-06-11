FROM debian:wheezy  
MAINTAINER Julian Ospald <hasufell@posteo.de>  
  
RUN dpkg --add-architecture i386 && \  
apt-get update && \  
apt-get install --no-install-recommends --assume-yes wine && \  
rm -rf /var/lib/apt/lists/*  
  
RUN useradd -m -d /home/wine wine  
  
ENV DISPLAY :0  

