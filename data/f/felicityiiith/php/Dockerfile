FROM php:5-apache  
  
ENV TIMEZONE Asia/Kolkata  
ENV PHP_INI_DIR /usr/local/etc/php  
RUN echo "[Date]\ndate.timezone = ${TIMEZONE}" >
$PHP_INI_DIR/conf.d/timezone.ini  
  
RUN apt-get update  
RUN apt-get install -y libicu-dev  
RUN docker-php-ext-install gettext intl mysqli  
RUN a2enmod rewrite && a2enmod headers  
  
ENV APACHE_DOCUMENT_ROOT /var/www/html/build  
RUN sed -ri -e 's!/var/www/html!${APACHE_DOCUMENT_ROOT}!g' /etc/apache2/sites-
available/*.conf  
RUN sed -ri -e 's!/var/www/!${APACHE_DOCUMENT_ROOT}!g'
/etc/apache2/apache2.conf /etc/apache2/conf-available/*.conf  

