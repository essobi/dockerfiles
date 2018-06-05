FROM node:alpine  
  
MAINTAINER Shingo Hisakawa shingohisakawa@gmail.com  
  
RUN apk add --update openrc alpine-sdk make cmake gcc g++ gfortran python py-
pip python-dev libpcap-dev  
RUN apk add vim emacs  
RUN npm install forever -g  
RUN npm install node-dash-button  
  
ADD dash.js /  
ADD start.sh /  
  
ENTRYPOINT /start.sh  

