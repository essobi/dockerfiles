FROM php:7.1.0  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update \  
&& buildDeps=" \  
git \  
libmemcached-dev \  
zlib1g-dev \  
" \  
&& doNotUninstall=" \  
libmemcached11 \  
libmemcachedutil2 \  
" \  
&& apt-get install -y $buildDeps --no-install-recommends \  
&& rm -r /var/lib/apt/lists/* \  
\  
&& docker-php-source extract \  
&& git clone --branch php7 https://github.com/php-memcached-dev/php-memcached
/usr/src/php/ext/memcached/ \  
&& docker-php-ext-install memcached \  
\  
&& docker-php-source delete \  
&& apt-mark manual $doNotUninstall \  
&& apt-get purge -y --auto-remove -o
APT::AutoRemove::RecommendsImportant=false $buildDeps \  
\  
&& curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer \  
&& curl -sL https://deb.nodesource.com/setup_6.x | bash - \  
&& apt-get install -y --no-install-recommends \  
nodejs \  
sshpass \  
rsync \  
git \  
openssh-client \  
unzip \  
zip \  
libfreetype6-dev \  
libjpeg62-turbo-dev \  
libmcrypt-dev \  
libpng12-dev \  
libcurl4-openssl-dev \  
zlib1g-dev \  
libicu-dev \  
g++ \  
libmagickwand-dev \  
\  
&& docker-php-ext-configure gd \  
\--with-gd \  
\--with-freetype-dir=/usr/include/ \  
\--with-png-dir=/usr/include/ \  
\--with-jpeg-dir=/usr/include/ \  
&& docker-php-ext-configure intl \  
&& pecl install imagick \  
&& docker-php-ext-enable imagick \  
&& docker-php-ext-install -j$(nproc) \  
gd \  
iconv \  
mcrypt \  
intl \  
pdo_mysql \  
mysqli \  
zip \  
exif \  
\  
&& npm install --global bower gulp \  
&& cp /usr/bin/sshpass /usr/local/bin/sshpass \  
&& chmod +x /usr/local/bin/sshpass \  
&& curl -LO https://deployer.org/releases/v3.3.0/deployer.phar \  
&& mv deployer.phar /usr/local/bin/dep \  
&& chmod +x /usr/local/bin/dep  
  

