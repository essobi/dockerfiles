FROM ubuntu:latest  
MAINTAINER miracler "1821518966@qq.com"  
ENV REFRESHED_AT 2016-2  
RUN apt-get update -y  
RUN apt-get install nginx -y  
RUN mkdir -p /var/www/nginx  
ADD nginx/global.conf /etc/nginx/conf.d/  
ADD nginx/nginx.conf /etc/nginx/nginx.conf  
RUN echo "sample" > /usr/share/nginx/html/index.html  
EXPOSE 80  

