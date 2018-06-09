# Pull of Ubuntu 12.04 TLS  
FROM ubuntu:12.04  
MAINTAINER Laurent Borensky version: 0.1  
RUN apt-get update  
RUN apt-get install -y apache2  
  
ENV APACHE_RUN_USER www-data  
ENV APACHE_RUN_GROUP www-data  
ENV APACHE_LOG_DIR /var/log/apache2  
  
ADD ./info.php /var/www/info.php  
  
EXPOSE 80  
ENTRYPOINT ["/usr/sbin/apache2"]  
CMD ["-D", "FOREGROUND"]  

