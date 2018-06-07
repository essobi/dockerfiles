# Dockerfile  
#  
# This image contains:  
# - PHP 7  
# - PHP extensions:  
# - sockets  
# - yaml-2.0.0  
# - memcached  
# - apache2 service  
# - memcached service  
# - supervisor  
#  
# This Docker image is used as an intermediate image for
mkats/yaml_cache_and_website.  
#  
# Build image using the command  
# docker build -t mkats/php7-apache-with-exts ./php7-apache-with-exts  
#  
FROM php:7.1.4-apache  
  
MAINTAINER Michalis Katsarakis version: 0.1  
USER root  
  
RUN buildDeps=" \  
libyaml-dev \  
libz-dev libmemcached-dev \  
" \  
&& set -x \  
&& apt-get update \  
&& apt-get install -y \  
libyaml-0-2 \  
git \  
memcached \  
supervisor \  
\--no-install-recommends \  
&& apt-get install -y $buildDeps \--no-install-recommends \  
&& rm -rf /var/lib/apt/lists/* \  
&& docker-php-ext-install -j$(nproc) \  
sockets \  
&& pecl channel-update pecl.php.net \  
&& pecl install yaml-2.0.0 < /usr/lib/x86_64-linux-gnu \  
&& docker-php-ext-enable yaml \  
  
&& mkdir -p /var/log/supervisor \  
&& mkdir -p /etc/supervisor/conf.d \  
&& mv /etc/supervisor/supervisord.conf /etc/supervisor/supervisord.conf.bak  
  
RUN cd /tmp/ \  
&& git clone https://github.com/php-memcached-dev/php-memcached.git
/usr/src/php/ext/memcached \  
&& cd /usr/src/php/ext/memcached \  
&& git checkout php7 \  
&& docker-php-ext-install memcached  
  
RUN apt-get purge -y --auto-remove -o
APT::AutoRemove::RecommendsImportant=false -o
APT::AutoRemove::SuggestsImportant=false $buildDeps  
  
RUN a2enmod rewrite \  
&& service apache2 restart  
  
COPY supervisord.conf /etc/supervisor/  
  
CMD ["supervisord", "-c", "/etc/supervisor/supervisord.conf"]  

