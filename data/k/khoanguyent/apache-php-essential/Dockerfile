FROM php:7.1.9-apache  
  
ARG PHP_EXT_LIST=" \  
mysqli \  
json \  
mbstring \  
pdo_sqlite \  
pdo_pgsql \  
pdo_mysql \  
pgsql \  
curl \  
fileinfo \  
zip \  
exif"  
  
ARG CUSTOM_BUILD_PKGS="\  
apache2-dev \  
libcurl4-openssl-dev \  
libmcrypt-dev \  
libbz2-dev \  
libpq-dev \  
zlib1g-dev \  
libsqlite3-dev"  
  
RUN apt-get update && apt-get install -yqq \  
git \  
wget \  
unzip \  
zip \  
zlibc \  
zlib1g \  
${CUSTOM_BUILD_PKGS} \  
  
# Reverse Proxy / Load Balancer (?)  
&& { \  
echo '<IfModule mod_setenvif.c>'; \  
echo 'SetEnvIf X-Forwarded-Proto "^https$" AND X-Forwarded-Ssl "^on$"
HTTPS=on'; \  
echo '</IfModule>'; \  
} | tee "$APACHE_CONFDIR/conf-available/reverseproxy.conf" \  
&& a2enconf reverseproxy \  
  
# Load mod_rewrite  
&& a2enmod rewrite \  
  
# Install PHP Extensions  
# See ARG PHP_EXT_LIST  
&& docker-php-ext-install -j$(nproc) ${PHP_EXT_LIST} \  
  
# Install Composer  
&& curl --silent --show-error https://getcomposer.org/installer | php --
--install-dir=/usr/local/bin --filename=composer \  
  
# Clean Up  
&& apt-get remove --purge -yqq ${CUSTOM_BUILD_PKGS} \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  

