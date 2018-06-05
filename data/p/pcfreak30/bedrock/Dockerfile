FROM php:5.6-apache  
  
RUN a2enmod rewrite  
  
# install the PHP extensions we need  
RUN apt-get update && apt-get install -y libpng12-dev libjpeg-dev git && rm
-rf /var/lib/apt/lists/* \  
&& docker-php-ext-configure gd --with-png-dir=/usr --with-jpeg-dir=/usr \  
&& docker-php-ext-install gd mysqli zip  
  
# Install WP-CLI  
RUN curl https://raw.githubusercontent.com/wp-cli/builds/gh-pages/phar/wp-
cli.phar \  
-o /usr/local/bin/wp \  
&& chmod +x /usr/local/bin/wp  
  
#Install composer  
RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/bin
--filename=composer  
  
WORKDIR /usr/src/wordpress  
  
# Clones bedrock git and checks out latest tag so this gives us
/usr/src/wordpress  
RUN git clone https://github.com/roots/bedrock -b 1.5.3 /usr/src/wordpress \  
&& git fetch -q --tags \  
&& git checkout $(git describe --tags $(git rev-list --tags --max-count=1)) \  
&& chown -R www-data:www-data /usr/src/wordpress  
  
#Copy entry point and php config  
COPY docker-entrypoint.sh /entrypoint.sh  
COPY php.ini /usr/local/etc/php/php.ini  
  
RUN sed -i 's#DocumentRoot.*#DocumentRoot /var/www/web#'
/etc/apache2/apache2.conf && mv \  
/var/www/html /var/www/web  
  
VOLUME /var/www  
WORKDIR /var/www  
# grr, ENTRYPOINT resets CMD now  
ENTRYPOINT ["/entrypoint.sh"]  
CMD ["apache2-foreground"]  

