FROM node:latest  
MAINTAINER Svetlana Linuxenko <linuxenko@yahoo.com>  
  
RUN npm install -g ember-cli@1.13.13 bower phantomjs  
  
RUN mkdir /app  
WORKDIR /app  
  
EXPOSE 4200 35729  
CMD ["ember server"]

