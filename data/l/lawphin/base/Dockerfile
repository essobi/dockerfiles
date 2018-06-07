FROM node:5.5  
MAINTAINER Thaweesak C <thaweesak@lawphin.com>  
  
ENV TERM xterm  
  
RUN apt-get update  
RUN apt-get install -y ruby python  
RUN apt-get install -y libkrb5-dev  
RUN apt-get install -y nano && export TERM=xterm  
RUN apt-get install -y cron  
  
# ADD crontab /etc/cron.d/lawphin-cron  
# RUN touch /var/log/test  
# CMD cron  
RUN npm install -g pm2 node-gyp request async  
RUN pm2 dump  

