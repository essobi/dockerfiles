FROM php:7.1.9-apache  
  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends sqlite3 \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN mkdir /var/www/res \  
&& chown www-data:www-data /var/www/res  
  
COPY html /var/www/html  
  
RUN sqlite3 < /var/www/html/sql/school.sql \  
&& chown www-data:www-data /var/www/res/school.db  
  
CMD ["apache2-foreground"]  
  

