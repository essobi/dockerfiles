FROM dinkel/nginx-phpfpm  
  
MAINTAINER Christian Luginbühl <dinkel@pimprecords.com>  
  
ENV OWNCLOUD_VERSION 8.2.2  
  
ENV OWNCLOUD_APP_ANTIVIRUS_VERSION 8.2.2  
  
RUN apt-get update && \  
DEBIAN_FRONTEND=noninteractive apt-get install --no-install-recommends -y \  
libav-tools \  
bzip2 \  
curl \  
# libreoffice \  
php5-apcu \  
php5-curl \  
php5-gd \  
php5-imagick \  
php5-imap \  
php5-intl \  
php5-ldap \  
php5-mcrypt \  
php5-mysql \  
php5-pgsql \  
php5-sqlite \  
smbclient && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
RUN curl
https://download.owncloud.org/community/owncloud-$OWNCLOUD_VERSION.tar.bz2 |
tar jx -C /var/ && \  
mv /var/owncloud/ /var/www/  
  
RUN curl -L
https://github.com/owncloud/files_antivirus/archive/v$OWNCLOUD_APP_ANTIVIRUS_VERSION.tar.gz
| tar zx -C /var/www/apps && \  
mv /var/www/apps/files_antivirus-$OWNCLOUD_APP_ANTIVIRUS_VERSION
/var/www/apps/files_antivirus  
  
RUN mv /var/www/apps /var/www/apps.dist && \  
mv /var/www/config /var/www/config.dist && \  
mkdir -p /var/www/apps /var/www/config /var/www/data && \  
chown -R www-data:www-data /var/www/apps /var/www/config /var/www/data && \  
find /var/www/apps.dist -type d -exec chmod 750 {} \; && \  
find /var/www/config.dist -type d -exec chmod 750 {} \; && \  
find /var/www/data -type d -exec chmod 750 {} \; && \  
find /var/www/apps.dist -type f -exec chmod 640 {} \; && \  
find /var/www/config.dist -type f -exec chmod 640 {} \; && \  
find /var/www/data -type f -exec chmod 640 {} \;  
  
RUN rm -rf /var/www/apps.dist/updater  
  
COPY default.conf /etc/nginx/conf.d/  
  
COPY www.conf /etc/php5/fpm/pool.d/  
  
COPY bootstrap.sh /  
  
ENTRYPOINT ["/bootstrap.sh"]  
  
VOLUME ["/var/www/apps", "/var/www/config", "/var/www/data"]  
  
# This script comes from the parent image  
CMD ["/run.sh"]  

