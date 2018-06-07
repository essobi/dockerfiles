FROM alpine:edge  
MAINTAINER Lars Nieuwenhuizen<lars.nieuwenhuizen@me.com>  
  
RUN addgroup -g 9000 -S php  
RUN adduser -D -h /home/php -u 9001 -G php php  
  
RUN apk add --no-cache wget ca-certificates \  
&& wget -O /etc/apk/keys/phpearth.rsa.pub
https://repos.php.earth/alpine/phpearth.rsa.pub \  
&& echo "https://repos.php.earth/alpine/v3.7" >> /etc/apk/repositories  
  
RUN apk add --no-cache libpng-dev \  
&& apk add --no-cache php7.1 git \  
&& apk add --no-cache \  
php7.1-fpm \  
php7.1-openssl \  
php7.1-pdo \  
php7.1-pdo_mysql \  
php7.1-pdo_sqlite \  
php7.1-ctype \  
php7.1-mbstring \  
php7.1-gd \  
php7.1-gettext \  
php7.1-iconv \  
php7.1-json \  
php7.1-exif \  
php7.1-curl \  
php7.1-xml \  
php7.1-xsl \  
php7.1-opcache \  
php7.1-phar \  
php7.1-gd \  
php7.1-redis \  
php7.1-tokenizer \  
php7.1-simplexml \  
php7.1-pcntl  
  
RUN apk add --no-cache \  
xvfb \  
ttf-freefont \  
fontconfig  
  
COPY ./www.conf /etc/php/7.1/php-fpm.d/www.conf  
  
RUN ln -s /usr/bin/php7.1 /usr/local/bin/php  
RUN chown php /usr/local/bin/php  
  
RUN chown -R php /var/log/php/7.1 && \  
chmod -R g+w /var/log/php/7.1  
  
RUN mkdir -p /var/www/html && \  
chown -R php /var/www/html && \  
chmod -R g+w /var/www/html  
  
RUN chown -R php /run/php  
  
USER php  
  
WORKDIR /var/www/html  
  
EXPOSE 9000  
ENTRYPOINT ["php-fpm7.1","--nodaemonize"]  

