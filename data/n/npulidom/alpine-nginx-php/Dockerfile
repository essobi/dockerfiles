# OS  
FROM nginx:alpine  
LABEL maintainer="nicolas.pulido@crazycake.cl"  
  
# build arguments  
ARG timezone="America/Santiago"  
# codecasts/php-alpine repository  
ADD https://php.codecasts.rocks/php-alpine.rsa.pub /etc/apk/keys/php-
alpine.rsa.pub  
# add repository  
RUN echo "@php https://php.codecasts.rocks/v3.7/php-7.2" >>
/etc/apk/repositories  
  
# packages  
RUN apk add --update --no-cache \  
bash \  
supervisor \  
nano \  
gettext \  
tzdata \  
curl \  
php7@php \  
php7-curl@php \  
php7-dom@php \  
php7-fpm@php \  
php7-gettext@php \  
php7-json@php \  
php7-mbstring@php \  
php7-mysqlnd@php \  
php7-openssl@php \  
php7-pdo@php \  
php7-pdo_mysql@php \  
php7-phar@php \  
php7-opcache@php \  
php7-session@php \  
php7-xml@php \  
php7-zlib@php \  
&& rm -rf /var/cache/apk/*  
  
# directory links  
RUN ln -s /etc/php7 /etc/php && \  
ln -s /usr/bin/php7 /usr/bin/php && \  
ln -s /usr/sbin/php-fpm7 /usr/bin/php-fpm && \  
ln -s /usr/lib/php7 /usr/lib/php  
  
# timezone  
ENV TZ=$timezone \  
COMPOSER_ALLOW_SUPERUSER=1  
RUN cp /usr/share/zoneinfo/$TZ /etc/localtime && \  
echo $TZ > /etc/timezone && date  
  
# php composer  
RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/bin
--filename=composer  
  
# set www-data group, prepare folders  
RUN set -x && \  
addgroup -g 82 -S www-data && \  
adduser -u 82 -D -S -G www-data www-data && \  
rm /etc/nginx/conf.d/default.conf && \  
mkdir -p /var/www/public /var/log/supervisord  
  
# copy files  
COPY .bashrc /root/.bashrc  
COPY supervisord.conf /etc/supervisord.conf  
COPY nginx.conf /etc/nginx/nginx.conf  
COPY nginx-sites.conf /etc/nginx/sites-enabled/default  
COPY php-fpm.conf /etc/php7/php-fpm.d/www.conf  
COPY start /root/start  
  
# expose  
EXPOSE 80  
# entrypoint  
ENTRYPOINT ["/root/start"]  

