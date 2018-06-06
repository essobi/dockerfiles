FROM colstrom/alpine  
  
RUN apk-install \  
ca-certificates \  
php-fpm \  
php-json \  
php-openssl \  
php-pear \  
php-phar \  
php \  
&& wget https://getcomposer.org/installer -O - | php -- --install-dir
/usr/local/bin --filename composer  
  
ENTRYPOINT ["php-fpm", "--nodaemonize", "-d", "listen=9000"]  

