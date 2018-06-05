FROM ianedington/wordpress:php7  
MAINTAINER Ian Edington <IanEdington@gmail.com>  
ENV REFRESHED_AT 2016-06-13  
# Install packages  
ENV DEBIAN_FRONTEND noninteractive  
RUN apt-get update && apt-get install -y \  
apache2 \  
libapache2-mod-php \  
phpmyadmin \  
php-xdebug \  
supervisor;  
  
# Add image configuration and scripts  
ADD run.sh /run.sh  
ADD apache.sh /apache.sh  
ADD start-apache2.sh /start-apache2.sh  
RUN chmod 755 /*.sh;  
  
# Configure Apache  
RUN echo "ServerName localhost" >> /etc/apache2/apache2.conf;  
# config to enable .htaccess  
ADD apache_default /etc/apache2/sites-available/000-default.conf  
RUN a2enmod rewrite  
  
# Configure phpMyAdmin  
RUN phpenmod -v ALL mcrypt  
RUN ln -s /usr/share/phpmyadmin /var/www/phpmyadmin  
RUN cp /var/www/phpmyadmin/config.sample.inc.php
/var/www/phpmyadmin/config.inc.php  
  
# supervisord services  
ADD supervisord-apache2.conf /etc/supervisor/conf.d/supervisord-apache2.conf  
  
# Configure /app folder with sample app  
ADD app/ /app  
RUN mkdir -p /app && rm -fr /var/www/html && ln -s /app /var/www/html  
  
# php-apache config variables  
ENV PHP_UPLOAD_MAX_FILESIZE 10M  
ENV PHP_POST_MAX_SIZE 10M  
  
# xdebug config variables  
ENV XDEBUG_REMOTE_HOST 192.168.99.1  
ENV XDEBUG_REMOTE_PORT 9000  
EXPOSE 80  
CMD ["/run.sh"]  

