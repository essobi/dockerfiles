# Dockerfile for running Slim  
FROM jchamberlain/php-fpm:latest  
  
# copy source code  
COPY . /var/www/  
RUN chown -R www-data /var/www/  
  
# run composer  
WORKDIR /var/www/  
RUN composer install --no-dev  
RUN chown -R www-data /var/www/vendor

