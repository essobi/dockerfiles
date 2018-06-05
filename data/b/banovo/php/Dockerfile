FROM php:7.1-fpm  
  
ENV LOCAL_UID 33  
  
ENV NODEREPO node_8.x  
  
# Install dependencies  
# apt-get update is called during the nodejs install script  
# See https://deb.nodesource.com/setup  
RUN set -xe \  
\  
# Add nodejs repo (jessie is coming from php) and deps to it  
&& apt-get update && apt-get install -y --force-yes apt-transport-https --no-
install-recommends \  
&& php -r "echo
file_get_contents('https://deb.nodesource.com/gpgkey/nodesource.gpg.key');" |
apt-key add - \  
&& echo "deb https://deb.nodesource.com/${NODEREPO} jessie main" >
/etc/apt/sources.list.d/nodesource.list \  
&& echo "deb-src https://deb.nodesource.com/${NODEREPO} jessie main" >>
/etc/apt/sources.list.d/nodesource.list \  
\  
# Install deps  
&& apt-get update && apt-get install -y --force-yes \  
libicu-dev \  
zlib1g-dev \  
libmcrypt-dev \  
libfreetype6-dev \  
libjpeg62-turbo-dev \  
libmcrypt-dev \  
libpng-dev \  
libxml2-dev \  
libicu52 \  
zlib1g \  
nodejs \  
sudo \  
\--no-install-recommends && rm -r /var/lib/apt/lists/*  
  
# Install extensions  
RUN set -xe \  
&& docker-php-ext-configure \  
gd \  
\--with-gd \  
\--with-freetype-dir=/usr/include/ \  
\--with-png-dir=/usr/include/ \  
\--with-jpeg-dir=/usr/include/ \  
\  
\  
&& docker-php-ext-install -j$(nproc) \  
gd \  
intl \  
mbstring \  
mcrypt \  
opcache \  
pdo_mysql \  
soap \  
exif \  
fileinfo \  
zip  
  
RUN pecl install \  
apcu-5.1.7 \  
&& docker-php-ext-enable --ini-name 05-opcache.ini \  
opcache \  
&& docker-php-ext-enable --ini-name 20-apcu.ini \  
apcu  
  
# Oro php settings  
RUN { \  
echo "memory_limit=1024M"; \  
echo "date.timezone=Europe/Berlin"; \  
echo "detect_unicode=off"; \  
echo "xdebug.scream=off"; \  
} > /usr/local/etc/php/conf.d/custom.ini  
  
COPY docker-entrypoint.sh /usr/local/bin/  
ENTRYPOINT ["docker-entrypoint.sh"]  
  
WORKDIR /var/www  
EXPOSE 9000  
CMD ["php-fpm"]  

