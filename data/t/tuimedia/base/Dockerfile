FROM php:7.2-fpm-alpine  
  
MAINTAINER Matt Robinson <matt@tuimedia.com>  
  
COPY files/phpfpm-www.conf /usr/local/etc/php-fpm.d/www.conf  
COPY files/nginx-gzip.conf /etc/nginx/conf.d/gzip.conf  
  
RUN echo "expose_php=off" > /usr/local/etc/php/conf.d/99_custom.ini \  
&& echo "display_errors=stderr" >> /usr/local/etc/php/conf.d/99_custom.ini \  
&& echo "date.timezone=Europe/London" >>
/usr/local/etc/php/conf.d/99_custom.ini \  
&& echo "variables_order=EGCPS" >> /usr/local/etc/php/conf.d/99_custom.ini  
  
RUN apk --update upgrade && \  
apk add \  
bash \  
git \  
icu-libs \  
mysql-client \  
netcat-openbsd \  
nginx \  
openssl \  
s6 \  
sudo \  
&& rm -rf /var/cache/apk/* > /dev/null \  
&& rm -f /etc/nginx/conf.d/default.conf  
  
RUN docker-php-source extract \  
&& apk add --no-cache --virtual .phpize-deps $PHPIZE_DEPS zlib-dev icu-dev
pcre-dev \  
&& pecl install apcu redis xdebug \  
&& docker-php-ext-enable apcu redis \  
&& docker-php-ext-install intl bcmath pdo_mysql opcache zip \  
&& apk del .phpize-deps \  
&& docker-php-source delete \  
&& rm -fr /tmp/pear/cache  
  
RUN curl -sS https://getcomposer.org/installer | php \  
&& mv composer.phar /usr/local/bin/composer \  
&& chmod a+x /usr/local/bin/composer  

