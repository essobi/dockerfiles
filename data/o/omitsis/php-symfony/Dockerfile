FROM php:5.6-fpm  
  
# Install  
RUN buildDeps=" \  
libpng12-dev \  
libjpeg-dev \  
libmcrypt-dev \  
libxml2-dev \  
freetype* \  
libicu-dev \  
libssl-dev \  
automake \  
libtool \  
libltdl-dev \  
ruby-full \  
vim \  
nano \  
"; \  
set -x \  
&& apt-get update && apt-get install -y $buildDeps \--no-install-recommends &&
rm -rf /var/lib/apt/lists/* \  
&& docker-php-ext-configure \  
gd --with-png-dir=/usr --with-jpeg-dir=/usr --with-freetype-dir \  
&& docker-php-ext-install \  
gd \  
mbstring \  
mysqli \  
mcrypt \  
mysql \  
pdo_mysql \  
soap \  
zip \  
intl \  
fileinfo \  
exif  
  
# apt-get install  
RUN apt-get update && \  
apt-get install libldap2-dev -y && \  
rm -rf /var/lib/apt/lists/* && \  
docker-php-ext-configure ldap --with-libdir=lib/x86_64-linux-gnu/ && \  
docker-php-ext-install ldap  
  
RUN apt-get update && \  
apt-get install -y --force-yes zlib1g fontconfig libfreetype6 libx11-6
libxext6 libxrender1 xvfb libfontconfig wkhtmltopdf  
  
# Install and configure Xdebug  
RUN pecl install xdebug-2.5.0 mongo \  
&& docker-php-ext-enable mongo \  
&& docker-php-ext-enable xdebug \  
&& sed -i '1 a xdebug.remote_autostart=true' /usr/local/etc/php/conf.d/docker-
php-ext-xdebug.ini \  
&& sed -i '1 a xdebug.remote_mode=req' /usr/local/etc/php/conf.d/docker-php-
ext-xdebug.ini \  
&& sed -i '1 a xdebug.remote_handler=dbgp' /usr/local/etc/php/conf.d/docker-
php-ext-xdebug.ini \  
&& sed -i '1 a xdebug.remote_connect_back=1 '
/usr/local/etc/php/conf.d/docker-php-ext-xdebug.ini \  
&& sed -i '1 a xdebug.remote_port=9000' /usr/local/etc/php/conf.d/docker-php-
ext-xdebug.ini \  
&& sed -i '1 a xdebug.remote_host=127.0.0.1' /usr/local/etc/php/conf.d/docker-
php-ext-xdebug.ini \  
&& sed -i '1 a xdebug.remote_enable=1' /usr/local/etc/php/conf.d/docker-php-
ext-xdebug.ini  
  
# Make sure the volume mount point is empty  
RUN rm -rf /var/www/html/*  
  
# Install composer  
RUN curl -sS https://getcomposer.org/installer | php -- --filename=composer
--install-dir=/bin  
  
## Install ruby and compass  
RUN gem update --system && gem install compass  
  
## Install symfony installer  
RUN curl -LsS https://symfony.com/installer -o /usr/local/bin/symfony  
RUN chmod a+x /usr/local/bin/symfony  
  
RUN export TERM=xterm  
  
RUN usermod -u 1000 www-data  

