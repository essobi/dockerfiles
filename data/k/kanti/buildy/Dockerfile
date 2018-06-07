FROM php:7.2-alpine  
MAINTAINER Matthias Vogel <git@kanti.de>  
  
# add file for https://github.com/pluswerk/grumphp-bom-task  
# @see FROM https://github.com/alpine-docker/git  
RUN apk --update add file bash git openssh libxml2-dev && \  
rm -rf /var/lib/apt/lists/* && \  
rm /var/cache/apk/*  
  
RUN docker-php-ext-install soap mysqli  
  
# @see FROM https://getcomposer.org/download/  
RUN cd /bin && \  
php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');" && \  
php -r "if (hash_file('SHA384', 'composer-setup.php') ===
'544e09ee996cdf60ece3804abc52599c22b1f40f4323403c44d44fdfdd586475ca9813a858088ffbc1f233e9b180f061')
{ echo 'Installer verified'; } else { echo 'Installer corrupt';
unlink('composer-setup.php'); } echo PHP_EOL;" && \  
php composer-setup.php --filename=composer && \  
php -r "unlink('composer-setup.php');" && \  
composer global require hirak/prestissimo && \  
composer clear-cache  

