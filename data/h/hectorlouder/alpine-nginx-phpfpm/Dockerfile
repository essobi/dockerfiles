FROM alpine:edge  
MAINTAINER Hector Valdivia <hect.valdivia@gmail.com>  
  
RUN apk --update add \  
nginx \  
git \  
php-fpm \  
php-cli \  
php-dev \  
php-phalcon \  
php-pdo \  
php-json \  
php-openssl \  
php-pear \  
php-mssql \  
php-mysql \  
php-pdo_mysql \  
php-mcrypt \  
php-sqlite3 \  
php-pdo_sqlite \  
php-ctype \  
php-zlib \  
supervisor  
  
RUN mkdir -p /etc/nginx  
RUN mkdir -p /var/run/php-fpm  
RUN mkdir -p /var/log/supervisor  
  
RUN rm /etc/nginx/nginx.conf  
ADD nginx.conf /etc/nginx/nginx.conf  
  
VOLUME ["/var/www", "/etc/nginx/sites-enabled"]  
  
ADD nginx-supervisor.ini /etc/supervisor.d/nginx-supervisor.ini  
  
EXPOSE 80 9000  
CMD ["/usr/bin/supervisord"]  

