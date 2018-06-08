# Version: 0.0.1  
FROM ubuntu:14.04  
MAINTAINER hzlu "hzlu2010@gmail.com"  
RUN apt-get update  
  
RUN apt-get install -y nginx  
RUN apt-get install -y vim  
  
RUN echo 'Hi, I am in your container' > /usr/share/nginx/html/index.html  
  
EXPOSE 80  

