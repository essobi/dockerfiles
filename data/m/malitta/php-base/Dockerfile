FROM php:7.1-apache  
MAINTAINER Malitta Nanayakkara <malitta@gmail.com>  
  
RUN apt-get update && apt-get install -y \  
curl \  
supervisor \  
vim \  
zip \  
wget  
  
COPY ./files/supervisor-apache.conf /etc/supervisor/conf.d/apache2.conf  
  
# Clean up the apt cache  
RUN rm -rf /var/lib/apt/lists/*  
  
# install composer  
RUN curl -sS https://getcomposer.org/installer | \  
php -- --install-dir=/usr/local/bin --filename=composer  
  
# Prepare vhost file and document root directory  
RUN rm -rf /var/www/html  
COPY ./files/public /var/www/public  
COPY ./files/000-default.conf /etc/apache2/sites-available/000-default.conf  
  
RUN a2enmod rewrite headers  
  
EXPOSE 80 443  
WORKDIR /var/www  
  
CMD ["/usr/bin/supervisord", "-n"]

