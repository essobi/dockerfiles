FROM php:7.1.6-apache  
MAINTAINER Andrea Falco <fox91fox@gmail.com>  
  
RUN persistentDeps=" \  
libfreetype6 \  
libjpeg62-turbo \  
libmcrypt4 \  
libpng12-0 \  
libvpx1 \  
libxpm4 \  
" \  
&& buildDeps=" \  
libfreetype6-dev \  
libjpeg62-turbo-dev \  
libmcrypt-dev \  
libpng12-dev \  
libvpx-dev \  
libxpm-dev \  
" \  
&& set -x \  
&& DEBIAN_FRONTEND=noninteractive apt-get update \  
&& DEBIAN_FRONTEND=noninteractive apt-get install -y $persistentDeps
$buildDeps --no-install-recommends \  
&& docker-php-ext-configure gd \  
\--with-jpeg-dir=/usr/include/ \  
\--with-png-dir=/usr/include/ \  
\--with-xpm-dir=/usr/include/ \  
\--with-vpx-dir=/usr/include/ \  
\--with-freetype-dir=/usr/include/ \  
\--enable-gd-native-ttf \  
&& docker-php-ext-install gd mbstring mcrypt mysqli \  
&& DEBIAN_FRONTEND=noninteractive apt-get purge -y --auto-remove -o
APT::AutoRemove::RecommendsImportant=false -o
APT::AutoRemove::SuggestsImportant=false $buildDeps \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
COPY bin /usr/bin  
  
RUN set -x \  
&& curl -SL https://files.phpmyadmin.net/phpmyadmin.keyring \  
| gpg --import - \  
&& cd /tmp \  
&& curl -o phpMyAdmin.tar.gz -sSL
"https://www.phpmyadmin.net/downloads/phpMyAdmin-latest-english.tar.gz" \  
&& curl -o phpMyAdmin.tar.gz.asc -sSL
"https://www.phpmyadmin.net/downloads/phpMyAdmin-latest-english.tar.gz.asc" \  
&& gpg --verify phpMyAdmin.tar.gz.asc \  
&& tar -xzC /var/www/html --strip-components=1 -f phpMyAdmin.tar.gz \  
&& chown -R www-data:www-data /var/www/html \  
&& rm phpMyAdmin.tar.gz* \  
&& bash /usr/bin/phpmyadmin-setup  

