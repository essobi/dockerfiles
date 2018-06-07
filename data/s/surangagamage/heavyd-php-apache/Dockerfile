#!/usr/bin/env docker  
FROM ubuntu:16.04  
MAINTAINER Suranga Gamage <suranga@webct.be>  
  
ENV INITRD=No TERM=dumb MY_TZ=Europe/Brussels  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update  
RUN apt-get -qq upgrade  
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys E5267A6C && \  
echo 'deb http://ppa.launchpad.net/ondrej/php/ubuntu xenial main' >>
/etc/apt/sources.list && \  
echo 'deb-src http://ppa.launchpad.net/ondrej/php/ubuntu xenial main' >>
/etc/apt/sources.list && \  
apt-get update && \  
DEBIAN_FRONTEND=noninteractive \  
apt-get install -q -y php7.1 \  
php7.1-cli \  
php7.1-dev \  
php7.1-bcmath \  
php7.1-bz2 \  
php7.1-mysql \  
php7.1-mbstring \  
php7.1-mcrypt \  
php7.1-gd \  
php7.1-curl \  
php7.1-intl \  
php7.1-common \  
php7.1-json \  
php7.1-recode \  
php7.1-soap \  
php7.1-xml \  
php7.1-zip \  
php7.1-opcache \  
php7.1-ldap  
  
RUN apt-get install -y --force-yes \  
build-essential \  
imagemagick \  
ca-certificates \  
apache2 \  
libapache2-mod-php7.1 \  
ca-certificates \  
net-tools \  
rsyslog \  
curl \  
wget \  
git \  
php-apcu \  
php-gettext \  
mysql-client  
  
RUN apt-get install -y locales  
RUN rm /etc/timezone && echo $MY_TZ >> /etc/timezone && locale-gen nl_BE.UTF-8
&& LC_ALL=nl_BE.UTF-8  
  
# Add supervisord  
RUN apt-get install -y supervisor  
  
# Add image configuration and scripts  
ADD start-apache2.sh /start-apache2.sh  
ADD run.sh /run.sh  
RUN chmod 755 /*.sh  
ADD supervisord-apache2.conf /etc/supervisor/conf.d/supervisord-apache2.conf  
  
# config to enable .htaccess  
ADD apache_default /etc/apache2/sites-available/000-default.conf  
RUN a2enmod rewrite  
  
# Configure /webdata folder  
RUN mkdir -p /webdata  
  
# Configure PHP apache ini settings  
RUN rm -f /etc/php/7.1/apache2/php.ini  
COPY php.ini /etc/php/7.1/apache2/php.ini  
  
# Configure PHP cli settings  
RUN rm -f /etc/php/7.1/cli/php.ini  
COPY php.ini /etc/php/7.1/cli/php.ini  
  
# Environment variables to configure php  
ENV PHP_UPLOAD_MAX_FILESIZE 250M  
ENV PHP_POST_MAX_SIZE 250M  
  
#Clean up  
RUN apt-get autoclean && apt-get autoremove && apt-get clean && rm -rf
/var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# Composer  
ENV COMPOSER_VERSION 1.5.5  
RUN curl -sSL https://getcomposer.org/installer | php -- --filename=composer
--install-dir=/usr/bin  
  
# Container ports and commands  
EXPOSE 80  
CMD ["/run.sh"]  

