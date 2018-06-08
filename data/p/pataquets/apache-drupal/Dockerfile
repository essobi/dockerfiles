FROM pataquets/apache-php:xenial  
  
ADD files/etc/php5/ /etc/php5/  
ADD files/etc/apache2/ /etc/apache2/  
  
RUN \  
apt-get update && \  
DEBIAN_FRONTEND=noninteractive \  
apt-get -y install \  
php-curl \  
php-gd \  
php-mysql \  
php-pgsql \  
php-sqlite3 \  
mysql-client \  
&& \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* \  
&& \  
a2enmod rewrite && \  
a2enconf drupal && \  
phpenmod drupal-recommended  
  
#############################################################################  
### Install Drush 6.6 via Git & Composer  
#############################################################################  
# - Install 'curl' package to download composer  
# - Temporarily disable 'drupal-recommended.ini' to enable 'allow_url_fopen'  
RUN \  
apt-get update && \  
DEBIAN_FRONTEND=noninteractive \  
apt-get -y install \  
curl \  
php-dom \  
&& \  
DEBIAN_FRONTEND=noninteractive \  
apt-get -y --no-install-recommends install git \  
&& \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* \  
&& \  
phpdismod drupal-recommended && \  
curl --fail --location https://getcomposer.org/installer | \  
php -- --install-dir=/usr/local/bin --filename=composer && \  
git clone --single-branch --branch 6.7.0 https://github.com/drush-
ops/drush.git \  
/usr/local/src/drush && \  
cd /usr/local/src/drush && \  
composer install --verbose --no-dev && \  
composer clear-cache --verbose && \  
phpenmod drupal-recommended && \  
rm -vrf /root/.composer && \  
ln -vs /usr/local/src/drush/drush /usr/bin/drush && \  
ln -vs /usr/local/src/drush/drush.complete.sh /etc/bash_completion.d/ && \  
drush --verbose version  
#############################################################################  

