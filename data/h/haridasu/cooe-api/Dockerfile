FROM node:6.9.4  
MAINTAINER Srihari Rao <harirao3@gmail.com>  
  
RUN npm install pm2 -g  
  
# use cached layer for node modules  
ADD package.json /tmp/package.json  
RUN cd /tmp && npm install  
RUN mkdir -p /usr/src && cp -a /tmp/node_modules /usr/src/  
  
# add project files  
WORKDIR /usr/src  
ADD . /usr/src  
  
EXPOSE 8080  
CMD ["pm2-dev", "./bin/www"]  

