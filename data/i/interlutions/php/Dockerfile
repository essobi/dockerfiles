FROM php:7.1-fpm  
  
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
bcmath \  
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
cp ioncube/ioncube_loader_lin_7.1.so $(php -r 'echo
ini_get("extension_dir");') && \  
echo "zend_extension=ioncube_loader_lin_7.1.so" >
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
ADD mail.ini /usr/local/etc/php/conf.d/mail.ini  
  
# Download composer as fallback if non is provided  
RUN curl -o /usr/local/bin/composer.phar http://getcomposer.org/composer.phar
&& \  
chmod +x /usr/local/bin/composer.phar && \  
ln -s /usr/local/bin/composer.phar /usr/local/bin/composer  
  
# Install git+ssh (for composer install)  
RUN apt-get update && \  
apt-get install -y --no-install-recommends git openssh-client rsync && \  
apt-get clean && \  
rm -r /var/lib/apt/lists/*  
  
# Install and configure fcron  
RUN groupadd -r -g 109 fcron && \  
useradd -u 109 -r fcron -g fcron && \  
apt-get update && \  
apt-get install -y --no-install-recommends wget vim && \  
wget http://fcron.free.fr/archives/fcron-3.3.0.src.tar.gz && \  
tar xfz fcron-3.3.0.src.tar.gz && \  
cd fcron-3.3.0 && \  
./configure && \  
make && \  
make install && \  
apt-get purge -y wget vim && \  
apt-get autoremove -y && \  
apt-get clean && \  
rm -Rf fcron-3.3.0*z && \  
rm -rf /var/lib/apt/lists/  
ADD fcron.conf /usr/local/etc  
ADD echomail /usr/local/bin  
RUN chown root:fcron /usr/local/etc/fcron.conf && \  
chmod 644 /usr/local/etc/fcron.conf  
  
# Default configuration for fpm  
COPY ./zz-fpm.conf /usr/local/etc/php-fpm.d/  
  
# Base php ini  
COPY ./docker-base.ini /usr/local/etc/php/conf.d/  
  
# Disable xdebug by default and add a script to reactivate  
# Just add a COPY ./xdebug.ini /usr/local/etc/php/conf.d/xdebug.ini.bak in
your project  
RUN docker-php-source extract && \  
pecl install xdebug && \  
docker-php-ext-enable xdebug && \  
docker-php-source delete  
COPY xdebug.sh /  
RUN mv /usr/local/etc/php/conf.d/docker-php-ext-xdebug.ini
/usr/local/etc/php/conf.d/docker-php-ext-xdebug.ini.bak  
  
# Tools to change the uid on run  
RUN apt-get update && \  
apt-get install -y --no-install-recommends sudo && \  
apt-get clean && \  
rm -r /var/lib/apt/lists/*  
  
# Cache composer downloads in a volume  
VOLUME /var/www/.composer  
  
# Script to wait for db  
RUN apt-get update && \  
apt-get install -y --no-install-recommends netcat && \  
apt-get clean && \  
rm -r /var/lib/apt/lists/*  
COPY wait-for /usr/local/bin  
  
COPY entrypoint-cron /usr/local/bin  
COPY entrypoint-chuid /usr/local/bin  
ENTRYPOINT ["entrypoint-chuid"]  
CMD ["php-fpm"]  

