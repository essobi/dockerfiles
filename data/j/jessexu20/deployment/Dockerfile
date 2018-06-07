FROM ubuntu:14.04  
MAINTAINER Jesse Xu, sxu11@ncsu.edu  
  
RUN apt-get update  
RUN apt-get -y install git  
RUN apt-get -y install nodejs  
RUN apt-get -y install npm  
RUN apt-get -y install tcl wget  
RUN apt-get -y install vim  
RUN apt-get -y install nodejs-legacy  
RUN wget http://download.redis.io/releases/redis-3.0.0.tar.gz  
RUN tar xzf redis-3.0.0.tar.gz  
WORKDIR redis-3.0.0  
RUN make  
RUN make test  
WORKDIR /  
RUN git clone https://github.com/jessexu20/deployment  
WORKDIR deployment/infrastructure  
RUN pwd  
RUN npm install  
WORKDIR /  
WORKDIR deployment/source  
RUN npm install  
RUN npm install -g bower  
RUN npm install -g grunt  
RUN npm install -g grunt-cli  
RUN bower install --allow-root  
RUN grunt less  
EXPOSE 6379  
EXPOSE 3000-3002  

