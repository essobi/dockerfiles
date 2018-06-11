# Version: 0.0.1  
FROM ubuntu:14.10  
MAINTAINER James Turnbull "james@example.com"  
ENV REFRESHED_AT 2015-04-16  
RUN apt-get update  
RUN apt-get install -y nginx  
RUN echo 'Hi, I am in your container' > /usr/share/nginx/html/index.html  
EXPOSE 80  

