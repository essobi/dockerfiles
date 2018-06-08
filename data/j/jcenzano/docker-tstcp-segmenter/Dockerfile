# Generate a docker for ts tcp segmenter  
# by Jordi Cenzano  
# VERSION 1.0.0  
FROM ubuntu:16.04  
MAINTAINER jordi.cenzano@gmail.com  
  
# Update  
RUN apt-get update -y  
  
# Upgrade  
RUN apt-get upgrade -y  
  
# Install curl  
RUN apt-get install curl -y  
  
# Install git  
RUN apt-get install git -y  
  
# Install nodejs  
RUN curl -sL https://deb.nodesource.com/setup_6.x | bash - && \  
apt-get install nodejs -y  
  
# Install node source code for segmenter  
RUN git clone https://github.com/jordicenzano/transport-stream-online-
segmenter.git && \  
cd /transport-stream-online-segmenter && \  
npm install --production  
  
# Clean up  
RUN apt-get clean  
  
# Start  
ENTRYPOINT ["/transport-stream-online-segmenter/./transport-stream-segmenter-
tcp.js"]

