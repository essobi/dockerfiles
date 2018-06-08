FROM ubuntu:14.04  
RUN sudo apt-get update && apt-get install -y nodejs npm  
RUN sudo npm install npm -g  
RUN sudo ln -s /usr/bin/nodejs /usr/bin/node  
RUN sudo npm install -g sails  
  
COPY . /testapp  
  
RUN cd /testapp;npm install  
EXPOSE 1337  
WORKDIR /testapp  

