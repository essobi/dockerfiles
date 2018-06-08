FROM php:5.6-apache  
  
MAINTAINER Maycon Brito <mayconfsbrito@gmal.com>  
  
RUN apt-get update && \  
apt-get install -y zlib1g-dev libicu-dev g++ libxml2-dev zip unzip curl git  
  
#RUN docker-php-pecl-install xdebug-2.5.5  
RUN docker-php-ext-configure intl && \  
docker-php-ext-install intl mbstring bcmath zip  
  
#ADD files/docker-php-pecl-install /usr/local/bin  
COPY php.ini /usr/local/etc/php/php.ini  
  
RUN php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');"
&& \  
php composer-setup.php --install-dir=/usr/bin --filename=composer && \  
php -r "unlink('composer-setup.php');"  
  
RUN a2enmod rewrite && service apache2 restart  
  
RUN composer create-project potsky/pimp-my-log /var/www/html  
COPY config.user.php /var/www/html/  
COPY config.user.d/ /var/www/html/config.user.d  
COPY config.auth.user.php /var/www/html/  
  
RUN chown -R www-data:www-data /var/www/html  
  
EXPOSE 80

