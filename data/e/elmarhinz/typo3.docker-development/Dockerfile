FROM php:7-apache  
MAINTAINER Elmar Hinz <t3elmar@gmail.com>  
  
# Load packages  
  
RUN apt-get update; \  
apt-get install -y --no-install-recommends \  
graphicsmagick \  
ghostscript \  
libfreetype6-dev \  
libjpeg62-turbo-dev \  
libmcrypt-dev \  
libpng12-dev \  
libxml2-dev \  
wget \  
zlib1g-dev \  
;  
  
# Configure PHP and Apache  
  
RUN docker-php-ext-configure gd \  
\--with-freetype-dir=/usr/include/ \  
\--with-jpeg-dir=/usr/include/; \  
\--with-png-dir=/usr/include/; \  
\--with-zlib-dir=/usr/include/; \  
docker-php-ext-install -j$(nproc) \  
gd \  
mysqli \  
opcache \  
soap \  
zip \  
; \  
pecl install redis; \  
pecl install xdebug; \  
docker-php-ext-enable redis xdebug; \  
a2enmod rewrite;  
COPY typo3.ini /usr/local/etc/php/conf.d/  
COPY xdebug.ini /usr/local/etc/php/conf.d/  
# Setup directories  
  
WORKDIR /var/www/html  
RUN \  
chmod 2770 /var/www/html; \  
mkdir typo3_src; \  
ln -s typo3_src/index.php; \  
ln -s typo3_src/typo3; \  
ln -s typo3_src/_.htaccess .htaccess; \  
mkdir typo3temp; \  
mkdir typo3conf; \  
mkdir fileadmin; \  
mkdir uploads; \  
touch FIRST_INSTALL; \  
chown -R www-data .;  
  
# Configure mount points  
  
VOLUME /var/www/html/typo3_src  
VOLUME /var/www/html/fileadmin  
VOLUME /var/www/html/typo3conf  
VOLUME /var/www/html/typo3temp  
VOLUME /var/www/html/uploads  
  
# Cleanup  
  
RUN apt-get -y purge \  
libfreetype6-dev \  
libjpeg62-turbo-dev \  
libmcrypt-dev \  
libpng12-dev \  
libxml2-dev \  
zlib1g-dev \  
; \  
apt-get autoremove -y; \  
apt-get clean; \  
rm -rf /var/lib/apt/lists/* /usr/src/*;  
  

