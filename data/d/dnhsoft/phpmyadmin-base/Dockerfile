FROM dnhsoft/php:7.1-apache  
  
RUN apt-get update && apt-get install -y \  
wget \  
mysql-client  
  
RUN docker-php-ext-install -j$(nproc) mysqli  
  
RUN pecl install apcu  
  
# setup apache configuration  
COPY ./000-default.conf /etc/apache2/sites-available/000-default.conf  
RUN a2enmod rewrite  
  
# setup phpmyadmin dir  
RUN mkdir -p /phpmyadmin && \  
rm -rf /var/www/html && ln -s /phpmyadmin /var/www/html  
  
# copy executables  
COPY ./install-pma.sh /install-pma.sh  
COPY ./wait-mysql.sh /wait-mysql.sh  
RUN chmod a+x /install-pma.sh /wait-mysql.sh  
  
RUN echo "" > /usr/local/etc/php/conf.d/pma-php.ini && \  
echo "upload_max_filesize = 128M" >> /usr/local/etc/php/conf.d/pma-php.ini &&
\  
echo "post_max_size = 256M" >> /usr/local/etc/php/conf.d/pma-php.ini && \  
echo "memory_limit = 256M" >> /usr/local/etc/php/conf.d/pma-php.ini && \  
echo "extension=mysqli.so" >> /usr/local/etc/php/conf.d/pma-php.ini && \  
echo "extension=apcu.so" >> /usr/local/etc/php/conf.d/pma-php.ini  
  
ENV DBHOST db  
ENV DBUSER root  
ENV DBPASS 123456  
ONBUILD COPY config.inc.php /config.inc.php

