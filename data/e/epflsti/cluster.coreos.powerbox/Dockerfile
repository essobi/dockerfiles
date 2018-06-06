FROM node:latest  
MAINTAINER Dominique Quatravaux <dominique.quatravaux@epfl.ch>  
  
RUN mkdir /powerbox  
ADD etcd-mirror /powerbox/etcd-mirror  
RUN rm -rf /powerbox/node_modules  
ADD app.js /powerbox/app.js  
ADD package.json /powerbox/package.json  
  
WORKDIR /powerbox  
RUN npm install  
CMD node app.js  
  

