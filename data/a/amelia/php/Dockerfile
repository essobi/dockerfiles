FROM amelia/dhparam:latest as dh  
FROM composer:latest as composer  
FROM nginx:mainline-alpine  
  
LABEL maintainer="amelia@dorks.io"  
  
ENV COMPOSER_ALLOW_SUPERUSER 1  
ENV COMPOSER_NO_INTERACTION 1  
ENV COMPOSER_HOME /usr/lib/composer  
ENV COMPOSER_CACHE_DIR /var/cache/composer  
  
# key from https://php.codecasts.rocks/php-alpine.rsa.pub on
2018-03-30T09:14:00+01:00  
ADD files/keys/php-alpine.rsa.pub /etc/apk/keys/php-alpine.rsa.pub  
  
# add the www-data user  
RUN set -x \  
&& addgroup -g 82 -S www-data \  
&& adduser -u 82 -D -S -G www-data www-data \  
&& apk --update add ca-certificates \  
&& update-ca-certificates \  
&& echo "@php https://php.codecasts.rocks/v3.7/php-7.2" >>
/etc/apk/repositories \  
&& apk --update add \  
php7@php \  
php7-fpm@php \  
\  
php7-ctype@php \  
php7-curl@php \  
php7-dom@php \  
php7-gd@php \  
php7-iconv@php \  
php7-intl@php \  
php7-json@php \  
php7-mbstring@php \  
php7-opcache@php \  
php7-openssl@php \  
php7-pcntl@php \  
php7-phar@php \  
php7-posix@php \  
php7-session@php \  
php7-xml@php \  
php7-zip@php \  
php7-zlib@php \  
\  
php7-pdo_pgsql@php \  
php7-pdo_mysql@php \  
\  
supervisor \  
&& ln -s /usr/bin/php7 /usr/bin/php \  
&& rm -rf /var/cache/apk/* \  
&& rm /etc/init.d/php-fpm7 \  
&& mkdir -p /var/log/nginx \  
&& mkdir -p /var/cache/nginx \  
&& mkdir -p /srv/code \  
&& chown www-data:www-data /srv/code  
  
# copy over composer  
COPY --from=composer /usr/bin/composer /usr/bin  
  
# copy over dhparams and a snakeoil cert  
COPY --from=dh /etc/ssl/dhparam.pem /etc/nginx/dhparam.pem  
COPY --from=dh /etc/ssl/snakeoil-cert.pem /etc/nginx/certs/certificate.pem  
COPY --from=dh /etc/ssl/snakeoil-key.pem /etc/nginx/certs/privkey.pem  
  
# add the supervisor config  
COPY files/supervisor/supervisor.conf /etc/supervisord.conf  
  
# add fpm files  
COPY ["files/php-fpm/php-fpm.conf", "files/php-fpm/php.ini", "/etc/php7/"]  
  
# add custom nginx files  
COPY files/nginx/nginx.conf /etc/nginx/nginx.conf  
  
RUN composer global require hirak/prestissimo \  
&& rm -rf /var/cache/composer/* \  
&& nginx -t \  
&& php-fpm7 -t  
  
WORKDIR /srv/code  
  
EXPOSE 80 443 9000  
  
CMD ["supervisord", "-n", "-c", "/etc/supervisord.conf"]  

