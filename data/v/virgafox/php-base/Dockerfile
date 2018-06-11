FROM php:apache  
  
RUN apt-get update && apt-get install -y git libfreetype6-dev libjpeg62-turbo-
dev libmcrypt-dev libpng12-dev  
  
RUN docker-php-ext-install pdo_mysql mysqli sockets mbstring mcrypt zip  
RUN docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-
dir=/usr/include/ && docker-php-ext-install gd  
  
RUN curl -sS https://getcomposer.org/installer | php  
RUN mv composer.phar /usr/local/bin/composer  
  
ADD php.ini /usr/local/etc/php/  
RUN a2enmod rewrite  
  
RUN echo "ServerName localhost" | tee /etc/apache2/conf-available/fqdn.conf  
RUN a2enconf fqdn  
  
ADD site.conf /etc/apache2/sites-available/site.conf  
RUN ln -s /etc/apache2/sites-available/site.conf /etc/apache2/sites-
enabled/site.conf  
  
ADD startup.sh /root/startup.sh  
RUN chmod +x /root/startup.sh  
  
RUN usermod -u 1000 www-data  
  
VOLUME /data  
  
CMD ["bash", "/root/startup.sh"]

