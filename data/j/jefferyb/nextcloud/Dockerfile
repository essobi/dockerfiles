FROM php:7.1-apache  
MAINTAINER Jeffery Bagirimvano <jeffery.rukundo@gmail.com>  
  
# Using Installing Nextcloud From the Command Line  
#
https://docs.nextcloud.com/server/9/admin_manual/installation/command_line_installation.html  
  
# nextcloud directory  
ENV WEB_INSTALL true  
ENV DATABASE mysql  
ENV DATABASE_NAME nextcloud  
ENV DATABASE_HOST mysql  
ENV DATABASE_USER root  
ENV DATABASE_ROOT_PASSWORD Chang3m3t0an0th3r  
ENV DATABASE_TABLE_PREFIX oc_  
ENV ADMIN_USER admin  
ENV ADMIN_PASS password  
ENV NEXTCLOUD_HOME /var/www/html  
ENV NEXTCLOUD_DATA $NEXTCLOUD_HOME/data  
ENV EXTERNAL_URL=""  
ENV ENABLE_SSL false  
ENV MEMCACHE false  
ENV TERM=xterm  
  
  
RUN \  
apt-get update && \  
apt-get install -y \  
libbz2-dev \  
bzip2 \  
libcurl4-openssl-dev \  
libfreetype6-dev \  
libicu-dev \  
libjpeg-dev \  
libldap2-dev \  
libmcrypt-dev \  
libmemcached-dev \  
libpng12-dev \  
libpq-dev \  
libxml2-dev \  
netcat \  
sudo \  
curl \  
w3m \  
unzip  
  
#
https://docs.nextcloud.com/server/9/admin_manual/installation/source_installation.html#prerequisites  
RUN docker-php-ext-configure gd --with-png-dir=/usr --with-jpeg-dir=/usr \  
&& docker-php-ext-configure ldap --with-libdir=lib/x86_64-linux-gnu/ \  
&& docker-php-ext-install exif gd intl ldap mbstring mcrypt mysqli opcache
pdo_mysql pdo_pgsql pgsql zip bz2  
  
  
# set recommended PHP.ini settings  
# see
https://docs.nextcloud.com/server/12/admin_manual/configuration_server/server_tuning.html#enable-
php-opcache  
RUN { \  
echo 'opcache.memory_consumption=128'; \  
echo 'opcache.interned_strings_buffer=8'; \  
echo 'opcache.max_accelerated_files=10000'; \  
echo 'opcache.revalidate_freq=1'; \  
echo 'opcache.fast_shutdown=1'; \  
echo 'opcache.enable_cli=1'; \  
echo 'opcache.enable=1'; \  
echo 'opcache.save_comments=1'; \  
} > /usr/local/etc/php/conf.d/opcache-recommended.ini  
RUN a2enmod rewrite && a2enmod headers  
  
# PECL extensions  
RUN set -ex \  
&& pecl install APCu-5.1.8 \  
&& pecl install memcached-3.0.2 \  
&& pecl install redis-3.1.1 \  
&& docker-php-ext-enable apcu redis memcached  
RUN a2enmod rewrite  
  
# Get nextcloud version  
RUN NEXTCLOUD_VERSION=$(w3m https://nextcloud.com/install/#instructions-server
-dump | grep -m 1 "Latest stable version" | sed 's/Latest stable version: //'
| sed 's/.(.*//') && \  
mkdir /root/setup && \  
cd /root/setup && \  
curl -O
https://download.nextcloud.com/server/releases/nextcloud-${NEXTCLOUD_VERSION}.zip
&& \  
curl -O
https://download.nextcloud.com/server/releases/nextcloud-${NEXTCLOUD_VERSION}.zip.md5
&& \  
# Verify the MD5  
md5sum -c nextcloud-${NEXTCLOUD_VERSION}.zip.md5 <
nextcloud-${NEXTCLOUD_VERSION}.zip && \  
curl -O
https://download.nextcloud.com/server/releases/nextcloud-${NEXTCLOUD_VERSION}.zip.asc
&& \  
curl -O https://nextcloud.com/nextcloud.asc && \  
gpg --import nextcloud.asc && \  
gpg --verify nextcloud-${NEXTCLOUD_VERSION}.zip.asc
nextcloud-${NEXTCLOUD_VERSION}.zip && \  
# Setup  
unzip nextcloud-${NEXTCLOUD_VERSION}.zip && \  
rm -fr $NEXTCLOUD_HOME && \  
cp -r nextcloud $NEXTCLOUD_HOME && \  
chown -R www-data:www-data $NEXTCLOUD_HOME && \  
cd && rm -fr /root/setup  
  
