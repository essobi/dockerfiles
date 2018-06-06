# Generate a docker for webserver that uses chunked files on growing files  
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
RUN git clone https://github.com/jordicenzano/webserver-chunked-
growingfiles.git && \  
cd /webserver-chunked-growingfiles && \  
npm install --production  
  
# Clean up  
RUN apt-get clean  
  
# Start  
ENTRYPOINT ["/webserver-chunked-growingfiles/./index.js"]  
CMD ["-p 8080"]

