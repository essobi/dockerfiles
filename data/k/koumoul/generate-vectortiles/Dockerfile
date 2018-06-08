FROM node:8  
MAINTAINER Lukas Martinelli <me@lukasmartinelli.ch>  
  
WORKDIR /usr/src/app  
COPY package.json .  
RUN npm install  
  
VOLUME /tm2source /export  
ENV SOURCE_PROJECT_DIR=/tm2source EXPORT_DIR=/export
TILELIVE_BIN=/usr/src/app/node_modules/.bin/tl  
  
COPY . /usr/src/app/  
CMD ["/usr/src/app/export-local.sh"]  

