FROM php:5.6-apache  
  
RUN a2enmod rewrite expires  
  
# install the PHP extensions  
RUN apt-get update \  
&& apt-get install -y libpng12-dev libjpeg-dev libpq-dev \  
&& rm -rf /var/lib/apt/lists/* \  
&& docker-php-ext-configure gd --with-png-dir=/usr --with-jpeg-dir=/usr \  
&& docker-php-ext-install gd opcache mysqli pgsql pdo_mysql pdo_pgsql  
  
# set recommended PHP.ini settings  
# see https://secure.php.net/manual/en/opache.installation.php  
RUN { \  
echo 'opcache.memory_consumption=128'; \  
echo 'opcache.interned_strings_buffer=8'; \  
echo 'opcache.max_accelerated_files=4000'; \  
echo 'opcache.revalidate_freq=60'; \  
echo 'opcache.fast_shutdown=1'; \  
echo 'opcache.enable_cli=1'; \  
} > /usr/local/etc/php/conf.d/opcache-recommended.ini  

