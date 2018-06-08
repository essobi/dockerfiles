FROM php:fpm-alpine  
  
RUN set -x \  
&& apk add --no-cache --update bash postfix \  
&& docker-php-ext-install zip pdo_mysql  
  
CMD postfix start && php-fpm  

