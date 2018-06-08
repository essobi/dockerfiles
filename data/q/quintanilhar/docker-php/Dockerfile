FROM alpine:3.3  
  
MAINTAINER Ricardo Quintaniha <ricardo.aquintanilha@gmail.com>  
  
RUN echo "@testing http://nl.alpinelinux.org/alpine/edge/testing" >>
/etc/apk/repositories;  
  
RUN apk add --update php \  
php-cli \  
php-pdo \  
php-pdo_sqlite \  
php-pdo_mysql \  
php-pdo_pgsql \  
php-redis@testing \  
php-memcached@testing \  
php-json \  
php-openssl \  
php-dev \  
php-curl \  
php-mcrypt \  
php-phar \  
php-xdebug@testing \  
&& rm -rf /var/cache/apk/* /var/tmp/* /tmp/*  
  
RUN sed -i 's/display_errors = Off/display_errors = On/g' /etc/php/php.ini \  
&& sed -i 's/extension/zend_extension/g' /etc/php/conf.d/xdebug.ini  
  
RUN /usr/bin/php -r "readfile('https://getcomposer.org/installer');" | \  
/usr/bin/php -- --install-dir=/usr/local/bin --filename=composer  

