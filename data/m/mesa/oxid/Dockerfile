FROM ubuntu:16.04  
MAINTAINER Daniel Langemann <daniel.langemann@gmx.de>  
  
RUN DEBIAN_FRONTEND=noninteractive ; apt-get update; apt-get -y upgrade --fix-
missing ; apt-get -y install \  
apache2 \  
libapache2-mod-php7.0 \  
php7.0-mysql \  
php7.0-gd \  
php7.0-xml \  
php7.0-json \  
php7.0-curl \  
php7.0-mbstring \  
php7.0-bcmath \  
php7.0-soap \  
php-xdebug \  
curl \  
unzip \  
git \  
mysql-client \  
&& apt-get autoremove -y \  
&& apt-get autoclean -y \  
&& a2enmod php7.0 \  
&& a2enmod rewrite  
  
# Url to OXID repository on github  
ENV OXID_SRC_URL "https://github.com/OXID-
eSales/oxideshop_ce/archive/master.zip"  
# PHP configuration  
ENV PHP_ERROR_REPORTING "-1"  
ENV PHP_MEMORY_LIMIT "256M"  
ENV PHP_DATE_TIMEZONE "Europe/Berlin"  
ENV PHP_DISPLAY_ERRORS "On"  
ENV PHP_UPLOAD_MAX_FILESIZE "8m"  
# Apache configuration  
ENV DOCKER_DOCUMENT_ROOT "/data/source/"  
ENV DOCKER_SERVER_ADMIN "admin@localhost"  
ENV DOCKER_ERROR_LOG "/dev/stdout"  
ENV DOCKER_CUSTOM_LOG "/dev/stdout combined"  
ENV DOCKER_ALLOW_OVERRIDE "All"  
ENV APACHE_RUN_USER "www-data"  
ENV APACHE_RUN_GROUP "www-data"  
ENV APACHE_LOG_DIR "/dev/stdout"  
ENV APACHE_LOCK_DIR "/var/lock/apache"  
ENV APACHE_PID_FILE "/tmp/apache2.pid"  
ENV APACHE_SERVERNAME "localhost"  
# admin credentials are updated on every container start  
ENV OXID_ADMIN_PASSWORD "oxid"  
ENV OXID_ADMIN_USERNAME "oxid"  
# OXID configuration for config.inc.php  
ENV OXID_SHOP_URL "http://localhost"  
ENV OXID_SHOP_SSL_URL "https://localhost"  
ENV OXID_UTF_MODE 1  
ENV OXID_IDEBUG 0  
ENV OXID_COMPILE_DIR "/tmp/oxid_tmp"  
# OXID configuration, equal names for mariaDB/mysql container vars  
ENV MYSQL_HOST "oxid_db"  
ENV MYSQL_USER "oxid"  
ENV MYSQL_PASSWORD "oxid"  
ENV MYSQL_DATABASE "oxid"  
ENV COMPOSER_ALLOW_SUPERUSER 1  
ENV COMPOSER_NO_INTERACTION 1  
ENV COMPOSER_DISCARD_CHANGES 1  
# Add global composer path  
ENV PATH "/root/.composer/vendor/bin:${PATH}"  
COPY etc/ /etc/  
COPY composer.phar /usr/local/bin/composer  
  
RUN chmod +x /etc/docker-entrypoint.sh ; \  
chmod +x /etc/install_oxid.sh ; \  
mkdir -p "${DOCKER_DOCUMENT_ROOT}" ; \  
echo "ServerName ${APACHE_SERVERNAME}" | tee /etc/apache2/conf-
available/fqdn.conf ; \  
ln -s /etc/apache2/conf-available/fqdn.conf /etc/apache2/conf-enabled/ ; \  
sed -i "s/Directory \/var\/www\//Directory \$\\{DOCKER_DOCUMENT_ROOT\\}/"
/etc/apache2/apache2.conf ; \  
sed -i "s/error_reporting.\\+/error_reporting = \${PHP_ERROR_REPORTING}/"
/etc/php/7.0/cli/php.ini ; \  
sed -i "s/error_reporting.\\+/error_reporting = \${PHP_ERROR_REPORTING}/"
/etc/php/7.0/apache2/php.ini ; \  
sed -i "s/memory_limit.\\+/memory_limit= \${PHP_MEMORY_LIMIT}/"
/etc/php/7.0/cli/php.ini ; \  
sed -i "s/memory_limit.\\+/memory_limit = \${PHP_MEMORY_LIMIT}/"
/etc/php/7.0/apache2/php.ini ; \  
sed -i "s/;*date.timezone.\\+/date.timezone= \${PHP_DATE_TIMEZONE}/"
/etc/php/7.0/cli/php.ini ; \  
sed -i "s/;*date.timezone.\\+/date.timezone = \${PHP_DATE_TIMEZONE}/"
/etc/php/7.0/apache2/php.ini ; \  
sed -i "s/;*display_errors.\\+/display_errors= \${PHP_DISPLAY_ERRORS}/"
/etc/php/7.0/cli/php.ini ; \  
sed -i "s/;*display_errors.\\+/display_errors = \${PHP_DISPLAY_ERRORS}/"
/etc/php/7.0/apache2/php.ini ; \  
sed -i "s/;*upload_max_filesize.\\+/upload_max_filesize=
\${PHP_UPLOAD_MAX_FILESIZE}/" /etc/php/7.0/cli/php.ini ; \  
sed -i "s/;*upload_max_filesize.\\+/upload_max_filesize =
\${PHP_UPLOAD_MAX_FILESIZE}/" /etc/php/7.0/apache2/php.ini ; \  
echo "xdebug.remote_enable=1" >> /etc/php/7.0/apache2/php.ini ; \  
echo "xdebug.remote_connect_back=1" >> /etc/php/7.0/apache2/php.ini ; \  
chmod +x /usr/local/bin/composer  
  
VOLUME /data  
  
EXPOSE 80  
WORKDIR /data/  
  
ENTRYPOINT ["/etc/docker-entrypoint.sh"]  
  
CMD /usr/sbin/apache2ctl -D FOREGROUND

