FROM php:7.1-apache  
  
MAINTAINER Adam Kempler <akempler@gmail.com>  
  
ENTRYPOINT ["/root/entrypoint.sh"]  
  
RUN rm /bin/sh \  
&& ln -s /bin/bash /bin/sh  
  
# Fix permissions on Mac  
RUN usermod -u 1000 www-data \  
&& usermod -G staff www-data  
  
RUN apt-get update \  
&& apt-get install -y \  
libpng12-dev \  
libjpeg-dev \  
libpq-dev \  
libxml2-dev \  
libfreetype6-dev \  
libmcrypt-dev \  
vim \  
php5-mysql \  
mysql-client \  
&& docker-php-ext-configure gd --with-freetype-dir=/usr --with-png-dir=/usr
--with-jpeg-dir=/usr \  
&& docker-php-ext-install gd mbstring opcache pdo pdo_mysql pdo_pgsql mysqli
zip soap xmlrpc \  
&& pecl install -o -f xdebug  
  
RUN a2enmod rewrite \  
&& a2enmod ssl \  
&& a2enmod headers  
  
# NOTE: composer, drush and xdbebug.sh are included in the CLI container.  
# Install Composer  
# RUN curl -sS https://getcomposer.org/installer | php \  
# && mv composer.phar /usr/local/bin/composer  
# Install Drush  
# RUN composer global require drush/drush \  
# && composer global update \  
# && ln -s /root/.composer/vendor/bin/drush /usr/local/bin/drush  
ADD conf/apache/default.conf /etc/apache2/sites-available/000-default.conf  
ADD conf/php/00_opcache.ini /usr/local/etc/php/conf.d/  
ADD conf/php/00_xdebug.ini /usr/local/etc/php/conf.d/  
ADD conf/php/php.ini /usr/local/etc/php/conf.d/  
# ADD conf/scripts/xdebug.sh /var/www/xdebug.sh  
RUN a2ensite 000-default.conf  
  
WORKDIR /var/www/html  
  
# Add entrypoint  
ADD entrypoint.sh /root  
RUN chmod +x /root/entrypoint.sh  

