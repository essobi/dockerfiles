FROM php:5.6-fpm  
  
ENV APACHE_RUN_USER www-data  
ENV APACHE_RUN_GROUP www-data  
ENV DEBIAN_FRONTEND=noninteractive  
  
RUN apt-get update && \  
apt-get -y install libpqxx-dev build-essential && \  
apt-get clean all  
RUN docker-php-ext-install pgsql  
RUN docker-php-ext-enable pgsql  
  
RUN echo date.timezone = "UTC" > /usr/local/etc/php/conf.d/timezone.ini  
COPY websystem/system /var/www/html/system  
COPY websystem/index.php /var/www/html/  
COPY resources /var/www/html/resources  
COPY application /var/www/html/application  
RUN chown -R "$APACHE_RUN_USER:$APACHE_RUN_GROUP" /var/www/html  

