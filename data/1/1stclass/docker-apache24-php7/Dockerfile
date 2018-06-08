# Note: After you created container, you cannot execute apt-get on the
container  
FROM php:7.2-apache  
RUN sed -ri -e 's!/var/www/html!${APACHE_DOCUMENT_ROOT}!g' /etc/apache2/sites-
available/*.conf /etc/apache2/conf-available/*.conf /etc/apache2/mods-
available/*.conf  
RUN sed -ri -e 's!/var/www/!${APACHE_DOCUMENT_ROOT}!g'
/etc/apache2/apache2.conf /etc/apache2/conf-available/*.conf
/etc/apache2/conf-available/*.conf /etc/apache2/mods-available/*.conf  
RUN sed -ri -e 's!AllowOverride None!AllowOverride All!g'
/etc/apache2/apache2.conf /etc/apache2/sites-available/*.conf
/etc/apache2/conf-available/*.conf /etc/apache2/mods-available/*.conf  
RUN a2enmod rewrite  
  
RUN apt-get update && apt-get install -y libssl-dev libcurl4-openssl-dev pkg-
config  
# apt-utils  
RUN apt-get update && \  
apt-get install -y curl zlib1g-dev  
  
RUN /usr/local/bin/docker-php-ext-install curl mysqli zip  
  
RUN echo '\  
log_errors = On\n\  
error_log = /dev/stderr\n\  
error_reporting = E_ALL\n\  
' >> /usr/local/etc/php/php.ini  
  
#COPY httpd.conf /usr/local/apache2/conf/httpd.conf  

