FROM 2dotstwice/nginx-php71-starter  
  
# nginx silex configuration for php-fpm  
# based on https://silex.symfony.com/doc/2.0/web_servers.html#nginx  
ADD ./files/etc/nginx/sites-available/default /etc/nginx/sites-
available/default  
ADD ./files/etc/nginx/silex/000-base.conf /etc/nginx/silex/000-base.conf  
ADD ./files/etc/nginx/silex/999-end.conf /etc/nginx/silex/999-end.conf  
  
# keep system environment variables in php-fpm  
RUN sed -i '$ a\  
clear_env=no' ${PHP_CONFIG_DIR}/fpm/pool.d/www.conf  
  
WORKDIR /usr/share/nginx/html

