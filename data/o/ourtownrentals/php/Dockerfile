FROM php:7.0-fpm  
  
MAINTAINER Evan Sosenko <razorx@evansosenko.com>  
  
RUN buildDeps=" \  
libfreetype6-dev \  
libjpeg-dev \  
libpng12-dev \  
libcurl4-gnutls-dev \  
"; \  
set -x \  
&& apt-get update \  
&& apt-get install -y --no-install-recommends --no-install-suggests \  
$buildDeps \  
libfreetype6 \  
libjpeg62-turbo \  
&& rm -rf /var/lib/apt/lists/* \  
&& docker-php-ext-configure gd \  
\--with-freetype-dir=/usr/include/ \  
\--with-jpeg-dir=/usr/include/ \  
&& docker-php-ext-install -j$(nproc) gd \  
&& docker-php-ext-install -j$(nproc) curl \  
&& docker-php-ext-install -j$(nproc) mysqli \  
&& apt-get purge -y --auto-remove $buildDeps  
  
RUN cd /tmp \  
&& curl -o ioncube.tar.gz \  
https://downloads.ioncube.com/loader_downloads/ioncube_loaders_lin_x86-64.tar.gz
\  
&& echo '7e112dec9097e9f688f6c9091523b60b72aafcdb ioncube.tar.gz' | shasum -c
\  
&& tar -xzf ioncube.tar.gz \  
&& mv ioncube/ioncube_loader_lin_7.0.so /usr/local/lib/php/extensions/* \  
&& rm -rf ioncube.tar.gz ioncube \  
&& echo "zend_extension=ioncube_loader_lin_7.0.so" \  
> /usr/local/etc/php/conf.d/00_docker-php-ext-ioncube_loader_lin_7.0.ini  

