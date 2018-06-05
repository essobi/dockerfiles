FROM php:7-fpm  
  
RUN requirements="libpng12-dev libmcrypt-dev libmcrypt4 libcurl3-dev
libfreetype6 libjpeg62-turbo libpng12-dev libfreetype6-dev libjpeg62-turbo-dev
mysql-client-5.5 libxml2-dev zlib1g-dev" \  
&& apt-get update && apt-get install -y $requirements && rm -rf
/var/lib/apt/lists/* \  
&& docker-php-ext-install pdo_mysql \  
&& docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-
dir=/usr/include/ \  
&& docker-php-ext-install gd \  
&& docker-php-ext-install mcrypt \  
&& docker-php-ext-install mbstring \  
&& docker-php-ext-install opcache \  
&& docker-php-ext-install soap \  
&& docker-php-ext-install zip \  
&& requirementsToRemove="libpng12-dev libmcrypt-dev libcurl3-dev libpng12-dev
libfreetype6-dev libjpeg62-turbo-dev libxml2-dev zlib1g-dev" \  
&& apt-get purge --auto-remove -y $requirementsToRemove  
  
ENV N98_MAGERUN_VERSION 1.97.22  
ENV N98_MAGERUN_URL
https://raw.githubusercontent.com/netz98/n98-magerun/$N98_MAGERUN_VERSION/n98-magerun.phar  
  
RUN curl -o /usr/local/bin/n98-magerun $N98_MAGERUN_URL \  
&& chmod +x /usr/local/bin/n98-magerun  
  
CMD ["php-fpm"]  

