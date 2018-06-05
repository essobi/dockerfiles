# remember to import your database, adjust paths, and user/password pairs in  
# <ark>/config/env_settings.php and ./docker-compose.yml  
  
FROM php:5.4-apache  
  
RUN a2enmod rewrite  
  
RUN apt-get update \  
&& apt-get install -y libpng12-dev libjpeg-dev libmagickwand-dev --no-install-
recommends \  
&& rm -rf /var/lib/apt/lists/* \  
&& docker-php-ext-configure gd --with-png-dir=/usr --with-jpeg-dir=/usr \  
&& docker-php-ext-install mysql mysqli gd zip  
# libpq-dev  
# mbstring pdo pdo_mysql pdo_pgsql  

