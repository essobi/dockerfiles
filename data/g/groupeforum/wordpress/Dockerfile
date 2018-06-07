FROM php:5.6-apache  
  
MAINTAINER Florian Girardey <florian@girardey.net>  
  
# Enable Apache mod_rewrite  
RUN a2enmod rewrite && a2enmod expires  
  
# install the PHP extensions we need  
RUN apt-get update && apt-get install -q -y libpng12-dev libjpeg-dev
libapache2-mod-xsendfile libxml2-dev exim4 mailutils \  
&& rm -rf /var/lib/apt/lists/* \  
&& docker-php-ext-configure gd --with-png-dir=/usr --with-jpeg-dir=/usr \  
&& docker-php-ext-install gd \  
&& docker-php-ext-install soap \  
&& docker-php-ext-install opcache  
RUN docker-php-ext-install mysqli  
  
# Install xdebug  
RUN pecl install xdebug  
  
# Fix permissions on all of the files  
RUN usermod -u 1000 www-data  
  
# Setup APACHE environment variables  
ENV APACHE_RUN_USER www-data  
ENV APACHE_RUN_GROUP www-data  
ENV APACHE_LOG_DIR /var/log/apache2  
ENV APACHE_LOCK_DIR /var/lock/apache2  
ENV APACHE_PID_FILE /var/run/apache2.pid  
  
# Update the default apache site with the config we created.  
COPY apache-config.conf /etc/apache2/sites-enabled/000-default.conf  
  
# Add PHP Configuration file for OPcache  
COPY php-opcache.ini /usr/local/etc/php/conf.d/php-opcache.ini  
  
# Add PHP Configuration file for WordPress  
COPY php-wordpress.ini /usr/local/etc/php/conf.d/php-wordpress.ini  
  
# Add PHP Configuration file for SMTP  
COPY php-smtp.ini /usr/local/etc/php/conf.d/php-smtp.ini  
  
# Add the Entrypoint script  
COPY docker-entrypoint.sh /root/entrypoint.sh  
RUN chmod +x /root/entrypoint.sh  
  
VOLUME /var/www/html  
  
ENTRYPOINT ["/root/entrypoint.sh"]  
CMD ["apache2-foreground"]

