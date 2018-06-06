FROM php:5.6-fpm  
  
MAINTAINER <julien.fastre@champs-libres.coop>  
  
RUN apt-get update && apt-get -y install wget ca-certificates \  
&& wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | apt-
key add -  
  
RUN echo "deb http://apt.postgresql.org/pub/repos/apt/ jessie-pgdg main" >
/etc/apt/sources.list.d/pgdg.list  
  
RUN apt-get update && apt-get -y install libicu52 \  
libicu-dev \  
g++ \  
postgresql-server-dev-9.4  
RUN docker-php-ext-install intl pdo_pgsql mbstring  
  
#remove unused packages  
RUN apt-get remove -y wget libicu-dev \  
g++ \  
&& apt-get autoremove -y  
  
#php configuration  
RUN echo "\  
[Date] \  
date.timezone = Europe/Brussels" \  
>> /usr/local/etc/php/php.ini \  
&& echo "\  
ping.path = /ping" \ >> /usr/local/etc/php-fpm.conf \  
&& echo "\  
pm.status_path = /status" >> /usr/local/etc/php-fpm.conf  
  
#install composer  
WORKDIR /tmp  
ADD https://getcomposer.org/installer installer  
RUN cat installer | php \  
&& mv composer.phar /usr/local/bin/composer \  
&& rm /tmp/installer  
  
#install flavor  
WORKDIR /var/www/chill  
RUN composer create-project chill-project/standard /var/www/chill \  
\--stability=dev --no-dev --no-install --no-interaction --prefer-dist \  
\--repository-url http://packages.chill.social  
ADD composer.json /var/www/chill/composer.json  
ADD AppKernel.php /var/www/chill/app/AppKernel.php  
ADD parameters.yml /var/www/chill/app/config/parameters.yml  
ADD parameters.php /var/www/chill/app/config/parameters.php  
RUN export SYMFONY_ENV=prod; composer install --no-interaction  
  
RUN ln -sf /dev/stdout /var/www/chill/app/logs/prod.log  
  
ADD entrypoint.sh /entrypoint.sh  
RUN chmod u+x /entrypoint.sh  
  
VOLUME ["/var/www/chill/web/js", "/var/www/chill/web/css",
"/var/www/chill/web/bundles"]  
  
ENTRYPOINT /entrypoint.sh  
  