# set recommended Strong Directory Permissions settings  
# see
https://docs.nextcloud.com/server/9/admin_manual/installation/installation_wizard.html#setting-
strong-directory-permissions  
RUN echo "#!/bin/bash \n\  
ncpath='/var/www/html' \n\  
htuser='www-data' \n\  
htgroup='www-data' \n\  
rootuser='root' \n\  
\n\  
printf \"Creating possible missing Directories\n\" \n\  
mkdir -p \$ncpath/data \n\  
mkdir -p \$ncpath/assets \n\  
mkdir -p \$ncpath/updater \n\  
\n\  
printf \"chmod Files and Directories\n\" \n\  
find \${ncpath} -type f -print0 | xargs -0 chmod 0640 \n\  
find \${ncpath} -type d -print0 | xargs -0 chmod 0750 \n\  
\n\  
printf \"chown Directories\n\" \n\  
chown -R \${rootuser}:\${htgroup} \${ncpath} \n\  
chown -R \${htuser}:\${htgroup} \${ncpath}/.htaccess \n\  
chown -R \${htuser}:\${htgroup} \${ncpath}/.user.ini \n\  
chown -R \${htuser}:\${htgroup} \${ncpath}/apps/ \n\  
chown -R \${htuser}:\${htgroup} \${ncpath}/assets/ \n\  
chown -R \${htuser}:\${htgroup} \${ncpath}/config/ \n\  
chown -R \${htuser}:\${htgroup} \${ncpath}/data/ \n\  
chown -R \${htuser}:\${htgroup} \${ncpath}/themes/ \n\  
chown -R \${htuser}:\${htgroup} \${ncpath}/updater/ \n\  
\n\  
chmod +x \${ncpath}/occ \n\  
\n\  
printf \"chmod/chown .htaccess\n\" \n\  
if [ -f \${ncpath}/.htaccess ] \n\  
then \n\  
chmod 0644 \${ncpath}/.htaccess \n\  
chown \${rootuser}:\${htgroup} \${ncpath}/.htaccess \n\  
fi \n\  
if [ -f \${ncpath}/data/.htaccess ] \n\  
then \n\  
chmod 0644 \${ncpath}/data/.htaccess \n\  
chown \${htgroup}:\${htgroup} \${ncpath}/.htaccess \n\  
chown \${rootuser}:\${htgroup} \${ncpath}/data/.htaccess \n\  
fi \n\  
" > /usr/local/bin/nextcloud_permissions && \  
chmod +x /usr/local/bin/nextcloud_permissions  
  
EXPOSE 80 443  
  
VOLUME ${NEXTCLOUD_DATA} $NEXTCLOUD_HOME/config  
  
CMD \  
nextcloud_permissions && \  
if [ $WEB_INSTALL = false ] ; then \  
while ! nc -z "$DATABASE_HOST" 3306; do sleep 3; done; \  
if [ ! -f "$NEXTCLOUD_HOME/config/config.php" ] ; then cd "$NEXTCLOUD_HOME" &&
sudo -u www-data php occ maintenance:install \  
\--database "${DATABASE}" \  
\--database-name "${DATABASE_NAME}" \  
\--database-host "${DATABASE_HOST}" \  
\--database-user "${DATABASE_USER}" \  
\--database-pass "${DATABASE_ROOT_PASSWORD}" \  
\--database-table-prefix "${DATABASE_TABLE_PREFIX}" \  
\--admin-user "${ADMIN_USER}" \  
\--admin-pass "${ADMIN_PASS}" \  
\--data-dir "${NEXTCLOUD_DATA}"; \  
fi; \  
fi && \  
if [ -f "$NEXTCLOUD_HOME/config/config.php" ] ; then \  
if [ $EXTERNAL_URL ] ; then grep -q -F "=> '${EXTERNAL_URL}'"
$NEXTCLOUD_HOME/config/config.php || sed -i "/0 => 'localhost'/a \ 1 =>
'${EXTERNAL_URL}'" $NEXTCLOUD_HOME/config/config.php; fi && \  
if [ $MEMCACHE = true ] ; then grep -q -F "memcache.local"
$NEXTCLOUD_HOME/config/config.php || sed -i "/'dbpassword' => /a \
'memcache.local' => '\\\OC\\\Memcache\\\APCu',"
$NEXTCLOUD_HOME/config/config.php; fi; \  
fi && \  
# Enable SSL  
if [ $ENABLE_SSL = true ] ; then \  
# Redirect to HTTPS  
DEFAULT_CONF="/etc/apache2/sites-available/000-default.conf" && \  
grep -q -F "ServerName ${EXTERNAL_URL}" ${DEFAULT_CONF} || sed -i
"/DocumentRoot \/var\/www\/html/a \ ServerName ${EXTERNAL_URL}"
${DEFAULT_CONF} && \  
grep -q -F "Redirect permanent" ${DEFAULT_CONF} || sed -i "/ServerName
${EXTERNAL_URL}/a \ Redirect permanent \/ https:\/\/${EXTERNAL_URL}\/"
${DEFAULT_CONF} && \  
  
# DEFAULT_SSL="/etc/apache2/sites-available/default-ssl.conf" && \  
# grep -q -F "ServerName ${EXTERNAL_URL}" ${DEFAULT_SSL} || sed -i
"/ServerAdmin/a \ ServerName ${EXTERNAL_URL}" ${DEFAULT_SSL} && \  
# grep -q -F "Header always set Strict-Transport-Security" ${DEFAULT_SSL} ||
sed -i "/ServerName ${EXTERNAL_URL}/a \\  
# <IfModule mod_headers.c> \\  
# Header always set Strict-Transport-Security \"max-age=15768000;
includeSubDomains; preload\" \\  
# </IfModule>" ${DEFAULT_SSL} ; \  
  
a2enmod ssl && a2ensite default-ssl ; \  
fi && \  
apache2-foreground  

