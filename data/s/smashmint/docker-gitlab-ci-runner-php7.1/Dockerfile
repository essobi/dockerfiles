# docker-gitlab-ci-runner-php7  
FROM bobey/docker-gitlab-ci-runner-php  
MAINTAINER Olivier Balais "obalais@gmail.com"  
  
ENV PHP_VERSION 7.1.0  
  
COPY files/ci-runner.ini /root/.phpenv/versions/7.1.0/etc/conf.d/ci-runner.ini  
  
RUN DEBIAN_FRONTEND=noninteractive apt-get remove -y --purge php*  
  
RUN DEBIAN_FRONTEND=noninteractive apt-get update  
RUN DEBIAN_FRONTEND=noninteractive apt-get -y install python-software-
properties  
RUN DEBIAN_FRONTEND=noninteractive apt-get -y install software-properties-
common  
RUN DEBIAN_FRONTEND=noninteractive LC_ALL=C.UTF-8 add-apt-repository
ppa:ondrej/php  
  
RUN DEBIAN_FRONTEND=noninteractive apt-get update && apt-get install -y \  
php7.1-cli \  
php7.1-common \  
php7.1-dev \  
php7.1-json \  
php7.1-opcache \  
php7.1-mysql \  
php7.1-phpdbg \  
php7.1-mbstring \  
php7.1-gd \  
php7.1-imap \  
php7.1-ldap \  
php7.1-pgsql \  
php7.1-sqlite \  
php7.1-pdo \  
php7.1-pspell \  
php7.1-recode \  
php7.1-tidy \  
php7.1-intl \  
php7.1-curl \  
php7.1-zip \  
php7.1-xml \  
php-mongodb \  
php-redis \  
php-memcache \  
php-xdebug  

