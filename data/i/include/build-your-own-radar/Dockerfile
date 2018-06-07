FROM node:7.10.0  
#FROM node:8.9.1  
MAINTAINER include <francisco.cabrita@gmail.com>  
  
ADD ./ /app  
  
RUN npm install && npm rebuild node-sass  
  
EXPOSE 8080  
WORKDIR /app  
  
CMD ["npm","run","dev"]  

