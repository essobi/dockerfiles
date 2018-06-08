FROM php:7.1-apache  
  
# Set default system timezone  
RUN ln -sf /usr/share/zoneinfo/Europe/Paris /etc/localtime  
  
# Install last update and php extension  
RUN apt-get update && apt-get install -y \  
git \  
vim \  
bzip2 \  
zip \  
libbz2-dev \  
libmcrypt-dev \  
libicu-dev \  
&& docker-php-ext-configure mysqli \  
&& docker-php-ext-install mysqli pdo_mysql bz2 mcrypt intl  
  
# Enable Apache Rewrite module  
RUN a2enmod rewrite  
  
#Install mysql server  
RUN apt-get update && \  
DEBIAN_FRONTEND=noninteractive apt-get -qq install mysql-server  
  
# Default Vhost for developement  
COPY vhost.conf /etc/apache2/sites-available/000-default.conf  
  
#Install composer  
RUN curl -sS https://getcomposer.org/installer | php \  
&& mv composer.phar /usr/bin/composer  
  
CMD ["apache2-foreground"]  

