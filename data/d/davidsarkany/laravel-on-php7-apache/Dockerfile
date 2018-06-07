FROM php:7-apache  
RUN docker-php-ext-install \  
pdo_mysql \  
opcache  
  
COPY --from=composer:latest /usr/bin/composer /usr/bin/composer  
  
ADD config/remoteip.conf /etc/apache2/mods-available/  
  
ENV APACHE_DOCUMENT_ROOT /var/www/html/public  
RUN sed -ri -e 's!/var/www/html!${APACHE_DOCUMENT_ROOT}!g' /etc/apache2/sites-
available/*.conf &&\  
sed -ri -e 's!/var/www/!${APACHE_DOCUMENT_ROOT}!g' /etc/apache2/apache2.conf
/etc/apache2/conf-available/*.conf &&\  
sed -ri -e 's!"%h %l %u %t \\\"%r\\\"!"%a %l %u %t \\\"%r\\\"!g'
/etc/apache2/apache2.conf &&\  
a2enmod remoteip &&\  
a2enmod rewrite

