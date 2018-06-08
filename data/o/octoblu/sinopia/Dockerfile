FROM node:0.10-onbuild  
EXPOSE 4873  
ENV PATH $PATH:/usr/local/bin  
  
MAINTAINER Octoblu <docker@octoblu.com>  
  
VOLUME /opt/sinopia/storage  
VOLUME /etc/sinopia  
WORKDIR /opt/sinopia  
RUN npm install --verbose sinopia@1.0.1  
RUN cd node_modules/sinopia && npm uninstall fs-ext  
  
CMD ["node", "/opt/sinopia/node_modules/sinopia/bin/sinopia", "--config",
"/etc/sinopia/config.yaml"]  

