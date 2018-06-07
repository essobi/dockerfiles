FROM alpine:latest  
MAINTAINER Łukasz Wojciechowski <lukasz@wizjostudio.pl>  
  
RUN apk --no-cache add php7 \  
php7-fpm \  
php7-json \  
php7-curl \  
php7-gd \  
php7-intl \  
php7-mcrypt \  
php7-pdo_mysql \  
php7-xml \  
php7-simplexml \  
php7-memcached \  
php7-redis \  
php7-mbstring \  
php7-soap \  
php7-xdebug \  
php7-phar \  
php7-ctype \  
php7-dom \  
php7-tokenizer \  
php7-zlib \  
curl && \  
curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/bin/
--filename=composer  
  
RUN sed -i -e "s/;cgi.fix_pathinfo=1/cgi.fix_pathinfo=0/g" /etc/php7/php.ini
&& \  
sed -i -e "s/upload_max_filesize\s*=\s*2M/upload_max_filesize = 100M/g"
/etc/php7/php.ini && \  
sed -i -e "s/post_max_size\s*=\s*8M/post_max_size = 100M/g" /etc/php7/php.ini
&& \  
sed -i -e "s/;daemonize\s*=\s*yes/daemonize = no/g" /etc/php7/php-fpm.conf &&
\  
sed -i -e "s/;catch_workers_output\s*=\s*yes/catch_workers_output = yes/g"
/etc/php7/php-fpm.d/www.conf && \  
sed -i -e "s/pm.max_children = 5/pm.max_children = 9/g" /etc/php7/php-
fpm.d/www.conf && \  
sed -i -e "s/pm.start_servers = 2/pm.start_servers = 3/g" /etc/php7/php-
fpm.d/www.conf && \  
sed -i -e "s/pm.min_spare_servers = 1/pm.min_spare_servers = 2/g"
/etc/php7/php-fpm.d/www.conf && \  
sed -i -e "s/pm.max_spare_servers = 3/pm.max_spare_servers = 4/g"
/etc/php7/php-fpm.d/www.conf && \  
sed -i -e "s/pm.max_requests = 500/pm.max_requests = 100/g" /etc/php7/php-
fpm.d/www.conf && \  
sed -i -e "s/listen\s*=\s*127.0.0.1:9000/listen = 9000/g" /etc/php7/php-
fpm.d/www.conf  
  
CMD ["php-fpm7", "-F"]  
  
EXPOSE 9000  

