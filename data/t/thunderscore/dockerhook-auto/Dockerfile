FROM debian:jessie  
  
MAINTAINER Test <test@example.com>  
  
RUN apt-get update && apt-get -y install apache2 && apt-get clean  
  
ENV APACHE_RUN_USER www-data  
ENV APACHE_RUN_GROUP www-data  
ENV APACHE_LOG_DIR /var/log/apache2  
COPY htdocs /var/www/html  
  
EXPOSE 80  
CMD ["/usr/sbin/apache2ctl", "-D", "FOREGROUND"]  

