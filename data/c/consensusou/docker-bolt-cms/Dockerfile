FROM php:7-apache  
  
MAINTAINER Consensus OÜ  
  
RUN apt-get update && apt-get install -y \  
libfreetype6-dev \  
libjpeg62-turbo-dev  
  
RUN docker-php-ext-install exif  
  
RUN docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-
dir=/usr/include/ \  
&& docker-php-ext-install -j$(nproc) gd  
  
RUN mkdir /var/www/bolt \  
&& cd /var/www/bolt \  
&& curl -O https://bolt.cm/distribution/bolt-latest.tar.gz \  
&& tar -xzf bolt-latest.tar.gz --strip-components=1 \  
&& php app/nut init  
  
RUN chmod -R 774 /var/www/bolt/app/cache/ /var/www/bolt/app/config/
/var/www/bolt/app/database/ /var/www/bolt/extensions/ \  
&& chmod -R 774 /var/www/bolt/public/thumbs/ /var/www/bolt/public/extensions/
/var/www/bolt/public/files/ \  
&& chown -R www-data /var/www/bolt  
  
RUN cd /var/www/bolt \  
&& vendor/bin/nut database:update \  
&& vendor/bin/nut user:add -e admin "Bolt User" webmaster@localhost.com
password root  
  
COPY bolt-cms-apache.conf /etc/apache2/sites-available/bolt-cms-apache.conf  
COPY apache2.conf /etc/apache2/apache2.conf  
  
RUN a2dissite 000-default.conf \  
&& a2ensite bolt-cms-apache.conf \  
&& a2enmod rewrite  
  
EXPOSE 80 443  
  
CMD ["apache2-foreground"]  

