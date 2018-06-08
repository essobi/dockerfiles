FROM node:alpine  
MAINTAINER Rachyandco  
  
RUN apk add --update git  
  
RUN mkdir -p /var/www  
  
WORKDIR /var/www  
  
RUN git clone https://github.com/jbaylina/referendum_cat_mirror.git  
RUN npm install -g http-server  
  
EXPOSE 8080  
CMD ["http-server"]  

