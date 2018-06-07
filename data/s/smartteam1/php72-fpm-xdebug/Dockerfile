# See https://github.com/docker-
library/php/blob/4677ca134fe48d20c820a19becb99198824d78e3/7.0/fpm/Dockerfile  
FROM smartteam1/php72-fpm:1.0  
# install xdebug  
RUN pecl install xdebug  
ADD xdebug.ini /usr/local/etc/php/conf.d/docker-php-ext-xdebug.ini  
RUN docker-php-ext-enable xdebug  
  

