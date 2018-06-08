FROM php:5.6.29-apache  
MAINTAINER Maikel Dollé <maikel@itmagix.nl>  
  
RUN apt-get -y update && apt-get -y upgrade && \  
apt-get install -y git-core libfreetype6-dev libjpeg62-turbo-dev libmcrypt-dev
libpng12-dev && \  
docker-php-ext-install pdo pdo_mysql && \  
docker-php-ext-install -j$(nproc) iconv mcrypt && \  
docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-
dir=/usr/include/ && \  
docker-php-ext-install -j$(nproc) gd && \  
docker-php-ext-install gettext && \  
docker-php-ext-install zip  
  
ENV TERM="xterm" \  
SPOTWEB_DB_TYPE=mysql \  
SPOTWEB_DB_HOST=database \  
SPOTWEB_DB_NAME=spotweb \  
SPOTWEB_DB_USER=spotweb \  
SPOTWEB_DB_PASS=bewtops  
  
ADD 000-default.conf /etc/apache2/sites-enabled/000-default.conf  
ADD ports.conf /etc/apache2  
ADD php.ini /usr/local/etc/php  
  
RUN git clone -b master --single-branch https://github.com/spotweb/spotweb.git
/var/www/html && \  
rm -rf /var/www/html/.git && \  
chmod -R 775 /var/www/html && \  
chown -R www-data:www-data /var/www/html  
  
COPY ./entrypoint.sh /entrypoint.sh  
RUN chmod u+x /entrypoint.sh  
  
RUN a2enmod rewrite  
  
EXPOSE 10000  
ENTRYPOINT ["/entrypoint.sh"]  

