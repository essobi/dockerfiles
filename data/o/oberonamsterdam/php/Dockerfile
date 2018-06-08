FROM php:5.6-fpm  
MAINTAINER chin@oberon.nl  
  
ENV DEBIAN_FRONTEND=noninteractive \  
TERM=xterm \  
PHP_MAX_EXECUTION_TIME=120 \  
PHP_MEMORY_LIMIT=256M \  
PHP_UPLOAD_LIMIT=8M \  
PHP_OPCACHE_LIMIT=64M \  
PHP_OPCACHE_REVALIDATE=2 \  
PHP_SESSION_SAVE_HANDLER=files \  
PHP_SESSION_SAVE_PATH="" \  
PHP_SMTP_HOST=localhost  
  
COPY production.ini /usr/local/etc/php/conf.d/00-production.ini  
COPY docker-settings.ini /usr/local/etc/php/conf.d/01-docker-settings.ini  
  
# PHP Configuration  
RUN echo "LANG=\"en_US.UTF-8\"" > /etc/default/locale && \  
echo "en_US.UTF-8 UTF-8" >> /etc/locale.gen && \  
echo "nl_NL.UTF-8 UTF-8" >> /etc/locale.gen  
  
# Install dependencies  
RUN apt-get update && apt-get install -y --no-install-recommends apt-utils  
  
RUN apt-get install -y supervisor cron nano && \  
apt-get install -y libsqlite3-dev zlib1g-dev libfreetype6-dev libjpeg62-turbo-
dev libmcrypt-dev libpng12-dev libpng-dev libicu-dev libz-dev libmemcached-dev
libcurl4-openssl-dev libxslt1-dev libffi-dev libssl-dev g++ libldap2-dev
libmagickwand-dev && \  
apt-get install -y git mercurial locales zip  
  
# PHP Configuration  
RUN mkdir -p /etc/mercurial && \  
echo "[trusted]" >> /etc/mercurial/hgrc && \  
echo "users = 1000" >> /etc/mercurial/hgrc && \  
echo "groups = 1000" >> /etc/mercurial/hgrc  
  
# PHP Configuration  
RUN \  
docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-
dir=/usr/include/ && \  
docker-php-ext-configure ldap --with-libdir=lib/x86_64-linux-gnu/ && \  
docker-php-ext-install -j$(nproc) gd exif mcrypt zip mbstring intl bcmath curl
pdo_mysql xsl soap mysqli simplexml sockets xmlrpc opcache mysql ldap && \  
pecl install memcache-3.0.8 && docker-php-ext-enable memcache && \  
pecl install memcached-2.2.0 && docker-php-ext-enable memcached && \  
pecl install redis-3.1.2 && docker-php-ext-enable redis && \  
pecl install imagick && docker-php-ext-enable imagick  
  
# Install nodejs  
RUN curl -sL https://deb.nodesource.com/setup_8.x | bash - && \  
apt-get install -y nodejs && \  
npm install -g yarn bower gulp pm2  
  
# Composer  
RUN \  
curl -sS https://getcomposer.org/installer | php && \  
mv composer.phar /usr/local/bin/composer && \  
chmod +x /usr/local/bin/composer  
  
# Cleanup  
RUN apt-get purge -y --auto-remove apt-utils libsqlite3-dev libz-dev
libcurl4-openssl-dev libffi-dev libssl-dev && \  
apt-get -y clean && \  
apt-get -y purge && \  
rm -rf /var/lib/apt/lists/* /tmp/*  
  
RUN echo "Europe/Amsterdam" > /etc/timezone && dpkg-reconfigure --frontend
noninteractive tzdata && \  
touch /var/log/cron.log  
  
RUN mkdir -p /app  
VOLUME /app  
WORKDIR /app  

