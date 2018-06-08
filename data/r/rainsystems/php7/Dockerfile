FROM php:7-apache  
  
RUN a2enmod rewrite && \  
curl -Ss https://download.newrelic.com/548C16BF.gpg | apt-key add - && \  
echo "deb http://apt.newrelic.com/debian/ newrelic non-free" >
/etc/apt/sources.list.d/newrelic.list && \  
echo newrelic-php5 newrelic-php5/application-name string "My App Name" |
debconf-set-selections && \  
echo newrelic-php5 newrelic-php5/license-key string "YOUR_LICENSE_KEY" |
debconf-set-selections && \  
apt-get update -y && apt-get install -y \  
git \  
imagemagick \  
libfreetype6-dev \  
libjpeg62-turbo-dev \  
libmcrypt-dev \  
libmemcached-dev \  
libpng12-dev \  
libpq-dev \  
npm \  
newrelic-php5 \  
php5-xdebug \  
ruby && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* && \  
docker-php-ext-install \  
bcmath \  
exif \  
gd \  
mbstring \  
pdo \  
pdo_mysql \  
pdo_pgsql \  
zip && \  
pecl install apcu && \  
gem install -n /usr/bin sass && \  
curl -sS https://getcomposer.org/installer | php && \  
mv composer.phar /usr/local/bin/composer && \  
rm -rf /var/www/*  

