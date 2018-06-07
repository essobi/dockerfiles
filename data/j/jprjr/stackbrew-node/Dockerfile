FROM stackbrew/ubuntu:12.04  
MAINTAINER John Regan <john@jrjrtech.com>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update  
RUN apt-get install -y python-software-properties python g++ make  
RUN add-apt-repository -y ppa:chris-lea/node.js  
RUN apt-get update  
RUN apt-get install -y nodejs  
RUN npm -g install socket.io  
RUN npm -g install forever  
RUN npm -g install coffee-script  
RUN npm -g install express  
RUN npm -g install body-parser  
RUN npm -g install underscore  
RUN npm -g install faye  
RUN npm -g install faye-websocket  
RUN npm -g install redis  
RUN npm -g install faye-redis  
RUN npm -g install request  
RUN npm -g install mysql  
RUN npm -g install ldapjs  
RUN npm -g install winston  
RUN npm -g install winston-elasticsearch  
RUN npm -g install winston-syslog  
RUN npm -g install winston-logstash  
RUN npm -g install primus --save  
  
# Remove things for building modules  
RUN apt-get remove -y manpages manpages-dev g++ gcc cpp make python-software-
properties unattended-upgrades ucf g++-4.6 gcc-4.6 cpp-4.6  
  
RUN useradd -m default  
  
WORKDIR /home/default  
  
USER  default  
ENV HOME /home/default  
ENV NODE_PATH /usr/lib/node_modules  
RUN touch /home/default/.foreverignore  
  
ENTRYPOINT ["forever"]  

