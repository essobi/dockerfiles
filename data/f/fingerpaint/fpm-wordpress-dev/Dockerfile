FROM wordpress:4.9.1-php7.0  
RUN ln -sf /usr/share/zoneinfo/EST5EDT /etc/localtime  
  
## Install and setup PHP Xdebug  
RUN pecl install xdebug-2.5.4 \  
&& docker-php-ext-enable xdebug  
ENV XDEBUGINI_PATH=/usr/local/etc/php/conf.d/php.ini  
RUN echo "zend_extension="`find /usr/local/lib/php/extensions/ -iname
'xdebug.so'` > $XDEBUGINI_PATH  
ADD xdebug.ini /tmp/xdebug.ini  
RUN cat /tmp/xdebug.ini >> $XDEBUGINI_PATH  
RUN echo "xdebug.remote_host=10.254.254.254" >> $XDEBUGINI_PATH  
  
RUN curl -O https://raw.githubusercontent.com/wp-cli/builds/gh-pages/phar/wp-
cli.phar && chmod +x wp-cli.phar && mv wp-cli.phar /usr/local/bin/wp  
  
COPY .htaccess /var/www/html  
  
## Expose ports  
EXPOSE 80  
EXPOSE 443

