FROM alpine:3.3  
MAINTAINER Chris Saunders <slapheadted@gmail.com>  
  
COPY . /code  
  
WORKDIR /code  
  
RUN apk add git --update  
  
RUN apk add nodejs --update  
  
RUN npm install -g gulp@3.9.1  
  
RUN npm install -g bower@1.7.7  
  
RUN npm install  
  
RUN bower --allow-root install -g  
  
CMD gulp serve  

