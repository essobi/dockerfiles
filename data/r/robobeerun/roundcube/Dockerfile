FROM php:7.0.24-fpm-jessie  
  
LABEL maintainer "Erwin Mueller <erwin.mueller@deventm.com>"  
  
ARG APT_CACHE  
  
RUN set -x \  
# Optional add proxy entries for apt.  
&& if [ -n "${APT_CACHE}" ]; then \  
echo Acquire::ftp::Proxy \"$APT_CACHE\"; >> /etc/apt/apt.conf.d/08proxy;\  
echo Acquire::http::Proxy \"$APT_CACHE\"; >> /etc/apt/apt.conf.d/08proxy;\  
echo Acquire::https::Proxy \"$APT_CACHE\"; >> /etc/apt/apt.conf.d/08proxy;\  
fi  
  
RUN set -x \  
&& DEBIAN_FRONTEND=noninteractive \  
&& apt-get update \  
&& apt-get install -y \  
rsync \  
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
libpspell-dev \  
freetds-dev \  
libicu-dev \  
libpng-dev \  
libfreetype6-dev \  
git \  
file \  
unzip \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN set -x \  
&& docker-php-ext-configure gd --with-png-dir=/usr --with-jpeg-dir=/usr \  
&& debMultiarch="$(dpkg-architecture --query DEB_BUILD_MULTIARCH)" \  
&& docker-php-ext-configure ldap --with-libdir="lib/$debMultiarch" \  
&& docker-php-ext-install -j$(nproc) \  
exif gd intl ldap mbstring mcrypt opcache pdo pdo_mysql pdo_pgsql pgsql \  
zip pspell sockets  
  
WORKDIR /tmp  
  
ENV ROUNDCUBE_VERSION="1.3.4" \  
ROUNDCUBE_SRC_DIR="/usr/src/roundcube"  
  
RUN set -x \  
&& ROUNDCUBE_DIST_DIR="/usr/src/roundcubemail-${ROUNDCUBE_VERSION}" \  
&& curl -fsSL -o roundcube.tar.gz
"https://github.com/roundcube/roundcubemail/releases/download/${ROUNDCUBE_VERSION}/roundcubemail-${ROUNDCUBE_VERSION}.tar.gz"
\  
&& tar -xzf /tmp/roundcube.tar.gz -C /usr/src/ \  
&& ln -s ${ROUNDCUBE_DIST_DIR} ${ROUNDCUBE_SRC_DIR} \  
&& rm roundcube.tar.gz \  
# Install Composer to resolve Roundcube dependencies  
&& curl -fsSL -o composer-setup.php https://getcomposer.org/installer \  
&& curl -fsSL -o composer-setup.sig https://composer.github.io/installer.sig \  
&& php -r "if (hash('SHA384', file_get_contents('./composer-setup.php')) !==
trim(file_get_contents('./composer-setup.sig'))) { echo 'Invalid installer' .
PHP_EOL; exit(1); }" \  
&& php ./composer-setup.php --install-dir=/tmp --filename=composer \  
# Resolve Roudcube Composer dependencies  
&& mv ${ROUNDCUBE_SRC_DIR}/composer.json-dist
${ROUNDCUBE_SRC_DIR}/composer.json \  
&& cd ${ROUNDCUBE_SRC_DIR} \  
&& /tmp/composer install --no-dev --optimize-autoloader \  
# Resolve Roudcube JS dependencies  
# Temp fix install script,  
# details: https://github.com/roundcube/roundcubemail/pull/5819  
&& sed -i -e 's/^\\( \\+\$extract = \$CACHEDIR .\\+;\\)$/\1 mkdir(\$extract,
0774, true);/' \  
${ROUNDCUBE_SRC_DIR}/bin/install-jsdeps.sh \  
&& ${ROUNDCUBE_SRC_DIR}/bin/install-jsdeps.sh \  
# Make default Roudcube configuration log to syslog  
&& sed -i -r 's/^([^\s]{9}log_driver[^\s]{2} =) [^\s]+$/\1 "syslog";/g' \  
${ROUNDCUBE_SRC_DIR}/config/defaults.inc.php \  
# Setup serve directories  
&& rm -rf ${ROUNDCUBE_SRC_DIR}/temp/* /tmp/* \  
&& chmod u=rwX,g=rX,o=rX -R ${ROUNDCUBE_DIST_DIR}  
  
ENV DEBUG="false" \  
WEB_ROOT="/var/www/html" \  
WEB_USER="www-data" \  
PHP_MAX_EXECUTION_TIME="300" \  
PHP_MEMORY_LIMIT="128M" \  
PHP_FPM_MAX_CHILDREN="10" \  
PHP_FPM_START_SERVERS="2" \  
PHP_FPM_MIN_SPARE_SERVERS="2" \  
PHP_FPM_MAX_SPARE_SERVERS="5" \  
PHP_FPM_MAX_REQUESTS="500" \  
PHP_FPM_REQUEST_SLOWLOG_TIMEOUT="0" \  
PHP_FPM_CATCH_WORKERS_OUTPUT="1" \  
PHP_OPCACHE_ENABLE_CLI="1" \  
PHP_OPCACHE_ENABLE="1" \  
PHP_OPCACHE_MEMORY_CONSUMPTION="128" \  
PHP_OPCACHE_MAX_ACCELERATED_FILES="6000"  
  
ADD rootfs/ /  
  
RUN set -x \  
&& ln -sf /dev/stdout /var/log/php-fpm-slow.log \  
&& chmod +x /*.sh \  
&& mkdir -p ${ROUNDCUBE_SRC_DIR}/db  
  
USER www-data  
  
WORKDIR $WEB_ROOT  
  
ENTRYPOINT ["/docker-entrypoint.sh"]  
  
CMD ["php-fpm"]  

