FROM php:7.0  
RUN docker-php-ext-install mysqli  
  
RUN curl -O https://raw.githubusercontent.com/wp-cli/builds/gh-pages/phar/wp-
cli.phar \  
&& chmod +x wp-cli.phar \  
&& mv wp-cli.phar /usr/local/bin/wp  
  
USER www-data  
  
WORKDIR /source  

