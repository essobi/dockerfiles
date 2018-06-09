FROM alpine:3.7  
# Install packages  
RUN apk --no-cache add php7 php7-fpm php7-mysqli php7-pdo php7-pdo_mysql
php7-iconv php7-json php7-openssl \  
php7-curl php7-zlib php7-xml php7-xmlwriter php7-phar php7-intl php7-dom
php7-xmlreader \  
php7-ctype php7-mbstring php7-gd php7-tokenizer php7-soap php7-bz2
php7-fileinfo \  
php7-simplexml php7-session nginx nodejs supervisor curl git  
  
# Configure nginx  
COPY config/nginx.conf /etc/nginx/nginx.conf  
  
# Configure PHP-FPM  
COPY config/fpm-pool.conf /etc/php7/php-fpm.d/zzz_custom.conf  
COPY config/php.ini /etc/php7/conf.d/zzz_custom.ini  
  
# Configure supervisord  
COPY config/supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
  
# Install composer  
RUN php -r "readfile('https://getcomposer.org/installer');" | php && \  
mv composer.phar /usr/bin/composer && \  
chmod +x /usr/bin/composer  
  
# Add application  
RUN mkdir -p /var/www/html  
WORKDIR /var/www/html  
  
EXPOSE 80 443  
CMD ["/bin/sh", "-c", "cp .env.example .env && composer install && npm install
--verbose && php artisan key:generate || : && php artisan migrate &&
supervisord -c /etc/supervisor/conf.d/supervisord.conf"]  

