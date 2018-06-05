FROM debian:wheezy  
  
MAINTAINER Berry Goudswaard <info@noregression.nl>  
  
ENV EXTRA_DEPS "libmagickwand5"  
ENV PHP_VERSION 5.3.29  
ENV PHP_INI_DIR /usr/local/etc/php  
ENV PHP_URL "http://museum.php.net/php5/php-$PHP_VERSION.tar.bz2"  
ENV PHP_EXTRA_EXT ""  
ENV PHP_EXTRA_BUILD_DEPS ""  
ENV XDEBUG_BRANCH "xdebug_2_2"  
ENV HOME /home/ci  
  
# persistent / runtime deps  
RUN export DEBIAN_FRONTEND=noninteractive \  
&& apt-get update \  
&& apt-get install -y \  
ca-certificates \  
curl \  
git \  
libc-client2007e \  
libmcrypt4 \  
libpcre3 \  
librecode0 \  
libsqlite3-0 \  
libxml2 \  
mysql-server \  
ssh-client \  
rsync \  
$EXTRA_DEPS \  
\--no-install-recommends \  
&& rm -r /var/lib/apt/lists/*  
  
# phpize deps  
RUN export DEBIAN_FRONTEND=noninteractive \  
&& apt-get update \  
&& apt-get install -y \  
autoconf \  
file \  
g++ \  
gcc \  
libc-dev \  
libmcrypt-dev \  
make \  
pkg-config \  
re2c \  
\--no-install-recommends \  
&& rm -r /var/lib/apt/lists/*  
  
RUN buildDeps=" \  
bzip2 \  
libcurl4-openssl-dev \  
libpcre3-dev \  
libreadline6-dev \  
librecode-dev \  
libsqlite3-dev \  
libssl-dev \  
libxml2-dev \  
libc-client-dev \  
libc-client2007e-dev \  
libc-dev \  
libjpeg-dev \  
libkrb5-dev \  
libpng-dev \  
$PHP_EXTRA_BUILD_DEPS \  
" \  
&& export DEBIAN_FRONTEND=noninteractive \  
&& apt-get update \  
&& apt-get install -y $buildDeps --no-install-recommends \  
&& mkdir -p $PHP_INI_DIR/conf.d \  
&& curl -SL "$PHP_URL" -o php.tar.bz2 \  
&& mkdir -p /usr/src/php \  
&& tar -xof php.tar.bz2 -C /usr/src/php --strip-components=1 \  
&& rm php.tar.bz2* \  
&& cd /usr/src/php \  
&& ./configure \  
\--disable-cgi \  
\--enable-bcmath \  
\--enable-libxml \  
\--enable-mysqlnd \  
\--enable-mbstring \  
\--enable-soap \  
\--enable-zip \  
\--with-config-file-path="$PHP_INI_DIR" \  
\--with-config-file-scan-dir="$PHP_INI_DIR/conf.d" \  
\--with-curl \  
\--with-gd \  
\--with-imap \  
\--with-imap-ssl \  
\--with-jpeg-dir=/usr/lib \  
\--with-kerberos \  
\--with-mcrypt \  
\--with-openssl \  
\--with-pdo-mysql=mysqlnd \  
\--with-mysql-sock=/var/run/mysqld/mysqld.sock \  
\--with-readline \  
\--with-zlib \  
$PHP_EXTRA_EXT \  
&& make \  
&& make install \  
&& make clean \  
&& echo 'pdo_mysql.default_socket=/var/run/mysqld/mysqld.sock' >
/usr/local/etc/php/conf.d/ext-pd_mysql.ini \  
&& echo 'date.timezone = UTC' > /usr/local/etc/php/conf.d/date.timezone.ini \  
&& rm -r /var/lib/apt/lists/* \  
&& apt-get purge -y --auto-remove -o
APT::AutoRemove::RecommendsImportant=false -o
APT::AutoRemove::SuggestsImportant=false $buildDeps  
  
RUN git clone --branch $XDEBUG_BRANCH git://github.com/xdebug/xdebug.git
/tmp/xdebug \  
&& cd /tmp/xdebug \  
&& phpize \  
&& ./configure --enable-xdebug \  
&& make \  
&& mkdir -p /usr/src/php/ext/xdebug \  
&& cp /tmp/xdebug/modules/xdebug.so /usr/src/php/ext/xdebug/xdebug.so \  
&& rm -Rf /tmp/xdebug \  
&& echo 'zend_extension=/usr/src/php/ext/xdebug/xdebug.so' >
/usr/local/etc/php/conf.d/ext-xdebug.ini  
  
RUN export DEBIAN_FRONTEND=noninteractive \  
&& apt-get update \  
&& apt-get install -y \  
libmagickwand-dev \  
\--no-install-recommends \  
&& git clone git://github.com/mkoppanen/imagick.git /tmp/imagick \  
&& cd /tmp/imagick \  
&& phpize \  
&& ./configure \  
&& make \  
&& mkdir -p /usr/src/php/ext/imagick \  
&& cp /tmp/imagick/modules/imagick.so /usr/src/php/ext/imagick/imagick.so \  
&& rm -Rf /tmp/imagick \  
&& echo 'extension=/usr/src/php/ext/imagick/imagick.so' >
/usr/local/etc/php/conf.d/ext-imagick.ini \  
&& apt-get purge -y --auto-remove -o
APT::AutoRemove::RecommendsImportant=false -o
APT::AutoRemove::SuggestsImportant=false libmagickwand-dev  
  
RUN useradd -ms /bin/bash ci \  
&& echo '#!/bin/bash' > /tmp/run.sh \  
&& echo 'service mysql start \' >> /tmp/run.sh \  
&& echo '&& chown ci:ci -R $HOME \' >> /tmp/run.sh \  
&& echo '&& su ci -c "export PATH=$PATH && /tmp/ci.sh"' >> /tmp/run.sh \  
&& chmod +x /tmp/run.sh  
  
RUN apt-get update \  
&& mkdir $HOME/bin \  
&& curl -sS https://getcomposer.org/installer | php -- --install-dir=$HOME/bin
--filename=composer \  
&& $HOME/bin/composer global require \  
phpunit/phpunit \  
sebastian/phpcpd \  
squizlabs/php_codesniffer \  
noregression/coverage-reporter  
  
WORKDIR $HOME/project  
  
ENV PATH $HOME/bin:$HOME/.composer/vendor/bin:$PATH  
  
CMD /tmp/run.sh  
  

