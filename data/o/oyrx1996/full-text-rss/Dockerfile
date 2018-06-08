FROM daocloud.io/php:5.6-apache  
RUN apt-get update && apt-get install -y \  
libfreetype6-dev \  
libjpeg62-turbo-dev \  
libmcrypt-dev \  
libpng12-dev \  
&& apt-get -y install libtidy-dev \  
&& docker-php-ext-install tidy \  
&& pecl install apcu-4.0.11 \  
&& echo extension=apcu.so > /usr/local/etc/php/conf.d/apcu.ini  
COPY . /var/www/html/  
RUN chmod -R 777 /var/www/html/cache/

