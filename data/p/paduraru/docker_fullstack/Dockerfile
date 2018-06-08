FROM ubuntu:14.04  
MAINTAINER Andrei Paduraru <andrei.paduraru@qualitance.com>  
RUN rm /bin/sh && ln -s /bin/bash /bin/sh  
  
#Install needed programs  
RUN apt-get update && apt-get install -y build-essential curl openssh-server
supervisor git  
  
#Make directories for supervisor  
RUN mkdir -p /var/run/sshd /var/log/supervisor  
  
#install mongo  
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 7F0CEB10  
RUN echo "deb http://repo.mongodb.org/apt/ubuntu trusty/mongodb-org/3.0
multiverse" | tee /etc/apt/sources.list.d/mongodb-org-3.0.list  
RUN apt-get update && \  
apt-get install -y mongodb-org && \  
mkdir -p /data/db  
  
#Install node js via nvm  
ENV NVM_DIR /usr/local/nvm  
ENV NODE_VERSION 0.12.7  
#install nvm  
RUN cd /home && curl
https://raw.githubusercontent.com/creationix/nvm/v0.28.0/install.sh | bash \  
&& source $NVM_DIR/nvm.sh \  
&& nvm install $NODE_VERSION \  
&& nvm alias default $NODE_VERSION \  
&& nvm use default  
#RUN ls $NVM_DIR  
ENV NODE_PATH $NVM_DIR/versions/node/v$NODE_VERSION/lib/node_modules  
ENV PATH $NVM_DIR/versions/node/v$NODE_VERSION/bin:$PATH  
RUN node -v  
RUN npm -v  
  
#install ruby  
RUN apt-get install -y ruby-full  
  
#install sass  
RUN gem install sass  
  
#Install bower  
RUN npm install -g bower  
  
#Install grunt  
RUN npm install -g grunt-cli  
  
#Install yeoman  
RUN npm install -g yo@~1.2.x  
  
#Install angular fullstack generator  
RUN npm install -g generator-angular-fullstack@2.1.1  
  
#install graphics magick  
RUN apt-get install -y graphicsmagick  
  
#DONE  

