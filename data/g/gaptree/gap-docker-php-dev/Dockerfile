FROM php:7.1.10-cli  
  
MAINTAINER "zhanjh@126.com"  
COPY install-composer.sh /install-composer.sh  
  
# ref: https://store.docker.com/images/php  
# ref https://github.com/RobLoach/docker-composer/blob/master/base/Dockerfile  
## issues  
# --with-zlib-dir=<DIR> -> zlib1g-dev  
# https://stackoverflow.com/questions/2977662/php-zip-installation-on-linux  
ENV COMPOSER_HOME /composer  
ENV COMPOSER_ALLOW_SUPERUSER 1  
ENV PATH /composer/vendor/bin:$PATH  
  
# Packages  
RUN set -ex \  
&& apt-get update \  
&& apt-get upgrade --no-install-recommends --no-install-suggests -y \  
&& apt-get install -y --no-install-recommends --no-install-suggests \  
git \  
unzip \  
libmcrypt-dev \  
libbz2-dev \  
zlib1g-dev \  
&& rm -rf /var/lib/apt/lists/*  
  
# PHP Extensions  
RUN set -ex && docker-php-ext-install mcrypt zip bz2 mbstring pdo pdo_mysql  
  
# PHP Extensions redis  
RUN set -ex \  
&& cd /tmp \  
&& git clone https://github.com/phpredis/phpredis phpredis \  
&& cd phpredis \  
&& git checkout master \  
  
&& phpize \  
&& ./configure \  
&& make \  
&& make install \  
&& cd / \  
&& rm -r /tmp/phpredis \  
&& docker-php-ext-enable redis  
  
# Composer packages  
RUN set -ex && sh ./install-composer.sh  

