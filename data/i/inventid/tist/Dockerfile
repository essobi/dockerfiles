FROM node:8.9  
MAINTAINER Rogier Slag <rogier@inventid.nl>  
  
RUN apt-get update && \  
apt-get install git curl unzip make gcc libpq-dev -y && \  
apt-get autoremove -y && \  
apt-get clean  
  
RUN mkdir /opt/tist  
RUN mkdir /opt/tist/migrations  
RUN mkdir /opt/tist/src  
  
VOLUME ["/opt/tist/config"]  
EXPOSE 9080  
ADD .babelrc /opt/tist/  
  
RUN npm install -g babel-cli babel-preset-es2015 pm2 yarn  
  
# Add the dependencies  
ADD package.json /opt/tist/package.json  
RUN cd /opt/tist && yarn install  
  
# Add the application  
ADD migrations /opt/tist/migrations/  
ADD *.js /opt/tist/src/  
RUN cd /opt/tist/src && babel -d ../ *.js  
ADD assets/ /opt/tist/assets/  
  
# Add the git sha thing  
ADD .git/refs/heads/master /opt/tist/_version  
  
# Run the entire thing!  
WORKDIR /opt/tist  
CMD ["/usr/local/bin/pm2", "start", "index.js", "--no-daemon", "--
instances=max"]  
  

