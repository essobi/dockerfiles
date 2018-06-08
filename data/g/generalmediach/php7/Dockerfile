FROM debian:stable-slim  
  
LABEL maintainer="Generalmedia SA <webmaster@generalmedia.ch>"  
  
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
php7.1 \  
php7.1-mysql \  
php7.1-gd \  
php7.1-opcache \  
php7.1-xml \  
php7.1-cli \  
php7.1-common \  
php7.1-intl \  
php7.1-xsl \  
php7.1-curl \  
php7.1-json \  
php-imagick \  
php7.1-zip \  
php7.1-dev \  
php7.1-bcmat \  
php7.1-mbstring \  
php7.1-mcrypt \  
libapache2-mod-php7.1 \  
ruby \  
ruby-dev \  
xfonts-75dpi \  
xfonts-base \  
zlib1g-dev \  
pkg-config \  
build-essential \  
logrotate  
  
# Install && enable redis  
RUN cd /tmp && git clone https://github.com/phpredis/phpredis.git && \  
cd phpredis && git checkout 3.1.6 && phpize && ./configure && \  
make && make install && cd .. && rm -rf phpredis && \  
echo "extension=redis.so" > /etc/php/7.1/mods-available/redis.ini && \  
ln -sf /etc/php/7.1/mods-available/redis.ini
/etc/php/7.1/apache2/conf.d/20-redis.ini && \  
ln -sf /etc/php/7.1/mods-available/redis.ini
/etc/php/7.1/cli/conf.d/20-redis.ini  
  
# Apache configuration  
RUN a2enmod rewrite headers ssl deflate expires  
COPY apache/vhost.conf /etc/apache2/sites-enabled/000-default.conf  
COPY apache/vhost-dev.conf /etc/apache2/sites-enabled/001-dev.conf  
COPY apache/deflate_gzip.conf /etc/apache2/mods-enabled/deflate_gzip.conf  
COPY apache/deflate_gzip.conf /etc/apache2/mods-available/deflate_gzip.conf  
  
# PHP.ini  
COPY php/*.ini /etc/php/7.1/mods-available/  
RUN ln -sf /etc/php/7.1/mods-available/99-gm.ini /etc/php/7.1/apache2/conf.d/
&& ln -sf /etc/php/7.1/mods-available/99-gm.ini /etc/php/7.1/cli/conf.d/  
  
#logrotation  
COPY docker/logrotate.conf /etc/logrotate.d/docker-container  
  
# composer  
RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/bin
--filename=composer  
ENV COMPOSER_ALLOW_SUPERUSER 1  
ENV COMPOSER_HOME /home/.composer  
  
# create TMP dir  
RUN mkdir -p /tmp/uploads/ && chmod +w -R /tmp/  
COPY docker/run-symfony.sh /var/www/run-symfony.sh  
# CHMOD + APACHE at runtime  
RUN /bin/bash -c 'chmod +x /var/www/run-symfony.sh'  
  
# logs apache to stdout+stderror  
RUN ln -sf /dev/stdout /var/log/apache2/access.log && ln -sf /dev/stderr
/var/log/apache2/error.log  

