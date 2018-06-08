#start from ubuntu  
FROM ubuntu:16.04  
MAINTAINER Mees van Dijk  
  
RUN apt-get update  
  
#install dependencies  
RUN apt-get install -y ffmpeg  
RUN apt-get install -y python2.7  
RUN apt-get install -y curl  
RUN apt-get install -y git  
RUN apt-get install -y build-essential  
  
#install node  
RUN curl -sL https://deb.nodesource.com/setup_6.x | bash -  
RUN apt-get install -y nodejs  
  
#set PYTHON env variable  
ENV PYTHON /usr/bin/python2.7  
#setup WORKDIR  
RUN mkdir -p /usr/app  
WORKDIR /usr/app  
  
#get source  
RUN git clone https://github.com/mees-/musicDerp.git .  
  
#install grunt-cli for compiling source  
RUN npm install -g grunt-cli  
  
#get node_modules  
RUN npm install node-opus  
RUN npm install discord.js  
RUN npm install  
  
#compile the source  
RUN grunt build  
  
#entry  
CMD ["npm","start"]  

