FROM node:5.3  
MAINTAINER Rogier Slag <rogier.slag@gmail.com>  
  
RUN apt-get update && \  
apt-get install git curl unzip make gcc -y && \  
apt-get autoremove -y && \  
apt-get clean  
  
RUN mkdir /opt/kafkalytics  
RUN mkdir /opt/kafkalytics/src  
  
VOLUME ["/opt/kafkalytics/config"]  
ADD .babelrc /opt/kafkalytics/  
  
RUN npm install -g babel-cli babel-preset-es2015  
  
# Add the dependencies  
ADD package.json /opt/kafkalytics/package.json  
RUN cd /opt/kafkalytics && npm install  
  
# Add the application  
ADD *.js /opt/kafkalytics/src/  
RUN cd /opt/kafkalytics/src && babel -d ../ *.js  
  
# Add the git sha thing  
ADD .git/refs/heads/master /opt/kafkalytics/_version  
  
# Run the entire thing!  
WORKDIR /opt/kafkalytics  
CMD ["node", "index.js"]  

