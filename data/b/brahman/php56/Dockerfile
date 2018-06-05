# from https://www.drupal.org/requirements/php#drupalversions  
FROM php:5.6-fpm  
  
# install the PHP extensions we need  
RUN apt-get update && apt-get install -y libpng12-dev libjpeg-dev libpq-dev
php5-memcached memcached mailutils ssmtp \  
&& rm -rf /var/lib/apt/lists/* \  
&& docker-php-ext-configure gd --with-png-dir=/usr --with-jpeg-dir=/usr \  
&& docker-php-ext-install gd mbstring mysqli pdo pdo_mysql pdo_pgsql zip
opcache  
  
# modify ssmtp settings  
RUN sed -ri -e 's/^(mailhub=).*/\1smtp-server/' -e
's/^#(FromLineOverride)/\1/' /etc/ssmtp/ssmtp.conf  
RUN echo 'sendmail_path = "/usr/sbin/ssmtp -t"' >
/usr/local/etc/php/conf.d/mail.ini  
  
WORKDIR /var/www  
  
VOLUME /var/www  
  
VOLUME /tmp  
  
CMD service memcached start&&php-fpm

