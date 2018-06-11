FROM php:7.2-apache  
  
# Install all necessary packages  
RUN apt-get -qq -y update -y && apt-get -qq -y install openssl \  
zip \  
unzip \  
git \  
wget \  
curl \  
supervisor \  
libicu-dev  
  
# Set Apache's run user to root, because /storage will be a volume  
ENV APACHE_RUN_USER root  
ENV APACHE_RUN_GROUP root  
  
# Change Apache's DocumentRoot, see https://hub.docker.com/_/php/  
ENV APACHE_DOCUMENT_ROOT /var/www/wolfpanel/public  
RUN sed -ri -e 's!/var/www/html!${APACHE_DOCUMENT_ROOT}!g' /etc/apache2/sites-
available/*.conf  
RUN sed -ri -e 's!/var/www/!${APACHE_DOCUMENT_ROOT}!g'
/etc/apache2/apache2.conf /etc/apache2/conf-available/*.conf  
  
# Configure PHP and delete its source afterwards for a smaller image  
RUN docker-php-ext-install pdo_mysql mysqli opcache intl pcntl  
RUN docker-php-source delete  
  
# Install Composer  
RUN curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer  
  
# Copy all source files, so DocumentRoot matches our app  
WORKDIR /var/www/wolfpanel  
COPY . .  
  
#COPY ./etc/supervisor/horizon.conf /etc/supervisor/conf.d/horizon.conf  
COPY ./.env.docker ./.env  
  
# Finally install all dependencies and dump the autoload for more performance  
RUN composer install && composer dump-autoload  
  
VOLUME /var/www/wolfpanel/storage

