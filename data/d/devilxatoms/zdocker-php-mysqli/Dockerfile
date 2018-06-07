FROM php:5.6-fpm  
MAINTAINER Brayan Caldera "ing.brayan.cm@gmail.com"  
RUN apt-get update && apt-get install -y sqlite php5-sqlite php5-mysql
php5-odbc mysql-client zlib1g-dev libmcrypt-dev cron awscli nodejs npm  
RUN docker-php-ext-install -j$(nproc) zip mysqli mcrypt mbstring bcmath pdo
pdo_mysql opcache  
  
COPY php-fpm.conf /usr/local/etc/  
COPY php.ini /usr/local/etc/php/php.ini  
  
EXPOSE 9000 8080  
CMD ["php-fpm", "-F", "-R"]  

