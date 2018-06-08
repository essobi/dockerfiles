FROM library/php:5.6-apache  
  
MAINTAINER Jason Callaway <jason@jasoncallaway.com>  
  
COPY index.php /var/www/html/  
RUN rm -f /var/www/html/index.html  
  
EXPOSE 80  
CMD ["apache2-foreground"]  
  
# This is a comment  

