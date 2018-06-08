FROM debian:jessie  
  
MAINTAINER David Dabo <david.dabo@generalmedia.ch>  
  
ENV DEBIAN_FRONTEND=noninteractive  
  
#install node 8 + npm  
RUN apt-get update && apt-get install -y apt-transport-https lsb-release ca-
certificates wget gnupg curl software-properties-common && \  
curl -sL https://deb.nodesource.com/setup_8.x | bash - && \  
wget -O /etc/apt/trusted.gpg.d/php.gpg https://packages.sury.org/php/apt.gpg
&& \  
echo "deb https://packages.sury.org/php/ $(lsb_release -sc) main" >
/etc/apt/sources.list.d/php.list  
  
RUN apt-get update && apt-get install -y \  
acl \  
apache2 \  
cron \  
git \  
vim \  
libicu-dev \  
libx11-6 \  
libxext6 \  
libxrender1 \  
make \  
openssl \  
nodejs \  
php5.6 \  
php5.6-mysql \  
php5.6-gd \  
php5.6-opcache \  
php5.6-xml \  
php5.6-cli \  
php5.6-common \  
php5.6-intl \  
php5.6-xsl \  
php5.6-curl \  
php5.6-json \  
php-imagick \  
php5.6-zip \  
php5.6-dev \  
php5.6-bcmat \  
php5.6-mbstring \  
php5.6-mcrypt \  
libapache2-mod-php5.6 \  
ruby \  
ruby-dev \  
xfonts-75dpi \  
xfonts-base \  
zlib1g-dev \  
pkg-config \  
build-essential  
  
# install xdebug (not enabled)  
RUN wget -c "http://xdebug.org/files/xdebug-2.4.0.tgz" && tar -xf
xdebug-2.4.0.tgz && cd xdebug-2.4.0 && phpize && \  
./configure && make && make install && \  
echo "zend_extension=xdebug.so" > /etc/php/5.6/mods-available/xdebug.ini  
  
# Apache configuration  
RUN a2enmod rewrite headers ssl deflate expires  
COPY apache/vhost.conf /etc/apache2/sites-enabled/000-default.conf  
COPY apache/vhost.conf /etc/apache2/sites-available/000-default.conf  
COPY apache/deflate_gzip.conf /etc/apache2/mods-enabled/deflate_gzip.conf  
COPY apache/deflate_gzip.conf /etc/apache2/mods-available/deflate_gzip.conf  
  
# PHP.ini  
COPY php/*.ini /etc/php/5.6/mods-available/  
RUN ln -sf /etc/php/5.6/mods-available/99-gm.ini /etc/php/5.6/apache2/conf.d/
&& ln -sf /etc/php/5.6/mods-available/99-gm.ini /etc/php/5.6/cli/conf.d/  
  
# create TMP dir  
RUN mkdir -p /tmp/uploads/ && chmod +w -R /tmp/  
COPY docker/run-magento.sh /var/www/run-magento.sh  
  
# CHMOD + APACHE at runtime  
RUN /bin/bash -c 'chmod +x /var/www/run-magento.sh'  
  
# logs apache to stdout+stderror  
RUN ln -sf /dev/stdout /var/log/apache2/access.log && ln -sf /dev/stderr
/var/log/apache2/error.log  

