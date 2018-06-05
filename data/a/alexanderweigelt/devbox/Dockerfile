FROM php:7.1-apache  
  
MAINTAINER Alexander Weigelt <webdesign@alexander-weigelt.de>  
  
# Add setup  
COPY setup/ /  
  
# using composer  
RUN curl -sS https://getcomposer.org/installer | \  
php -- --install-dir=/usr/bin/ --filename=composer \  
&& apt-get update \  
&& apt-get install -y \  
git \  
zip \  
unzip \  
libfreetype6-dev \  
libjpeg62-turbo-dev \  
libmcrypt-dev \  
libpng-dev \  
libxml2-dev \  
libxslt-dev \  
libicu-dev \  
libyaml-dev \  
# Install php extensions  
&& docker-php-ext-install -j$(nproc) \  
mysqli \  
mcrypt \  
pdo_mysql \  
opcache \  
json \  
calendar \  
bcmath \  
mbstring \  
soap \  
xsl \  
zip \  
intl \  
&& docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-
dir=/usr/include/ \  
&& docker-php-ext-install -j$(nproc) gd \  
# Install PECL extensions  
&& pecl install redis \  
&& pecl install xdebug \  
&& pecl install yaml \  
&& docker-php-ext-enable redis yaml \  
# Install Node.js  
&&curl -sL https://deb.nodesource.com/setup_8.x | bash \  
&& apt-get install -y nodejs build-essential \  
# Install Grunt CLI  
&& npm install -g grunt-cli \  
# enable mod_rewrite for Apache 2.2  
&& a2enmod rewrite \  
&& service apache2 restart \  
# Set chmod  
&& chmod +x /usr/local/bin/* \  
&& chown -R www-data:www-data /var/www/html

