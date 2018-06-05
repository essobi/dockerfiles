FROM php:7.1.10-apache  
  
LABEL maintainer="sebastian.plattner@gmail.com"  
  
ENV PORT 8080  
ENTRYPOINT []  
CMD sed -i "s/80/$PORT/g" /etc/apache2/sites-available/000-default.conf
/etc/apache2/ports.conf && docker-php-entrypoint apache2-foreground  
  
RUN apt-get update && apt-get install -y \  
libxml2-dev git curl\  
&& docker-php-ext-install pdo pdo_mysql soap  
  
RUN apt-get clean  
  
RUN curl -sS https://getcomposer.org/installer | php \  
&& mv composer.phar /usr/local/bin/ \  
&& ln -s /usr/local/bin/composer.phar /usr/local/bin/composer  
  
COPY . /var/www/html/  
WORKDIR /var/www/html  
  
RUN composer install --prefer-source --no-interaction  
  
EXPOSE $PORT  
  
RUN chmod -R a+w /var/www/html/skins/default/templates_c  
RUN chown www-data:www-data -R /var/www/html/  
  
ENV PATH="~/.composer/vendor/bin:./vendor/bin:${PATH}"  

