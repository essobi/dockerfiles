FROM php:7.1-apache  
  
COPY . /var/www  
  
RUN apt-get update \  
&& apt-get install -y \  
\--no-install-recommends \  
unzip \  
libpcre3 \  
libpcre3-dev \  
libzip-dev \  
&& rm -rf /var/lib/apt/lists/* \  
&& pecl install \  
zip \  
oauth-2.0.2 \  
&& docker-php-ext-enable \  
oauth \  
&& docker-php-ext-install \  
pdo \  
pdo_mysql \  
&& curl https://getcomposer.org/installer | php \  
&& mv composer.phar /usr/local/bin/composer \  
&& composer install -n -d .. \  
&& apt-get purge -y \  
unzip  

