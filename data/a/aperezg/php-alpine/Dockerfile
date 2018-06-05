FROM alpine:edge  
  
MAINTAINER Adrian Perez <perezg.adrian@gmail.com>  
  
RUN echo "http://dl-4.alpinelinux.org/alpine/edge/testing" >>
/etc/apk/repositories \  
&& apk --update add \  
php7 \  
php7-fpm \  
php7-mcrypt \  
php7-mbstring \  
php7-pdo \  
php7-pdo_mysql \  
php7-pdo_pgsql \  
php7-pdo_sqlite \  
php7-curl \  
php7-openssl \  
php7-gettext \  
php7-bcmath \  
php7-zip \  
php7-mysqli \  
php7-json \  
php7-soap \  
php7-zlib \  
php7-xml \  
php7-dom \  
php7-ctype \  
php7-gd \  
php7-intl \  
php7-posix \  
php7-session \  
php7-iconv \  
php7-phar \  
# Clean up  
&& rm -rf /var/cache/apk/*  
  
COPY config/php.ini /etc/php7/conf.d/50-setting.ini  
COPY config/php-fpm.conf /etc/php7/php-fpm.conf  
  
RUN ln -s /usr/bin/php7 /usr/bin/php  
  
VOLUME /app  
EXPOSE 9000  
  
CMD ["php-fpm7", "-F"]

