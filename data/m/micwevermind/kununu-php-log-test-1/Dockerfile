#FROM richarvey/nginx-php-fpm:latest  
FROM library/php:7.2-apache  
  
RUN rm -rf /var/www/html/*  
ADD webroot/ /var/www/html/  
ADD run.sh /run.sh  
CMD /run.sh  

