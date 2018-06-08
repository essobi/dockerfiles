FROM php:7.0-fpm-alpine  
  
RUN apk update && apk add \  
postgresql-dev \  
curl \  
jpeg-dev \  
libpng-dev \  
freetype-dev \  
openssl \  
openssl-dev \  
libmcrypt-dev \  
nginx \  
supervisor \  
zip \  
unzip \  
git  
  
# configure gd library  
RUN docker-php-ext-configure gd \  
\--enable-gd-native-ttf \  
\--with-jpeg-dir=/usr/lib \  
\--with-freetype-dir=/usr/include/freetype2  
  
# Install extensions using the helper script provided by the base image  
RUN docker-php-ext-install \  
mcrypt \  
pdo_mysql \  
pdo_pgsql \  
gd \  
zip \  
pdo \  
mbstring  
  
COPY ./conf/laravel.ini /usr/local/etc/php/conf.d  
COPY ./conf/laravel.pool.conf /usr/local/etc/php-fpm.d/  
COPY ./conf/nginx.conf /etc/nginx/nginx.conf  
COPY ./conf/default.conf /etc/nginx/conf.d/default.conf  
COPY ./conf/supervisord.conf /etc/supervisor/supervisord.conf  
  
RUN curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer  
  
WORKDIR /var/www/html  
  
CMD ["/usr/bin/supervisord", "-c", "/etc/supervisor/supervisord.conf"]  
  
EXPOSE 80 443  

