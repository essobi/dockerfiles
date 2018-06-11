  
FROM ubuntu:16.04  
MAINTAINER executorj@gmail.com  
  
RUN apt update && apt install -y apache2 apache2-utils && apt clean  
  
RUN a2enmod dav dav_fs auth_digest  
RUN a2dissite 000-default  
  
ENV APACHE_RUN_USER www-data  
ENV APACHE_RUN_GROUP www-data  
ENV APACHE_LOG_DIR /var/log/apache2  
ENV APACHE_PID_FILE /var/run/apache2.pid  
ENV APACHE_LOCK_DIR /var/lock/apache2  
ENV APACHE_RUN_DIR /var/run/apache2  
  
RUN mkdir -p /var/lock/apache2; chown www-data /var/lock/apache2  
RUN mkdir -p /var/webdav; chown www-data /var/webdav  
  
RUN mkdir /run/apache2  
  
ADD webdav.conf /etc/apache2/sites-available/webdav.conf  
RUN a2ensite webdav  
  
ADD run.sh /  
  
EXPOSE 80  
CMD ["/run.sh"]  

