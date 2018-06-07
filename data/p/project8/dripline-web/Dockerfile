FROM php:7.0-apache  
  
# Get amqp and ssl dependencies  
RUN apt-get update && apt-get install -y \  
libpq-dev \  
php-amqplib \  
ssl-cert  
  
# build ssl/require certs  
RUN make-ssl-cert generate-default-snakeoil &&\  
a2enmod ssl &&\  
ln -s /etc/apache2/sites-available/default-ssl.conf /etc/apache2/sites-
enabled/default-ssl.conf &&\  
ln -s /etc/apache2/mods-available/rewrite.load /etc/apache2/mods-
enabled/rewrite.load  
  
# install docker-specific php dependencies  
RUN docker-php-source extract \  
&& docker-php-ext-install -j$(nproc) bcmath \  
&& docker-php-source delete  
  
# add local content and config  
ADD . /var/www/html/dripline-web  
ADD platform/php.ini /usr/local/etc/php/php.ini  

