FROM ubuntu:16.04  
MAINTAINER Pietro Bonaccorso 'pietro.b@mosaicoon.com'  
LABEL description='This image embeds Nginx 1.9 and php-fpm using PHP 7'  
  
ENV APP_CWD='/app/code' \  
APP_USER='application' \  
APP_GROUP='application' \  
VHOST_ROOT='/app/code' \  
VHOST_INDEX='index.php' \  
VHOST_TRYFILES='try_files $uri $uri/ /index.php?$query_string;' \  
PHP_MAXEXECUTIONTIME='30' \  
PHP_MEMORYLIMIT='128M' \  
PHP_DISPLAYERRORS='Off' \  
PHP_DISPLASTARTUPERRORS='Off' \  
PHP_ERRORREPORTING='E_ALL & ~E_DEPRECATED & ~E_STRICT' \  
PHP_VARIABLESORDER='GPCS' \  
PHP_POSTMAXSIZE='8M' \  
PHP_UPLOADMAXFILESIZE='2M' \  
PHP_SHORTOPENTAG='Off' \  
PHP_MODULESPATH='/usr/lib/php/20151012' \  
FPM_USER='application' \  
FPM_GROUP='application' \  
FPM_LISTEN='127.0.0.1:9000' \  
FPM_CLEARENV='no'  
RUN apt-get update  
RUN apt-get install -y sudo software-properties-common curl git wget  
RUN apt-add-repository ppa:ondrej/php -y  
RUN apt-get update  
  
RUN apt-get install -y --allow-unauthenticated php-cli php-dev php-pear \  
php-mysql php-pgsql php-sqlite3 \  
php-apcu php-json php-curl php-gd \  
php-gmp php-imap php-mcrypt php-xdebug \  
php-memcached php-redis php-mbstring php-zip \  
pkg-config libssl-dev libsslcommon2-dev && \  
pecl install mongodb  
  
RUN cp /usr/lib/php/20151012/mongodb.so /etc/php/7.0/mods-available/mongodb.so  
  
RUN apt-get install -y --allow-unauthenticated nginx php-fpm  
  
#install composer  
RUN wget https://getcomposer.org/composer.phar -O /usr/bin/composer && chmod
+x /usr/bin/composer  
  
#install supervisord  
RUN apt-get install -y supervisor  
  
#TEST packages  
RUN apt-get install -y --allow-unauthenticated vim inetutils-ping  
  
#Add configuration files  
COPY . /docker  
  
#start bootloader in build  
RUN /bin/bash /docker/scripts/bootloader.sh  
  
RUN mkdir /run/php  
  
#expose ports  
EXPOSE 80 443  
ENTRYPOINT ["bash", "/docker/scripts/entrypoint.sh"]  
CMD ["start-stack"]  
  
WORKDIR $APP_CWD  

