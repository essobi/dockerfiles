FROM drupal:8.1-fpm  
  
RUN apt-get update \  
&& apt-get install -y git \  
&& rm -rf /var/lib/apt/lists/* \  
&& docker-php-ext-install bcmath  
  
RUN curl -sS https://getcomposer.org/installer | php \  
&& mv composer.phar /usr/local/bin/composer  
  
RUN composer config repositories.drupal composer https://packagist.drupal-
composer.org \  
&& composer require "drupal/commerce 8.2.x-dev" \--prefer-dist \  
&& chown -R www-data:www-data modules  
  
VOLUME /var/www/html  

