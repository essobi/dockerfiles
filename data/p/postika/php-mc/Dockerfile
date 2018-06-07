FROM postika/php-mc  
MAINTAINER alexp@postika.eu  
  
RUN apk update && apk add autoconf automake gcc g++ make  
RUN pecl -q install xdebug  
RUN docker-php-ext-enable xdebug  
RUN echo 'xdebug.remote_enable=1' >> /usr/local/etc/php/conf.d/docker-php-ext-
xdebug.ini  
RUN echo 'xdebug.remote_port=8999' >> /usr/local/etc/php/conf.d/docker-php-
ext-xdebug.ini  
RUN rm -rf /tmp/* && rm -rf /var/cache/apk/*  

