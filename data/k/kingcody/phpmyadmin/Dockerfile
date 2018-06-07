FROM kingcody/php:nginx  
MAINTAINER Cody Mize <docker@codymize.com>  
  
# Set default env  
ENV PMA_SECRET=blowfish_secret \  
PMA_USERNAME=pma \  
PMA_PASSWORD=password \  
MYSQL_USERNAME=mysql \  
MYSQL_PASSWORD=password  
  
# Install additional dependencies  
RUN apt-get update && apt-get install -y \  
bzip2 \  
libfreetype6-dev \  
libjpeg62-turbo-dev \  
libmcrypt-dev \  
libpng12-dev \  
mysql-client && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* && \  
rm -rf /usr/share/man/{??,??_*}  
  
# Install php extensions  
RUN docker-php-ext-install \  
ctype \  
mbstring \  
mcrypt \  
mysqli \  
opcache \  
zip && \  
docker-php-ext-configure gd --with-freetype-dir=/usr/include/ \--with-jpeg-
dir=/usr/include/ && \  
docker-php-ext-install gd  
  
# Install phpMyAdmin  
ENV PHPMYADMIN_VERSION=4.6.6  
RUN curl -sSL
"https://files.phpmyadmin.net/phpMyAdmin/${PHPMYADMIN_VERSION}/phpMyAdmin-${PHPMYADMIN_VERSION}-english.tar.bz2"
| \  
tar -xjC /var/www/html --strip 1  
# Custom templates  
ENV TEMPLATES="/var/www/html/sql/create_user.sql:/var/www/html/config.inc.php"  
COPY sources/templates /var/www/html/  
# Copy setup and start scripts  
COPY sources/bin /usr/local/bin/  
  
CMD ["phpmyadmin-start"]  

