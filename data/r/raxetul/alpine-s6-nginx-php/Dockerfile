FROM raxetul/alpine-s6-nginx  
MAINTAINER Emrah URHAN <raxetul@gmail.com>  
  
RUN apk update && apk add --no-cache \  
php7-bcmath \  
php7-bz2 \  
php7-curl \  
php7-ctype \  
php7-dom \  
php7-fpm \  
php7-gd \  
php7-gettext \  
php7-gmp \  
php7-iconv \  
php7-json \  
php7-mbstring \  
php7-mcrypt \  
php7-mysqli \  
php7-odbc \  
php7-openssl \  
php7-pdo \  
php7-pdo_dblib \  
php7-pdo_mysql \  
php7-pdo_odbc \  
php7-pdo_pgsql \  
php7-pdo_sqlite \  
php7-session \  
php7-soap \  
php7-sqlite3 \  
php7-xmlreader \  
php7-xmlrpc \  
php7-zip \  
php7-zlib \  
&& rm -rf /var/cache/apk/*  
## Feed backs for missing php modules are welcomed.  
  
ADD php-fpm /s6/php-fpm  
  
RUN chmod +x /s6/php-fpm/run /s6/php-fpm/finish \  
&& chown root /s6/php-fpm/run /s6/php-fpm/finish \  
&& mkdir -p /run/nginx && touch /run/nginx/nginx.pid \  
&& sed -i "s/;listen.owner = nobody/listen.owner = nginx/g" /etc/php7/php-
fpm.d/www.conf \  
&& sed -i "s/;listen.group = nobody/listen.group = nginx/g" /etc/php7/php-
fpm.d/www.conf \  
&& sed -i "s/user = nobody/user = nginx/g" /etc/php7/php-fpm.d/www.conf \  
&& sed -i "s/group = nobody/group = nginx/g" /etc/php7/php-fpm.d/www.conf \  
&& sed -i "s|;*daemonize\s*=\s*yes|daemonize = no|g" /etc/php7/php-fpm.conf \  
&& sed -i "s/listen = 127.0.0.1:9000/listen = \/var\/run\/php-fpm.sock/g"
/etc/php7/php-fpm.d/www.conf \  
&& sed -i "s/;env/env/g" /etc/php7/php-fpm.d/www.conf  
  
## Don't setup ENTRYPOINT, it is set to s6 superviser in alpine-s6-base image,
see Dockerfile of alpine-s6-base image  

