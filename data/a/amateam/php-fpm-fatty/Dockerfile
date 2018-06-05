FROM php:7.1-fpm  
  
ARG JPEGOPTIM_VERSION=1.4.4  
ARG ZOPFLI_VERSION=1.0.1  
ARG DOCKERIZE_VERSION=0.3.0  
  
RUN apt-get update -y && \  
apt-get install -y \  
git \  
libfreetype6-dev \  
libjpeg62-turbo-dev \  
libmcrypt-dev \  
libpng12-dev \  
libzip-dev \  
libbz2-dev \  
libcurl4-openssl-dev \  
libxml2-dev \  
libssl-dev \  
openssl \  
libgmp3-dev \  
libc-client-dev \  
libkrb5-dev \  
zlib1g-dev \  
libicu-dev \  
libpq-dev \  
libsqlite3-dev && \  
rm -rf /var/lib/apt/lists/*  
RUN docker-php-source extract && \  
mkdir -p /usr/src/php/ext/spl/modules && \  
touch /usr/src/php/ext/spl/modules/spl.fake-module && \  
docker-php-ext-configure gd --with-freetype-dir=/usr/include/ \--with-jpeg-
dir=/usr/include/ && \  
docker-php-ext-configure imap --with-kerberos --with-imap-ssl && \  
docker-php-ext-install -j$(nproc) \  
bcmath \  
bz2 \  
curl \  
dom \  
exif \  
fileinfo \  
ftp \  
gd \  
gettext \  
gmp \  
hash \  
iconv \  
imap \  
intl \  
json \  
mbstring \  
mcrypt \  
mysqli \  
opcache \  
pcntl \  
pdo \  
pdo_mysql \  
pdo_pgsql \  
pdo_sqlite \  
pgsql \  
phar \  
session \  
xml \  
zip && \  
pecl install apcu && \  
docker-php-ext-enable apcu && \  
pecl install xdebug && \  
docker-php-source delete && \  
rm -rf /tmp/pear  
RUN curl -Ss -L https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer && \  
chmod a+x /usr/local/bin/composer  
RUN git clone https://github.com/google/zopfli.git /tmp/zopfli && \  
cd /tmp/zopfli && \  
git checkout zopfli-$ZOPFLI_VERSION && \  
make libzopfli zopfli libzopflipng zopflipng && \  
mv *.so.* /usr/lib/ && \  
mv zopfli /usr/local/bin && \  
mv zopflipng /usr/local/bin && \  
cd / && rm -rf /tmp/zopfli  
RUN git clone https://github.com/tjko/jpegoptim.git /tmp/jpegoptim && \  
cd /tmp/jpegoptim && \  
git checkout -f RELEASE.$JPEGOPTIM_VERSION && \  
./configure && \  
make && make strip && make install && \  
cd / && rm -rf /tmp/jpegoptim  
RUN curl -sS -L
https://github.com/jwilder/dockerize/releases/download/v$DOCKERIZE_VERSION/dockerize-
linux-amd64-v$DOCKERIZE_VERSION.tar.gz -o /tmp/dockerize.tar.gz && \  
tar -C /usr/local/bin -xzvf /tmp/dockerize.tar.gz && \  
rm /tmp/dockerize.tar.gz  
RUN chown -R www-data:www-data /var/www  
  
ADD templates /usr/local/etc/php/conf.template.d  
ADD entrypoint.sh /usr/local/bin/entrypoint  
ENTRYPOINT ["/usr/local/bin/entrypoint"]  
CMD ["php-fpm"]  

