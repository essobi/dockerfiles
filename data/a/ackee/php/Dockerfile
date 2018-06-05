FROM php:5.6-apache  
# install silex dependencies  
RUN apt-get update && \  
DEBIAN_FRONTEND=noninteractive apt-get install -y \  
libfreetype6-dev \  
libjpeg62-turbo-dev \  
libmcrypt-dev \  
libpng12-dev \  
libbz2-dev \  
libxslt-dev \  
php-pear \  
curl \  
git \  
subversion \  
unzip \  
wget \  
libpcre3-dev \  
&& rm -r /var/lib/apt/lists/* \  
&& a2enmod rewrite  
  
# PHP Extensions  
RUN docker-php-ext-install bcmath mcrypt zip bz2 mbstring pcntl xsl \  
&& docker-php-ext-configure gd --with-freetype-dir=/usr/include/ \--with-jpeg-
dir=/usr/include/ \  
&& docker-php-ext-install gd \  
&& docker-php-ext-install pdo_mysql \  
&& echo "date.timezone = Europe/Prague" >> /usr/local/etc/php/php.ini  
  
# setup apache  
RUN sed -i '14 a Options Indexes FollowSymLinks' /etc/apache2/sites-
available/000-default.conf  
  
WORKDIR /var/www/  

