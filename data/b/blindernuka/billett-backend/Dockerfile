FROM php:5.6-fpm  
MAINTAINER Henrik Steen <henrist@henrist.net>  
  
ENV SIMPLESAMLPHP_VERSION 1.14.7  
ENV SIMPLESAMLPHP_SHA256
a7a24d4dc89819f7e53141b38ae36b092a5c1fc9cb2e3cee253c765e5942be52  
  
ENV GOSU_VERSION 1.9  
RUN \  
# system packages  
apt-get update \  
&& apt-get install -y --no-install-recommends \  
curl \  
git \  
libfreetype6-dev \  
libjpeg62-turbo-dev \  
libmcrypt-dev \  
libpng12-dev \  
unzip \  
wget \  
&& rm -rf /var/lib/apt/lists/* \  
\  
# gosu in entrypoint  
&& dpkgArch="$(dpkg --print-architecture | awk -F- '{ print $NF }')" \  
&& wget -O /usr/local/bin/gosu
"https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-$dpkgArch"
\  
&& wget -O /usr/local/bin/gosu.asc
"https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-$dpkgArch.asc"
\  
&& export GNUPGHOME="$(mktemp -d)" \  
&& gpg --keyserver ha.pool.sks-keyservers.net --recv-keys
B42F6819007F00F88E364FD4036A9C25BF357DD4 \  
&& gpg --batch --verify /usr/local/bin/gosu.asc /usr/local/bin/gosu \  
&& rm -r "$GNUPGHOME" /usr/local/bin/gosu.asc \  
&& chmod +x /usr/local/bin/gosu \  
&& gosu nobody true \  
\  
# php extensions  
&& docker-php-ext-install -j$(nproc) mcrypt pdo_mysql \  
&& docker-php-ext-configure gd --with-freetype-dir=/usr/include --with-jpeg-
dir=/usr/include \  
&& docker-php-ext-install -j$(nproc) gd \  
\  
# set up composer  
&& php -r "copy('https://getcomposer.org/installer', '/tmp/composer-
setup.php');" \  
&& php -r "if (hash_file('SHA384', '/tmp/composer-setup.php') ===
'e115a8dc7871f15d853148a7fbac7da27d6c0030b848d9b3dc09e2a0388afed865e6a3d6b3c0fad45c48e2b5fc1196ae')
{ echo 'Installer verified'; } else { echo 'Installer corrupt';
unlink('/tmp/composer-setup.php'); } echo PHP_EOL;" \  
&& php /tmp/composer-setup.php --install-dir=/usr/local/bin
--filename=composer \  
&& php -r "unlink('/tmp/composer-setup.php');" \  
\  
# simplesamlphp  
&& mkdir /var/simplesamlphp \  
&& cd /var/simplesamlphp \  
&& curl -fSL
"https://github.com/simplesamlphp/simplesamlphp/releases/download/v$SIMPLESAMLPHP_VERSION/simplesamlphp-$SIMPLESAMLPHP_VERSION.tar.gz"
-o simplesamlphp.tar.gz \  
&& echo "$SIMPLESAMLPHP_SHA256 *simplesamlphp.tar.gz" | sha256sum -c - \  
&& tar --strip-components=1 -zxf simplesamlphp.tar.gz \  
&& rm simplesamlphp.tar.gz \  
\  
# billett  
&& mkdir -p /var/billett/cache \  
&& mkdir -p /var/billett/logs \  
&& mkdir -p /var/billett/meta \  
&& mkdir -p /var/billett/sessions \  
&& mkdir -p /var/billett/views \  
&& chown -R www-data:www-data /var/billett /var/www /var/www/html  
  
# configure simplesamlphp  
COPY simplesamlphp/config.override.php /var/simplesamlphp/config/  
COPY simplesamlphp/authsources.php /var/simplesamlphp/config/  
COPY simplesamlphp/saml20-idp-remote.php /var/simplesamlphp/metadata/  
RUN cd /var/simplesamlphp && tail -n +2 config/config.override.php
>>config/config.php  
  
COPY composer.* /var/www/html/  
  
# create directories that are scanned on composer install  
# this is later replaced with new source, but we need this  
# here to have cache of composer modules to avoid cache miss  
# in case only our code is updated and not dependencies  
USER www-data  
RUN mkdir -p app/commands \  
app/controllers \  
app/models \  
app/database/migrations \  
app/database/seeds \  
app/tests \  
app/src \  
&& echo -e '#!/usr/bin/env php\n<?php' >artisan \  
&& echo -e '#!/usr/bin/env php\n<?php' >app/tests/TestCase.php \  
&& chmod +x artisan \  
&& composer install \  
&& mv vendor /var/www/html-vendor \  
&& ln -s /var/www/html-vendor /var/www/html/vendor  
  
COPY . /var/www/html/  
  
# we run composer install again so the post process commands  
# are run  
RUN composer install  
  
USER root  
COPY container/entrypoint.sh /entrypoint.sh  
COPY container/dev.sh /dev.sh  
  
VOLUME ["/var/simplesamlphp", "/var/billett"]  
ENTRYPOINT ["/entrypoint.sh"]  
CMD ["php-fpm"]  

