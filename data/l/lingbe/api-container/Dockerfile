FROM ubuntu:14.04  
MAINTAINER lingbe.com  
# Image base for lingbe api:  
# "ubuntu 14.04 dependencies (imagemagic)", "node", and "mongo" in same
container (this can run tests)  
# Inspiration node: https://hub.docker.com/r/jackwfishvision/ubuntu-
node/~/dockerfile/  
# Inspiration mongo: https://hub.docker.com/r/spittet/node-
mongodb/~/dockerfile/  
# Imagemagic crazy dependencies: https://hub.docker.com/r/spittet/node-
mongodb/~/dockerfile/  
  
# Node 6.x steps (apt-get update & curl)  
RUN apt-get update && apt-get install -y curl  
RUN curl -sL https://deb.nodesource.com/setup_6.x | sudo -E bash -  
RUN apt-get install nodejs  
  
# MongoDB steps  
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv EA312927 \  
&& echo "deb http://repo.mongodb.org/apt/debian wheezy/mongodb-org/3.2 main" |
tee /etc/apt/sources.list.d/mongodb-org-3.2.list \  
&& apt-get update \  
&& apt-get install -y mongodb-org --no-install-recommends  
  
# Imagemagic steps  
RUN apt-get install -y \  
# Docker basic ubuntu requeriments for compile node-gyp  
build-essential \  
# Imagemagic prerequisites  
libmagickcore5-extra \  
imagemagick \  
# Imagemagick-native native wrap  
libmagick++-dev \  
  
# Clean  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# Terminal options  
ENV TERM=xterm  
  
## END of Dockerfile  
  
# Inside the container check versions  
# $ mongod --version  
# $ node -v  
# $ npm -v  

