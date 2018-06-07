FROM php:7.0-fpm  
EXPOSE 9000  
  
ENV PHP_TIMEZONE=Europe/London \  
OPCACHE_REVALIDATE_FREQUENCY=60  
  
ADD layer /  
  
RUN chmod 755 /start.sh \  
&& apt-get update && apt-get install -y \  
supervisor \  
python-dev \  
libxml2-dev \  
libz-dev \  
libmemcached-dev \  
libmcrypt-dev \  
libicu-dev \  
libpq-dev \  
libfreetype6-dev \  
libjpeg62-turbo-dev \  
libmcrypt-dev \  
libpng12-dev \  
libxslt1-dev \  
zlib1g-dev \  
git \  
zip \  
unzip \  
&& docker-php-ext-configure \  
gd \  
\--with-jpeg-dir \  
\--with-png-dir \  
\--with-vpx-dir \  
\--with-freetype-dir \  
&& docker-php-ext-install \  
pdo \  
pdo_mysql \  
pdo_pgsql \  
pgsql \  
opcache \  
mysqli \  
mcrypt \  
ctype \  
gd \  
intl \  
xml \  
xsl \  
iconv \  
json \  
phar \  
soap \  
dom \  
&& git clone https://github.com/Jan-E/uploadprogress /usr/local/lib/php-
ext/uploadprogress \  
&& cd /usr/local/lib/php-ext/uploadprogress \  
&& phpize && ./configure && make && make install \  
&& git clone https://github.com/php-memcached-dev/php-memcached --branch php7
/usr/local/lib/php-ext/memcached \  
&& cd /usr/local/lib/php-ext/memcached \  
&& phpize && ./configure --disable-memcached-sasl && make && make install \  
&& php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');" \  
&& php -r "if (hash_file('SHA384', 'composer-setup.php') ===
'55d6ead61b29c7bdee5cccfb50076874187bd9f21f65d8991d46ec5cc90518f447387fb9f76ebae1fbbacf329e583e30')
{ require_once 'composer-setup.php'; } else { die('Installation failed,
checksum mismatch.'); }" \  
&& php -r "unlink('composer-setup.php');" \  
&& mv composer.phar /usr/local/bin/composer  
  
CMD ["/start.sh"]  

