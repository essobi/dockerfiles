FROM php:7.0-alpine  
  
RUN apk add \--update postgresql-dev gettext-dev libpng-dev icu-dev openldap-
dev zlib-dev \  
&& docker-php-ext-install gd gettext intl ldap mysqli pdo_mysql pdo_pgsql
pgsql zip  
  
RUN php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');"
\  
&& php composer-setup.php \--install-dir=/usr/local/bin \--filename=composer \  
&& php -r "unlink('composer-setup.php');" \  
&& php -m  

