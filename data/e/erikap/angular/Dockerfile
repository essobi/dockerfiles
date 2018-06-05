FROM ubuntu:16.04  
MAINTAINER Erika Pauwels <erika.pauwels@gmail.com>  
  
# Install nodejs as per http://askubuntu.com/questions/672994/how-to-install-
nodejs-4-on-ubuntu-15-04-64-bit-edition  
RUN apt-get -y update; apt-get -y install wget python build-essential git
libfontconfig  
RUN wget -qO- https://deb.nodesource.com/setup_7.x > node_setup.sh  
RUN bash node_setup.sh  
RUN apt-get -y install nodejs \  
&& npm install -g npm@3.10.9  
RUN npm install -g typings @angular/cli@1.0.4  
  
WORKDIR /app  

