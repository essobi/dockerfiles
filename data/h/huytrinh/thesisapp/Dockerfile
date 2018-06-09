FROM node:latest  
  
MAINTAINER HuyTrinh trinhphandinhhuy@gmail.com  
  
RUN mkdir -p /usr/src/app  
  
WORKDIR /usr/src/app  
  
COPY . /usr/src/app  
  
RUN cd /usr/src/app  
  
RUN npm install  
  
EXPOSE 3000  
CMD ["node", "/usr/src/app/server/bin/www"]

