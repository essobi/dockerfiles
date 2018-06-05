FROM php:5.6-apache  
  
MAINTAINER Kersten Burkhardt "kersten@beyond-agentur.com"  
  
RUN echo "Europe/Berlin" > /etc/timezone && \  
dpkg-reconfigure -f noninteractive tzdata  
  
ADD etc/locale.gen /etc/locale.gen  
RUN apt-get update && apt-get -yq --force-yes install locales \  
&& rm -r /var/lib/apt/lists/* \  
&& locale-gen \  
&& DEBIAN_FRONTEND=noninteractive dpkg-reconfigure locales  
  
RUN apt-get update \  
&& apt-get install -y \  
imagemagick \  
graphicsmagick \  
zip \  
unzip \  
wget \  
curl \  
git \  
mysql-client \  
moreutils \  
dnsutils \  
openssl \  
grep \  
nano \  
cron \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer  
  
RUN docker-php-ext-install -j$(nproc) bcmath  
  
RUN buildRequirements="libbz2-dev" \  
&& apt-get update && apt-get install -y ${buildRequirements} \  
&& docker-php-ext-install -j$(nproc) bz2 \  
&& apt-get purge -y ${buildRequirements} \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN docker-php-ext-install -j$(nproc) calendar  
  
RUN docker-php-ext-install -j$(nproc) ctype  
  
RUN buildRequirements="libcurl4-openssl-dev" \  
&& apt-get update && apt-get install -y ${buildRequirements} \  
&& docker-php-ext-install -j$(nproc) curl \  
&& apt-get purge -y ${buildRequirements} \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN buildRequirements="libxml2-dev" \  
&& apt-get update && apt-get install -y ${buildRequirements} \  
&& docker-php-ext-install -j$(nproc) dom \  
&& apt-get purge -y ${buildRequirements} \  
&& rm -rf /var/lib/apt/lists/*  
# && docker-php-ext-install -j$(nproc) enchant \  
RUN docker-php-ext-install -j$(nproc) exif  
  
RUN docker-php-ext-install -j$(nproc) fileinfo  
  
# && docker-php-ext-install -j$(nproc) filter \  
RUN buildRequirements="libssl-dev" \  
&& apt-get update && apt-get install -y ${buildRequirements} \  
&& docker-php-ext-install -j$(nproc) ftp \  
&& apt-get purge -y ${buildRequirements} \  
&& rm -rf /var/lib/apt/lists/*  
# gd  
RUN buildRequirements="libpng12-dev libjpeg62-turbo-dev libfreetype6-dev" \  
&& apt-get update && apt-get install -y ${buildRequirements} \  
&& docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-
dir=/usr/include/ \  
&& docker-php-ext-install -j$(nproc) gd \  
&& apt-get purge -y ${buildRequirements} \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN docker-php-ext-install -j$(nproc) gettext \  
&& docker-php-ext-install -j$(nproc) hash  
  
RUN docker-php-ext-install -j$(nproc) iconv  
  
RUN buildRequirements="libc-client2007e-dev libkrb5-dev" \  
&& apt-get update && apt-get install -y ${buildRequirements} \  
&& docker-php-ext-configure imap --with-kerberos --with-imap-ssl \  
&& docker-php-ext-install -j$(nproc) imap \  
&& apt-get purge -y ${buildRequirements} \  
&& runtimeRequirements="libc-client2007e" \  
&& apt-get install -y --auto-remove ${runtimeRequirements} \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN buildRequirements="libicu-dev g++" \  
&& apt-get update && apt-get install -y ${buildRequirements} \  
&& docker-php-ext-install -j$(nproc) intl \  
&& apt-get purge -y ${buildRequirements} \  
&& runtimeRequirements="libicu52" \  
&& apt-get install -y --auto-remove ${runtimeRequirements} \  
&& rm -rf /var/lib/apt/lists/*  
# imagick  
RUN runtimeRequirements="libmagickwand-6.q16-dev --no-install-recommends" \  
&& apt-get update && apt-get install -y ${runtimeRequirements} \  
&& ln -s /usr/lib/x86_64-linux-gnu/ImageMagick-6.8.9/bin-Q16/MagickWand-config
/usr/bin/ \  
&& pecl install imagick \  
&& echo "extension=imagick.so" > /usr/local/etc/php/conf.d/ext-imagick.ini \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN docker-php-ext-install -j$(nproc) json  
  
RUN docker-php-ext-install -j$(nproc) mbstring  
  
# mcrypt  
RUN runtimeRequirements="re2c libmcrypt-dev" \  
&& apt-get update && apt-get install -y ${runtimeRequirements} \  
&& docker-php-ext-install -j$(nproc) mcrypt \  
&& rm -rf /var/lib/apt/lists/*  
# mysqli  
RUN docker-php-ext-install -j$(nproc) mysqli  
  
RUN docker-php-ext-install -j$(nproc) opcache  
  
RUN docker-php-ext-install -j$(nproc) pcntl  
  
RUN docker-php-ext-install -j$(nproc) pdo  
  
RUN docker-php-ext-install -j$(nproc) pdo_mysql  
  
RUN buildRequirements="libsqlite3-dev" \  
&& apt-get update && apt-get install -y ${buildRequirements} \  
&& docker-php-ext-install -j$(nproc) pdo_sqlite \  
&& apt-get purge -y ${buildRequirements} \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN buildRequirements="libssl-dev" \  
&& apt-get update && apt-get install -y ${buildRequirements} \  
&& docker-php-ext-install -j$(nproc) phar \  
&& apt-get purge -y ${buildRequirements} libssl-doc \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN docker-php-ext-install -j$(nproc) posix  
  
RUN runtimeRequirements="libpspell-dev" \  
&& apt-get update && apt-get install -y ${runtimeRequirements} \  
&& docker-php-ext-install -j$(nproc) pspell \  
&& apt-get purge -y ${buildRequirements} \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN runtimeRequirements="libedit-dev" \  
&& apt-get update && apt-get install -y ${runtimeRequirements} \  
&& docker-php-ext-install -j$(nproc) readline \  
&& apt-get purge -y ${buildRequirements} \  
&& rm -rf /var/lib/apt/lists/*  
# recode  
RUN runtimeRequirements="librecode-dev" \  
&& apt-get update && apt-get install -y ${runtimeRequirements} \  
&& docker-php-ext-install -j$(nproc) recode \  
&& apt-get purge -y ${buildRequirements} \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN docker-php-ext-install -j$(nproc) session  
  
RUN docker-php-ext-install -j$(nproc) simplexml  
  
RUN docker-php-ext-install -j$(nproc) soap  
  
RUN docker-php-ext-install -j$(nproc) sockets  
  
RUN docker-php-ext-install -j$(nproc) sysvmsg  
  
RUN docker-php-ext-install -j$(nproc) sysvsem  
  
RUN docker-php-ext-install -j$(nproc) sysvshm  
  
RUN runtimeRequirements="libtidy-dev" \  
&& apt-get update && apt-get install -y ${runtimeRequirements} \  
&& docker-php-ext-install -j$(nproc) tidy \  
&& apt-get purge -y ${buildRequirements} \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN docker-php-ext-install -j$(nproc) tokenizer  
  
RUN docker-php-ext-install -j$(nproc) wddx  
  
RUN buildRequirements="libxml2-dev" \  
&& apt-get update && apt-get install -y ${buildRequirements} \  
&& docker-php-ext-install -j$(nproc) xml \  
&& apt-get purge -y ${buildRequirements} \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN buildRequirements="libxml2-dev" \  
&& apt-get update && apt-get install -y ${buildRequirements} \  
&& docker-php-ext-install -j$(nproc) xmlrpc \  
&& apt-get purge -y ${buildRequirements} \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN runtimeRequirements="libxslt-dev" \  
&& apt-get update && apt-get install -y ${runtimeRequirements} \  
&& docker-php-ext-install -j$(nproc) xsl \  
&& apt-get purge -y ${buildRequirements} \  
&& rm -rf /var/lib/apt/lists/*  
# yaml  
RUN buildRequirements="libyaml-dev" \  
&& apt-get update && apt-get install -y ${buildRequirements} \  
&& pecl install yaml-beta \  
&& echo "extension=yaml.so" > /usr/local/etc/php/conf.d/ext-yaml.ini \  
&& apt-get purge -y ${buildRequirements} \  
&& rm -rf /var/lib/apt/lists/*  
# libsodium  
RUN buildRequirements="libsodium-dev" \  
&& apt-get update && apt-get install -y ${buildRequirements} \  
&& pecl install libsodium \  
&& echo "extension=libsodium.so" > /usr/local/etc/php/conf.d/ext-libsodium.ini
\  
&& apt-get purge -y ${buildRequirements} \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN docker-php-ext-install -j$(nproc) zip  
  
# grpc  
RUN runtimeRequirements="" \  
&& apt-get update && apt-get install -y ${runtimeRequirements} \  
&& pecl install grpc \  
&& echo "extension=grpc.so" > /usr/local/etc/php/conf.d/ext-grpc.ini \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN rm -r /var/www/html  
  
# create symlink to support standard /usr/bin/php  
RUN ln -s /usr/local/bin/php /usr/bin/php  
  
# Adjust some php settings  
ADD etc/php/conf.d/* /usr/local/etc/php/conf.d/  
  
RUN a2enmod rewrite  
RUN a2enmod autoindex  
RUN a2enmod alias  
RUN a2enmod deflate  
RUN a2enmod expires  
RUN a2enmod filter  
RUN a2enmod mime  
RUN a2enmod headers  
RUN a2enmod setenvif  
  
ADD etc/apache2/sites-available/000-default.conf /etc/apache2/sites-
available/000-default.conf

