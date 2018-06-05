# PHP with MySQL client  
# usage:  
# docker run --name phpmysql -p 80:80 -d silgon/phpmysql # or  
# docker run --name phpmysql -v $PWD:/var/www/html -p 80:80 -d silgon/phpmysql  
# test with: curl http://localhost  
FROM php:5.6-apache  
MAINTAINER Silgon <silgon3200@gmail.com>  
  
RUN docker-php-ext-install mysql mysqli pdo pdo_mysql  
RUN rm -rf /var/lib/apt/lists/*  
  
COPY index.html /var/www/html  
# next commands are not needed because they are repeated from others  
EXPOSE 80  
CMD ["apache2-foreground"]  

