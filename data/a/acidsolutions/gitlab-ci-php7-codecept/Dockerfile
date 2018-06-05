FROM php:latest  
MAINTAINER Daniel Lucas <daniel@acid.fr>  
  
# Install system libraries needed for tests  
RUN apt-get update -yqq && \  
apt-get install -yqq git \  
openssh-client \  
wget \  
libcurl4-gnutls-dev \  
libicu-dev \  
libmcrypt-dev \  
libvpx-dev \  
libjpeg-dev \  
libpng-dev \  
libxpm-dev \  
zlib1g-dev \  
libfreetype6-dev \  
libxml2-dev \  
libexpat1-dev \  
libbz2-dev \  
libgmp3-dev \  
libldap2-dev \  
unixodbc-dev \  
libpq-dev \  
libsqlite3-dev \  
libaspell-dev \  
libsnmp-dev \  
libpcre3-dev \  
libtidy-dev \  
libxslt-dev  
  
# Compile PHP and include necessary extensions  
RUN docker-php-ext-install mbstring \  
mcrypt \  
pdo_mysql \  
curl \  
json \  
intl \  
&& docker-php-ext-configure gd --with-freetype-dir=/usr/include/ \--with-jpeg-
dir=/usr/include/ \  
&& docker-php-ext-install gd \  
xml \  
zip \  
bz2 \  
opcache \  
xsl  
  
# Install xdebug  
RUN yes | pecl install xdebug \  
&& echo "zend_extension=$(find /usr/local/lib/php/extensions/ -name
xdebug.so)" > /usr/local/etc/php/conf.d/xdebug.ini  
  
# Install phpdox  
RUN wget
https://github.com/theseer/phpdox/releases/download/0.9.0/phpdox-0.9.0.phar \  
&& chmod +x phpdox-0.9.0.phar \  
&& mv phpdox-0.9.0.phar /usr/bin/phpdox  
  
# Install phploc  
RUN wget https://phar.phpunit.de/phploc.phar \  
&& chmod +x phploc.phar \  
&& mv phploc.phar /usr/bin/phploc  
  
# Install pdepend  
RUN wget http://static.pdepend.org/php/latest/pdepend.phar \  
&& chmod +x pdepend.phar \  
&& mv pdepend.phar /usr/bin/pdepend  
  
# Install phpmd  
RUN wget -c http://static.phpmd.org/php/latest/phpmd.phar \  
&& chmod +x phpmd.phar \  
&& mv phpmd.phar /usr/bin/phpmd

