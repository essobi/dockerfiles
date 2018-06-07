FROM drupal:8.4  
# install extra tools  
RUN apt-get update \  
&& apt-get install -y git \  
&& rm -rf /var/lib/apt/lists/*  
# install Composer globally  
RUN curl -sS https://getcomposer.org/installer | php \  
&& mv composer.phar /usr/local/bin/composer  
  
  
# download lightning  
RUN cd /var \  
&& rm -rf /var/www \  
&& composer create-project acquia/lightning-project:^8.1.0 www --no-
interaction -vvv \  
&& ln -s /var/www/docroot /var/www/html \  
&& chown -R www-data:www-data /var/www/docroot  

