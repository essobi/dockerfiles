FROM node:8.8.1-alpine  
  
MAINTAINER DUONG Dinh Cuong <dinhcuong@ononpay.com>  
  
COPY . /var/www/  
WORKDIR /var/www  
  
RUN apk update \  
&& apk upgrade \  
&& apk add --no-cache bash curl \  
&& cd /var/www && npm install \  
&& rm -rf /var/cache/apk/*  
  
EXPOSE 80  
CMD ["npm", "start"]  
  

