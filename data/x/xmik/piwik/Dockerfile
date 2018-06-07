FROM php:5.6-apache  
  
MAINTAINER pierre@piwik.org  
  
RUN apt-get update && apt-get install -y \  
libjpeg-dev \  
libfreetype6-dev \  
libgeoip-dev \  
libpng12-dev \  
libldap2-dev \  
zip \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN docker-php-ext-configure gd --with-freetype-dir=/usr --with-png-dir=/usr
--with-jpeg-dir=/usr \  
&& docker-php-ext-configure ldap --with-libdir=lib/x86_64-linux-gnu/ \  
&& docker-php-ext-install -j$(nproc) gd mbstring mysql pdo_mysql zip ldap
opcache  
  
RUN pecl install APCu geoip  
  
ENV PIWIK_VERSION 3.1.1  
RUN curl -fsSL -o piwik.tar.gz \  
"https://builds.piwik.org/piwik-${PIWIK_VERSION}.tar.gz" \  
&& curl -fsSL -o piwik.tar.gz.asc \  
"https://builds.piwik.org/piwik-${PIWIK_VERSION}.tar.gz.asc" \  
&& export GNUPGHOME="$(mktemp -d)" \  
&& gpg --keyserver ha.pool.sks-keyservers.net --recv-keys
814E346FA01A20DBB04B6807B5DBD5925590A237 \  
&& gpg --batch --verify piwik.tar.gz.asc piwik.tar.gz \  
&& rm -r "$GNUPGHOME" piwik.tar.gz.asc \  
&& tar -xzf piwik.tar.gz -C /usr/src/ \  
&& rm piwik.tar.gz  
  
COPY php.ini /usr/local/etc/php/php.ini  
  
RUN curl -fsSL -o /usr/src/piwik/misc/GeoIPCity.dat.gz
http://geolite.maxmind.com/download/geoip/database/GeoLiteCity.dat.gz \  
&& gunzip /usr/src/piwik/misc/GeoIPCity.dat.gz  
  
COPY docker-entrypoint.sh /entrypoint.sh  
  
# WORKDIR is /var/www/html (inherited via "FROM php")  
# "/entrypoint.sh" will populate it at container startup from /usr/src/piwik  
VOLUME /var/www/html  
  
# For OpenShift:  
# Run apache2 on a custom port (8080), because openshift makes apache run  
# as a non-root user and he does not have access to port 80.  
# https://askubuntu.com/a/338239  
# https://github.com/openshift/origin/issues/6629  
RUN sed -i "s/Listen 80/Listen 8080/g" /etc/apache2/ports.conf && sed -i
"s/<VirtualHost \\*:80>/<VirtualHost \\*:8080>/g" /etc/apache2/sites-
enabled/000-default.conf  
# In order to drop the root user, we have to make some directories world  
# writeable as OpenShift default security model is to run the container under  
# random UID.  
RUN mkdir -p /var/run/apache2 && chmod 777 -R /var/run/apache2 &&\  
mkdir -p /var/log/apache2 && chmod 777 -R /var/log/apache2 &&\  
mkdir -p /var/lock/apache2 && chmod 777 -R /var/lock/apache2  
# Compare also with: https://github.com/sclorg/s2i-php-container/  
ENTRYPOINT ["/entrypoint.sh"]  
CMD ["apache2-foreground"]  

