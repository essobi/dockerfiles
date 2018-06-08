FROM serkin/php7-fpm  
  
MAINTAINER serkin.alexander@gmail.com  
  
RUN pecl install mongodb \  
&& pecl install xdebug-beta \  
&& docker-php-ext-enable xdebug  
  
RUN echo "extension=mongodb.so" > $PHP_INI_DIR/conf.d/mongodb.ini  

