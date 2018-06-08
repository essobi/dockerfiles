FROM php:5.6-apache  
  
# Apache configuration  
RUN a2enmod rewrite  
RUN echo "ServerName localhost" >> /etc/apache2/apache2.conf  
  
RUN mkdir /var/www/crabtree && mkdir /var/www/crabtree/web  
RUN rm -rf /var/www/html  
RUN ln -s /var/www/crabtree/web /var/www/html  
  
WORKDIR /var/www/crabtree  
  
# Install Composer.  
RUN curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer  
  
# Set user 1000 and group staff to www-data, enables write permission.  
# https://github.com/boot2docker/boot2docker/issues/581#issuecomment-114804894  
RUN usermod -u 1000 www-data  
RUN usermod -G staff www-data  
  
# Adding custom PHP settings.  
COPY php.ini /usr/local/etc/php/conf.d/php.ini  
  
VOLUME ["/var/www/crabtree"]  

