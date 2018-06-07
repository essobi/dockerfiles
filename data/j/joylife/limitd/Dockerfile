FROM node:6.9.4  
MAINTAINER Joy Life Services <services@withjoy.com>  
VOLUME /var/limitddb  
EXPOSE 9231  
RUN mkdir /usr/src/app  
  
WORKDIR /usr/src/app  
  
#copy package.json and install dependencies  
COPY package.json /usr/src/app/package.json  
RUN cd /usr/src/app && npm install  
  
COPY limitd.config /etc/limitd.config  
CMD cd /usr/src/app && npm start  

