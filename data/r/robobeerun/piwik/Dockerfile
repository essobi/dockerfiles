FROM piwik:3.3.0-fpm  
LABEL maintainer "Erwin Mueller <erwin@muellerpublic.de>"  
  
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
&& apt-get install -y rsync \  
&& rm -rf /var/lib/apt/lists/*  
  
ENV WEB_ROOT="/var/www/html" \  
WEB_USER="www-data"  
  
RUN set -x \  
&& mkdir -p ${WEB_ROOT} \  
&& chown ${WEB_USER}.${WEB_USER} $WEB_ROOT  
  
# Php configuration.  
  
ENV DEBUG="false" \  
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
&& chmod +x /*.sh \  
&& mv /entrypoint.sh /entrypoint-old.sh \  
&& ln -sf /dev/stdout /var/log/php-fpm-slow.log  
  
USER ${WEB_USER}  
  
WORKDIR ${WEB_ROOT}  
  
ENTRYPOINT ["/docker-entrypoint.sh"]  
  
CMD ["php-fpm"]  

