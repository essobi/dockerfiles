############################################################  
# Dockerfile to build prestashop apache-php container images  
# Based on phusion/baseimage  
############################################################  
# Set the base image to phusion/baseimage  
FROM phusion/baseimage:latest  
CMD ["/sbin/my_init"]  
  
# File Author / Maintainer  
MAINTAINER Jonathan Temlett - Daedalus Solutions (jono@daedalus.co.za)  
  
RUN apt-get update  
RUN apt-get -y upgrade  
  
# Install apache, PHP, and supplimentary programs. curl and lynx-cur are for
debugging the container.  
RUN DEBIAN_FRONTEND=noninteractive apt-get -y install apache2 libapache2-mod-
php7.0 php php-fpm php-mysql php-zip php-gd php-pear php-apcu php-dev php-json
php-intl php-mcrypt php-mbstring php-curl php-imap curl lynx-cur  
  
# Enable apache mods.  
RUN a2enmod php7.0  
RUN a2enmod rewrite  
  
# Update the PHP.ini file, enable <? ?> tags and quieten logging.  
RUN sed -i "s/^short_open_tag.*/short_open_tag = Off/"
/etc/php/7.0/apache2/php.ini  
RUN sed -i "s/^error_reporting.*/error_reporting = E_ERROR | E_WARNING |
E_PARSE/" /etc/php/7.0/apache2/php.ini  
RUN sed -i "s/^upload_max_filesize.*/upload_max_filesize = 256M/"
/etc/php/7.0/apache2/php.ini  
RUN sed -i "s/^post_max_size.*/post_max_size = 256M/"
/etc/php/7.0/apache2/php.ini  
RUN sed -i "s/^allow_url_fopen.*/allow_url_fopen = On/"
/etc/php/7.0/apache2/php.ini  
RUN sed -i "s/^register_globals.*/register_globals = Off/"
/etc/php/7.0/apache2/php.ini  
RUN sed -i "s/^magic_quotes_*.*/magic_quotes_* = Off/"
/etc/php/7.0/apache2/php.ini  
RUN sed -i "s/^safe_mode.*/safe_mode = Off/" /etc/php/7.0/apache2/php.ini  
RUN sed -i "s/^max_execution_time.*/max_execution_time = 60/"
/etc/php/7.0/apache2/php.ini  
  
# Manually set up the apache environment variables  
ENV APACHE_RUN_USER www-data  
ENV APACHE_RUN_GROUP www-data  
ENV APACHE_LOG_DIR /var/log/apache2  
ENV APACHE_LOCK_DIR /var/lock/apache2  
ENV APACHE_PID_FILE /var/run/apache2.pid  
  
EXPOSE 80  
RUN mkdir /var/www/site  
RUN chown -R www-data:www-data /var/www/site/  
  
# Update the default apache site with the config we created.  
ADD apache-config.conf /etc/apache2/sites-enabled/000-default.conf  
  
# By default, simply start apache.  
CMD /usr/sbin/apache2ctl -D FOREGROUND;

