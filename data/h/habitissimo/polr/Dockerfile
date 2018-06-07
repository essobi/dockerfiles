FROM library/php:7.1.1-apache  
MAINTAINER Joan Font <jfont@habitissimo.com>  
  
# Install git  
RUN apt-get update && \  
apt-get install -y git zlib1g-dev && \  
apt-get clean && \  
rm -rf /tmp/* && \  
rm -rf /var/tmp/* && \  
rm -rf /var/lib/apt/lists/*  
  
RUN docker-php-ext-install pdo \  
pdo_mysql \  
tokenizer \  
zip  
  
# Install composer  
RUN curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer  
  
# See https://github.com/cydrobolt/polr  
ADD . /var/www/html  
  
RUN composer install --no-dev -o  
RUN chmod -R 755 . && chown -R www-data .  
  
COPY site.conf /etc/apache2/sites-available/000-default.conf  
RUN a2enmod rewrite  
  
RUN touch .env

