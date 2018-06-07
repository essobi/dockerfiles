FROM node:6  
MAINTAINER Jabed Bangali <jabedhasan21@gmail.com>  
  
RUN mkdir -p /usr/api  
COPY . /usr/api  
WORKDIR /usr/api  
RUN npm install --production  
  
ENV PORT 3000  
EXPOSE $PORT  
  
CMD ["node", "./bin/www"]  

