FROM php:5.6-apache  
  
  
RUN apt-get update  
RUN apt-get install -y libldap2-dev  
  
RUN docker-php-ext-configure ldap --with-libdir=lib/x86_64-linux-gnu  
RUN docker-php-ext-install ldap  
  
RUN docker-php-ext-install iconv mysqli pdo pdo_mysql  
  
RUN a2enmod rewrite  
  
COPY config/php.ini /etc/php5/fpm/php.ini  

