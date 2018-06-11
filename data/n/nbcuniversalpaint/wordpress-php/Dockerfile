FROM php:7.1-fpm-alpine  
  
RUN curl -O https://raw.githubusercontent.com/wp-cli/builds/gh-pages/phar/wp-
cli.phar && \  
chmod +x wp-cli.phar && \  
mv wp-cli.phar /usr/local/bin/wp && \  
apk update && \  
apk add --no-cache --virtual .build-deps mysql zip zlib && \  
docker-php-ext-install mbstring pdo pdo_mysql mysqli && \  
apk del .build-deps && \  
rm -rf /tmp/* /var/cache/apk/*  
  
COPY ./conf.d/php.ini /etc/php/7.1/fpm/php.ini  
COPY ./conf.d/www.conf /etc/php-fpm.d/www.conf  
  
WORKDIR /var/www  

