FROM php:7.1-fpm  
  
MAINTAINER Peeratchai Petpadriew <p.petpadriew@gmail.com>  
  
ENV TZ=Asia/Bangkok  
  
RUN \  
# ENV variables  
PECL_EXTENSIONS="xdebug-2.5.5"; \  
PHP_EXTENSIONS="mysqli opcache zip pdo_mysql intl"; \  
DEV_DEPS="libicu-dev zlibc zlib1g zlib1g-dev"; \  
TMP_DEV_DEPS="g++"; \  
# update package list  
apt-get update -qqy \  
# install  
&& apt-get -qqy --fix-missing --no-install-recommends install \  
git \  
nodejs \  
npm \  
# dev dependencies which still persist after the build process  
$DEV_DEPS \  
# temp dev dependencies which will be deleted at the end of the build process  
$TMP_DEV_DEPS \  
# php + pecl extensions  
&& docker-php-source extract \  
&& pecl channel-update pecl.php.net \  
&& pecl install $PECL_EXTENSIONS \  
&& docker-php-ext-install $PHP_EXTENSIONS \  
&& docker-php-ext-enable `echo $PECL_EXTENSIONS | sed -e "s/[^a-z ]//g"` \  
&& docker-php-source delete \  
# composer  
&& curl -sSL https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer \  
# capture std error  
&& ln -sf /dev/stderr /var/log/php7.1-fpm.log \  
&& ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
\  
# cleanup  
&& apt-get purge -y --auto-remove $TMP_DEV_DEPS \  
&& apt-get clean \  
&& apt-get autoclean \  
&& apt-get autoremove \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* /usr/share/doc/*
/usr/share/man/*  
  
WORKDIR /var/www/project  

