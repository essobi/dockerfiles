# use official php image with apache all configured nicely  
FROM php:5.6-apache  
MAINTAINER cam@theminery.com  
  
ENV \  
IJG_VERSION=9b \  
PNGOUT_VERSION=20150319  
# enable mod_rewrite (for .htaccess rules)  
RUN a2enmod rewrite  
  
# update package manager and install  
RUN apt-get update && apt-get install -y \  
libmcrypt-dev \  
ntp \  
phpunit \  
php5-gd \  
phpunit-selenium \  
php-invoker \  
phpunit-dbunit \  
vim \  
wget \  
unzip \  
php5-geoip \  
libgeoip-dev \  
zlib1g-dev \  
libmagickwand-dev \  
advancecomp \  
gifsicle \  
jpegoptim \  
libimage-exiftool-perl \  
pngnq \  
tar \  
libpng-dev \  
libjpeg-progs \  
git \  
optipng \  
pngquant \  
libc-client-dev \  
libkrb5-dev  
  
RUN rm -rf /var/lib/apt/lists/*  
  
#install imagick  
RUN pecl install imagick-beta \  
&& echo "extension=imagick.so" > /usr/local/etc/php/conf.d/ext-imagick.ini \  
&& apt-get remove -y \  
libmagickwand-dev \  
&& apt-get install -y \  
libmagickwand-6.q16-2 \  
&& apt-get autoremove -y  
  
# pngout  
RUN wget http://static.jonof.id.au/dl/kenutils/pngout-20150319-linux.tar.gz
&&\  
tar -xf pngout-20150319-linux.tar.gz &&\  
rm pngout-20150319-linux.tar.gz &&\  
cp pngout-20150319-linux/x86_64/pngout /bin/pngout &&\  
rm -rf pngout-20150319-linux  
  
# install php extensions  
RUN docker-php-ext-configure imap --with-kerberos --with-imap-ssl  
RUN docker-php-ext-install exif mcrypt mysql mysqli pdo pdo_mysql opcache zip
imap  
  
RUN pecl install apcu-4.0.11 \  
&& echo "extension=apcu.so" > /usr/local/etc/php/conf.d/apcu.ini  
  
RUN pecl install xdebug \  
&& echo "zend_extension=$(find /usr/local/lib/php/extensions/ -name
xdebug.so)" > /usr/local/etc/php/conf.d/xdebug.ini \  
&& echo "xdebug.remote_enable=on" >> /usr/local/etc/php/conf.d/xdebug.ini \  
&& echo "xdebug.remote_autostart=off" >> /usr/local/etc/php/conf.d/xdebug.ini  
  
RUN echo "extension=/usr/lib/php5/20131226/gd.so" >
/usr/local/etc/php/conf.d/gd.ini  
  
# install geoip extension  
RUN pecl install geoip \  
&& echo "extension=geoip.so" > /usr/local/etc/php/conf.d/geoip.ini \  
&& wget http://geolite.maxmind.com/download/geoip/database/GeoLiteCity.dat.gz
-O /usr/share/GeoIP/GeoLiteCity.dat.gz \  
&& gunzip /usr/share/GeoIP/GeoLiteCity.dat.gz \  
&& mv /usr/share/GeoIP/GeoLiteCity.dat /usr/share/GeoIP/GeoIPCity.dat  
  
# install codeception  
RUN wget http://codeception.com/codecept.phar && chmod +x codecept.phar && mv
codecept.phar /usr/local/bin/codecept  
  
RUN wget https://getcomposer.org/download/1.2.0/composer.phar && chmod +x
composer.phar && mv composer.phar /usr/local/bin/composer

