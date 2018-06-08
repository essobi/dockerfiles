FROM php:5.6.25-apache  
  
COPY moodle-config.php /var/www/html/config.php  
  
# Set default variables for the config.  
#  
# MOODLE_URL is the URL to hit the document root from outside, with no
trailing slash  
ENV MYSQL_TYPE=mariadb \  
MYSQL_DATABASE=moodle \  
MYSQL_USER=moodleuser \  
MYSQL_PASSWORD=your-database-password \  
MYSQL_HOSTNAME=localhost \  
MYSQL_PORT=3306 \  
MOODLE_URL=https://moodle.example.com  
  
RUN chown -R $APACHE_RUN_USER:$APACHE_RUN_GROUP /var/www/html \  
&& apt-get update \  
&& apt-get install -y zlib1g-dev libpng-dev libjpeg-dev libxml2-dev libicu-dev
\  
&& docker-php-ext-configure gd \--with-jpeg-dir=/usr/include/ \  
&& docker-php-ext-install -j$(nproc) mysql mysqli pdo pdo_mysql zip gd xmlrpc
soap intl opcache  
  
VOLUME /var/www/html  
VOLUME /var/moodledata  
  
COPY moodle.ini /usr/local/etc/php/conf.d/  

