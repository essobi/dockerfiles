FROM php:7.0-apache  
  
RUN apt-get update && apt-get install -y php-pear libyaml-dev libfreetype6-dev
libjpeg62-turbo-dev libmcrypt-dev libpng12-dev drush  
  
RUN docker-php-ext-install pdo pdo_mysql session opcache  
RUN docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-
dir=/usr/include/  
RUN docker-php-ext-install gd  
  
RUN pecl install yaml  
RUN echo "extension=yaml.so" > /usr/local/etc/php/conf.d/ext-yaml.ini  
  
RUN pecl install xdebug  
  
RUN echo "zend_extension=xdebug.so" >> /usr/local/etc/php/conf.d/ext-
xdebug.ini && echo "xdebug.remote_enable=1" >> /usr/local/etc/php/conf.d/ext-
xdebug.ini && echo "xdebug.remote_host=localhost" >>
/usr/local/etc/php/conf.d/ext-xdebug.ini && echo "xdebug.remote_port=9001" >>
/usr/local/etc/php/conf.d/ext-xdebug.ini && echo "xdebug.profiler_enable=1" >>
/usr/local/etc/php/conf.d/ext-xdebug.ini && echo
"xdebug.profiler_output_dir='/tmp'" >> /usr/local/etc/php/conf.d/ext-
xdebug.ini && echo "xdebug.idekey=lkh" >> /usr/local/etc/php/conf.d/ext-
xdebug.ini && echo "xdebug.max_nesting_level=256" >>
/usr/local/etc/php/conf.d/ext-xdebug.ini && echo "xdebug.remote_autostart = 1"
>> /usr/local/etc/php/conf.d/ext-xdebug.ini  
  
RUN a2enmod rewrite  
RUN a2enmod headers  
  
COPY src/ /var/www/html/  
VOLUME /var/www/html  

