FROM php:5.6-apache  
  
RUN apt-get update && apt-get install -y \  
php5-mysql \  
libfreetype6-dev \  
libjpeg62-turbo-dev \  
libmcrypt-dev \  
libpng12-dev \  
libbz2-dev \  
php-pear \  
curl \  
git \  
subversion \  
unzip \  
&& pecl install zip \  
&& docker-php-ext-install mysql mysqli pdo pdo_mysql mcrypt zip bz2 mbstring \  
&& cd /tmp && curl -sS https://getcomposer.org/installer | php && mv
composer.phar /usr/local/bin/composer  
  
RUN echo "date.timezone=${PHP_TIMEZONE:-UTC}" >
$PHP_INI_DIR/conf.d/date_timezone.ini  
  
ENV COMPOSER_ALLOW_SUPERUSER 1  
COPY config/symfony.conf /etc/apache2/sites-enabled  
  
# Add files needed for Composer  
COPY symfony/composer.json /var/www/html/  
COPY symfony/composer.lock /var/www/html/  
RUN mkdir app  
COPY symfony/app /var/www/html/app  
  
# Run Composer to install dependencies  
WORKDIR /var/www/html/  
RUN composer install --no-scripts  
  
COPY symfony /var/www/html/

