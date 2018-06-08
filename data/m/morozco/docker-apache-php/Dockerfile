FROM php:5.6.26-apache  
MAINTAINER Miguel Cortes <miguel.cortes@decameron.com>  
RUN apt-get update  
RUN apt-get install -y vim  
ADD miguel.com.conf /etc/apache2/sites-available/  
ADD index.php /var/www/miguel.com/  
RUN rm /etc/apache2/sites-available/000-default.conf  
RUN chown -R www-data:www-data /var/www/miguel.com  
RUN chmod -R 755 /var/www  
RUN a2ensite miguel.com.conf  
RUN a2dissite 000-default.conf  
RUN service apache2 restart  

