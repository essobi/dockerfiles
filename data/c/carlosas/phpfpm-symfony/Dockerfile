FROM php:7-fpm  
  
# Set timezone  
ENV TIMEZONE=Europe/Madrid  
RUN ln -snf /usr/share/zoneinfo/${TIMEZONE} /etc/localtime \  
&& echo ${TIMEZONE} > /etc/timezone \  
&& printf '[PHP]\ndate.timezone = "%s"\n', ${TIMEZONE} >
/usr/local/etc/php/conf.d/tzone.ini  
  
# Install main needed packages  
RUN apt-get update \  
&& apt-get install -y curl wget git unzip openssl zlib1g-dev libicu-dev g++
libpng12-dev libjpeg-dev libmcrypt-dev libxml2-dev nano vim  
  
# Install PHP extensions  
RUN docker-php-ext-configure intl \  
&& docker-php-ext-install pdo pdo_mysql zip mysqli pcntl mcrypt soap gd
mbstring gettext intl bcmath json iconv session  
  
# Install composer  
RUN curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer  
  
# Install PHPREDIS  
ENV PHPREDIS_VERSION 3.0.0  
RUN mkdir -p /usr/src/php/ext/redis \  
&& curl -L
https://github.com/phpredis/phpredis/archive/$PHPREDIS_VERSION.tar.gz | tar
xvz -C /usr/src/php/ext/redis --strip 1 \  
&& echo 'redis' >> /usr/src/php-available-exts \  
&& docker-php-ext-install redis  
  
# Create an alias for the console  
RUN echo 'alias symfony="php /var/www/application/bin/console"' >> ~/.bashrc  
  
WORKDIR /var/www/application  

