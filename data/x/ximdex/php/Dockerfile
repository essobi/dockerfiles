FROM php:7-fpm-alpine  
# Install modules  
  
RUN apk add --no-cache unzip icu-dev pwgen gettext gettext-dev libcurl
libmcrypt-dev libxml2-dev libxslt-dev freetype libpng libjpeg-turbo freetype-
dev libpng-dev libjpeg-turbo-dev curl-dev tzdata  
  
RUN docker-php-ext-configure gd \  
\--with-gd \  
\--with-freetype-dir=/usr/include/ \  
\--with-png-dir=/usr/include/ \  
\--with-jpeg-dir=/usr/include/ && \  
docker-php-ext-install gd \  
&& docker-php-ext-configure sysvmsg \  
&& docker-php-ext-configure sysvsem \  
&& docker-php-ext-configure sysvshm \  
&& docker-php-ext-install pcntl sysvmsg sysvsem sysvshm gettext pdo pdo_mysql
curl xmlrpc gd intl xsl mcrypt opcache \  
&& apk del --no-cache freetype-dev libpng-dev libjpeg-turbo-dev  
  
RUN apk add --no-cache openssl  
  
RUN echo "Europe/Madrid" > /etc/timezone  
  
RUN touch /var/log/cron.log && \  
echo "* * * * * (/usr/local/bin/php
/var/www/html/modules/ximSYNC/scripts/scheduler/scheduler.php) >>
/var/www/html/logs/scheduler.log 2>&1" >> mycron && \  
crontab mycron && \  
rm mycron  
  
CMD crond && php-fpm

