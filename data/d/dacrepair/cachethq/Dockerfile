FROM php:apache  
MAINTAINER DACRepair@gmail.com  
  
# Start  
RUN apt-get update  
  
# Install GIT  
RUN apt-get -y install git  
  
# Install GD  
RUN apt-get install -y libfreetype6-dev libjpeg62-turbo-dev libpng12-dev  
RUN docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-
dir=/usr/include/  
RUN docker-php-ext-install gd  
  
# Install APCu  
RUN pecl install apcu  
RUN echo "extension=apcu.so" > /usr/local/etc/php/conf.d/apcu.ini  
  
# Install PDO Plugins  
RUN apt-get -y install unzip libsqlite3-dev libpq-dev mysql-client  
RUN docker-php-ext-install pdo pdo_mysql pdo_pgsql pdo_sqlite  
  
# Install composer  
RUN curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer  
  
# Install Cachet  
RUN git clone https://github.com/cachethq/Cachet.git /var/www/html  
  
# Enable Rewrite  
RUN a2enmod rewrite  
RUN a2dissite 000-default  
  
RUN echo "<VirtualHost *:80>" >> /etc/apache2/sites-enabled/cachet.conf  
RUN echo "DocumentRoot /var/www/html/public" >> /etc/apache2/sites-
enabled/cachet.conf  
RUN echo "<Directory /var/www/html/public>" >> /etc/apache2/sites-
enabled/cachet.conf  
RUN echo "Require all granted" >> /etc/apache2/sites-enabled/cachet.conf  
RUN echo "Options Indexes FollowSymLinks" >> /etc/apache2/sites-
enabled/cachet.conf  
RUN echo "AllowOverride All" >> /etc/apache2/sites-enabled/cachet.conf  
RUN echo "Order allow,deny" >> /etc/apache2/sites-enabled/cachet.conf  
RUN echo "Allow from all" >> /etc/apache2/sites-enabled/cachet.conf  
RUN echo "</Directory>" >> /etc/apache2/sites-enabled/cachet.conf  
RUN echo "</VirtualHost>" >> /etc/apache2/sites-enabled/cachet.conf  
  
# Run composer Install  
RUN composer install --no-dev -o  
  
# Set some permissions  
RUN chmod -R 777 /var/www/html/bootstrap/  
RUN rm -rf /var/www/html/bootstrap/cache/*  
  
EXPOSE 80  
CMD ["apache2-foreground"]  

