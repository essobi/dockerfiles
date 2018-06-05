FROM avatao/ubuntu:16.04  
  
RUN apt-get update \  
&& apt-get -qy install \  
nginx \  
php7.0 \  
php7.0-fpm \  
php7.0-mcrypt \  
php7.0-sqlite3 \  
supervisor \  
&& rm -rf /var/lib/apt/lists/* \  
&& rm -fr /var/www/html  
  
COPY ./ /  
  
RUN mkdir /var/cache/nginx /var/run/php-fpm \  
&& chown -R www-data:www-data /var/lib/nginx /var/cache/nginx /var/run/php-fpm
/var/log \  
&& rm /etc/php/7.0/fpm/pool.d/www.conf  
  
VOLUME ["/var/cache/nginx", "/var/run/php-fpm", "/var/log", "/var/lib/nginx"]  
  
USER www-data  
  
CMD ["supervisord", "-c", "/etc/supervisor/conf.d/php-fpm.conf"]  

