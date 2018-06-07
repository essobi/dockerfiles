#  
# - Base nginx / php-fpm image  
#  
FROM ubuntu:14.04  
MAINTAINER JINWOO <jinwoo@yellotravel.com>  
  
#  
# Prepare the container  
#  
RUN ln -sf /usr/share/zoneinfo/Asia/Seoul /etc/localtime  
  
ENV PHP_VERSION 5.6.22  
RUN echo "PHP version = ${PHP_VERSION}"  
  
ENV PHP_VERSION 5.6.22  
ENV DOCKERIZE_VERSION v0.2.0  
ENV PHP_LIB redis-2.2.8 yaml-1.2.0 amqp-1.7.0 memcached-2.2.0 apcu-4.0.11  
ENV PHALCON_VER 2.0.12  
  
ENV PHP_INI_DIR /etc/php  
  
ENV PHP_EXTRA_CONFIGURE_ARGS --enable-fpm --with-fpm-user=www-data --with-fpm-
group=www-data --with-curl --with-iconv \  
\--with-libdir=lib64 --with-openssl --enable-opcache \  
\--with-gd \  
\--with-mysql \  
\--with-mysqli \  
\--with-pdo-mysql \  
\--enable-sockets \  
\--disable-cgi \  
\--enable-mysqlnd \  
\--enable-bcmath \  
\--with-bz2 \  
\--enable-calendar \  
\--with-curl \  
\--with-gd \  
\--with-jpeg-dir \  
\--enable-gd-native-ttf \  
\--enable-mbstring \  
\--with-mcrypt \  
\--with-mysqli \  
\--with-pdo-mysql \  
\--enable-pcntl \  
\--with-openssl \  
\--with-xsl \  
\--with-readline \  
\--with-zlib \  
\--enable-intl \  
\--enable-zip  
  
  
ENV PHP_BUILD_DEPS bzip2 \  
re2c \  
file \  
libbz2-dev \  
libcurl4-openssl-dev \  
libjpeg-dev \  
libmcrypt-dev \  
libpng12-dev \  
libreadline6-dev \  
libssl-dev \  
libxslt1-dev \  
libxml2-dev \  
mysql-client \  
libmysqlclient-dev\  
libyaml-dev \  
librabbitmq-dev \  
libsasl2-dev \  
libicu-dev \  
g++  
  
  
# ENV LANG en_US.UTF-8  
# ENV LC_ALL en_US.UTF-8  
RUN sed -i 's/archive.ubuntu.com/ftp.daum.net/g' /etc/apt/sources.list  
  
