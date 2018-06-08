FROM php:7.0-apache  
MAINTAINER Jonas Renggli <jonas.renggli@swisscom.com>  
  
# Install general utilities  
RUN apt-get update \  
&& apt-get install -y \  
vim \  
net-tools \  
procps \  
telnet \  
netcat \  
&& rm -r /var/lib/apt/lists/*  
  
# Install utilities used by TYPO3 CMS / Flow / Neos  
RUN apt-get update \  
&& apt-get install -y \  
imagemagick \  
graphicsmagick \  
zip \  
unzip \  
wget \  
curl \  
git \  
mysql-client \  
moreutils \  
dnsutils \  
&& rm -rf /var/lib/apt/lists/*  
  
# gd  
RUN buildRequirements="libpng-dev libjpeg-dev libfreetype6-dev" \  
&& apt-get update && apt-get install -y ${buildRequirements} \  
&& docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-
dir=/usr/lib \  
&& docker-php-ext-install gd \  
&& apt-get purge -y ${buildRequirements} \  
&& rm -rf /var/lib/apt/lists/*  
  
# pdo_mysql  
RUN docker-php-ext-install pdo_mysql  
  
# mbstring  
RUN docker-php-ext-install mbstring  
  
# opcache  
RUN docker-php-ext-install opcache  
  
# geoip  
RUN runtimeRequirements="libgeoip-dev" \  
&& apt-get update && apt-get install -y ${runtimeRequirements} \  
&& pecl install geoip-1.1.1 \  
&& echo "extension=geoip.so" > /usr/local/etc/php/conf.d/ext-geoip.ini \  
&& rm -rf /var/lib/apt/lists/*  
  
COPY assets/php.ini /usr/local/etc/php/conf.d/php.ini  
  
# locales  
COPY assets/locale.gen /etc/locale.gen  
RUN apt-get update \  
&& apt-get install -y locales \  
&& rm -r /var/lib/apt/lists/* \  
&& locale-gen  
  
# Activate login for user www-data  
RUN chsh www-data -s /bin/bash  
  
# new home folder for user  
RUN usermod -d /var/www/html www-data  
  
# SSMTP  
RUN apt-get update \  
&& apt-get install -y ssmtp \  
&& rm -rf /var/lib/apt/lists/*  
COPY assets/ssmtp.conf /opt/docker/ssmtp.conf  
  
# Cron  
RUN apt-get update \  
&& apt-get install -y cron \  
&& rm -rf /var/lib/apt/lists/*  
  
# Piwik  
ENV PIWIK_VERSION 3.5.1  
RUN cd /var/www/html && \  
curl -L -O http://builds.matomo.org/piwik-${PIWIK_VERSION}.tar.gz && \  
tar --strip 1 -xzf piwik-${PIWIK_VERSION}.tar.gz && \  
rm piwik-${PIWIK_VERSION}.tar.gz && \  
chown -R www-data:www-data tmp config  
  
RUN wget -O misc/GeoIPCity.dat.gz
http://geolite.maxmind.com/download/geoip/database/GeoLiteCity.dat.gz && \  
gunzip misc/GeoIPCity.dat.gz  
  
COPY assets/config.ini.php.docker /var/www/html/config/config.ini.php.docker  
  
# Piwik Cron  
COPY assets/piwik-archive /etc/cron.d/piwik-archive  
  
# Plugin WebsiteGroups  
RUN mkdir -p /var/www/html/plugins/WebsiteGroups && \  
cd /var/www/html/plugins/WebsiteGroups && \  
wget -O WebsiteGroups.tar.gz https://github.com/PiwikPRO/plugin-
WebsiteGroups/archive/0.2.0.tar.gz && \  
tar xzf WebsiteGroups.tar.gz --strip 1 && \  
rm -f WebsiteGroups.tar.gz  
  
# Plugin ClickHeat  
RUN mkdir -p /var/www/html/plugins/ClickHeat && \  
cd /var/www/html/plugins/ClickHeat && \  
wget -O ClickHeat.tar.gz https://github.com/piwikjapan/plugin-
clickheat/archive/0.1.5.tar.gz && \  
tar xzf ClickHeat.tar.gz --strip 1 && \  
rm -f ClickHeat.tar.gz && \  
mkdir -p /var/www/html/tmp/cache/clickheat/{logs,cache}  
  
# Set permissions  
RUN cd /var/www/html && \  
chown -R www-data:www-data tmp config  
  
COPY assets/entrypoint.sh /entrypoint.sh  
  
RUN set -ex; \  
unlink /var/log/apache2/error.log; \  
unlink /var/log/apache2/access.log; \  
touch /var/log/error.log; \  
touch /var/log/access.log  
  
ENTRYPOINT ["/entrypoint.sh"]  
CMD ["apache2-foreground"]  

