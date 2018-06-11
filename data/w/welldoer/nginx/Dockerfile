FROM ubuntu:14.04  
MAINTAINER welldoer  
ENV REFRESHED_AT 2015-12-05  
RUN apt-get update  
RUN apt-get -y -q install nginx  
RUN mkdir -p /var/www/html  
ADD nginx/global.conf /etc/nginx/conf.d/  
ADD nginx/nginx.conf /etc/nginx/nginx.conf  
EXPOSE 80  

