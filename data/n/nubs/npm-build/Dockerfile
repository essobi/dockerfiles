FROM alpine:3.4  
MAINTAINER Spencer Rinehart <anubis@overthemonkey.com>  
  
RUN apk add --no-cache --virtual .nodejs nodejs  
  
RUN mkdir /code  
WORKDIR /code  
  
# Setup PATH to prioritize local npm bin ahead of system PATH.  
ENV PATH node_modules/.bin:$PATH  
  
CMD ["npm", "install"]  

