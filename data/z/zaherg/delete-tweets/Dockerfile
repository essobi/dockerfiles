FROM php:7.1-fpm-alpine  
  
MAINTAINER Zaher Ghaibeh <z@zah.me>  
  
ADD ./ /var/www  
  
COPY docker-entrypoint.sh /docker-entrypoint.sh  
  
WORKDIR /var/www  
  
RUN mkdir config \  
&& php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');" \  
&& php composer-setup.php --quiet \  
&& rm composer-setup.php \  
&& php composer.phar install --no-dev --no-suggest \  
&& rm -f composer.phar \  
&& wget -O /usr/local/bin/dumb-init https://github.com/Yelp/dumb-
init/releases/download/v1.2.0/dumb-init_1.2.0_amd64 \  
&& chmod +x /usr/local/bin/dumb-init  
  
ENTRYPOINT ["/docker-entrypoint.sh"]  
  
CMD ["php", "tweet"]

