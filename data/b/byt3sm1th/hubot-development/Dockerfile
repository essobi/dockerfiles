FROM node:latest  
MAINTAINER @byt3smith  
  
# Install requirements and clean up after ourselves  
RUN apt-get -q update \  
&& apt-get -qy install git-core redis-server \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# Install hubot and related  
RUN npm install -g hubot yo generator-hubot coffee-script  
  
# Setup a user to run the install  
RUN adduser --disabled-password --gecos "" yeoman  
USER yeoman  
WORKDIR /home/yeoman  
  
# Create hubot  
RUN yo hubot --name hubot-development --description "Hubot" \--adapter slack
--defaults  
  
# Default command to start hubot  
CMD bin/hubot --adapter slack  

