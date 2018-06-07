FROM node:argon-slim  
  
MAINTAINER Steven <ineva@qq.com>  
  
ENV HOME /data  
VOLUME $HOME  
WORKDIR $HOME  
EXPOSE 3000  
RUN npm install -g npm_lazy  
  
COPY config.js /config.js  
  
RUN rm -rf /tmp/*  
  
CMD npm_lazy -c /config.js  

