FROM node:7.0-slim  
MAINTAINER Oliver Lineham <requests@fyi.org.nz>  
  
RUN mkdir /opt/alaveteli-squeaker  
WORKDIR /opt/alaveteli-squeaker  
  
ADD . /opt/alaveteli-squeaker  
RUN npm install  
  
CMD node /opt/alaveteli-squeaker/index.js