RUN apt-get update && apt-get install -y ca-certificates curl libxml2 autoconf
\  
gcc libc-dev make pkg-config \  
runit nano less tmux wget git \  
$PHP_BUILD_DEPS $PHP_EXTRA_BUILD_DEPS \  
\--no-install-recommends && rm -r /var/lib/apt/lists/*  
  
ENV PHP7_KEY "1A4E8B7277C42E53DBA9C7B9BCAA30EA9C0D5763
6E4F6AB321FDC07F2C332E3AC2BF0BC433CFC8B3"  
ENV PHP5_KEY "6E4F6AB321FDC07F2C332E3AC2BF0BC433CFC8B3
0BD78B5F97500D450838F95DFE857D9A90D90EC1"  
RUN gpg --keyserver pool.sks-keyservers.net --recv-keys $PHP5_KEY \  
&& mkdir -p $PHP_INI_DIR/conf.d \  
&& set -x \  
&& curl -SL "http://php.net/get/php-$PHP_VERSION.tar.bz2/from/this/mirror" -o
php.tar.bz2 \  
&& curl -SL "http://php.net/get/php-$PHP_VERSION.tar.bz2.asc/from/this/mirror"
-o php.tar.bz2.asc \  
&& gpg --verify php.tar.bz2.asc \  
&& mkdir -p /usr/src/php \  
&& tar -xof php.tar.bz2 -C /usr/src/php --strip-components=1 \  
&& rm php.tar.bz2* \  
&& cd /usr/src/php \  
&& ./configure \  
\--sysconfdir="$PHP_INI_DIR" \  
\--with-config-file-path="$PHP_INI_DIR" \  
\--with-config-file-scan-dir="$PHP_INI_DIR/conf.d" \  
$PHP_EXTRA_CONFIGURE_ARGS \  
&& make -j"$(nproc)" \  
&& make install \  
&& { find /usr/local/bin /usr/local/sbin -type f -executable -exec strip
--strip-all '{}' \+ || true; } \  
&& apt-get purge -y --auto-remove -o
APT::AutoRemove::RecommendsImportant=false -o
APT::AutoRemove::SuggestsImportant=false $buildDeps \  
&& make clean  
  
RUN userdel www-data && groupadd -r www-data -g 433 && \  
mkdir /home/www-data && \  
mkdir -p /var/www && \  
useradd -u 431 -r -g www-data -d /home/www-data -s /sbin/nologin -c "Docker
image user for web application" www-data && \  
chown -R www-data:www-data /home/www-data /var/www && \  
chmod 700 /home/www-data && \  
chmod 711 /var/www  
  
  
COPY files /  
  
RUN cp /usr/src/php/php.ini-production ${PHP_INI_DIR}/php.ini  
RUN sh -c "echo 'date.timezone = asia/seoul' >> ${PHP_INI_DIR}/php.ini"  
RUN sed -i 's/short_open_tag = Off/short_open_tag = On/g'
${PHP_INI_DIR}/php.ini  
  
RUN mkdir -p /usr/src/pecl && cd /usr/src/pecl \  
&& wget
https://github.com/phalcon/cphalcon/archive/phalcon-v${PHALCON_VER}.tar.gz \  
&& tar zxvf phalcon-v${PHALCON_VER}.tar.gz && cd /usr/src/pecl/cphalcon-
phalcon-v${PHALCON_VER}/build \  
&& ./install \  
&& echo "extension=phalcon.so" > $PHP_INI_DIR/conf.d/phalcon.ini \  
&& wget
https://launchpad.net/libmemcached/1.0/1.0.18/+download/libmemcached-1.0.18.tar.gz
\  
&& tar xzf libmemcached-1.0.18.tar.gz \  
&& cd libmemcached-1.0.18 \  
&& ./configure --enable-sasl \  
&& make -j"$(nproc)" \  
&& sudo make install \  
&& wget
http://nz.archive.ubuntu.com/ubuntu/pool/universe/libr/librabbitmq/librabbitmq4_0.7.1-1_amd64.deb
\  
&& sudo dpkg -i librabbitmq4_0.7.1-1_amd64.deb \  
&& wget
http://nz.archive.ubuntu.com/ubuntu/pool/universe/libr/librabbitmq/librabbitmq-
dev_0.7.1-1_amd64.deb \  
&& sudo dpkg -i librabbitmq-dev_0.7.1-1_amd64.deb \  
&& rm -rf *.deb libmemcached-1.0.18* \  
&& rm -rf /usr/src/pecl/*  
  
# Install composer  
RUN bash -c "wget http://getcomposer.org/composer.phar && chmod +x
composer.phar && mv composer.phar /usr/local/bin/composer"  
# Install PHPUnit  
RUN bash -c "wget https://phar.phpunit.de/phpunit.phar && chmod +x
phpunit.phar && mv phpunit.phar /usr/local/bin/phpunit"  
  
RUN wget
https://github.com/jwilder/dockerize/releases/download/$DOCKERIZE_VERSION/dockerize-
linux-amd64-$DOCKERIZE_VERSION.tar.gz \  
&& tar -C /usr/local/bin -xzvf dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz
\  
&& rm -f dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz  
  
RUN bash -c "/usr/local/bin/docker-pecl-install ${PHP_LIB}" && rm -rf
/usr/src/pecl/*  
  
#  
# Docker properties  
#  
  
VOLUME ["/var/www", "/etc/php"]  
  
EXPOSE 9000  
  
#CMD ["/usr/local/sbin/runsvdir-init"]  
CMD ["/run.sh"]  

