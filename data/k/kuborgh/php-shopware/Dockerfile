FROM kuborgh/php:7.0-fpm  
  
# Add some native php extensions  
RUN apt-get update &&\  
apt-get install -y --no-install-recommends \  
icu-devtools libbsd-dev libbz2-dev libedit-dev libfreetype6 libfreetype6-dev \  
libicu-dev libicu52 libjpeg62-turbo libjpeg62-turbo-dev libmcrypt-dev \  
libmcrypt4 libpng12-0 libpng12-dev libsqlite3-dev libtinfo-dev libxml2-dev \  
libxslt1-dev libxslt1.1 zlib1g-dev \  
&& \  
rm -r /var/lib/apt/lists/* && \  
docker-php-ext-configure gd \  
\--with-freetype-dir=/usr/include/ \  
\--with-png-dir=/usr/include/ \  
\--with-jpeg-dir=/usr/include/ \  
&& \  
docker-php-ext-install -j$(nproc) \  
bz2 \  
dom \  
exif \  
fileinfo \  
hash \  
iconv \  
mcrypt \  
intl \  
opcache \  
pcntl \  
pdo \  
pdo_mysql \  
pdo_sqlite \  
readline \  
session \  
simplexml \  
xml \  
xsl \  
zip \  
gd \  
&& \  
# Clean up  
apt-get purge -y \  
icu-devtools libbsd-dev libbz2-dev libedit-dev libfreetype6-dev \  
libicu-dev libjpeg62-turbo-dev libmcrypt-dev \  
libpng12-dev libsqlite3-dev libtinfo-dev libxml2-dev \  
libxslt1-dev zlib1g-dev  
  
# APCu  
RUN docker-php-source extract && \  
pecl install apcu && \  
docker-php-ext-enable apcu && \  
docker-php-source delete  
# ioncube loader  
RUN apt-get update && \  
apt-get install -y --no-install-recommends wget && \  
wget
https://downloads.ioncube.com/loader_downloads/ioncube_loaders_lin_x86-64.tar.gz
&& \  
tar xfz ioncube_loaders_lin_x86-64.tar.gz && \  
cp ioncube/ioncube_loader_lin_7.0.so $(php -r 'echo
ini_get("extension_dir");') && \  
echo "zend_extension=ioncube_loader_lin_7.0.so" >
/usr/local/etc/php/conf.d/00-ioncube.ini && \  
rm -Rf ioncube_loaders_lin_x86-64.tar.gz ioncube && \  
apt-get remove -y wget && \  
apt-get autoremove -y && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
# Enable mailing via ssmtp  
RUN apt-get update && \  
apt-get install -y --no-install-recommends ssmtp && \  
apt-get clean && \  
rm -r /var/lib/apt/lists/*  
  
# download composer as fallback if non is provided  
RUN curl -o /usr/local/bin/composer.phar http://getcomposer.org/composer.phar
&& \  
chmod +x /usr/local/bin/composer.phar && \  
ln -s /usr/local/bin/composer.phar /usr/local/bin/composer  
  
# Add some basic php.ini directives  
ADD php.ini /usr/local/etc/php/conf.d/php-ini-overrides.ini  

