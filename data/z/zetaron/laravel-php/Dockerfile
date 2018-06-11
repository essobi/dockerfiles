FROM php:7-fpm  
  
WORKDIR /var/www/html  
EXPOSE 9000  
CMD ["/usr/bin/start-php-fpm"]  
  
ADD start-php-fpm.sh /usr/bin/start-php-fpm  
ADD php-fpm.conf /usr/local/etc/php-fpm.conf  
  
RUN curl -o /usr/bin/docker-php-pecl-install -L
https://raw.githubusercontent.com/helderco/docker-
php/master/template/bin/docker-php-pecl-install \  
&& chmod +x /usr/bin/docker-php-pecl-install  
  
# Install laravel system requirements  
RUN apt-get update && apt-get install -y \  
libmcrypt-dev \  
# deps for pdo_mysql  
mysql-client \  
# deps of pdo_pgsql  
libpq-dev \  
postgresql-client \  
# deps of pdo_sqlite  
libsqlite3-dev \  
# deps for mongodb driver  
libssl-dev \  
# no deps  
&& docker-php-ext-install tokenizer \  
mbstring \  
pdo \  
# has deps  
&& docker-php-ext-install mcrypt \  
pdo_mysql \  
pdo_pgsql \  
pdo_sqlite \  
&& docker-php-pecl-install mongodb  

