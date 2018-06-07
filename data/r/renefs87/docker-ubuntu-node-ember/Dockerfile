FROM ubuntu:14.04  
RUN apt-get -y update  
RUN apt-get -y install git sudo make gcc tar curl bzip2 libfreetype6
libfontconfig  
  
# Note the new setup script name for Node.js v0.12  
RUN curl -sL https://deb.nodesource.com/setup_4.x | sudo bash -  
  
# Then install with:  
RUN apt-get install -y nodejs  
  
RUN npm install -g ember-cli  
  
RUN npm install -g bower  
  
RUN npm install -g phantomjs-prebuilt

