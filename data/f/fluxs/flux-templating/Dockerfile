FROM node:4.2  
MAINTAINER Alban Mouton <alban.mouton@gmail.com>  
  
RUN mkdir -p /usr/src/app  
WORKDIR /usr/src/app  
  
COPY package.json /usr/src/app/  
RUN npm install --production \  
&& npm cache clean  
COPY . /usr/src/app/  
  
EXPOSE 3111  
CMD node server.js  

