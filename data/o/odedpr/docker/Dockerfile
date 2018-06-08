# VERSION 0.0.1  
FROM ubuntu:12.04  
MAINTAINER Oded Priva "oded@devops.co.il"  
RUN apt-get update  
RUN apt-get install -y nginx  
RUN rm -v /etc/nginx/nginx.conf  
ADD nginx.conf /etc/nginx/  
RUN echo "daemon off;" >> /etc/nginx/nginx.conf  
EXPOSE 80  
CMD service nginx start  

