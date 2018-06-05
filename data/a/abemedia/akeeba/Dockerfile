FROM php:7.1-apache  
LABEL maintainer="Michael Babker <michael.babker@joomla.org> (@mbabker)"  
# Disable remote database security requirements.  
ENV JOOMLA_INSTALLATION_DISABLE_LOCALHOST_CHECK=1  
# Enable Apache Rewrite Module  
RUN a2enmod rewrite  
  
# Install PHP extensions  
RUN set -ex; \  
\  
savedAptMark="$(apt-mark showmanual)"; \  
\  
apt-get update; \  
apt-get install -y --no-install-recommends \  
libbz2-dev \  
libjpeg-dev \  
libldap2-dev \  
libmemcached-dev \  
libpng-dev \  
libpq-dev \  
; \  
\  
docker-php-ext-configure gd --with-png-dir=/usr --with-jpeg-dir=/usr; \  
debMultiarch="$(dpkg-architecture --query DEB_BUILD_MULTIARCH)"; \  
docker-php-ext-configure ldap --with-libdir="lib/$debMultiarch"; \  
docker-php-ext-install \  
bz2 \  
gd \  
ldap \  
mysqli \  
pdo \  
pdo_mysql \  
pdo_pgsql \  
pgsql \  
zip \  
; \  
\  
pecl install \  
APCu-5.1.10 \  
memcached-3.0.4 \  
redis-3.1.6 \  
; \  
\  
docker-php-ext-enable \  
apcu \  
memcached \  
redis \  
; \  
\  
# reset apt-mark's "manual" list so that "purge --auto-remove" will remove all
build dependencies  
apt-mark auto '.*' > /dev/null; \  
apt-mark manual $savedAptMark; \  
ldd "$(php -r 'echo ini_get("extension_dir");')"/*.so \  
| awk '/=>/ { print $3 }' \  
| sort -u \  
| xargs -r dpkg-query -S \  
| cut -d: -f1 \  
| sort -u \  
| xargs -rt apt-mark manual; \  
\  
apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false;
\  
rm -rf /var/lib/apt/lists/*  
  
VOLUME /var/www/html  
  
# Define Kickstart version  
ENV AKEEBA_KICKSTART_VERSION 5.4.2  
  
# Download package and extract to web volume  
RUN v=`echo $AKEEBA_KICKSTART_VERSION | tr "." "-"` \  
&& curl -o kickstart.zip -SL
https://www.akeebabackup.com/download/official/akeeba-
kickstart/${v}/kickstart-core-${v}-zip.zip \  
&& php -r '$z = new ZipArchive; $z->open("kickstart.zip");
$z->extractTo("./kickstart");' \  
&& mv kickstart/kickstart.php /usr/src/ \  
&& rm -rf kickstart* \  
&& chown -R www-data:www-data /usr/src/kickstart.php  
  
# Copy init scripts and custom .htaccess  
COPY docker-entrypoint.sh /entrypoint.sh  
COPY makedb.php /makedb.php  
  
ENTRYPOINT ["/entrypoint.sh"]  
CMD ["apache2-foreground"]  

