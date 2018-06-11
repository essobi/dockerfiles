FROM ubuntu:15.10  
MAINTAINER Elvin Tan <elvin@elvin.net>  
RUN apt-get -y update  
RUN apt-get install -y nginx  
RUN mkdir -p /www  
RUN mkdir -p /var/lib/nginx  
COPY index.html /www/index.html  
COPY nginx.conf /etc/nginx/nginx.conf  
VOLUME ["/www"]  
EXPOSE 80  
CMD ["nginx"]  

