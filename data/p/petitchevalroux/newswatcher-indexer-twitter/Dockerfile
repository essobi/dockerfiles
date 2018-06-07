FROM node:4  
MAINTAINER Patrick Poulain <docker@m41l.me>  
RUN mkdir -p /opt/app  
ADD . /opt/app  
RUN mkdir -p /opt/app/config  
ADD ./config/docker.json /opt/app/config/default.json  
RUN cd /opt/app && \  
npm install --production  
WORKDIR /opt/app  
CMD ["npm", "start"]

