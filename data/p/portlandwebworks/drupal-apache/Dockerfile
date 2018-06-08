FROM php:5.6-apache  
MAINTAINER portlandwebworks  
  
ENTRYPOINT ["/root/entrypoint.sh"]  
  
# Change our shell  
RUN rm /bin/sh \  
&& ln -s /bin/bash /bin/sh  
  
# Install pre-requisite software  
RUN apt-get update \  
&& apt-get install -y libpng12-dev libjpeg-dev libpq-dev libxml2-dev \  
&& apt-get clean  
  
# Enable apache mods  
RUN a2enmod rewrite \  
&& a2enmod ssl \  
&& a2enmod headers  
  
# Install additional PHP extensions  
RUN docker-php-ext-configure gd --with-png-dir=/usr --with-jpeg-dir=/usr \  
&& docker-php-ext-install gd mbstring pdo pdo_mysql pdo_pgsql zip soap xmlrpc
opcache \  
&& pecl install -o -f xdebug \  
&& rm -rf /tmp/pear  
  
# Copy configs  
ADD conf/* $PHP_INI_DIR/conf.d/  
  
# Apache config  
ADD vhost/000-default.conf /etc/apache2/sites-available/  
  
# Setup self-signed ssl  
ADD vhost/default-ssl.conf /etc/apache2/sites-available/  
  
# Enable non-ssl  
RUN a2ensite 000-default.conf  
  
# Enable ssl  
RUN a2ensite default-ssl.conf  
  
# Add entrypoint  
ADD entrypoint.sh /root

