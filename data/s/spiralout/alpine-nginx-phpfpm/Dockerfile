FROM alpine:edge  
MAINTAINER Josh Sandlin <josh@thenullbyte.org>  
MAINTAINER Spiral Out <spiralout.eu@gmail.com>  
  
RUN apk --update add \  
nginx \  
php-fpm \  
php-pdo \  
php-json \  
php-openssl \  
php-mysql \  
php-pdo_mysql \  
php-mcrypt \  
php-sqlite3 \  
php-pdo_sqlite \  
php-ctype \  
php-zlib \  
php-dom \  
php-xml \  
php-xmlreader \  
php-iconv \  
supervisor  
#php-dev php-pear autoconf openssl-dev g++ make && \  
#pear update-channels && \  
#php /usr/share/pear/peclcmd.php install -f mongodb && \  
#echo "extension=mongodb.so" >> `php --ini | grep "Loaded Configuration" | sed
-e "s|.*:\s*||"` && \  
#apk del --purge php-dev php-pear autoconf openssl-dev g++  
RUN mkdir -p /etc/nginx  
RUN mkdir -p /var/run/php-fpm  
RUN mkdir -p /var/log/supervisor  
  
RUN rm /etc/nginx/nginx.conf  
ADD nginx.conf /etc/nginx/nginx.conf  
  
VOLUME ["/var/www", "/etc/nginx/sites-enabled"]  
  
ADD nginx-supervisor.ini /etc/supervisor.d/nginx-supervisor.ini  
  
EXPOSE 80 9000  
CMD ["/usr/bin/supervisord"]  

