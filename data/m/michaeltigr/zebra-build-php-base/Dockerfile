FROM composer:latest  
  
LABEL maintainer "Michael Molchanov <mmolchanov@adyax.com>"  
  
USER root  
  
# SSH config.  
RUN mkdir -p /root/.ssh  
ADD config/ssh /root/.ssh/config  
RUN chown root:root /root/.ssh/config && chmod 600 /root/.ssh/config  
  
# Install base.  
RUN apk add --update --no-cache \  
bash \  
build-base \  
bzip2 \  
curl \  
freetype \  
git \  
libbz2 \  
libffi \  
libffi-dev \  
libjpeg-turbo \  
libmcrypt \  
libpq \  
libpng \  
libxml2 \  
libxslt \  
mysql-client \  
openssh \  
openssl \  
openssl-dev \  
procps \  
postgresql-client \  
rsync \  
sqlite \  
tar \  
unzip \  
wget \  
zlib \  
&& rm -rf /var/lib/apt/lists/*  
  
# PHP modules.  
RUN set -xe \  
&& apk add --no-cache --virtual .build-deps \  
$PHPIZE_DEPS \  
curl-dev \  
libedit-dev \  
libxml2-dev \  
sqlite-dev \  
autoconf \  
subversion \  
freetype-dev \  
libjpeg-turbo-dev \  
libmcrypt-dev \  
libpng-dev \  
bzip2-dev \  
libstdc++ \  
libxslt-dev \  
openldap-dev \  
make \  
patch \  
postgresql-dev \  
&& export CFLAGS="$PHP_CFLAGS" \  
CPPFLAGS="$PHP_CPPFLAGS" \  
LDFLAGS="$PHP_LDFLAGS" \  
&& docker-php-source extract \  
&& cd /usr/src/php \  
&& docker-php-ext-install bcmath mcrypt zip bz2 mbstring pcntl xsl mysqli
pgsql pdo_mysql pdo_pgsql \  
&& docker-php-ext-configure gd --with-freetype-dir=/usr/include/ \--with-jpeg-
dir=/usr/include/ \  
&& docker-php-ext-install gd \  
&& docker-php-ext-configure ldap --with-libdir=lib/ \  
&& docker-php-ext-install ldap \  
&& git clone --branch="php7" https://github.com/phpredis/phpredis.git
/usr/src/php/ext/redis \  
&& docker-php-ext-install redis \  
&& php -m && php -r "new Redis();" \  
&& docker-php-source delete \  
&& apk del .build-deps  

