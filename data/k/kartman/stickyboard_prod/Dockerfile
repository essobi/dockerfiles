FROM node:boron  
  
MAINTAINER Karthic Ashokan "karthicashokan@icloud.com"  
# Add the application resources URL  
# RUN echo "deb http://archive.ubuntu.com/ubuntu/ $(/etc/lsb-release -sc) main
universe" >> /etc/apt/sources.list  
# Update the sources list  
RUN apt-get update  
  
# Copy the application folder inside the container  
ADD . /StickyBoard_prod  
  
# Exposing a web port  
EXPOSE 8080  
# Set the default directory where CMD will execute  
WORKDIR /StickyBoard_prod  
  
# RUN  
CMD set NODE_PATH=/StickyBoard_prod/node_modules  
CMD npm install express --save  
CMD npm install  
CMD webpack  
CMD node server  

