FROM node:4.4.7-wheezy  
MAINTAINER Chuka Ofili <chuka.ofili@deliveryscience.co>  
MAINTAINER Sola Ajayi <sola@varsoftng.com>  
RUN rm /bin/sh && ln -s /bin/bash /bin/sh  
RUN echo 'debconf debconf/frontend select Noninteractive' | debconf-set-
selections  
  
RUN mkdir -p /www  
WORKDIR /www  
  
ADD application/package.json /www/package.json  
RUN npm install -quiet \  
&& npm cache clear;  
RUN npm install -g sails;  
  
ADD application /www  
  
CMD ["npm", "start"]

