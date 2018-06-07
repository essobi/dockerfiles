############################################################  
# Dockerfile to build a Classic CMaNGOS register page  
############################################################  
  
FROM php:5.6-apache  
RUN docker-php-ext-install mysql mysqli pdo pdo_mysql  
  
ADD index.html /var/www/html/  
ADD register.php /var/www/html/  
ADD css /var/www/html/css  
ADD bg /var/www/html/bg  
  
  
EXPOSE 80

