FROM nginx:alpine  
MAINTAINER Marcio Camurati <marcio.camurati@gmail.com>  
  
RUN rm -rf /usr/share/nginx/html/*  
ADD ./web /usr/share/nginx/html/  
  
WORKDIR /usr/share/nginx/html/data

