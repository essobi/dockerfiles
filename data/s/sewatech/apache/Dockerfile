FROM debian:jessie  
  
RUN apt-get update && apt-get install -y apache2 && apt-get clean  
  
ENV APACHE_RUN_USER www-data  
ENV APACHE_RUN_GROUP www-data  
ENV APACHE_LOG_DIR /var/log/apache2  
  
ADD html/ /var/www/html/  
  
EXPOSE 80  
ENTRYPOINT ["/usr/sbin/apache2ctl"]  
CMD ["-D", "FOREGROUND"]  

