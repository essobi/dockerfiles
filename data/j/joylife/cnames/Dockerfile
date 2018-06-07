FROM node:5.11  
MAINTAINER Joy Life Services <services@withjoy.com>  
  
  
RUN mkdir -p /usr/src/app  
WORKDIR /usr/src/app  
  
COPY cnames/package.json /usr/src/app  
RUN npm install  
COPY cnames /usr/src/app  
  
CMD ["npm", "start"]  

