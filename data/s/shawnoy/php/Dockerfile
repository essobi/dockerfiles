FROM php:7.2.2-fpm-alpine  
  
LABEL maintainer "shawnoy@outlook.com"  
  
ARG COMPOSER_VERSION=1.6.3  
  
RUN php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');"
&& \  
php -r "if (hash_file('SHA384', 'composer-setup.php') ===
'544e09ee996cdf60ece3804abc52599c22b1f40f4323403c44d44fdfdd586475ca9813a858088ffbc1f233e9b180f061')
{ echo 'Installer verified'; } else { echo 'Installer corrupt';
unlink('composer-setup.php'); } echo PHP_EOL;" && \  
php composer-setup.php \--install-dir=/usr/local/bin \--filename=composer
\--version=1.6.3 && \  
php -r "unlink('composer-setup.php');"  

