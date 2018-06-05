FROM ubuntu:latest  
MAINTAINER M. Arif Wicaksana <arif@belalangtempur.com>  
  
RUN apt-get update && apt-get install -y apache2  
  
EXPOSE 80  
CMD ["/usr/sbin/apache2ctl", "-D", "FOREGROUND"]  
  

