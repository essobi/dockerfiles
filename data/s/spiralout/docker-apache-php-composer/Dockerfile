FROM ubuntu:latest  
  
MAINTAINER Spiral Out <spiralout.eu@gmail.com>  
  
# disable interactive functions.  
ENV DEBIAN_FRONTEND noninteractive  
  
# Install apache, php and supplimentary programs. also remove the list from
the apt-get update at the end ;-)  
RUN apt-get update && \  
apt-get install -y apache2 \  
libapache2-mod-php5 \  
php5-mysql \  
php5-gd \  
php-pear \  
php-apc \  
php5-mcrypt \  
php5-json \  
php5-curl \  
curl lynx-cur \  
&& rm -rf /var/lib/apt/lists/* \  
&& apt-get clean -y  
# Install composer for PHP dependencies  
RUN cd /tmp && curl -sS https://getcomposer.org/installer | php && mv
composer.phar /usr/local/bin/composer  
  
# Enable apache mods.  
RUN a2enmod php5  
RUN a2enmod rewrite  
  
# Update the PHP.ini file, enable <? ?> tags and quieten logging.  
RUN sed -i "s/short_open_tag = Off/short_open_tag = On/"
/etc/php5/apache2/php.ini  
RUN sed -i "s/error_reporting = .*$/error_reporting = E_ERROR | E_WARNING |
E_PARSE/" /etc/php5/apache2/php.ini  
  
# Manually set up the apache environment variables  
ENV APACHE_RUN_USER www-data  
ENV APACHE_RUN_GROUP www-data  
ENV APACHE_LOG_DIR /var/log/apache2  
ENV APACHE_LOCK_DIR /var/lock/apache2  
ENV APACHE_PID_FILE /var/run/apache2.pid  
  
EXPOSE 80  
# Copy site into place.  
ADD www /var/www/site  
  
# Update the default apache site with the config we created.  
ADD apache-config.conf /etc/apache2/sites-enabled/000-default.conf  
  
# By default, simply start apache.  
CMD /usr/sbin/apache2ctl -D FOREGROUND  
  
# expose container at port 80  
EXPOSE 80  

