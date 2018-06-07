FROM debian:wheezy  
  
MAINTAINER "Dean Mraz" <deanm@runtriz.com>  
  
# Update Package Lists  
RUN apt-get update  
  
# Install laravel required extensions  
RUN apt-get update -y && \  
apt-get install -y \  
php5-cli php5 php-pear \  
php5-mysqlnd php5-pgsql php5-sqlite \  
php5-json php5-curl php5-gd \  
php5-gmp php5-imap php5-mcrypt \  
php5-memcached php5-xdebug  
  
# Configure PHP  
RUN sed -i "s/short_open_tag = Off/short_open_tag = On/"
/etc/php5/apache2/php.ini && \  
sed -i "s/short_open_tag = Off/short_open_tag = On/" /etc/php5/cli/php.ini &&
\  
sed -i "s/;date.timezone =.*/date.timezone = UTC/" /etc/php5/apache2/php.ini
&& \  
sed -i "s/;date.timezone =.*/date.timezone = UTC/" /etc/php5/cli/php.ini && \  
sed -i "s/display_errors = Off/display_errors = stderr/"
/etc/php5/apache2/php.ini && \  
sed -i "s/upload_max_filesize = 2M/upload_max_filesize = 30M/"
/etc/php5/apache2/php.ini && \  
sed -i "s/;opcache.enable=0/opcache.enable=0/" /etc/php5/apache2/php.ini  
  
# install utlities  
RUN apt-get install -y curl zip unzip git mysql-client  
  
## ---- Install PHP Composer  
RUN curl -sS https://getcomposer.org/installer | php && mv composer.phar
/usr/local/bin/composer  
  
# Install apache  
RUN apt-get install -y apache2  
  
## copy apache2 config  
ADD files/apache2.conf /etc/apache2/apache2.conf  
  
## setup sites  
ADD files/site /etc/apache2/sites-available/default  
  
RUN mkdir /var/www/html  
RUN chown www-data.www-data /var/www/html  
RUN echo "<?php phpinfo();" >> /var/www/html/index.php  
  
# Activate a2enmod  
RUN a2enmod rewrite  
  
# Set Apache environment variables (can be changed on docker run with -e)  
ENV APACHE_RUN_USER=www-data \  
APACHE_RUN_GROUP=www-data \  
APACHE_LOG_DIR=/var/log/apache2 \  
APACHE_PID_FILE=/var/run/apache2.pid \  
APACHE_RUN_DIR=/var/run/apache2 \  
APACHE_LOCK_DIR=/var/lock/apache2 \  
APACHE_SERVER_ADMIN=admin@localhost \  
APACHE_SERVER_NAME=localhost \  
APACHE_SERVER_ALIAS=docker.localhost \  
APACHE_DOCUMENT_ROOT=/var/www \  
APACHE_DOCUMENT_PUBLIC=/var/www/html  
  
### ---- Simple startup script to avoid some issues observed with container
restart  
ADD files/run-apache.sh /run-apache.sh  
RUN chmod -v +x /run-apache.sh  
  
## --- Start Apache ---- ##  
EXPOSE 80  
CMD ["/run-apache.sh"]  

