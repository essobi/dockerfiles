FROM ubuntu:14.04  
MAINTAINER icanfly "lpwork@foxmail.com"  
ENV REFRESHED_AT 2016-09-14  
RUN apt-get update  
RUN apt-get -y -q install nginx  
RUN mkdir -p /var/www/html  
  
ADD nginx/global.conf /etc/nginx/conf.d/  
ADD nginx/nginx.conf /etc/nginx/nginx.conf  
  
EXPOSE 80  
#RUN yum install -y vim  
ADD hello.txt /data/work/hello.txt  
  
RUN echo "OK,everything is done"  

