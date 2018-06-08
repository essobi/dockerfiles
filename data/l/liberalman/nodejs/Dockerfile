FROM node:7  
MAINTAINER Liberalman <zscchina@163.com>  
  
# Pre-install npm packages  
RUN npm install -g node-gyp && \  
npm install -g pm2 && \  
npm cache clean && \  
rm -rf /tmp/* /var/tmp/*  
  
RUN mkdir -p /var/www  
  
ONBUILD WORKDIR /var/www  
ONBUILD COPY . /var/www  
ONBUILD RUN npm i --production  
ONBUILD CMD ["npm", "start"]  

