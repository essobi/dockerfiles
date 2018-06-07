FROM pataquets/apache-php:5.3  
  
VOLUME /app  
  
ADD files/etc/php5/ /etc/php5/  
ADD files/etc/apache2/sites-available/ /etc/apache2/sites-available/  
  
RUN \  
apt-get update && \  
DEBIAN_FRONTEND=noninteractive \  
apt-get -y install \  
php5-curl \  
php5-gd \  
php5-mysql \  
php5-pgsql \  
php5-sqlite \  
&& \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/ \  
&& \  
a2enmod rewrite  
  
RUN \  
ln -s /app /var/www/  
  
RUN \  
a2ensite 0000default && \  
a2dissite default && \  
service apache2 reload  

