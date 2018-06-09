# Version: 0.0.1  
FROM ubuntu:latest  
MAINTAINER Torsten Kramer "tk@nowhere.nil"  
RUN apt-get update && apt-get install -y nginx  
RUN echo 'Hi, I am in your containter' >/var/www/html/index.html  
ENTRYPOINT ["/usr/sbin/nginx"]  
CMD ["-h"]  
EXPOSE 80  

