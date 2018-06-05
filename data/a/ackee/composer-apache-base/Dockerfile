FROM php:7-apache  
  
# install composer dependencies  
RUN apt-get update && \  
DEBIAN_FRONTEND=noninteractive apt-get install -y \  
libfreetype6-dev \  
libjpeg62-turbo-dev \  
libmcrypt-dev \  
libpng12-dev \  
libbz2-dev \  
libxslt-dev \  
libldap2-dev \  
php-pear \  
curl \  
git \  
subversion \  
unzip \  
wget \  
&& rm -r /var/lib/apt/lists/* \  
&& a2enmod rewrite  
  
# PHP Extensions  
RUN docker-php-ext-install bcmath mcrypt zip bz2 mbstring pcntl xsl \  
&& docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-
dir=/usr/include/ \  
&& docker-php-ext-install gd \  
&& docker-php-ext-configure ldap --with-libdir=lib/x86_64-linux-gnu/ \  
&& docker-php-ext-install ldap \  
&& docker-php-ext-install pdo pdo_mysql  
  
# install composer  
RUN curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer  
  

