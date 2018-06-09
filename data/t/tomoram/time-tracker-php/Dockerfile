FROM php:7.0-apache  
  
RUN docker-php-ext-install pdo pdo_mysql sockets  
  
# Install ZLib (for composer)  
RUN apt-get update \  
&& apt-get install -y zlib1g-dev \  
&& docker-php-ext-install zip  
  
# Install PHP Curl extension (for composer)  
RUN apt-get update \  
&& apt-get install -y libcurl4-openssl-dev \  
&& docker-php-ext-install curl  
  
# Install git (for composer)  
RUN apt-get update \  
&& apt-get install -y git  
  
# Install Composer  
RUN php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');"
\  
&& php composer-setup.php \--install-dir=/usr/local/bin \--filename=composer \  
&& php -r "unlink('composer-setup.php');"  

