FROM node:6.11  
MAINTAINER Joy Life Services <services@withjoy.com>  
  
RUN mkdir -p /usr/src/app  
RUN chown node:node /usr/src/app  
USER node  
  
WORKDIR /usr/src/app  
  
COPY package.json /usr/src/app  
RUN npm install  
COPY . /usr/src/app  
RUN npm install  
  
CMD ["npm", "start"]  
  

