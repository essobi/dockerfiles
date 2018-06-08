FROM dockerfile/nodejs  
  
MAINTAINER goldeneggg  
  
# install coffee, hubot  
RUN npm install -g coffee-script hubot  
  
# install redis  
RUN apt-get update -y  
RUN apt-get install -y redis-server  
  
# create hubot  
WORKDIR /root  
RUN hubot --create mybot  
WORKDIR /root/mybot  
RUN npm install  

