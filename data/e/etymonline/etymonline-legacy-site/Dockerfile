FROM ubuntu:12.04  
MAINTAINER Drew Carey Buglione <drew@etymonline.com>  
  
RUN apt-get install -y apache2  
RUN apt-get install -y libapache2-mod-php5 && a2enmod php5  
RUN apt-get install -y php5-mysql  
  
RUN sed -i -e s/"display_errors = Off"/"display_errors = On"/
/etc/php5/apache2/php.ini  
  
ENV APACHE_RUN_USER www-data  
ENV APACHE_RUN_GROUP www-data  
ENV APACHE_LOG_DIR /var/log/apache2  
  
RUN rm -r /var/www/  
ADD . /var/www/  
  
EXPOSE 80  
ENTRYPOINT ["/usr/sbin/apache2"]  
CMD ["-D", "FOREGROUND"]  

