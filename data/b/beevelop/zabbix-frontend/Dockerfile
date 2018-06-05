FROM php:5-apache  
  
MAINTAINER Maik Hummel <m@ikhummel.com>  
  
WORKDIR /opt  
  
COPY php.ini /usr/local/etc/php/  
COPY zabbix.conf.php.tpl ./  
COPY start ./  
COPY conf.env ./  
  
RUN apt-get update && apt-get install -yq git \  
gettext \  
libfreetype6-dev \  
libjpeg62-turbo-dev \  
libmcrypt-dev \  
libpng12-dev && \  
apt-get install -yq libmagickwand-dev --no-install-recommends && \  
docker-php-ext-install iconv mcrypt && \  
docker-php-ext-configure gd --with-freetype-dir=/usr/include/ \--with-jpeg-
dir=/usr/include/ \--with-png-dir=/usr/include/ && \  
docker-php-ext-install gd mysqli pdo_mysql bcmath mbstring sockets xml ctype
session gettext && \  
pecl install imagick-beta && \  
docker-php-ext-enable imagick && \  
mkdir zabbix && \  
curl -sL
"http://sourceforge.net/projects/zabbix/files/ZABBIX%20Latest%20Development/3.0.0alpha6/zabbix-3.0.0alpha6.tar.gz/download"
| tar xz -C zabbix --strip-components=1 && \  
cp -R zabbix/frontends/php/. /var/www/html && \  
chown -R www-data:www-data /var/www/html && \  
a2enmod rewrite && \  
  
chmod +x start && \  
  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* && \  
apt-get autoremove -y && \  
apt-get clean  
  
CMD ./start

