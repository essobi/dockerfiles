FROM phpdockerio/php7-fpm:latest  
  
# Install selected extensions and other stuff  
RUN apt-get update && \  
apt-get -y --no-install-recommends install \  
php7.0-mysql \  
php7.0-sqlite3 \  
php7.0-bz2 \  
php7.0-gd \  
php7.0-imagick \  
php7.0-imap \  
php7.0-intl \  
php7.0-mbstring \  
php7.0-odbc \  
php7.0-xdebug \  
unzip && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* \  
/tmp/* \  
/var/tmp/* \  
/usr/share/doc/*  
  
COPY api.zip /tmp/api.zip  
  
RUN mkdir -p /var/www/cakephpapp && \  
cd /tmp && \  
unzip api.zip -d /var/www/cakephpapp && \  
chown www-data:www-data -R /var/www/cakephpapp  
  
WORKDIR "/var/www/cakephpapp"

