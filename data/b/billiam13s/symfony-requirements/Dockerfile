FROM php:7.0-fpm  
  
ENV SYS_DEPS \  
libicu-dev  
  
ENV BUILD_DEPS \  
libssl-dev  
  
ENV PHP_DEPS \  
intl \  
opcache  
  
RUN set -xe \  
&& apt-get update \  
&& apt-get install -y --no-install-recommends \  
$SYS_DEPS \  
$BUILD_DEPS \  
&& docker-php-ext-install -j$(nproc) $PHP_DEPS  
  
# clean up unneeded libs  
RUN set -xe \  
&& rm -rf /var/lib/apt/lists/* \  
&& apt-get purge -y --auto-remove -o
APT::AutoRemove::RecommendsImportant=false  

