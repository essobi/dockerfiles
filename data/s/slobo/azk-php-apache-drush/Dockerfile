# The image includes:  
#  
# PARENT:  
# - Git  
# - Vim  
# - Node  
# - MySQL Client  
# - PostgreSQL Client  
# - MongoDB  
# - Apache2 with root  
#  
# THIS:  
# - PHP Version 5.5  
# - Composer  
# - Drush  
  
FROM azukiapp/apache2  
MAINTAINER Slobodan Miskovic <slobodan@miskovic.ca>  
  
# Install PHP5 + Apache2 + Libs  
# Enable php and apache modules  
RUN phpDeps='libxml2 \  
libcurl4-openssl-dev \  
libapache2-mod-php5 \  
php5-dev \  
php5-cli \  
php5-mysql \  
php5-pgsql \  
php5-mcrypt \  
php5-memcached \  
php5-xdebug \  
php5-curl \  
php5-json \  
php5-gd \  
php-pear \  
php-apc' \  
&& apt-get update -qq \  
&& apt-get install -y -qq $phpDeps \  
&& apt-get clean -qq \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* \  
&& apt-get purge -y --auto-remove $buildDeps \  
&& a2enmod rewrite \  
&& php5enmod mcrypt memcached \  
&& sed -i -e "s/variables_order.*/variables_order = \"EGPCS\"/g"
/etc/php5/apache2/php.ini \  
&& sed -i -e "s/;opcache.memory_consumption.*/opcache.memory_consumption =
200/g" /etc/php5/apache2/php.ini \  
&& curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer \  
&& composer global require drush/drush:~6.1.0@rc \  
&& ln -sf /root/.composer/vendor/bin/drush.php /usr/local/bin/drush  
  
EXPOSE 80  
WORKDIR /app  
  
CMD ["apache2-foreground"]  

