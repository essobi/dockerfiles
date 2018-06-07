FROM alpine  
  
MAINTAINER EgoFelix <docker@egofelix.de>  
  
RUN apk --no-cache add \  
supervisor \  
nginx \  
php7-fpm \  
php7-json \  
php7-mbstring \  
php7-session \  
php7-mysqli \  
php7-zip \  
php7-opcache \  
phpmyadmin  
  
RUN set -x ; \  
addgroup -g 82 -S www-data ; \  
adduser -u 82 -D -S -G www-data www-data && exit 0 ; exit 1  
  
RUN mkdir -p /etc/supervisor.d && \  
mkdir -p /srv/sessions /srv/logs && \  
mkdir -p /run/nginx /run/php7 && \  
chown -R www-data:www-data /srv /run/php7 && \  
ln -s /usr/share/webapps/phpmyadmin/ /srv/http && \  
rm /etc/phpmyadmin/config.inc.php  
  
COPY www.conf /etc/php7/php-fpm.d  
COPY php-fpm.ini /etc/supervisor.d  
COPY nginx.ini /etc/supervisor.d  
COPY nginx.conf /etc/nginx  
  
EXPOSE 80  
VOLUME ["/etc/phpmyadmin"]  
ENTRYPOINT /usr/bin/supervisord --nodaemon --configuration
/etc/supervisord.conf

