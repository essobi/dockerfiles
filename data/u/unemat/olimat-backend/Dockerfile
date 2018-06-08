FROM node:8.4.0-alpine  
MAINTAINER Josias Iquabius <iquabius@gmail.com>  
  
WORKDIR /olimat/api  
  
COPY package.json package-lock.json ./  
  
RUN npm install --quiet  
  
COPY ./public ./public  
COPY ./config ./config  
  
COPY ./src ./src  
  
COPY ./knexfile.js ./knexfile.js  
COPY ./db ./db  
  
CMD npm start  

