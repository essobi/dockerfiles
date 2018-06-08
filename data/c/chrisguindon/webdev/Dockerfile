###  
# Copyright (c) 2017 Eclipse Foundation and others.  
#  
# This program and the accompanying materials are made  
# available under the terms of the Eclipse Public License 2.0  
# which accompanies this distribution, and is available  
# at http://eclipse.org/legal/epl-2.0  
###  
  
FROM php:7.0.25-apache  
MAINTAINER Christopher Guindon <chris.guindon@eclipse-foundation.org>  
  
# Setup home-data root  
WORKDIR /home  
  
RUN set -ex \  
&& buildDeps=' \  
libjpeg62-turbo-dev \  
libpng12-dev \  
libpq-dev \  
libldap2-dev \  
libmcrypt-dev \  
libz-dev \  
libmemcached-dev \  
' \  
&& apt-get update && apt-get install -y --no-install-recommends $buildDeps
curl git libmcrypt4 \  
&& rm -rf /var/lib/apt/lists/* \  
&& docker-php-ext-configure gd \  
\--with-jpeg-dir=/usr \  
\--with-png-dir=/usr \  
&& docker-php-ext-install -j "$(nproc)" bcmath gd mbstring pdo pdo_mysql
pdo_pgsql mysqli zip mcrypt \  
&& docker-php-ext-configure ldap --with-libdir=lib/x86_64-linux-gnu/ \  
&& docker-php-ext-install ldap \  
&& pecl install oauth-2.0.2 \  
&& echo "extension=oauth.so" >> $PHP_INI_DIR/conf.d/oauth.ini \  
&& pecl install xdebug \  
&& echo "extension=xdebug.so" >> $PHP_INI_DIR/conf.d/xdebug.ini \  
&& git clone https://github.com/php/pecl-php-uploadprogress.git /tmp/php-
uploadprogress \  
&& cd /tmp/php-uploadprogress \  
&& phpize \  
&& ./configure \--prefix=/usr \  
&& make \  
&& make install \  
&& echo 'extension=uploadprogress.so' > $PHP_INI_DIR/conf.d/uploadprogress.ini
\  
&& rm -rf /tmp/* \  
&& cd /home \  
&& pecl install -o -f redis \  
&& rm -rf /tmp/pear \  
&& docker-php-ext-enable redis \  
&& docker-php-ext-enable mcrypt \  
&& pecl install memcached-3.0.3 \  
&& docker-php-ext-enable memcached \  
&& pecl install apcu-5.1.8 \  
&& echo extension=apcu.so > $PHP_INI_DIR/conf.d/apcu.ini \  
&& version=$(php -r "echo PHP_MAJOR_VERSION.PHP_MINOR_VERSION;") \  
&& curl -A "Docker" -o /tmp/blackfire-probe.tar.gz -D - -L -s
https://blackfire.io/api/v1/releases/probe/php/linux/amd64/$version \  
&& tar zxpf /tmp/blackfire-probe.tar.gz -C /tmp \  
&& mv /tmp/blackfire-*.so $(php -r "echo
ini_get('extension_dir');")/blackfire.so \  
&& printf
"extension=blackfire.so\nblackfire.agent_socket=tcp://blackfire:8707\n" >
$PHP_INI_DIR/conf.d/blackfire.ini \  
&& apt-mark manual \  
libjpeg62-turbo \  
libpq5 \  
&& apt-get purge -y --auto-remove $buildDeps \  
&& a2enmod alias authz_host deflate dir expires headers mime php7 rewrite
setenvif \  
&& git clone --recursive git://github.com/chrisguindon/eclipsefdn-home-
data.git /home/data \  
&& chown -R www-data:www-data /home/data/  
  
# Setup web root  
WORKDIR /var/www/html  
COPY index.php /var/www/html  
RUN chown -R www-data:www-data /var/www/html

