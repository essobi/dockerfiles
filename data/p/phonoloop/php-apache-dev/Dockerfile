FROM phonoloop/php-apache  
MAINTAINER phonoloop <phonoloop@spaceape.be>  
  
# Install Composer  
RUN curl -s http://getcomposer.org/installer | php \  
&& mv composer.phar /usr/local/bin/composer  
  
# Install Composer global dependencies  
# To create a project using CLI do:  
# For Lavarel: docker exec “container id” composer create-project
laravel/laravel . or “name (optional)”  
RUN composer global require "laravel/installer"  
# For Lumen: docker exec “container id” composer create-project laravel/lumen
. or “name (optional)”  
RUN composer global require "laravel/lumen-installer"  
  
# Install Xdebug  
RUN pecl install xdebug-2.5.0 \  
&& docker-php-ext-enable xdebug  
  
COPY ./xdebug.ini /usr/local/etc/php/php.ini  

