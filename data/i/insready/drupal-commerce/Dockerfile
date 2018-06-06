FROM drupal:8.5  
# install the PHP extensions we need  
RUN apt-get update \  
&& apt-get install -y git \  
&& rm -rf /var/lib/apt/lists/* \  
&& docker-php-ext-install bcmath  
  
# install Composer globally  
RUN curl -sS https://getcomposer.org/installer | php \  
&& mv composer.phar /usr/local/bin/composer  
  
# install Drupal Commerce 2.x http://docs.drupalcommerce.org/v2/install.html  
RUN composer config repositories.drupal composer https://packages.drupal.org/8
\  
&& composer require "drupal/commerce" \--prefer-dist \  
&& chown -R www-data:www-data modules  

