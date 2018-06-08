FROM php:apache  
  
RUN a2enmod rewrite && \  
docker-php-ext-install mysqli gettext  
  
ENV APP_HOME /var/www/html  
  
VOLUME /var/www/html  
WORKDIR $APP_HOME  
  
EXPOSE 80  

