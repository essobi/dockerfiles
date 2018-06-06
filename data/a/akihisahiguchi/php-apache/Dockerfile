FROM php:7-apache  
COPY config/php.ini /usr/local/etc/php/  
  
RUN a2enmod rewrite  
RUN echo "ServerName localhost" >> /etc/apache2/conf-available/servername.conf
&& a2enconf servername  
  
RUN docker-php-ext-install opcache mbstring  
RUN pecl install apcu-beta && echo extension=apcu.so >
/usr/local/etc/php/conf.d/apcu.ini  

