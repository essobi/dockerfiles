FROM alpine:3.6  
  
MAINTAINER jn.germon@gmail.com  
  
RUN apk update && \  
apk add \  
php7 \  
php7-bcmath \  
php7-dom \  
php7-ctype \  
php7-curl \  
php7-fileinfo \  
php7-fpm \  
php7-gd \  
php7-iconv \  
php7-intl \  
php7-json \  
php7-mbstring \  
php7-mcrypt \  
php7-mysqlnd \  
php7-opcache \  
php7-openssl \  
php7-pdo \  
php7-pdo_mysql \  
php7-pdo_pgsql \  
php7-pdo_sqlite \  
php7-phar \  
php7-posix \  
php7-simplexml \  
php7-session \  
php7-soap \  
php7-tokenizer \  
php7-xml \  
php7-xmlreader \  
php7-xmlwriter \  
php7-zip \  
bash \  
&& rm -rf /var/cache/apk/*  
  
ADD php-fpm.conf /etc/php7/php-fpm.conf  
ADD php-fpm.ini /etc/php7/conf.d/50-setting.ini  
  
COPY entrypoint.sh /  
  
RUN chmod u+x /entrypoint.sh  
  
EXPOSE 9000  
  
ENTRYPOINT ["/entrypoint.sh"]  
  
CMD ["php-fpm7", "--nodaemonize"]  

