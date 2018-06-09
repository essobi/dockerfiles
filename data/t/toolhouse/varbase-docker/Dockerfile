FROM drupal:8.4  
# Install extra tools  
RUN apt-get update \  
&& apt-get install -y git \  
&& rm -rf /var/lib/apt/lists/*  
# Install Composer  
RUN curl -sS https://getcomposer.org/installer | php \  
&& mv composer.phar /usr/local/bin/composer  
  
  
# Install Varbase  
RUN cd /var \  
&& rm -rf /var/www \  
&& composer create-project vardot/varbase-project:^8.4.19 www --no-dev --no-
interaction -vvv \  
&& ln -s /var/www/docroot /var/www/html \  
&& chown -R www-data:www-data /var/www/docroot

