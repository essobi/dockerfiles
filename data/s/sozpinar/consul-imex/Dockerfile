FROM php:7.1-alpine  
  
WORKDIR /app  
COPY . ./  
  
RUN apk --update add git \  
&& php -r "readfile('https://getcomposer.org/download/1.4.1/composer.phar');"
> /usr/local/bin/composer \  
&& chmod +x /usr/local/bin/composer \  
&& composer install -o --no-dev --no-interaction --prefer-source \  
&& rm /usr/local/bin/composer \  
&& apk del git  
  
ENV RUNNING_IN_CONTAINER=1  
WORKDIR /consul-imex  
ENTRYPOINT ["php", "/app/scripts/consul-imex.php"]  

