# Pull base image.  
FROM ubuntu:14.04  
MAINTAINER colin.hom@thebetterfoundation.com  
  
# Install base packages  
RUN apt-get update  
RUN apt-get upgrade -y  
RUN apt-get install -y nodejs nodejs-legacy npm imagemagick git  
  
# Install nodebb  
RUN cd /opt && git clone -b v0.7.x https://github.com/NodeBB/NodeBB nodebb  
  
# Define working directory.  
WORKDIR /opt/nodebb  
  
RUN npm install  
  
EXPOSE 4567  
ADD ./entrypoint.bash ./  
  
ENTRYPOINT ./entrypoint.bash  
  

