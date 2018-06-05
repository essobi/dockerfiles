FROM php:5.6-apache  
  
# PHP installer args  
ENV PHP_EXTRA_CONFIGURE_ARGS --enable-mysqlnd  
  
# Install modules  
RUN apt-get update && apt-get install -y \  
libfreetype6-dev \  
libjpeg62-turbo-dev \  
libmcrypt-dev \  
libpng12-dev \  
&& docker-php-ext-install iconv mcrypt \  
&& docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-
dir=/usr/include/ \  
&& docker-php-ext-install gd mysqli pdo pdo_mysql mysql  
RUN sed -i "s/AllowOverride None/AllowOverride All/g"
/etc/apache2/apache2.conf  
RUN a2enmod rewrite  
  
# add a default error log  
RUN touch /var/log/php_errors.log  
RUN chmod 777 /var/log/php_errors.log  
COPY php.ini /usr/local/etc/php/  
  
# Add image configuration and scripts  
ADD run.sh /run.sh  
RUN chmod 755 /*.sh  
RUN usermod -u 1000 www-data  
  
EXPOSE 80  
CMD ["/run.sh"]

