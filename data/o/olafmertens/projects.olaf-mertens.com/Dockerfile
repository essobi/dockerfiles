FROM ubuntu:14.04  
MAINTAINER Olaf Mertens "mail@olaf-mertenscom"  
ENV REFRESHED_AT 2015-11-26  
RUN apt-get update  
RUN apt-get install -y nginx  
RUN echo 'This is test website version 3...' >
/usr/share/nginx/html/index.html  
EXPOSE 80  
ENTRYPOINT ["/usr/sbin/nginx", "-g", "daemon off;"]  

