FROM php:7.2-zts  
  
# install dependencies  
RUN apt-get update && apt-get -y --no-install-recommends install \  
git \  
ssh \  
libicu-dev \  
libxml2-dev \  
libcurl3-dev \  
libsodium-dev \  
libjpeg-dev \  
libpng-dev \  
libwebp-dev \  
libfreetype6-dev \  
libmemcached-dev \  
libedit-dev \  
libxslt1-dev \  
zlib1g-dev \  
libmagickwand-6.q16-dev \  
libpq-dev \  
libsqlite3-dev \  
&& ln -s /usr/lib/x86_64-linux-gnu/ImageMagick-6.9.7/bin-Q16/MagickWand-config
/usr/bin  
  
# build & install extensions  
RUN pecl install \  
apcu \  
igbinary \  
msgpack \  
redis \  
imagick \  
xdebug \  
## manual build memcached  
&& pecl download memcached \  
&& mkdir memcached \  
&& tar xzvf memcached*.tgz -C memcached --strip-components=1 \  
&& cd memcached \  
&& phpize \  
&& ./configure --enable-memcached-igbinary --enable-memcached-msgpack
--enable-memcached-json \  
&& make \  
&& make install \  
&& cd .. \  
&& rm -rf memcached \  
## manual build phalcon  
&& export PHALCON_VERSION=`curl --silent
"https://api.github.com/repos/phalcon/cphalcon/releases/latest" | grep
'"tag_name":' | sed -E 's/.*"([^"]+)".*/\1/' | sed -E 's/^.//'` \  
&& cd /tmp \  
&& curl -sSLO
https://codeload.github.com/phalcon/cphalcon/tar.gz/v$PHALCON_VERSION \  
&& tar xvzf v$PHALCON_VERSION \  
&& cd cphalcon-$PHALCON_VERSION/build \  
&& ./install \  
&& rm -rf /tmp/cphalcon-$PHALCON_VERSION \  
## manual build pthreads  
&& cd /tmp \  
&& git clone https://github.com/krakjoe/pthreads.git pthreads \  
&& cd pthreads \  
&& phpize \  
&& ./configure \  
&& make \  
&& make install \  
&& cd .. \  
&& rm -rf pthreads \  
# cleanup pear  
&& rm -rf /tmp/pear \  
# install & enable default extensions  
&& docker-php-ext-enable pthreads \  
&& docker-php-ext-configure gd \  
\--with-jpeg-dir=/usr/include/ \  
\--with-png-dir=/usr/include/ \  
\--with-webp-dir=/usr/include/ \  
\--with-freetype-dir=/usr/include/ \  
&& docker-php-ext-configure pgsql \  
\--with-pgsql=/usr/local/pgsql \  
&& docker-php-ext-install -j$(nproc) \  
bcmath \  
gd \  
iconv \  
intl \  
mysqli \  
opcache \  
pdo_mysql \  
pdo_pgsql \  
pdo_sqlite \  
pgsql \  
sodium \  
xsl \  
zip  
  
# install phpunit  
RUN curl -o phpunit.phar -sSL https://phar.phpunit.de/phpunit-7.phar && \  
chmod +x phpunit.phar && \  
mv phpunit.phar /usr/local/bin/phpunit  
  
# install composer  
RUN curl -sS https://getcomposer.org/installer | php && \  
chmod +x composer.phar && \  
mv composer.phar /usr/local/bin/composer  
  
# configure ssh  
RUN mkdir -p ~/.ssh && \  
echo "Host *" > ~/.ssh/config && \  
echo " PasswordAuthentication no" >> ~/.ssh/config && \  
echo " StrictHostKeyChecking no" >> ~/.ssh/config && \  
echo " UserKnownHostsFile /dev/null" >> ~/.ssh/config  
  
# cleanup  
RUN apt-get -y autoremove && \  
apt-get -y clean && \  
apt-get -y autoclean && \  
rm -rf /var/lib/apt/lists/* && \  
rm -rf /var/cache/apt/* && \  
rm -rf /usr/share/locale/* && \  
rm -rf /usr/share/doc/* \  
rm -rf /var/log/* \  
rm -rf /var/www/html  
  
WORKDIR /var/www

