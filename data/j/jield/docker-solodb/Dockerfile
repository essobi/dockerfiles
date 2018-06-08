FROM debian:jessie  
  
# With inspiration from https://github.com/punkstar/bitbucket-pipelines-
php7-mysql  
MAINTAINER Johan van der Heide <info@jield.nl>  
  
ENV DEBIAN_FRONTEND noninteractive  
ENV LC_ALL en_US.UTF-8  
ENV LANGUAGE en_US:en  
  
# Base  
RUN \  
apt-get update && \  
apt-get -y --no-install-recommends install wget locales apt-transport-https
lsb-release apt-utils curl ca-certificates openssh-client && \  
echo "en_US.UTF-8 UTF-8" >> /etc/locale.gen && \  
locale-gen en_US.UTF-8 && \  
/usr/sbin/update-locale LANG=en_US.UTF-8 && \  
update-ca-certificates  
  
# Sury and dotdeb resources  
RUN \  
wget -O /etc/apt/trusted.gpg.d/php.gpg https://packages.sury.org/php/apt.gpg
&& \  
echo "deb https://packages.sury.org/php/ $(lsb_release -sc) main" >>
/etc/apt/sources.list.d/php.list && \  
apt-get update && \  
apt-get -y --no-install-recommends upgrade  
  
# Install PHP  
RUN \  
apt-get install -y git zip && \  
apt-get install -y php7.1-fpm php7.1-cli php7.1-common php7.1-intl
php7.1-redis php7.1-gd php7.1-mcrypt php7.1-igbinary php7.1-mysql
php7.1-mbstring php7.1-zip php7.1-xml php7.1-curl php7.1-json php7.1-opcache
php7.1-readline php7.1-soap  
  
# Install composer  
RUN curl -sS https://getcomposer.org/installer | php -- --filename=composer
--install-dir=/usr/bin  
  
# Cleanup apt  
RUN \  
apt-get autoclean && apt-get clean && apt-get autoremove  
  

