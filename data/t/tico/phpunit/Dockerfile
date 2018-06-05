FROM tico/composer:latest AS builder  
  
RUN composer require phpunit/phpunit:^7 -a --no-interaction --ignore-platform-
reqs -d /tmp  
  
FROM alpine:latest  
WORKDIR /tmp  
VOLUME ["/app"]  
WORKDIR /app  
ENTRYPOINT ["/tmp/vendor/bin/phpunit"]  
CMD ["--help"]  
  
COPY --from=builder /tmp /tmp  
  
RUN apk --no-cache add \  
php7 \  
php7-bcmath \  
php7-ctype \  
php7-curl \  
php7-dom \  
php7-exif \  
php7-fileinfo \  
php7-gd \  
php7-json \  
php7-ldap \  
php7-mbstring \  
php7-mcrypt \  
php7-mysqli \  
php7-opcache \  
php7-openssl \  
php7-pcntl \  
php7-pdo \  
php7-pdo_mysql \  
php7-pdo_pgsql \  
php7-pdo_sqlite \  
php7-phar \  
php7-redis \  
php7-session \  
php7-simplexml \  
php7-soap \  
php7-tokenizer \  
php7-xdebug \  
php7-xml \  
php7-xmlreader \  
php7-xmlwriter \  
php7-zip \  
php7-zlib \  
&& sed -i 's/nn and/nn, Nikita Chernyi (Docker), Julien Breux (Docker) and/g'
/tmp/vendor/phpunit/phpunit/src/Runner/Version.php \  
# Enable X-Debug  
&& sed -i 's/\;z/z/g' /etc/php7/conf.d/xdebug.ini \  

