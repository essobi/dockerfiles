FROM node:4  
MAINTAINER Luiz Coura <luizcoura@gmail.com>  
  
RUN mkdir -p /usr/local/m2k  
COPY . /usr/local/m2k  
  
WORKDIR /usr/local/m2k  
  
RUN npm install  
CMD ["npm", "start"]

