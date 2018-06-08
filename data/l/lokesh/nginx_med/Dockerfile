#VERSION 1.0  
FROM ubuntu:latest  
MAINTAINER Lokeshwar R Vangala "lokesh.reddy@microfocus.com"  
ENV REFRESHED_AT 19-11-2016  
RUN apt-get -yq update  
RUN apt-get -yq install nginx  
RUN mkdir -p /var/www/html/  
ADD conf/global.conf /etc/nginx/conf.d/  
ADD conf/nginx.conf /etc/nginx/nginx.conf  
EXPOSE 80  
ENTRYPOINT ["/usr/sbin/nginx"]  

