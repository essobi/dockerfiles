FROM buildpack-deps:jessie  
  
# persistent / runtime deps  
ENV PHPIZE_DEPS \  
autoconf \  
file \  
g++ \  
gcc \  
libc-dev \  
make \  
pkg-config \  
re2c  
RUN apt-get update && apt-get install -y \  
$PHPIZE_DEPS \  
ca-certificates \  
curl \  
libedit2 \  
libsqlite3-0 \  
libxml2 \  
xz-utils \  
\--no-install-recommends && rm -r /var/lib/apt/lists/*  
  
ENV PHP_INI_DIR /usr/local/etc/php  
RUN mkdir -p $PHP_INI_DIR/conf.d  
  
# Apply stack smash protection to functions using local buffers and alloca()  
# Make PHP's main executable position-independent (improves ASLR security
mechanism, and has no performance impact on x86_64)  
# Enable optimization (-O2)  
# Enable linker optimization (this sorts the hash buckets to improve cache
locality, and is non-default)  
# Adds GNU HASH segments to generated executables (this is used if present,
and is much faster than sysv hash; in this configuration, sysv hash is also
generated)  
# https://github.com/docker-library/php/issues/272  
ENV PHP_CFLAGS="-fstack-protector-strong -fpic -fpie -O2"  
ENV PHP_CPPFLAGS="$PHP_CFLAGS"  
ENV PHP_LDFLAGS="-Wl,-O1 -Wl,--hash-style=both -pie"  
  
ENV GPG_KEYS 1A4E8B7277C42E53DBA9C7B9BCAA30EA9C0D5763
6E4F6AB321FDC07F2C332E3AC2BF0BC433CFC8B3  
  
ENV PHP_VERSION 7.1.8  
ENV
PHP_URL="https://secure.php.net/get/php-$PHP_VERSION.tar.xz/from/this/mirror"
PHP_ASC_URL="https://secure.php.net/get/php-$PHP_VERSION.tar.xz.asc/from/this/mirror"  
ENV
PHP_SHA256="8943858738604acb33ecedb865d6c4051eeffe4e2d06f3a3c8f794daccaa2aab"  
  
RUN set -xe \  
\  
fetchDeps=' \  
wget \  
'; \  
apt-get update; \  
apt-get install -y --no-install-recommends $fetchDeps; \  
rm -rf /var/lib/apt/lists/*; \  
\  
mkdir -p /usr/src; \  
cd /usr/src; \  
\  
wget -O php.tar.xz "$PHP_URL"; \  
\  
if [ -n "$PHP_SHA256" ]; then \  
echo "$PHP_SHA256 *php.tar.xz" | sha256sum -c -; \  
fi; \  
\  
export GNUPGHOME="$(mktemp -d)"; \  
# if [ -n "$PHP_ASC_URL" ]; then \  
# wget -O php.tar.xz.asc "$PHP_ASC_URL"; \  
# for key in $GPG_KEYS; do \  
# gpg --keyserver ha.pool.sks-keyservers.net --recv-keys "$key"; \  
# done; \  
# gpg --batch --verify php.tar.xz.asc php.tar.xz; \  
# fi; \  
\  
apt-get purge -y --auto-remove $fetchDeps  
  
COPY docker-php-source /usr/local/bin/  
  
RUN buildDeps=" \  
$PHP_EXTRA_BUILD_DEPS \  
libcurl4-openssl-dev \  
libedit-dev \  
libsqlite3-dev \  
libssl-dev \  
libxml2-dev \  
" \  
&& apt-get update && apt-get install -y $buildDeps --no-install-recommends &&
rm -rf /var/lib/apt/lists/* \  
\  
&& export CFLAGS="$PHP_CFLAGS" \  
CPPFLAGS="$PHP_CPPFLAGS" \  
LDFLAGS="$PHP_LDFLAGS" \  
&& docker-php-source extract \  
&& cd /usr/src/php \  
&& ./configure \  
\--with-config-file-path="$PHP_INI_DIR" \  
\--with-config-file-scan-dir="$PHP_INI_DIR/conf.d" \  
\--disable-cgi \  
# --enable-ftp is included here because ftp_ssl_connect() needs ftp to be
compiled statically (see https://github.com/docker-library/php/issues/236)  
\--enable-ftp \  
# --enable-mbstring is included here because otherwise there's no way to get
pecl to use it properly (see https://github.com/docker-library/php/issues/195)  
\--enable-mbstring \  
# --enable-mysqlnd is included here because it's harder to compile after the
fact than extensions are (since it's a plugin for several extensions, not an
extension in itself)  
\--enable-mysqlnd \  
\  
\--with-curl \  
\--with-libedit \  
\--with-openssl \  
\--with-zlib \  
$PHP_EXTRA_CONFIGURE_ARGS \  
&& make -j "$(nproc)" \  
&& make install \  
&& { find /usr/local/bin /usr/local/sbin -type f -executable -exec strip
--strip-all '{}' \+ || true; } \  
&& make clean \  
&& docker-php-source delete  
  
COPY docker-php-ext-* /usr/local/bin/  
# NodeJS  
RUN groupadd --gid 1000 node \  
&& useradd --uid 1000 \--gid node --shell /bin/bash --create-home node  
  
RUN for key in \  
9554F04D7259F04124DE6B476D5A82AC7E37093B \  
94AE36675C464D64BAFA68DD7434390BDBE9B9C5 \  
0034A06D9D9B0064CE8ADF6BF1747F4AD2306D93 \  
FD3A5288F042B6850C66B31F09FE44734EB7990E \  
71DCFD284A79C3B38668286BC97EC7A07EDE3FC1 \  
DD8F2338BAE7501E3DD5AC78C273792F7D83545D \  
B9AE9905FFD7803F25714661B63B535A4C206CA9 \  
C4F0DFFF4E8C1A8236409D08E73BC641CC11F4C8 \  
56730D5401028683275BD23C23EFEFE93C4CFFFE \  
; do \  
gpg --keyserver ha.pool.sks-keyservers.net --recv-keys "$key"; \  
done  
  
  
ENV NPM_CONFIG_LOGLEVEL info  
ENV NODE_VERSION 8.3.0  
ENV NPM_VERSION 5.3.0  
  
RUN curl -sSLO "https://nodejs.org/dist/v$NODE_VERSION/node-v$NODE_VERSION-
linux-x64.tar.xz" \  
&& curl -sSLO "https://nodejs.org/dist/v$NODE_VERSION/SHASUMS256.txt.asc" \  
&& gpg --batch --decrypt --output SHASUMS256.txt SHASUMS256.txt.asc \  
&& grep " node-v$NODE_VERSION-linux-x64.tar.xz\$" SHASUMS256.txt | sha256sum
-c - \  
&& tar -xJf "node-v$NODE_VERSION-linux-x64.tar.xz" -C /usr/local --strip-
components=1 \  
&& rm "node-v$NODE_VERSION-linux-x64.tar.xz" SHASUMS256.txt.asc SHASUMS256.txt
\  
&& ln -s /usr/local/bin/node /usr/local/bin/nodejs \  
&& npm install -g npm@"$NPM_VERSION" \  
&& npm cache verify  
  
# Install modules  
RUN apt-get update \  
&& apt-get install -yqq \  
git \  
unzip \  
libmcrypt-dev \  
libicu-dev \  
libcurl4-gnutls-dev \  
libicu-dev \  
libmcrypt-dev \  
libvpx-dev \  
libjpeg-dev \  
libpng-dev \  
libxpm-dev \  
zlib1g-dev \  
libfreetype6-dev \  
libxml2-dev \  
libexpat1-dev \  
libbz2-dev \  
libgmp3-dev \  
libldap2-dev \  
unixodbc-dev \  
libpq-dev \  
libsqlite3-dev \  
libaspell-dev \  
libsnmp-dev \  
libpcre3-dev \  
libtidy-dev \  
&& docker-php-ext-install pdo_mysql \  
&& docker-php-ext-install iconv \  
&& docker-php-ext-install mcrypt \  
&& docker-php-ext-install intl \  
&& docker-php-ext-install opcache \  
&& docker-php-ext-install mbstring \  
&& docker-php-ext-install curl \  
&& docker-php-ext-install json \  
&& docker-php-ext-install intl \  
&& docker-php-ext-install gd \  
&& docker-php-ext-install xml \  
&& docker-php-ext-install bz2 \  
&& docker-php-ext-install opcache  
  
# Extra pagkages version  
ENV BEHAT_VERSION 3.3.0  
ENV PHPSPEC_VERSION 4.0.2  
# Install extra packages  
RUN curl -sSLO https://getcomposer.org/composer.phar \  
&& mv composer.phar /usr/local/bin/composer \  
&& chmod +x /usr/local/bin/composer \  
&& curl -sSLO https://deployer.org/deployer.phar \  
&& mv deployer.phar /usr/local/bin/dep \  
&& chmod +x /usr/local/bin/dep \  
&& curl -sSLO http://static.phpmd.org/php/latest/phpmd.phar \  
&& mv phpmd.phar /usr/local/bin/phpmd \  
&& chmod +x /usr/local/bin/phpmd \  
&& curl -sSOL https://squizlabs.github.io/PHP_CodeSniffer/phpcs.phar \  
&& mv phpcs.phar /usr/local/bin/phpcs \  
&& chmod +x /usr/local/bin/phpcs \  
&& curl -sSOL https://squizlabs.github.io/PHP_CodeSniffer/phpcbf.phar \  
&& mv phpcbf.phar /usr/local/bin/phpcbf \  
&& chmod +x /usr/local/bin/phpcbf \  
&& curl -sSOL https://phar.phpunit.de/phpunit.phar \  
&& mv phpunit.phar /usr/local/bin/phpunit \  
&& chmod +x /usr/local/bin/phpunit \  
&& curl -sSOL http://get.sensiolabs.org/sami.phar \  
&& mv sami.phar /usr/local/bin/sami \  
&& chmod +x /usr/local/bin/sami \  
&& curl -sSOL
https://github.com/Behat/Behat/releases/download/v$BEHAT_VERSION/behat.phar \  
&& mv behat.phar /usr/local/bin/behat \  
&& chmod +x /usr/local/bin/behat \  
&& curl -sSOL
https://github.com/phpspec/phpspec/releases/download/4.0.2/phpspec.phar \  
&& mv phpspec.phar /usr/local/bin/phpspec \  
&& chmod +x /usr/local/bin/phpspec  
  
RUN pecl install xdebug-2.5.5 \  
&& docker-php-ext-enable xdebug  
  
RUN apt-get purge -y --auto-remove -o
APT::AutoRemove::RecommendsImportant=false $buildDeps  
  
RUN mkdir /srv/http  
  
ADD php.ini /usr/local/etc/php/php.ini  
  
ADD known_hosts /root/.ssh/known_hosts  
ADD id_rsa /root/.ssh/id_rsa  
  
WORKDIR /srv/http  

