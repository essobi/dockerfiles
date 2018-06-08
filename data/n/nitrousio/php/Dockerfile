FROM nitrousio/nodejs:latest  
MAINTAINER Nitrous.IO <hello@nitrous.io>  
  
ENV NITROUS_PREVIEW_PORT 80  
  
RUN \  
apt-get update && \  
DEBIAN_FRONTEND=noninteractive apt-get -y install \  
apache2 \  
libapache2-mod-php5 \  
mysql-server \  
php5-curl \  
php5-gd \  
php5-mysql \  
php-apc \  
php-pear && \  
apt-get clean  
  
RUN curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer version=1.0.0-alpha9  
  
RUN \  
/bin/bash -c \  
'ln -s /var/www/html /home/$NITROUS_USERNAME/www && \  
rm /home/$NITROUS_USERNAME/www/index.html && \  
echo "<?php phpinfo(); ?>" > /home/$NITROUS_USERNAME/www/index.php && \  
chown -R $NITROUS_USERNAME:www-data /var/www && \  
chmod 775 /var/www && \  
chown -h $NITROUS_USERNAME:www-data /home/$NITROUS_USERNAME/www'  
  
RUN \  
sed -i 's|variables_order.*|variables_order = "EGPCS"|g'
/etc/php5/apache2/php.ini && \  
sed -i 's|upload_max_filesize.*|upload_max_filesize = 100M|g'
/etc/php5/apache2/php.ini && \  
sed -i 's|post_max_size.*|post_max_size = 100M|g' /etc/php5/apache2/php.ini &&
\  
sed -i 's|bind-address.*|bind-address = 0.0.0.0|g' /etc/mysql/my.cnf  
  
EXPOSE $NITROUS_PREVIEW_PORT  

