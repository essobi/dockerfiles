FROM ubuntu:12.04  
MAINTAINER Somesh Yadav<somesh.yadav@imaginea.com>  
  
RUN apt-get update  
RUN apt-get install -y apache2  
RUN apt-get install -y nmap  
  
ENV APACHE_RUN_USER www-data  
ENV APACHE_RUN_GROUP www-data  
ENV APACHE_LOG_DIR /var/log/apache2  
  
EXPOSE 80  
CMD ["/usr/sbin/apache2", "-D", "FOREGROUND"]  

