FROM php:5.6-apache  
MAINTAINER gpapkala <grzegorz@maou.pl>  
  
# Install all required extensions  
RUN requirements="libmcrypt-dev g++ libicu-dev libmcrypt4 libpng12-0
libpng12-dev libicu52 mysql-client" \  
&& apt-get update && apt-get install -y $requirements \  
&& docker-php-ext-install pdo_mysql \  
&& docker-php-ext-install mcrypt \  
&& docker-php-ext-install mbstring \  
&& docker-php-ext-install intl \  
&& docker-php-ext-install gd \  
&& requirementsToRemove="libmcrypt-dev g++ libicu-dev" \  
&& apt-get purge --auto-remove -y $requirementsToRemove \  
&& rm -rf /var/lib/apt/lists/*  
  
# Install composer  
RUN curl -sSL https://getcomposer.org/installer | php \  
&& mv composer.phar /usr/local/bin/composer \  
&& apt-get update \  
&& apt-get install -y zlib1g-dev git \  
&& docker-php-ext-install zip \  
&& apt-get purge -y --auto-remove zlib1g-dev \  
&& rm -rf /var/lib/apt/lists/*  
  
# Run xdebug installation.  
RUN mkdir -p /usr/src/php/ext/ && \  
curl -L http://pecl.php.net/get/xdebug-2.3.3.tgz >>
/usr/src/php/ext/xdebug.tgz && \  
tar -xf /usr/src/php/ext/xdebug.tgz -C /usr/src/php/ext/ && \  
rm /usr/src/php/ext/xdebug.tgz && \  
docker-php-ext-install xdebug-2.3.3 && \  
docker-php-ext-install pcntl && \  
php -m  
  
# Globally install phpunit and phpcs  
RUN composer global require 'cakephp/cakephp-codesniffer:dev-master' \  
&& composer global require 'phpunit/phpunit' \  
&& export PATH=~/.composer/vendor/bin:$PATH  
  
# install node/npm  
RUN groupadd --gid 1000 node \  
&& useradd --uid 1000 --gid node --shell /bin/bash --create-home node  
  
# gpg keys listed at https://github.com/nodejs/node#release-team  
RUN set -ex \  
&& for key in \  
9554F04D7259F04124DE6B476D5A82AC7E37093B \  
94AE36675C464D64BAFA68DD7434390BDBE9B9C5 \  
FD3A5288F042B6850C66B31F09FE44734EB7990E \  
71DCFD284A79C3B38668286BC97EC7A07EDE3FC1 \  
DD8F2338BAE7501E3DD5AC78C273792F7D83545D \  
B9AE9905FFD7803F25714661B63B535A4C206CA9 \  
C4F0DFFF4E8C1A8236409D08E73BC641CC11F4C8 \  
56730D5401028683275BD23C23EFEFE93C4CFFFE \  
; do \  
gpg --keyserver pgp.mit.edu --recv-keys "$key" || \  
gpg --keyserver keyserver.pgp.com --recv-keys "$key" || \  
gpg --keyserver ha.pool.sks-keyservers.net --recv-keys "$key" ; \  
done  
  
ENV NPM_CONFIG_LOGLEVEL info  
ENV NODE_VERSION 8.7.0  
RUN ARCH= && dpkgArch="$(dpkg --print-architecture)" \  
&& case "${dpkgArch##*-}" in \  
amd64) ARCH='x64';; \  
ppc64el) ARCH='ppc64le';; \  
*) echo "unsupported architecture"; exit 1 ;; \  
esac \  
&& curl -SLO "https://nodejs.org/dist/v$NODE_VERSION/node-v$NODE_VERSION-
linux-$ARCH.tar.xz" \  
&& curl -SLO --compressed
"https://nodejs.org/dist/v$NODE_VERSION/SHASUMS256.txt.asc" \  
&& gpg --batch --decrypt --output SHASUMS256.txt SHASUMS256.txt.asc \  
&& grep " node-v$NODE_VERSION-linux-$ARCH.tar.xz\$" SHASUMS256.txt | sha256sum
-c - \  
&& tar -xJf "node-v$NODE_VERSION-linux-$ARCH.tar.xz" -C /usr/local \--strip-
components=1 \  
&& rm "node-v$NODE_VERSION-linux-$ARCH.tar.xz" SHASUMS256.txt.asc
SHASUMS256.txt \  
&& ln -s /usr/local/bin/node /usr/local/bin/nodejs  
  
# Enable apache mods  
RUN a2enmod rewrite  
  
RUN usermod -u 1001 www-data  

