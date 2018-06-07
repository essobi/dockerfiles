FROM php:7.1-fpm  
  
# Install PHP7  
RUN buildDeps=" \  
libpng12-dev \  
libjpeg-dev \  
libmcrypt-dev \  
libxml2-dev \  
freetype* \  
libxslt1-dev \  
cron \  
libicu-dev \  
"; \  
set -x \  
&& apt-get update && apt-get install -y $ImageDeps $buildDeps --no-install-
recommends && rm -rf /var/lib/apt/lists/* \  
&& docker-php-ext-configure \  
gd --with-png-dir=/usr --with-jpeg-dir=/usr --with-freetype-dir \  
&& docker-php-ext-install -j "$(getconf _NPROCESSORS_ONLN)" \  
gd \  
mbstring \  
mysqli \  
mcrypt \  
pdo_mysql \  
soap \  
zip \  
bcmath \  
intl \  
xsl \  
&& curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer  
  
# Install Tools  
RUN apt-get update && \  
apt-get install -y \  
vim \  
zip \  
bzip2 \  
jq \  
mysql-client \  
git-core \  
&& apt-get purge -y --auto-remove  
  
#ADD SSH RSA_KEY AND CONFIG  
#RUN mkdir -p /root/.ssh && \  
# touch /root/.ssh/known_hosts

