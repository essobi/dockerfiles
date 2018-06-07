FROM php:7.2  
  
MAINTAINER Joshua Gigg <giggsey@gmail.com>  
  
ENV XDEBUG_VERSION 2.5.1  
  
ENV MEMCACHE_REVISION 'e702b5f'  
# Install additional packages  
RUN apt-get update && apt-get install -y git gnupg2 msmtp-mta openssh-client
rsync --no-install-recommends && rm -r /var/lib/apt/lists/*  
  
RUN curl -sL https://deb.nodesource.com/setup_6.x | bash - \  
&& apt-get install -y nodejs --no-install-recommends \  
&& rm -r /var/lib/apt/lists/*  
# Install php extensions  
RUN buildDeps=" \  
freetds-dev \  
libbz2-dev \  
libc-client-dev \  
libenchant-dev \  
libfreetype6-dev \  
libgmp3-dev \  
libicu-dev \  
libjpeg62-turbo-dev \  
libkrb5-dev \  
libldap2-dev \  
libmcrypt-dev \  
libmemcached-dev \  
libpq-dev \  
libpspell-dev \  
librabbitmq-dev \  
libsasl2-dev \  
libsnmp-dev \  
libssl-dev \  
libtidy-dev \  
libxml2-dev \  
libxpm-dev \  
libxslt1-dev \  
zlib1g-dev \  
" \  
&& phpModules=" \  
bcmath bz2 calendar dba enchant exif ftp gd gettext gmp imap intl ldap
mbstring mysqli opcache pcntl pdo pdo_dblib pdo_mysql pdo_pgsql pgsql pspell
shmop snmp soap sockets sysvmsg sysvsem sysvshm tidy wddx xmlrpc xsl zip
xdebug \  
" \  
&& echo "deb http://httpredir.debian.org/debian jessie contrib non-free" >
/etc/apt/sources.list.d/additional.list \  
&& apt-get update && apt-get install -y libc-client2007e libpng-dev
libenchant1c2a libfreetype6 libjpeg62-turbo libmcrypt4 libpq5 libsybdb5
libx11-6 libxpm4 libxslt1.1 snmp --no-install-recommends \  
&& apt-get install -y $buildDeps --no-install-recommends \  
&& docker-php-source extract \  
&& cd /usr/src/php/ext/ \  
&& git clone git://github.com/xdebug/xdebug.git \  
&& ln -s /usr/include/x86_64-linux-gnu/gmp.h /usr/include/gmp.h \  
&& ln -s /usr/lib/x86_64-linux-gnu/libldap_r.so /usr/lib/libldap.so \  
&& ln -s /usr/lib/x86_64-linux-gnu/libldap_r.a /usr/lib/libldap_r.a \  
&& ln -s /usr/lib/x86_64-linux-gnu/libsybdb.a /usr/lib/libsybdb.a \  
&& ln -s /usr/lib/x86_64-linux-gnu/libsybdb.so /usr/lib/libsybdb.so \  
&& docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-
dir=/usr/include/ \--with-xpm-dir=/usr/include/ \  
&& docker-php-ext-configure imap --with-imap --with-kerberos --with-imap-ssl \  
&& docker-php-ext-configure ldap --with-ldap-sasl \  
&& docker-php-ext-install $phpModules \  
&& printf "\n" | pecl install amqp \  
&& pecl install mongodb \  
&& pecl install redis \  
&& for ext in $phpModules; do \  
rm -f /usr/local/etc/php/conf.d/docker-php-ext-$ext.ini; \  
done \  
&& git clone https://github.com/websupport-sk/pecl-memcache.git /tmp/memcache/
\  
&& cd /tmp/memcache/ \  
&& git reset --hard $MEMCACHE_REVISION \  
&& phpize \  
&& ./configure && make && make install \  
&& rm -rf /tmp/memcache/ \  
&& docker-php-source delete \  
&& apt-get purge -y --auto-remove -o
APT::AutoRemove::RecommendsImportant=false -o
APT::AutoRemove::SuggestsImportant=false $buildDeps  
  
RUN apt-get update && apt-get install -y libpng-dev --no-install-recommends \  
&& rm -r /var/lib/apt/lists/*  
# Install composer and put binary into $PATH  
RUN curl -sS https://getcomposer.org/installer | php \  
&& mv composer.phar /usr/local/bin/ \  
&& ln -s /usr/local/bin/composer.phar /usr/local/bin/composer  
  
COPY entrypoint.sh /entrypoint.sh  
ENTRYPOINT ["/entrypoint.sh"]  
CMD ["php", "-a"]  

