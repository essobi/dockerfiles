FROM php:7.1-cli  
  
RUN echo "memory_limit=-1" > $PHP_INI_DIR/conf.d/memory-limit.ini \  
&& echo "date.timezone=${PHP_TIMEZONE:-Europe/Moscow}" >
"$PHP_INI_DIR/conf.d/date_timezone.ini"  
  
RUN ln -fs /usr/share/zoneinfo/${PHP_TIMEZONE:-Europe/Moscow} /etc/localtime  
ENV DEV_PACKAGES="libfreetype6-dev libjpeg62-turbo-dev libmcrypt-dev
libpng12-dev libbz2-dev \  
libxslt-dev libldap2-dev libz-dev libmemcached-dev libtidy-dev
libcurl4-openssl-dev libc-client2007e-dev \  
libkrb5-dev libmagickwand-6.q16-dev libxml2-dev libedit-dev libicu-dev
librecode-dev libxslt1-dev \  
libyaml-dev python-pip python2.7-dev" \  
DEBIAN_FRONTEND="noninteractive"  
RUN apt-get update -q && \  
apt-get install -qy --no-install-recommends \  
curl \  
git \  
subversion \  
unzip \  
wget \  
openssh-client \  
libimage-exiftool-perl \  
libtidy-0.99 \  
libc-client2007e \  
libmagickwand-6.q16-2 \  
libmcrypt4 \  
libmemcached11 \  
librecode0 \  
libmemcachedutil2 \  
libxslt1.1 \  
libyaml-0-2 \  
python2.7 \  
build-essential \  
locales locales-all \  
&& rm -r /var/lib/apt/lists/*  
  
ENV LANG='en_US.UTF-8' \  
LANGUAGE='en_US.UTF-8' \  
LC_ALL='en_US.UTF-8'  
RUN apt-get update -q \  
&& apt-get install -qy --no-install-recommends ${DEV_PACKAGES} \  
&& CFLAGS="-I/usr/src/php" docker-php-ext-install bcmath mcrypt zip bz2
mbstring pcntl xsl tidy curl \  
pdo pdo_mysql dom xml xmlreader xmlrpc xmlwriter simplexml readline soap
tokenizer \  
ctype calendar sysvmsg sysvsem sysvshm shmop gettext fileinfo sockets opcache
\  
&& docker-php-ext-configure recode --with-recode && docker-php-ext-install
recode \  
&& docker-php-ext-configure exif --enable-exif && docker-php-ext-install exif
\  
&& docker-php-ext-configure intl --enable-intl && docker-php-ext-install intl
\  
&& docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-
dir=/usr/include/ \  
&& docker-php-ext-install gd \  
&& docker-php-ext-configure imap --with-kerberos --with-imap-ssl && docker-
php-ext-install imap \  
&& echo 'autodetect' | pecl install -o -f imagick && docker-php-ext-enable
imagick \  
&& echo 'no' | pecl install -o -f memcached && docker-php-ext-enable memcached
\  
&& pecl install -o -f igbinary msgpack && docker-php-ext-enable igbinary
msgpack \  
&& pecl install -o -f redis && docker-php-ext-enable redis \  
&& wget -q http://pecl.php.net/get/translit -O /tmp/translit && pecl install
-o -f /tmp/translit && docker-php-ext-enable translit \  
&& pecl install xdebug && docker-php-ext-enable xdebug \  
&& pip install awscli --upgrade \  
&& apt-get purge -y --auto-remove -o
APT::AutoRemove::RecommendsImportant=false ${DEV_PACKAGES} \  
&& rm -r /var/lib/apt/lists/* /tmp/translit  
  
  
ENV PATH="/composer/vendor/bin:$PATH" \  
COMPOSER_ALLOW_SUPERUSER=1 \  
COMPOSER_HOME="/composer" \  
COMPOSER_VERSION="1.5.2"  
RUN curl -s -f -L -o /tmp/installer.php
https://raw.githubusercontent.com/composer/getcomposer.org/da290238de6d63faace0343efbdd5aa9354332c5/web/installer
\  
&& php -r " \  
\$signature =
'669656bab3166a7aff8a7506b8cb2d1c292f042046c5a994c43155c0be6190fa0355160742ab2e1c88d40d5be660b410';
\  
\$hash = hash('SHA384', file_get_contents('/tmp/installer.php')); \  
if (!hash_equals(\$signature, \$hash)) { \  
unlink('/tmp/installer.php'); \  
echo 'Integrity check failed, installer is either corrupt or worse.' .
PHP_EOL; \  
exit(1); \  
}" \  
&& php /tmp/installer.php --no-ansi --install-dir=/usr/bin --filename=composer
--version=${COMPOSER_VERSION} \  
&& rm /tmp/installer.php \  
&& composer --ansi --version --no-interaction  
  
RUN composer require -d /composer --ansi --no-interaction phpunit/php-invoker
phpunit/dbunit  
  
RUN git config --global user.email "yourci@gmail.com" && git config --global
user.name "YourCI"  
  
ENV NODE_VERSION=8.9.1 \  
NPM_CONFIG_LOGLEVEL=info  
  
RUN curl -SLO "https://nodejs.org/dist/v$NODE_VERSION/node-v$NODE_VERSION-
linux-x64.tar.xz" \  
&& tar -xJf "node-v$NODE_VERSION-linux-x64.tar.xz" -C /usr/local \--strip-
components=1 \  
&& rm "node-v$NODE_VERSION-linux-x64.tar.xz" \  
&& ln -s /usr/local/bin/node /usr/local/bin/nodejs \  
&& npm install --global gulp-cli \  
&& chown -R root. /usr/local/lib  
  
RUN ln -sf /usr/bin/python2.7 /usr/bin/python  
  
RUN git clone \--recursive https://github.com/sass/node-sass.git /root/node-
sass \  
&& cd /root/node-sass && npm install && node scripts/build -f \  
&& mkdir -p /usr/local/lib/node-sass/ \  
&& cp vendor/linux-x64*/binding.node /usr/local/lib/node-sass/ \  
&& rm -rf /root/node-sass  
  
ENV SASS_BINARY_PATH=/usr/local/lib/node-sass/binding.node  
  
ENV DOCKER_VER=17.05.0-ce  
  
RUN curl -s -L -o "/tmp/docker-$DOCKER_VER.tgz"
"https://get.docker.com/builds/Linux/x86_64/docker-$DOCKER_VER.tgz" \  
&& tar -xz -C /tmp -f "/tmp/docker-$DOCKER_VER.tgz" \  
&& mv /tmp/docker/* /usr/bin  
  
WORKDIR /app  
  
#USER www-data  

