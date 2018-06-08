## Start with a PHP image with Apache installed  
FROM fingerpaint/fpm-php7-apache-docker  
  
ADD apache/ssl-certs/* /var/www/  
ADD apache/000-default-ssl.conf /etc/apache2/sites-enabled  
  
## Install and setup PHP Xdebug  
RUN pecl install xdebug-2.5.4 \  
&& docker-php-ext-enable xdebug  
ENV XDEBUGINI_PATH=/usr/local/etc/php/conf.d/php.ini  
RUN echo "zend_extension="`find /usr/local/lib/php/extensions/ -iname
'xdebug.so'` > $XDEBUGINI_PATH  
ADD xdebug.ini /tmp/xdebug.ini  
RUN cat /tmp/xdebug.ini >> $XDEBUGINI_PATH  
RUN echo "xdebug.remote_host=10.254.254.254" >> $XDEBUGINI_PATH  

