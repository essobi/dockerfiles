FROM php:7.1-fpm-alpine  
  
ENV S6_OVERLAY_VERSION=v1.19.1.1  
ENV PHPREDIS_VERSION 3.1.2  
RUN apk update && apk add \  
nginx curl libpng-dev libmcrypt-dev postgresql-dev \  
&& mkdir -p /usr/src/php/ext/redis \  
&& curl -L
https://github.com/phpredis/phpredis/archive/$PHPREDIS_VERSION.tar.gz | tar
xvz -C /usr/src/php/ext/redis --strip 1 \  
&& echo 'redis' >> /usr/src/php-available-exts \  
&& docker-php-ext-install mcrypt mbstring bcmath pdo_pgsql pdo_mysql opcache
redis gd \  
&& curl -sSL https://github.com/just-
containers/s6-overlay/releases/download/${S6_OVERLAY_VERSION}/s6-overlay-
amd64.tar.gz | tar xfz - -C / \  
&& ln -sf /dev/stdout /var/log/nginx/access.log \  
&& ln -sf /dev/stderr /var/log/nginx/error.log \  
&& apk del curl  
  
ADD ./nginx.conf /etc/nginx/nginx.conf  
ADD ./services.d /etc/services.d  
EXPOSE 80  
CMD "/init"  

