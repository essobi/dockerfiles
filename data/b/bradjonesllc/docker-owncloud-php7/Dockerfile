FROM php:7.0-apache  
  
RUN apt-get update && apt-get install -y \  
bzip2 \  
libcurl4-openssl-dev \  
libfreetype6-dev \  
libicu-dev \  
libjpeg-dev \  
libldap2-dev \  
libmcrypt-dev \  
libpng12-dev \  
libpq-dev \  
libxml2-dev \  
&& rm -rf /var/lib/apt/lists/*  
  
#
https://doc.owncloud.org/server/8.1/admin_manual/installation/source_installation.html#prerequisites  
RUN docker-php-ext-configure gd --with-png-dir=/usr --with-jpeg-dir=/usr \  
&& docker-php-ext-configure ldap --with-libdir=lib/x86_64-linux-gnu/ \  
&& docker-php-ext-install exif gd intl ldap mbstring mcrypt mysqli opcache
pdo_mysql pdo_pgsql pgsql zip  
  
# set recommended PHP.ini settings  
# see https://secure.php.net/manual/en/opcache.installation.php  
RUN { \  
echo 'opcache.memory_consumption=128'; \  
echo 'opcache.interned_strings_buffer=8'; \  
echo 'opcache.max_accelerated_files=4000'; \  
echo 'opcache.revalidate_freq=60'; \  
echo 'opcache.fast_shutdown=1'; \  
echo 'opcache.enable_cli=1'; \  
} > /usr/local/etc/php/conf.d/opcache-recommended.ini  
  
RUN a2enmod rewrite  
  
ENV OWNCLOUD_VERSION 9.1.0  
  
RUN curl -fsSL -o owncloud.tar.bz2 \  
"https://download.owncloud.org/community/owncloud-${OWNCLOUD_VERSION}.tar.bz2"
\  
&& curl -fsSL -o owncloud.tar.bz2.asc \  
"https://download.owncloud.org/community/owncloud-${OWNCLOUD_VERSION}.tar.bz2.asc"
\  
&& export GNUPGHOME="$(mktemp -d)" \  
# gpg key from https://owncloud.org/owncloud.asc  
&& gpg --keyserver ha.pool.sks-keyservers.net --recv-keys
E3036906AD9F30807351FAC32D5D5E97F6978A26 \  
&& gpg --batch --verify owncloud.tar.bz2.asc owncloud.tar.bz2 \  
&& rm -r "$GNUPGHOME" owncloud.tar.bz2.asc \  
&& tar -xjf owncloud.tar.bz2 -C /usr/src/ \  
&& rm owncloud.tar.bz2 \  
&& rm -rf /var/www/html \  
&& mv /usr/src/owncloud /var/www/html \  
&& chown -R www-data /var/www/html  
  
COPY entrypoint.sh /entrypoint.sh  
  
ENTRYPOINT ["/entrypoint.sh"]  
CMD ["apache2-foreground"]  

