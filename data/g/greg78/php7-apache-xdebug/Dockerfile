FROM php:7-apache  
  
ARG DEBIAN_FRONTEND=noninteractive  
  
# modules apache  
RUN a2enmod rewrite \  
&& a2enmod headers  
  
RUN echo 'ServerName localhost' >> /etc/apache2/apache2.conf \  
&& service apache2 restart  
  
RUN apt-get update && apt-get install -y --no-install-recommends apt-utils  
  
# XDebug  
RUN pecl install xdebug-2.6.0beta1 \  
&& docker-php-ext-enable xdebug  
  
# Install utilities  
RUN apt-get update && apt-get install -y \  
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
libssl-dev \  
pkg-config \  
openssl \  
libcurl4-openssl-dev \  
libsqlite3-dev \  
libsqlite3-0 \  
sqlite3 \  
&& rm -rf /var/lib/apt/lists/*  
# gd  
RUN apt-get update && apt-get install -y \  
libfreetype6-dev \  
libjpeg62-turbo-dev \  
libpng-dev \  
&& docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-
dir=/usr/include/ \  
&& docker-php-ext-install -j$(nproc) gd \  
&& rm -rf /var/lib/apt/lists/*  
# imagick  
RUN apt-get update && apt-get install -y \  
libmagickwand-dev --no-install-recommends \  
&& pecl install imagick \  
&& docker-php-ext-enable imagick \  
&& rm -rf /var/lib/apt/lists/*  
# exif  
RUN docker-php-ext-install exif \  
&& docker-php-ext-configure exif --enable-exif  
  
# opcache  
RUN docker-php-ext-install opcache  
  
# soap  
RUN docker-php-ext-install soap  
  
# zip  
RUN docker-php-ext-install zip  
  
# pdo_pgsql pdo_mysql  
RUN apt-get update && apt-get install -y \  
libghc-postgresql-libpq-dev \  
&& docker-php-ext-configure pgsql -with-pgsql=/usr/include/postgresql/ \  
&& docker-php-ext-install pgsql pdo_pgsql pdo_mysql \  
&& rm -rf /var/lib/apt/lists/*  
# mysqli  
RUN docker-php-ext-install mysqli  
  
# Install program to configure locales  
RUN apt-get update && apt-get install -y locales  
# Install needed default locale for PHP setlocale  
RUN echo 'en_US.UTF-8 UTF-8' >> /etc/locale.gen \  
&& echo 'fr_FR.UTF-8 UTF-8' >> /etc/locale.gen \  
&& ln -s /etc/locale.alias /usr/share/locale/locale.alias \  
&& locale-gen  
# Set default locale for the environment  
ENV LC_ALL fr_FR.UTF-8  
# wkhtmltopdf  
RUN wget
https://github.com/wkhtmltopdf/wkhtmltopdf/releases/download/0.12.4/wkhtmltox-0.12.4_linux-
generic-amd64.tar.xz \  
&& tar -xvf wkhtmltox-0.12.4_linux-generic-amd64.tar.xz \  
&& mv -v wkhtmltox/bin/* /usr/bin/ \  
&& rm wkhtmltox-0.12.4_linux-generic-amd64.tar.xz  
  
# Clean up APT when done.  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

