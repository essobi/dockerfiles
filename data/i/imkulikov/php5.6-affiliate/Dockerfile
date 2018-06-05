FROM php:5-fpm  
  
ENV TERM xterm  
ENV IONCUBE_URL
"http://downloads3.ioncube.com/loader_downloads/ioncube_loaders_lin_x86-64.tar.gz"  
  
RUN set -xe \  
&& buildDeps=" \  
$PHP_EXTRA_BUILD_DEPS \  
libpng12-dev \  
libxpm-dev \  
libjpeg-dev \  
libicu-dev \  
libx11-dev \  
libfreetype6-dev \  
" \  
&& workDeps=" \  
libicu52 \  
libjpeg62 \  
libpng12-0 \  
libxpm4 \  
libfreetype6 \  
libx11-6 \  
" \  
&& apt-get update \  
&& apt-get install -y $buildDeps --no-install-recommends \  
&& apt-get install -y $workDeps --no-install-recommends \  
# Install IonCube Loader:  
&& curl -sfSL $IONCUBE_URL -o ioncube.tar.gz \  
&& tar xvfz ioncube.tar.gz \  
&& PHP_VERSION=$(php -r "echo PHP_MAJOR_VERSION.'.'.PHP_MINOR_VERSION;") \  
&& PHP_EXT_DIR=$(php-config --extension-dir) \  
&& mkdir -p $PHP_EXT_DIR \  
&& cp "ioncube/ioncube_loader_lin_${PHP_VERSION}.so" $PHP_EXT_DIR \  
&& rm -rf ioncube ioncube.tar.gz \  
&& docker-php-ext-configure \  
gd \  
\--with-freetype-dir=/usr/include/ \  
\--with-jpeg-dir=/usr/include/ \  
\--with-png-dir=/usr/include/ \  
\--with-xpm-dir=/usr/include/ \  
&& docker-php-ext-install -j$(nproc) \  
gd \  
intl \  
pcntl \  
mysqli \  
opcache \  
pdo_mysql \  
&& docker-php-ext-enable \  
gd \  
intl \  
pcntl \  
mysqli \  
opcache \  
pdo_mysql \  
&& echo "zend_extension = $PHP_EXT_DIR/ioncube_loader_lin_${PHP_VERSION}.so" >
/usr/local/etc/php/conf.d/00-ioncube.ini \  
# Clean caches and temp-files:  
&& docker-php-source delete \  
&& apt-get purge -y --auto-remove -o
APT::AutoRemove::RecommendsImportant=false $buildDeps \  
&& rm -rf /var/cache/apt/* 2> /dev/null || echo "OK" \  
&& rm -rf /var/lib/apt/lists/* 2> /dev/null || echo "OK" \  
&& rm -rf /usr/src 2> /dev/null || echo "OK" \  
&& rm -rf /tmp/* 2> /dev/null || echo "OK" \  
&& rm -rf /tmp/.* 2> /dev/null || echo "OK" \  
&& rm -rf /root/* 2> /dev/null || echo "OK" \  
&& rm -rf /root/.* 2> /dev/null || echo "OK"

