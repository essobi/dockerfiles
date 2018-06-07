FROM php:7-apache  
MAINTAINER Ando Roots <ando@sqroot.eu>  
  
WORKDIR /var/www  
EXPOSE 80 443  
# Install PHP and Apache2 extensions required by Laravel  
RUN apt-get update && \  
apt-get install -y libmcrypt-dev zlib1g-dev && \  
docker-php-ext-install pdo pdo_mysql mcrypt mbstring zip && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* /var/www/html && \  
a2enmod rewrite ssl allowmethods headers  
  
# Add and enable VirtualHost definition  
COPY build/000-default.conf /etc/apache2/sites-available/  
RUN a2dissite default-ssl && \  
rm /etc/apache2/sites-available/default-ssl.conf && \  
a2ensite 000-default && \  
curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer  
  
# Override default Apache2 runtime conf  
COPY build/apache2.conf /etc/apache2/  
  
# Add PHP conf  
COPY build/php.ini /usr/local/etc/php/conf.d/  
  
# Bundle the source code into the image  
# See https://github.com/jlhawn/dockramp/issues/2  
COPY ./ /var/www  
  
# Install Composer dependencies  
RUN bash -c 'if [[ ! -d "./vendor" ]]; then composer install --no-dev; fi'  
  
# Allow www-data to write to Laravel's cache/storage directories.  
# This is done with chmod as the COPY command copies everything into root
ownership -  
# this can not be changed (and won't be implemented by Docker due to frozen
Dockerfile syntax)  
RUN chown -R www-data:www-data . && \  
chmod -R 760 storage bootstrap/cache && \  
chmod -R ug+x artisan vendor/bin  
  

