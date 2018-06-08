###  
# Automated Build for dklein/moodle Image  
# Version 1.3  
# (c) 2017 Dennis Klein  
#  
FROM php:apache  
  
MAINTAINER Dennis Klein <dennis.klein@gmx.com>  
  
# update the ubuntu installation to the latest release and install needed
packages  
ENV DEBIAN_FRONTEND=noninteractive  
RUN rm -rf /var/lib/apt/lists/* && \  
apt-get -y update && \  
apt-get -y upgrade && \  
apt-get -y install git && \  
apt-get -y clean && \  
apt-get -y autoclean  
  
# clone and checkout moodle  
ENV MOODLE_VERSION=v3.2.2  
RUN cd /var/www/html && \  
git clone https://github.com/moodle/moodle.git . && \  
git checkout $MOODLE_VERSION  
  
# default volume for moodle data  
RUN mkdir -p /var/www/moodledata && chown www-data:www-data
/var/www/moodledata  
VOLUME /var/www/moodledata  
  
# install php extension deps  
RUN apt-get -y install zlib1g-dev libxml2-dev libxslt1-dev \  
libfreetype6-dev libjpeg62-turbo-dev libmcrypt-dev libpng12-dev \  
libicu-dev libldap2-dev  
  
# configure php extensions  
RUN docker-php-ext-configure ldap --with-libdir=lib/x86_64-linux-gnu && \  
docker-php-ext-configure gd --with-freetype-dir=/usr/include \--with-jpeg-
dir=/usr/include  
# install php extensions  
RUN docker-php-ext-install zip mysqli xml xsl xmlrpc intl soap gd ldap  

