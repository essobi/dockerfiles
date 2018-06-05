FROM php:5.6-fpm  
MAINTAINER Camil Blanaru <camil@edka.io>  
  
#install laravel requirements and aditional extensions  
RUN requirements="libmcrypt-dev g++ libicu-dev libmcrypt4 libicu52 zlib1g-dev
git" \  
&& apt-get update && apt-get install -y $requirements \  
&& docker-php-ext-install pdo_mysql \  
&& docker-php-ext-install mcrypt \  
&& docker-php-ext-install mbstring \  
&& docker-php-ext-install intl \  
&& docker-php-ext-install json \  
&& docker-php-ext-install zip \  
&& requirementsToRemove="libmcrypt-dev g++ libicu-dev zlib1g-dev" \  
&& apt-get purge --auto-remove -y $requirementsToRemove \  
&& rm -rf /var/lib/apt/lists/*  
  
#install composer globally  
RUN curl -sSL https://getcomposer.org/installer | php \  
&& mv composer.phar /usr/local/bin/composer  
  
#replace default php-fpm config  
RUN rm -v /usr/local/etc/php-fpm.conf  
  
COPY config/php-fpm.conf /usr/local/etc/  
  
#add custom php.ini  
COPY config/php.ini /usr/local/etc/php/  
  
#Change www-data UID  
RUN usermod -u 1000 www-data \  
&& groupmod -g 1000 www-data  
  
# Setup Volume  
VOLUME ["/usr/share/nginx/html"]  
  
#Set Workdir  
WORKDIR /usr/share/nginx/html  
  
#Add entrypoint  
COPY docker-entrypoint.sh /entrypoint.sh  
  
ENTRYPOINT ["/entrypoint.sh"]  
  
CMD ["php-fpm"]  

