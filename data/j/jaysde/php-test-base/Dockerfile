FROM php:7.1-fpm-alpine  
  
ENV COMPOSER_ALLOW_SUPERUSER 1  
ENV COMPOSER_HOME /composer  
ENV COMPOSER_VERSION 1.3.2  
  
EXPOSE 8000  
  
RUN apk update && apk upgrade \  
&& apk add gcc libxml2 libxslt libcurl libc-dev libxml2-dev libxslt-dev make
curl icu-dev zlib-dev git redis autoconf\  
&& docker-php-ext-install intl \  
&& pecl install redis \  
&& pecl install apcu \  
&& pecl install xdebug \  
&& docker-php-ext-install mbstring \  
&& docker-php-ext-install zip \  
&& docker-php-ext-enable apcu \  
&& docker-php-ext-enable redis \  
&& docker-php-ext-enable xdebug \  
&& curl -s -f -L -o /tmp/installer.php
https://raw.githubusercontent.com/composer/getcomposer.org/5fd32f776359b8714e2647ab4cd8a7bed5f3714d/web/installer
\  
&& php -r " \  
\$signature =
'55d6ead61b29c7bdee5cccfb50076874187bd9f21f65d8991d46ec5cc90518f447387fb9f76ebae1fbbacf329e583e30';
\  
\$hash = hash('SHA384', file_get_contents('/tmp/installer.php')); \  
if (!hash_equals(\$signature, \$hash)) { \  
unlink('/tmp/installer.php'); \  
echo 'Integrity check failed, installer is either corrupt or worse.' .
PHP_EOL; \  
exit(1); \  
}" \  
&& php /tmp/installer.php --no-ansi --install-dir=/usr/bin --filename=composer
--version=${COMPOSER_VERSION} \  
&& rm /tmp/installer.php \  
&& composer --ansi --version --no-interaction \  
&& composer -n global require hirak/prestissimo \  
&& apk del gcc libxml2-dev libxslt-dev make \  
&& rm -rf /var/cache/apk/*  
  
ADD 60-user.ini /usr/local/etc/php/conf.d/  

