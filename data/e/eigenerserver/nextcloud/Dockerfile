FROM eigenerserver/apache2:1.0  
LABEL description="Hedgehog Cloud by www.eigener-server.ch
https://www.eigener-server.ch/en/igel-cloud \  
is licensed under a Creative Commons Attribution 4.0 International Lizenz \  
http://creativecommons.org/licenses/by/4.0/ \  
To remove the links visit https://www.eigener-server.ch/en/igel-cloud"  
  
RUN apt-get update && \  
apt-get install -y --no-install-recommends wget bzip2 cron sudo supervisor &&
\  
apt-get install -y --no-install-recommends --reinstall ca-certificates && \  
apt-get install -y --no-install-recommends libmagickwand-dev && \  
pecl install imagick && docker-php-ext-enable imagick && \  
docker-php-ext-install json && \  
docker-php-ext-install ctype && \  
docker-php-ext-install dom && \  
docker-php-ext-install posix && \  
docker-php-ext-install zip && \  
apt install -y --no-install-recommends libcurl3-dev && \  
docker-php-ext-install curl && \  
apt install -y --no-install-recommends libicu-dev && \  
docker-php-ext-install intl && \  
docker-php-ext-install fileinfo && \  
docker-php-ext-install bz2 && \  
apt install -y --no-install-recommends libldap2-dev && \  
docker-php-ext-configure ldap --with-libdir=lib/x86_64-linux-gnu && \  
docker-php-ext-install ldap && \  
docker-php-ext-install xml && \  
docker-php-ext-install mbstring && \  
pecl install APCu && \  
docker-php-ext-enable apcu && \  
pecl install redis && \  
docker-php-ext-enable redis && \  
docker-php-ext-enable opcache && \  
apt install -y --no-install-recommends sudo && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/*  
  
ENV NEXTCLOUD_VERSION=12.0.7  
ENV NEXTCLOUD_GPG="2880 6A87 8AE4 23A2 8372 792E D758 99B9 A724 937A"  
RUN cd /tmp && \  
NEXTCLOUD_DOWNLOAD="nextcloud-${NEXTCLOUD_VERSION}.tar.bz2" && \  
wget -q https://download.nextcloud.com/server/releases/${NEXTCLOUD_DOWNLOAD}
&& \  
wget -q
https://download.nextcloud.com/server/releases/${NEXTCLOUD_DOWNLOAD}.sha256 &&
\  
wget -q
https://download.nextcloud.com/server/releases/${NEXTCLOUD_DOWNLOAD}.asc && \  
wget -q https://nextcloud.com/nextcloud.asc && \  
CHECK_1="$(echo -n $(sha256sum -c ${NEXTCLOUD_DOWNLOAD}.sha256) | tail -c 2)"
&& \  
if [ "${CHECK_1}" != "OK" ]; then echo "Checksum match error: ${CHECK_1}" &&
exit 1; fi && \  
gpg --import nextcloud.asc && \  
CHECK_2="$(echo -n $(gpg --verify nextcloud-12.0.7.tar.bz2.asc
nextcloud-12.0.7.tar.bz2 2>&1 \  
| sed -n -e 's/^.*Primary key fingerprint: //p' ))" && \  
if [ "${CHECK_2}" != "${NEXTCLOUD_GPG}" ]; then echo "Fingerprint match error:
${CHECK_2}" && exit 1; fi && \  
  
mkdir -p /var/www/html && \  
tar xjvf ${NEXTCLOUD_DOWNLOAD} --strip 1 \--owner='root' \--group='www-data'
-C /var/www/html && \  
rm -rf /tmp/*  
  
RUN a2enmod rewrite && \  
a2enmod headers && \  
a2enmod env && \  
a2enmod dir && \  
a2enmod mime  
  
COPY nextcloud.conf /etc/apache2/sites-available/nextcloud.conf  
RUN ln -s /etc/apache2/sites-available/nextcloud.conf /etc/apache2/sites-
enabled/nextcloud.conf  
  
################################################################################  
# License Dont remove this -> see https://www.eigener-server.ch/en/igel-cloud/
#  
COPY defaults.php /host/  
################################################################################  
ENV NEXTCLOUD_DB_NAME=eigenerserver  
ENV NEXTCLOUD_DB_USER=eigenerserver  
ENV NEXTCLOUD_DB_PASSWORD=eigenerserver  
ENV NEXTCLOUD_DOMAIN=eigener-server.ch  
ENV NEXTCLOUD_ADMIN_PASSWORD=eigenerserver  
  
VOLUME ["/host/nextcloud"]  
  
RUN mkdir -p /var/log/supervisor && \  
mkdir -p /etc/supervisor/conf.d  
  
COPY run.sh /usr/local/bin/run.sh  
COPY permissions.sh /usr/local/bin/permissions.sh  
RUN chmod +x /usr/local/bin/*  
RUN /usr/local/bin/permissions.sh  
  
COPY crontab.txt /crontab.txt  
RUN /usr/bin/crontab /crontab.txt  
  
COPY supervisord.conf /etc/supervisor/conf.d/nextcloud.conf  
  
ENTRYPOINT ["/bin/bash","/usr/local/bin/run.sh"]  
  
CMD ["/usr/bin/supervisord"]  

