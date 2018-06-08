FROM telegraf:latest  
MAINTAINER Jacob Tomlinson <jacob@tom.linson.uk>  
  
RUN apt-get update -y && apt-get install npm -y && \  
ln -s /usr/bin/nodejs /usr/bin/node  
  
RUN npm install gamedig -g  

