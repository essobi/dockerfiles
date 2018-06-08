FROM php:7-apache  
  
RUN curl -L
https://github.com/simpspector/simpspector/releases/download/alpha1/simpspector.tar.gz
| tar zx -C /var/www  
RUN rm -rf /var/www/html && ln -s /var/www/simpspector/web /var/www/html  
RUN chown -Rf www-data:www-data /var/www/simpspector/var && chmod +x
/var/www/simpspector/bin/*  
  
RUN a2enmod rewrite && service apache2 restart  

