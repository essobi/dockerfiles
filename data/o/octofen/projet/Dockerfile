FROM ubuntu:latest  
  
RUN apt-get update && apt-get -y upgrade && DEBIAN_FRONTEND=noninteractive
apt-get -y install \  
apache2 php7.0 php7.0-mysql libapache2-mod-php7.0 curl lynx-cur  
  
RUN a2enmod php7.0  
RUN a2enmod rewrite  
  
RUN sed -i "s/short_open_tag = Off/short_open_tag = On/"
/etc/php/7.0/apache2/php.ini  
RUN sed -i "s/error_reporting = .*$/error_reporting = E_ERROR | E_WARNING |
E_PARSE/" /etc/php/7.0/apache2/php.ini  
  
ENV APACHE_RUN_USER www-data  
ENV APACHE_RUN_GROUP www-data  
ENV APACHE_LOG_DIR /var/log/apache2  
ENV APACHE_LOCK_DIR /var/lock/apache2  
ENV APACHE_PID_FILE /var/run/apache2.pid  
  
RUN echo "ServerName localhost" >> /etc/apache2/httpd.conf  
RUN echo "ServerName localhost" >> /etc/apache2/apache2.conf  
  
EXPOSE 80  
ADD www /var/www/site  
  
ADD apache-config.conf /etc/apache2/sites-enabled/000-default.conf  
  
CMD /usr/sbin/apache2ctl -D FOREGROUND  

