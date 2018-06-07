FROM php:7.0.9-apache  
  
RUN curl -Ss https://download.newrelic.com/548C16BF.gpg | apt-key add - && \  
echo "deb http://apt.newrelic.com/debian/ newrelic non-free" >
/etc/apt/sources.list.d/newrelic.list && \  
echo newrelic-php5 newrelic-php5/application-name string "My App Name" |
debconf-set-selections && \  
echo newrelic-php5 newrelic-php5/license-key string "YOUR_LICENSE_KEY" |
debconf-set-selections && \  
apt-get update && \  
apt-get install -y \  
git \  
libgpgme11-dev \  
libicu-dev \  
libmcrypt-dev \  
newrelic-php5 \  
npm \  
xvfb && \  
ln -s /usr/bin/nodejs /usr/bin/node && \  
/usr/bin/npm install -g less && \  
docker-php-ext-install \  
intl \  
mbstring \  
mcrypt \  
pdo \  
pdo_mysql \  
zip \  
&& \  
a2enmod rewrite && \  
a2enmod headers && \  
pecl install gnupg && \  
newrelic-install install && \  
curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/sbin --filename=composer  

