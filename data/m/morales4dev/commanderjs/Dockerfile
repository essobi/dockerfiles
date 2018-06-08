FROM ubuntu:14.04  
MAINTAINER Alberto Morales Morales @morales4dev "mail@albertomorales.eu"  
RUN apt-get update  
RUN apt-get update --fix-missing  
RUN apt-get install -y curl  
  
RUN curl -sL https://deb.nodesource.com/setup_6.x | sudo -E bash -  
  
RUN sudo apt-get install -y nodejs  
RUN sudo apt-get install -y build-essential  
RUN sudo apt-get install -y git  
  
WORKDIR /home/commander  
  
RUN touch doclone.morales4dev  
  
RUN git clone https://github.com/alberto-morales/commanderJS.git  
  
ADD commander-config.json /home/commander/  
COPY settings.json /home/commander/commanderJS/app/util/  
  
WORKDIR /home/commander/commanderJS  
RUN npm install -y  
  
WORKDIR /home/commander/commanderJS/app  
  
CMD node app.js  

