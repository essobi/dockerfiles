FROM php:5-apache  
  
WORKDIR /racktables  
  
RUN \  
apt-get update \  
  
&& DEBIAN_FRONTEND=noninteractive \  
apt-get install -y libpng12-dev \  
libfreetype6-dev \  
libjpeg62-turbo-dev \  
libmcrypt-dev \  
libsnmp-dev \  
  
&& docker-php-ext-install gd \  
snmp \  
pdo_mysql \  
mcrypt \  
bcmath \  
mbstring  
  
COPY . /racktables  
  
RUN \  
make install \  
&& find /etc/apache2 -type f -print0 \  
| xargs -0 sed -i
's@/var/www/html@/usr/local/share/RackTables/wwwroot@g;s@Directory
/var/www@Directory /usr/local/share/RackTables@g' \  
&& touch /usr/local/share/RackTables/wwwroot/inc/secret.php \  
&& chmod 666 /usr/local/share/RackTables/wwwroot/inc/secret.php \  
&& chown -R www-data: /usr/local/share/RackTables/wwwroot  
  
ENTRYPOINT ["/racktables/entrypoint.sh"]  

