FROM php:5-apache  
  
MAINTAINER Raymond Piller <ray@unt.edu>  
  
  
# Apache & PHP configuration  
RUN a2enmod rewrite  
ADD docker/apache/vhost.conf /etc/apache2/sites-enabled/000-default.conf  
ADD docker/php/php.ini /usr/local/etc/php/php.ini  
  
# Install OS Requirements && PHP Core Extensions  
RUN requirements="wget git libfreetype6-dev libjpeg62-turbo-dev libpng12-dev"
\  
&& apt-get update && apt-get install -y $requirements \  
&& docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-
dir=/usr/include/ \  
&& docker-php-ext-install -j$(nproc) gd  
  
# Add the application  
WORKDIR /var/www  
ADD docker docker  
ADD html html  
RUN chmod +x /var/www/docker/apache/run.sh \  
&& chmod +x /var/www/docker/apache/start_safe_perms  
  
# Cleanup  
RUN chown -R www-data /var/www \  
&& apt-get remove -y wget git \  
&& rm -rf /var/lib/apt/lists/* \  
&& apt-get purge --auto-remove -y  
  
CMD ["/var/www/docker/apache/run.sh"]

