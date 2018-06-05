FROM php:5.6-apache  
MAINTAINER Benjamin Hutchins <ben@hutchins.co>  
  
ENV PIWIK_VERSION 3.2.0  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends \  
zip \  
unzip \  
wget \  
moreutils \  
dnsutils \  
&& rm -rf /var/lib/apt/lists/*  
  
# PHP gd module  
RUN buildRequirements="libpng12-dev libjpeg-dev libfreetype6-dev" \  
&& apt-get update && apt-get install -y ${buildRequirements} \  
&& docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-
dir=/usr/lib \  
&& docker-php-ext-install gd \  
&& apt-get purge -y ${buildRequirements} \  
&& rm -rf /var/lib/apt/lists/*  
  
# Additional PHP modules  
RUN docker-php-ext-install pdo_mysql mbstring opcache  
  
# PHP geoip module  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends \  
libgeoip-dev \  
&& pecl install geoip \  
&& echo "extension=geoip.so" > /usr/local/etc/php/conf.d/ext-geoip.ini \  
&& rm -rf /var/lib/apt/lists/*  
  
# php.ini  
COPY assets/php.ini /usr/local/etc/php/conf.d/php.ini  
  
# locales  
RUN apt-get update \  
&& apt-get install -y locales \  
&& rm -r /var/lib/apt/lists/* \  
&& locale-gen  
  
COPY assets/locale.gen /etc/locale.gen  
  
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
RUN wget http://builds.piwik.org/piwik-${PIWIK_VERSION}.tar.gz \  
&& tar --strip 1 -xzf piwik-${PIWIK_VERSION}.tar.gz \  
&& rm piwik-${PIWIK_VERSION}.tar.gz \  
&& chown -R www-data:www-data tmp config  
  
# Piwik config directory  
RUN cp -r /var/www/html/config /var/www/html/config.original/  
  
VOLUME /var/www/html/config/  
  
# GeoIP database  
RUN wget -O misc/GeoIPCity.dat.gz
http://geolite.maxmind.com/download/geoip/database/GeoLiteCity.dat.gz && \  
gunzip misc/GeoIPCity.dat.gz  
  
# Expose plugins as volume, so you can easily mount it for adding additional
plugins  
VOLUME /var/www/html/plugins/  
  
COPY assets/entrypoint.sh /entrypoint.sh  
ENTRYPOINT ["/entrypoint.sh"]  
CMD ["apache2-foreground"]  

