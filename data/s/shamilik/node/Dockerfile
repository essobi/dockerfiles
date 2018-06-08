# Build an image of latest stable node  
FROM node  
MAINTAINER Shamil Yakupov <shamilik@yandex.ru>  
  
WORKDIR /usr/src/app  
EXPOSE 3000  
RUN apt-get update && apt-get dist-upgrade -y  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  

