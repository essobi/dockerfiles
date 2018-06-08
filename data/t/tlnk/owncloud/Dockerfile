#Dockerfile ownloud  
FROM tlnk/ubuntu:latest  
MAINTAINER tlnk <support@tlnk.fr>  
  
ARG VERSION  
ARG BUILD_DATE  
ARG VCS_REF  
ARG URL  
  
EXPOSE 80  
#Install packages  
RUN apt-get update -y && \  
apt-get upgrade -y && \  
apt-get install -y \  
apache2 \  
libapache2-mod-php \  
php-gd \  
php-json \  
php-mysql \  
php-sqlite3 \  
php-pgsql \  
php-curl \  
php-intl \  
php-mcrypt \  
php-imagick \  
php-zip \  
php-xml \  
php-mbstring \  
php-soap \  
php-ldap \  
php-apcu \  
php-redis \  
smbclient \  
php-smbclient \  
mysql-client \  
postgresql-client \  
sqlite \  
gettext-base  
  
COPY entrypoint /entrypoint  
COPY owncloud.conf /etc/apache2/sites-available/000-default.conf  
  
RUN mkdir /var/www/owncloud && \  
mkdir /var/www/owncloud/data && \  
mkdir /var/www/owncloud/config && \  
wget -qO- -O owncloud-${VERSION}.zip
https://download.owncloud.org/community/owncloud-${VERSION}.zip && \  
unzip owncloud-${VERSION}.zip -d /var/www && \  
rm owncloud-${VERSION}.zip && \  
chown -R www-data:www-data /var/www/owncloud && \  
a2enmod rewrite headers && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* /etc/apache2/sites-
available/default-ssl.conf && \  
rm -rf /var/www/html && \  
chmod +x /entrypoint/*sh && \  
chmod +x /entrypoint/entrypoint.d/*.sh  
  
WORKDIR /var/www/owncloud  
  
ENTRYPOINT ["/bin/bash", "/entrypoint/entrypoint.sh"]  
CMD ["/usr/sbin/apache2ctl", "-D", "FOREGROUND"]  
  
LABEL org.label-schema.version=$VERSION  
LABEL org.label-schema.build-date=$BUILD_DATE  
LABEL org.label-schema.vcs-ref=$VCS_REF  
LABEL org.label-schema.vcs-url="https://github.com/tle06/owncloud.git"  
LABEL org.label-schema.name="ownCloud"  
LABEL org.label-schema.vendor="ownCloud GmbH"  
LABEL org.label-schema.schema-version="1.0"

