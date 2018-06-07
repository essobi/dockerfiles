FROM node:6  
MAINTAINER Aaroza Developer <developer@aaroza.com>  
  
RUN mkdir -p /usr/api  
COPY . /usr/api  
WORKDIR /usr/api  
RUN npm install --production  
  
ENV PORT 3000  
EXPOSE $PORT  
  
CMD ["node", "./bin/www"]  

