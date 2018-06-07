FROM runashop/php7-phalcon-dev:latest  
  
# Compile Xdebug  
RUN set -xe && \  
# Add virtual packages. It will remove when done.  
apk add --no-cache --virtual .build-deps autoconf g++ make && \  
pecl install xdebug && \  
docker-php-ext-enable xdebug && \  
apk del .build-deps && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

