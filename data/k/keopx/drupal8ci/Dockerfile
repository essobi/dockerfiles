FROM keopx/apache-php:7.0  
MAINTAINER keopx <keopx@keopx.net>  
  
# Based on https://github.com/Lullabot/drupal8ci.  
# Working dir  
WORKDIR /var/www/html  
  
RUN apt-get update && apt-get install -y \  
imagemagick \  
libmagickwand-dev \  
mariadb-client \  
sqlite \  
php7.1-sqlite3 \  
sudo  
  
# Remove the vanilla Drupal project that comes with this image.  
RUN rm -rf ..?* .[!.]* *  
  
# Change docroot since we use Composer Drupal project.  
RUN sed -ri -e 's!/var/www/html!/var/www/html/web!g' /etc/apache2/sites-
available/*.conf  
RUN sed -ri -e 's!/var/www!/var/www/html/web!g' /etc/apache2/apache2.conf
/etc/apache2/conf-available/*.conf  
  
# Install XDebug.  
RUN phpenmod xdebug  
  
# Install Robo CI.  
RUN wget https://robo.li/robo.phar --directory-prefix=/tmp  
RUN chmod +x /tmp/robo.phar && mv /tmp/robo.phar /usr/local/bin/robo  
  
# Install Dockerize.  
ENV DOCKERIZE_VERSION v0.6.0  
RUN wget
https://github.com/jwilder/dockerize/releases/download/$DOCKERIZE_VERSION/dockerize-
linux-amd64-$DOCKERIZE_VERSION.tar.gz \  
&& tar -C /usr/local/bin -xzvf dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz
\  
&& rm dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz  
  
# Install ImageMagic to take screenshots.  
#RUN pecl install imagick  

