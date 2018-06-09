FROM drupal  
  
# Install Composer  
RUN \  
curl -fsSL https://getcomposer.org/installer | php && \  
mv composer.phar /usr/local/bin/composer && \  
chmod -v a+x /usr/local/bin/composer  
  
# Install Drush 8.x and MariaDB client binary (Drush dependency)  
RUN \  
curl -fsSL -o /usr/local/bin/drush \  
"https://github.com/drush-ops/drush/releases/download/8.1.16/drush.phar" && \  
chmod -v +x /usr/local/bin/drush \  
&& \  
apt-get update && \  
DEBIAN_FRONTEND=noninteractive \  
apt-get -y install \  
mariadb-client \  
&& \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
# Configure error logging and disable OPcache  
RUN \  
rm -v \  
/usr/local/etc/php/conf.d/docker-php-ext-opcache.ini \  
/usr/local/etc/php/conf.d/opcache-recommended.ini \  
&& \  
echo "log_errors=on" >> /usr/local/etc/php/conf.d/referup-errors.ini && \  
echo "error_log=/dev/tty" >> /usr/local/etc/php/conf.d/referup-errors.ini \  
&& \  
sed -i 's/\-DFOREGROUND/\-DFOREGROUND \-c \"ErrorLog \/dev\/stderr\"/' \  
/usr/local/bin/apache2-foreground  

