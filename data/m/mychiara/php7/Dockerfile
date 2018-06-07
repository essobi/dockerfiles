#!/usr/bin/env docker  
  
FROM mychiara/webbase:latest  
MAINTAINER Andy Ruck mychiara+docker ___at___ gmail com  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get install -y language-pack-en-base && \  
LC_ALL=en_US.UTF-8 \  
add-apt-repository ppa:ondrej/php && \  
  
apt-get update && \  
  
apt-get install --no-install-recommends -yq --force-yes \  
build-essential \  
imagemagick \  
ca-certificates \  
php7.0 \  
php7.0-cli \  
php7.0-dev \  
php7.0-fpm \  
php7.0-bcmath \  
php7.0-bz2 \  
php7.0-mysql \  
php7.0-mbstring \  
php7.0-mcrypt \  
php7.0-ldap \  
php7.0-gd \  
php-imagick \  
php7.0-curl \  
php7.0-sqlite \  
php7.0-intl \  
php7.0-common \  
php7.0-json \  
php7.0-opcache \  
php7.0-recode \  
php-redis \  
php7.0-soap \  
php7.0-xml \  
php7.0-zip \  
&& \  
  
curl https://getcomposer.org/installer | php -- && mv composer.phar
/usr/local/bin/composer && chmod +x /usr/local/bin/composer && \  
mkdir -p /var/log/php && ln -sf /dev/stdout /var/log/php/error.log && ln -sf
/dev/stdout /var/log/php7-fpm.log && \  
  
apt-get autoclean && apt-get -y autoremove && \  
apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# RUN git clone https://github.com/phpredis/phpredis.git && \  
# cd phpredis && \  
# git checkout php7 && \  
# phpize && \  
# ./configure && \  
# make && make install && \  
# cd .. && \  
# rm -rf phpredis  
  
# Copy local .inis to the image  
ADD files/php.ini /etc/php/7.0/fpm/php.ini  
ADD files/php-cli.ini /etc/php/7.0/cli/php.ini  
ADD files/php-fpm.conf /etc/php/7.0/fpm/php-fpm.conf  
ADD files/www.conf /etc/php/7.0/fpm/pool.d/www.conf  
  
RUN echo "extension=redis.so" > /etc/php/7.0/mods-available/redis.ini && \  
ln -sf /etc/php/7.0/mods-available/redis.ini
/etc/php/7.0/fpm/conf.d/20-redis.ini && \  
ln -sf /etc/php/7.0/mods-available/redis.ini
/etc/php/7.0/cli/conf.d/20-redis.ini  
  
  
# init system  
RUN mkdir -p /etc/service/php-fpm /var/run/php-fpm  
ADD /files/start.sh /etc/service/php-fpm/run  
RUN chmod +x /etc/service/php-fpm/run  
  
VOLUME "/app-src"  
  
EXPOSE 9000

