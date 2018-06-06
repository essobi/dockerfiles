FROM php:7.0-apache  
  
ENV LC_ALL=C.UTF-8 \  
LANG=C.UTF-8 \  
DEFAULT_TIMEZONE="Australia/Melbourne" \  
COMPOSER_ALLOW_SUPERUSER=1  
  
RUN set -xe && \  
apt-get -qq update && \  
apt-get -qq install \  
apt-transport-https \  
\--no-install-recommends && \  
curl -sL 'https://deb.nodesource.com/gpgkey/nodesource.gpg.key' | apt-key add
- && \  
echo 'deb https://deb.nodesource.com/node_8.x jessie main' >
/etc/apt/sources.list.d/nodesource.list && \  
apt-get -qq update && \  
apt-get -qq install nodejs --no-install-recommends && \  
apt-get purge -qq --auto-remove \  
-o APT::AutoRemove::RecommendsImportant=false \  
-o APT::AutoRemove::SuggestsImportant=false \  
apt-transport-https \  
&& \  
apt-get clean && \  
rm -r /var/lib/apt/lists/* && \  
rm /etc/apt/sources.list.d/nodesource.list && \  
apt-key del 68576280 && \  
true  
  
RUN set -xe && \  
fetchDeps=' \  
zlib1g-dev \  
libpng12-dev \  
libjpeg-dev \  
libicu-dev \  
libmagickwand-dev \  
libxml2-dev \  
' && \  
apt-get -qq update && \  
apt-get -qq install --no-install-recommends \  
git \  
zlib1g \  
libpng12-0 \  
libjpeg62-turbo \  
libmemcached-dev \  
libicu52 \  
libmagickwand-6.q16-2 \  
libxml2 \  
$fetchDeps \  
&& \  
docker-php-ext-configure gd --with-png-dir=/usr --with-jpeg-dir=/usr && \  
git clone --branch php7 https://github.com/php-memcached-dev/php-memcached
/usr/src/php/ext/memcached && \  
echo "memcached" >> /usr/src/php-available-exts && \  
docker-php-ext-configure memcached && \  
docker-php-ext-install \  
zip \  
pdo \  
pdo_mysql \  
gd \  
opcache \  
mbstring \  
bcmath \  
intl \  
pcntl \  
memcached \  
soap \  
shmop \  
&& \  
pecl install apcu && \  
echo "extension=apcu.so" > /usr/local/etc/php/conf.d/apcu.ini && \  
pecl install -o redis && \  
echo "extension=redis.so" > /usr/local/etc/php/conf.d/redis.ini && \  
pecl install -o imagick && \  
echo "extension=imagick.so" > /usr/local/etc/php/conf.d/imagick.ini && \  
pecl install -o ds && \  
echo "extension=ds.so" > /usr/local/etc/php/conf.d/ds.ini && \  
rm -rf /tmp/pear && \  
apt-get purge -qq --auto-remove \  
-o APT::AutoRemove::RecommendsImportant=false \  
-o APT::AutoRemove::SuggestsImportant=false \  
$fetchDeps && \  
apt-get clean && \  
rm -r /var/lib/apt/lists/* && \  
true  
  
RUN set -xe && \  
apt-get -qq update && \  
apt-get -qq install --no-install-recommends \  
libfontconfig1 \  
libfreetype6 \  
libx11-6 \  
libxext6 \  
libxrender1 \  
xz-utils \  
&& \  
mkdir -p /opt && \  
cd /opt && \  
curl -sSL
https://downloads.wkhtmltopdf.org/0.12/0.12.4/wkhtmltox-0.12.4_linux-generic-
amd64.tar.xz | tar -xJv && \  
ln -s /opt/wkhtmltox/bin/wkhtmltopdf /usr/local/bin/wkhtmltopdf && \  
ln -s /opt/wkhtmltox/bin/wkhtmltoimage /usr/local/bin/wkhtmltoimage && \  
apt-get purge -qq --auto-remove \  
-o APT::AutoRemove::RecommendsImportant=false \  
-o APT::AutoRemove::SuggestsImportant=false \  
xz-utils && \  
apt-get clean && \  
rm -r /var/lib/apt/lists/* && \  
true  
  
RUN set -xe && \  
php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');" && \  
php -r "if (hash_file('SHA384', 'composer-setup.php') === '$(curl
https://composer.github.io/installer.sig)') { echo 'Installer verified'; }
else { echo 'Installer corrupt'; unlink('composer-setup.php'); } echo
PHP_EOL;" && \  
php composer-setup.php --install-dir=/usr/local/bin --filename=composer && \  
php -r "unlink('composer-setup.php');" && \  
true  
  
RUN set -xe && \  
curl -sSL
https://github.com/jwilder/dockerize/releases/download/v0.2.0/dockerize-linux-
amd64-v0.2.0.tar.gz | \  
tar -C /usr/local/bin -xzv && \  
true  
  
RUN set -xe && \  
npm install -g uglify-js uglifycss yarn && \  
ln -s /usr/bin/uglify* /usr/local/bin/ && \  
npm cache verify && \  
rm -rf /tmp/* && \  
true  
  
COPY opcache.ini config.ini /usr/local/etc/php/conf.d/  
  
WORKDIR /app  

