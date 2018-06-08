FROM php:7.0-fpm  
  
RUN apt-get update && apt-get install -y \  
bzip2 \  
libcurl4-openssl-dev \  
libfreetype6-dev \  
libicu-dev \  
libjpeg-dev \  
libldap2-dev \  
libmcrypt-dev \  
libmemcached-dev \  
libpng12-dev \  
libpq-dev \  
libxml2-dev \  
git \  
&& rm -rf /var/lib/apt/lists/*  
  
#
https://docs.nextcloud.com/server/9/admin_manual/installation/source_installation.html  
RUN docker-php-ext-configure gd --with-png-dir=/usr --with-jpeg-dir=/usr \  
&& docker-php-ext-configure ldap --with-libdir=lib/x86_64-linux-gnu \  
&& docker-php-ext-install gd exif intl mbstring mcrypt ldap mysqli opcache
pdo_mysql pdo_pgsql pgsql zip  
  
# set recommended PHP.ini settings  
# see https://secure.php.net/manual/en/opcache.installation.php  
RUN { \  
echo 'opcache.memory_consumption=128'; \  
echo 'opcache.interned_strings_buffer=8'; \  
echo 'opcache.max_accelerated_files=10000'; \  
echo 'opcache.revalidate_freq=1'; \  
echo 'opcache.fast_shutdown=1'; \  
echo 'opcache.enable_cli=1'; \  
echo 'opcache.enable=1'; \  
} > /usr/local/etc/php/conf.d/opcache-recommended.ini  
  
# PECL extensions  
RUN set -ex \  
&& pecl install APCu-5.1.7 \  
&& pecl install redis-3.1.0 \  
&& docker-php-ext-enable apcu redis  
  
# Memcached  
RUN git clone https://github.com/php-memcached-dev/php-memcached
/usr/src/php/ext/memcached \  
&& cd /usr/src/php/ext/memcached && git checkout -b php7 origin/php7 \  
&& docker-php-ext-configure memcached \  
&& docker-php-ext-install memcached \  
&& rm -fr /usr/src/php/ext/memcached  
  
ENV NEXTCLOUD_VERSION 12.0.2  
VOLUME /var/www/html  
  
RUN curl -fsSL -o nextcloud.tar.bz2 \  
"https://download.nextcloud.com/server/releases/nextcloud-${NEXTCLOUD_VERSION}.tar.bz2"
\  
&& curl -fsSL -o nextcloud.tar.bz2.asc \  
"https://download.nextcloud.com/server/releases/nextcloud-${NEXTCLOUD_VERSION}.tar.bz2.asc"
\  
&& export GNUPGHOME="$(mktemp -d)" \  
# gpg key from https://nextcloud.com/nextcloud.asc  
&& gpg --keyserver pgp.mit.edu --recv-keys
28806A878AE423A28372792ED75899B9A724937A \  
&& gpg --batch --verify nextcloud.tar.bz2.asc nextcloud.tar.bz2 \  
&& rm -r "$GNUPGHOME" nextcloud.tar.bz2.asc \  
&& tar -xjf nextcloud.tar.bz2 -C /usr/src/ \  
&& rm nextcloud.tar.bz2  
  
COPY docker-entrypoint.sh /entrypoint.sh  
RUN chmod 755 /entrypoint.sh  
RUN apt-get clean  
  
ENTRYPOINT ["/entrypoint.sh"]  
CMD ["php-fpm"]  

