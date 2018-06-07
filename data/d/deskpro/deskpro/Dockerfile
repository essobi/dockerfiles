FROM php:7.0-apache  
  
RUN set -x \  
&& apt-get update \  
&& apt-get install -y --no-install-recommends \  
cron \  
libc-client-dev \  
libfreetype6-dev \  
libicu-dev \  
libjpeg62-turbo-dev \  
libkrb5-dev \  
libldap2-dev \  
libmcrypt-dev \  
libpng-dev \  
libxml2-dev \  
libzip-dev \  
mariadb-client \  
unzip \  
&& docker-php-ext-install -j$(nproc) \  
iconv \  
intl \  
mcrypt \  
opcache \  
pdo_mysql \  
soap \  
zip \  
&& docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-
dir=/usr/include/ \  
&& docker-php-ext-install -j$(nproc) gd \  
&& docker-php-ext-configure imap --with-kerberos --with-imap-ssl \  
&& docker-php-ext-install -j$(nproc) imap \  
&& docker-php-ext-configure ldap --with-libdir=lib/x86_64-linux-gnu/ \  
&& docker-php-ext-install -j$(nproc) ldap \  
&& apt-get remove -y \  
libc-client-dev \  
libfreetype6-dev \  
libicu-dev \  
libjpeg62-turbo-dev \  
libkrb5-dev \  
libldap2-dev \  
libmcrypt-dev \  
libpng-dev \  
libxml2-dev \  
libzip-dev \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN a2enmod rewrite  
  
RUN curl -L https://www.deskpro.com/downloads/deskpro.zip -o
/usr/src/deskpro.zip  
  
ENV GOSU_VERSION 1.10  
RUN set -ex; \  
\  
fetchDeps=' \  
ca-certificates \  
dirmngr \  
gnupg \  
wget \  
'; \  
apt-get update; \  
apt-get install -y --no-install-recommends $fetchDeps; \  
rm -rf /var/lib/apt/lists/*; \  
\  
dpkgArch="$(dpkg --print-architecture | awk -F- '{ print $NF }')"; \  
wget -O /usr/local/bin/gosu
"https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-$dpkgArch";
\  
wget -O /usr/local/bin/gosu.asc
"https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-$dpkgArch.asc";
\  
\  
# verify the signature  
export GNUPGHOME="$(mktemp -d)"; \  
gpg --keyserver ha.pool.sks-keyservers.net --recv-keys
B42F6819007F00F88E364FD4036A9C25BF357DD4; \  
gpg --batch --verify /usr/local/bin/gosu.asc /usr/local/bin/gosu; \  
rm -rf "$GNUPGHOME" /usr/local/bin/gosu.asc; \  
\  
chmod +x /usr/local/bin/gosu; \  
# verify that the binary works  
gosu nobody true; \  
\  
apt-get purge -y --auto-remove $fetchDeps  
  
VOLUME /var/www/html  
  
RUN rm -rf /etc/apache2/sites-enabled/000-default.conf  
  
COPY deskpro.conf /etc/apache2/sites-enabled/deskpro.conf  
  
COPY php.ini /usr/local/etc/php/  
  
COPY docker-entrypoint.sh deskpro-docker-cron /usr/local/bin/  
  
ENTRYPOINT ["docker-entrypoint.sh"]  
CMD ["apache2-foreground"]  

