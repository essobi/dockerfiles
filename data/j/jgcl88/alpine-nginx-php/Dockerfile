FROM alpine:3.7  
  
COPY . /  
  
RUN echo "http://dl-cdn.alpinelinux.org/alpine/edge/testing" >>
/etc/apk/repositories \  
&& apk update \  
&& apk add --no-cache \  
nginx \  
nano \  
curl \  
supervisor \  
git \  
zip \  
unzip \  
php7 \  
php7-phar \  
php7-dom \  
php7-fpm \  
php7-mbstring \  
php7-mcrypt \  
php7-opcache \  
php7-pdo \  
php7-pdo_mysql \  
php7-pdo_pgsql \  
php7-pdo_sqlite \  
php7-pdo_odbc \  
php7-pdo_dblib \  
php7-mongodb \  
php7-json \  
php7-xml \  
php7-xmlwriter \  
php7-xmlrpc \  
php7-xmlreader \  
php7-simplexml \  
php7-soap \  
php7-tokenizer \  
php7-openssl \  
php7-json \  
php7-curl \  
php7-ctype \  
php7-zlib \  
php7-posix \  
php7-pcntl \  
php7-iconv \  
php7-session \  
&& addgroup -g 1000 -S www \  
&& adduser -u 1000 -D -S -G www -h /app -g www www \  
&& chown -R www:www /var/lib/nginx \  
&& mkdir -p /etc/nginx/sites-enabled \  
&& mkdir -p /etc/php7/php-fpm.d \  
&& cp -rf /docker/nginx/nginx.conf /etc/nginx/nginx.conf \  
&& cp -rf /docker/nginx/default.conf /etc/nginx/sites-enabled/default \  
&& cp -rf /docker/php/php.ini /etc/php7/php.ini \  
&& cp -rf /docker/php/www.conf /etc/php7/php-fpm.d/www.conf \  
&& cp -rf /docker/supervisor/supervisor.conf /etc/supervisord.conf \  
&& curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/bin
--filename=composer  
  
WORKDIR /app  
  
# portal  
EXPOSE 80  
  
# start  
CMD ["/docker/start.sh"]

