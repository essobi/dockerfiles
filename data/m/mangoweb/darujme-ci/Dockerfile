# available as https://hub.docker.com/r/mangoweb/darujme-ci/  
# to rebuild go to https://hub.docker.com/r/mangoweb/darujme-
ci/~/settings/automated-builds/  
  
FROM php:7.1-cli  
  
# Install linux stuff  
RUN apt-get update && apt-get install --no-install-recommends -y \  
apt-utils \  
git \  
ssh \  
unzip \  
wget \  
zip  
  
# Add PostgreSQL repository  
RUN echo "deb http://apt.postgresql.org/pub/repos/apt/ jessie-pgdg main" >
/etc/apt/sources.list.d/pgdg.list  
RUN wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc |
apt-key add -  
  
# Install PHP extensions deps  
RUN apt-get update && apt-get install --no-install-recommends -y \  
freetds-dev \  
g++ \  
libaio-dev \  
libc-client-dev \  
libfreetype6-dev \  
libicu-dev \  
libjpeg62-turbo-dev \  
libkrb5-dev \  
libmcrypt-dev \  
libpng12-dev \  
libssl-dev \  
libxml2-dev \  
openssl \  
postgresql-server-dev-9.5 \  
zlib1g-dev  
  
# Install PHP extensions  
RUN docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-
dir=/usr/include/ \  
&& docker-php-ext-configure imap --with-kerberos --with-imap-ssl \  
&& pecl install redis \  
&& docker-php-ext-install \  
gd \  
iconv \  
imap \  
intl \  
mbstring \  
mcrypt \  
mysqli \  
pcntl \  
pdo_mysql \  
pdo_pgsql \  
pgsql \  
soap \  
sockets \  
zip \  
&& docker-php-ext-enable \  
redis \  
opcache  
  
# Install Mango CLI  
# https://nodejs.org/en/download/package-manager/#debian-and-ubuntu-based-
linux-distributions  
RUN curl -sL https://deb.nodesource.com/setup_7.x | bash \  
&& apt-get install -y \  
build-essential \  
nodejs \  
&& env USER=root CFLAGS="-fPIC" CXXFLAGS="-fPIC" npm install -g mango-cli \  
&& nodejs --version && npm --version && mango --version  
  
# Clean repository  
RUN apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  

