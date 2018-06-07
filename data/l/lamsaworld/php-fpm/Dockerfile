FROM alpine:3.4  
RUN apk --update add \  
php5 \  
php5-dom \  
php5-ctype \  
php5-curl \  
php5-fpm \  
php5-gd \  
php5-intl \  
php5-mcrypt \  
php5-json \  
php5-opcache \  
php5-pdo \  
php5-pdo_mysql \  
php5-posix \  
php5-xml \  
php5-iconv \  
php5-phar \  
php5-openssl  
  
COPY php.ini /etc/php5/conf.d/50-setting.ini  
COPY php-fpm.conf /etc/php5/php-fpm.conf  
  
VOLUME /app  
EXPOSE 8000  
# Xdebug  
RUN touch /var/log/xdebug.log && chmod 666 /var/log/xdebug.log  
  
# Symfony root folder  
RUN adduser -D -u 1000 fpm && addgroup fpm fpm && mkdir -p /app && chown -R
fpm:fpm /app  
  
CMD ["php-fpm", "-F"]

