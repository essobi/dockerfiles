FROM php:7.2-apache  
LABEL maintainer="ono.naoyaa@gmail.com"  
  
# Install the required packages and remove the apt cache.  
RUN apt-get update -yqq \  
&& apt-get install -yqq --no-install-recommends \  
git \  
&& rm -rf /var/lib/apt/lists  
  
# Enable PHP extensions  
RUN docker-php-ext-install pdo pdo_mysql mysqli  
  
# COPY site conf file  
COPY ./site.conf /etc/apache2/sites-available/000-default.conf  
  
# Enable Apache modules  
RUN a2enmod rewrite  
  
# Restart Apache  
RUN service apache2 restart  
  
# Install composer  
ADD https://getcomposer.org/download/1.5.2/composer.phar
/usr/local/bin/composer  
RUN chmod +x /usr/local/bin/composer  
  
# Copy the code into /var/www/html/ inside the image  
COPY . /var/www/html  
  
# Create tmp directory and make it writable by the web server  
RUN rm -rf app/tmp && mkdir app/tmp && chown -R www-data:www-data app/tmp  
  
EXPOSE 80  

