FROM php:7.2-fpm-alpine3.6  
ADD https://php.codecasts.rocks/php-alpine.rsa.pub /etc/apk/keys/php-
alpine.rsa.pub  
  
RUN apk --update add ca-certificates  
  
RUN echo "@php http://php.codecasts.rocks/v3.6/php-7.2" >>
/etc/apk/repositories  
  
RUN apk add --update php-ftp@php  
RUN apk add --update php-pdo_mysql@php  
RUN apk add --update php-gettext@php  
RUN apk add --update php-openssl@php  
RUN apk add --update php-memcached@php  
RUN apk add --update php-bcmath@php  
RUN apk add --update php-zip@php  
RUN apk add --update php-sockets@php  
RUN apk add --update php-xdebug@php  
RUN apk add --update php-redis@php  
RUN apk add --update php-imagick@php  
RUN apk add --update php-iconv@php  
  
RUN apk add --no-cache $PHPIZE_DEPS && pecl install xdebug && docker-php-ext-
enable xdebug  
  
RUN echo "zend_extension=/usr/local/lib/php/extensions/no-debug-non-
zts-20170718/xdebug.so" >> /etc/php7/php.ini \  
&& echo "xdebug.remote_enable=1" >> /etc/php7/php.ini \  
&& echo "xdebug.remote_mode=req" >> /etc/php7/php.ini \  
&& echo "xdebug.remote_port=9000" >> /etc/php7/php.ini \  
&& echo "xdebug.remote_autostart=1" >> /etc/php7/php.ini \  
&& echo "xdebug.remote_connect_back=0" >> /etc/php7/php.ini \  
&& echo "xdebug.remote_log=/var/log/xdebug.log" >> /etc/php7/php.ini  
  
RUN echo "date.timezone=Europe/London" >> /etc/php7/php.ini \  
&& touch /var/log/xdebug.log \  
&& chown root:root /var/log/xdebug.log \  
&& chmod a+w /var/log/xdebug.log  
  
# composer  
RUN curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer  
RUN composer global require "hirak/prestissimo"  
  
# phpunit  
RUN composer global require "phpunit/phpunit"  
  
# phpcs  
RUN composer global require "squizlabs/php_codesniffer=*"  
  
ENV PATH /root/.composer/vendor/bin:$PATH  
  
CMD ["php-fpm"]  

