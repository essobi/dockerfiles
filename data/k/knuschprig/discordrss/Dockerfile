FROM ubuntu:16.04  
FROM node:8.2  
LABEL maintainer "knuschprig <contact@knuschprig.ch>"  
  
# Base image setup and important dependencies  
RUN apt-get update && apt-get upgrade -y && apt-get install sudo  
RUN apt-get install npm git -y  
WORKDIR /opt  
RUN git clone https://github.com/synzen/Discord.RSS.git  
WORKDIR /opt/Discord.RSS  
RUN npm install  
RUN chmod 755 /opt/Discord.RSS/*  
RUN useradd -ms /bin/bash feedbot  
RUN chown -R feedbot:root /opt/Discord.RSS/  
  
USER feedbot  
VOLUME ["/opt/Discord.RSS/"]  
WORKDIR /opt/Discord.RSS  
  
CMD [ "npm", "start" ]  

