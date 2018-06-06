FROM ubuntu:16.04  
MAINTAINER Chris Sim <chris.sim@dailyvanity.sg>  
  
RUN apt-get -y update && apt-get install -y python-software-properties
software-properties-common  
  
RUN apt-get install -y \  
build-essential \  
imagemagick \  
libpcre3 \  
git \  
rsyslog \  
curl \  
wget \  
nano \  
vim  
  
WORKDIR /tmp  
  
RUN wget https://deb.nodesource.com/setup_6.x  
RUN chmod +x setup_6.x  
RUN ./setup_6.x  
RUN curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add -  
RUN echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee
/etc/apt/sources.list.d/yarn.list  
  
RUN apt-get -y update && apt-get -y install nodejs yarn && apt-get -y upgrade  
RUN npm install -g bower webpack gulp-cli grunt-cli  
  
RUN apt-get autoclean && apt-get autoremove && apt-get clean && rm -rf
/var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
EXPOSE 80 1337  
WORKDIR /var/www/html  
VOLUME /var/www/html  
  
CMD node app.js

