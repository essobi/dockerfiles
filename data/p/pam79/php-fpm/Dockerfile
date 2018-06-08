FROM php:7.2.1-fpm  
  
MAINTAINER Abdullah Morgan <paapaabdullahm@gmail.com>  
  
# Setup essential pkgs & libs via apt  
RUN apt update && apt upgrade -y; \  
apt install -y \  
apt-utils \  
aspell-en \  
curl \  
file \  
firebird-dev \  
libc-client-dev \  
libc6 \  
libcurl3 \  
libcurl3-dev \  
libfreetype6-dev \  
libgmp-dev \  
libgmp10 \  
libicu-dev \  
libjpeg62-turbo-dev \  
libkrb5-dev \  
libldap2-dev \  
libldb-dev \  
libmagickwand-dev \  
libmcrypt-dev \  
libmhash-dev \  
libpq-dev \  
libpspell-dev \  
librecode-dev \  
librecode0 \  
libsqlite3-0 \  
libsqlite3-dev \  
libssl-dev \  
libtidy-dev \  
libxml2-dev \  
libxslt-dev \  
mysql-client \  
re2c \  
ucf \  
\--no-install-recommends; \  
#  
# Setup libpng via dpkg  
wget
http://mirrors.kernel.org/ubuntu/pool/main/libp/libpng/libpng12-0_1.2.54-1ubuntu1_amd64.deb;
\  
dpkg -i libpng12-0_1.2.54-1ubuntu1_amd64.deb; apt install -f; \  
rm -f libpng12-0_1.2.54-1ubuntu1_amd64.deb; \  
#  
# Setup php extensions via docker-php-ext  
docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-
dir=/usr/include/; \  
docker-php-ext-configure imap --with-kerberos --with-imap-ssl; \  
docker-php-ext-configure ldap --with-libdir=lib/x86_64-linux-gnu; \  
docker-php-ext-install \  
bcmath \  
calendar \  
ctype \  
curl \  
dba \  
dom \  
exif \  
fileinfo \  
ftp \  
gettext \  
gmp \  
hash \  
iconv \  
imap \  
interbase \  
intl \  
json \  
ldap \  
mbstring \  
mysqli \  
opcache \  
pcntl \  
pdo \  
pdo_firebird \  
pdo_mysql \  
pdo_pgsql \  
pdo_sqlite \  
pgsql \  
phar \  
posix \  
pspell \  
recode \  
session \  
shmop \  
simplexml \  
soap \  
sockets \  
sysvmsg \  
sysvsem \  
sysvshm \  
tidy \  
tokenizer \  
wddx \  
xml \  
xmlrpc \  
xmlwriter \  
xsl \  
zip \  
-j$(nproc) intl gd; \  
ln -s /usr/include/x86_64-linux-gnu/gmp.h /usr/local/include/; \  
#  
# Setup php extensions via pecl  
yes | pecl install imagick xdebug mongodb; \  
docker-php-ext-enable imagick xdebug mongodb; \  
usermod -u 1000 www-data; \  
rm -rf /var/lib/apt/lists/*;  
  
EXPOSE 9000  
CMD ["php-fpm"]

