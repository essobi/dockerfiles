FROM php:5.6-apache  
  
LABEL Maintainer="Westerus <westerus@gmail.com>" \  
Name="TikiWiki" \  
Description="Imágen con los cambios realizados sobre Tikiwiki 17.x" \  
Version="1.0.0"  
  
ARG APT_FLAGS_COMMON="-qq -y"  
ARG APT_FLAGS_PERSISTANT="${APT_FLAGS_COMMON} --no-install-recommends"  
ARG APT_FLAGS_DEV="${APT_FLAGS_COMMON} --no-install-recommends"  
  
ARG APTUPDATE="apt-get ${APT_FLAGS_COMMON} update"  
ARG APTUPGRADE="apt-get ${APT_FLAGS_PERSISTANT} upgrade"  
ARG APTAUTOREMOVE="apt-get ${APT_FLAGS_COMMON} autoremove"  
ARG APTCLEAN="apt-get ${APT_FLAGS_COMMON} clean"  
ARG DELTEMP="rm -rf /var/lib/apt/lists/* /var/tmp/* /tmp/*"  
ARG APTINSTALL="apt-get ${APT_FLAGS_PERSISTANT} install"  
ARG APTREMOVE="apt-get ${APT_FLAGS_COMMON} purge"  
  
ENV TZ="Europe/Madrid" \  
DEBIAN_FRONTEND="noninteractive"  
  
RUN set -x; \  
rm /etc/localtime \  
&& ln -s /usr/share/zoneinfo/Europe/Madrid /etc/localtime \  
&& date \  
&& $APTUPDATE \  
&& $APTUPGRADE \  
&& $APTINSTALL \  
libfreetype6-dev \  
libjpeg62-turbo-dev \  
libmcrypt-dev \  
libpng12-dev \  
libldap2-dev \  
libldb-dev \  
libmemcached-dev \  
libsasl2-dev \  
zlib1g-dev \  
imagemagick \  
unzip \  
curl \  
git \  
&& a2enmod ssl \  
&& ln -s /usr/lib/x86_64-linux-gnu/libldap.so /usr/lib/libldap.so \  
&& ln -s /usr/lib/x86_64-linux-gnu/liblber.so /usr/lib/liblber.so \  
&& docker-php-ext-install -j$(nproc) \  
iconv \  
mcrypt \  
mysql \  
pdo_mysql \  
ldap \  
zip \  
calendar \  
mysqli \  
opcache \  
mbstring \  
&& docker-php-ext-configure gd --with-freetype-dir=/usr/include/ \--with-jpeg-
dir=/usr/include/ \  
&& docker-php-ext-install -j$(nproc) gd \  
&& pecl channel-update pecl.php.net \  
&& printf "yes\n" | pecl install memcached-2.2.0 \  
&& printf "yes\n" | pecl install memcache-3.0.8 \  
&& printf "yes\n" | pecl install xdebug-2.5.5 \  
&& docker-php-ext-enable memcached \  
&& docker-php-ext-enable memcache \  
&& docker-php-ext-enable xdebug \  
&& a2enmod rewrite expires ssl \  
&& curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer  
  
EXPOSE 80 443  

