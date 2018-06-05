FROM php:5.6-apache  
MAINTAINER Marcello de Sales <marcello@quantogastei.com>  
  
# Enabling the PHP MySQL PDO library required by CakePHP  
# http://stackoverflow.com/questions/15223480/unable-to-connect-cakephp-
database-on-godaddy-  
# https://github.com/docker-library/php/issues/91#event-283633935  
# https://hub.docker.com/_/php/ "How to install more PHP extensions"  
RUN docker-php-ext-install mysql mysqli pdo pdo_mysql  
  
# Enabling the header module  
RUN ln -s /etc/apache2/mods-available/headers.load /etc/apache2/mods-enabled  
RUN ln -s /etc/apache2/mods-available/rewrite.load /etc/apache2/mods-enabled  
  
# Starting apache in the foreground  
CMD ["apache2-foreground"]  
  

