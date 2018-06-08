# Build an image of latest stable nginx  
FROM nginx  
MAINTAINER Shamil Yakupov <shamilik@yandex.ru>  
  
RUN apt-get update && apt-get dist-upgrade -y  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

