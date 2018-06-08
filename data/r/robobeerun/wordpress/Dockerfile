FROM wordpress:4.9.5-php5.6-fpm  
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
&& apt-get install -y rsync wget unzip \  
&& rm -rf /var/lib/apt/lists/*  
  
ENV WEB_ROOT="/var/www/html" \  
WEB_USER="www-data"  
  
RUN set -x \  
&& mkdir -p ${WEB_ROOT} \  
&& chown ${WEB_USER}.${WEB_USER} $WEB_ROOT  
  
ADD rootfs/ /  
  
RUN set -x \  
&& chmod +x /*.sh \  
&& mv /usr/local/bin/docker-entrypoint.sh /usr/local/bin/docker-entrypoint-
org.sh \  
&& ln -sf /dev/stdout /var/log/php-fpm-slow.log  
# Install plugins  
  
RUN set -x \  
&& /install_wp_plugin.sh https://downloads.wordpress.org/plugin/all-in-one-wp-
security-and-firewall.zip
'5cc8bccd322a0338526931adb9cba5da0604d0ba610a2cf55bc56c862cda7edd'  
RUN set -x \  
&& /install_wp_plugin.sh https://downloads.wordpress.org/plugin/wp-super-
cache.1.5.9.zip
'13986a20f1b8c46a5145f33f47b80d0d6ce83317361d94af32a0907718401a42'  
RUN set -x \  
&& /install_wp_plugin.sh https://downloads.wordpress.org/plugin/wp-piwik.zip
'7cb9e6e8bc551b35e0bc7c9f3aa3ce3f6c71bd6833c3d5401e7bdc791f645466'  
RUN set -x \  
&& /install_wp_plugin.sh https://downloads.wordpress.org/plugin/contact-
form-7.5.0.1.zip
'057f13f9afd6a38dbf563c362d86cd71aa1f036679c9a586915150350351669c'  
RUN set -x \  
&& /install_wp_plugin.sh https://downloads.wordpress.org/plugin/black-studio-
tinymce-widget.2.6.2.zip
'4a771904f28bf47ab2fd2bea1672bd7e5ab1becca4fd756a41acf149f67f4244'  
RUN set -x \  
&& /install_wp_plugin.sh https://downloads.wordpress.org/plugin/wp-
optimize.2.2.3.zip
'59c811df5c168ad5cf7b6ce4da9d45859b6b8276bc70504d80b665d1088782f4'  
RUN set -x \  
&& /install_wp_plugin.sh https://downloads.wordpress.org/plugin/the-events-
calendar.4.6.14.1.zip
'bc8ca2f8872d620f4c071bbe34847cd639d7f1f59f342054e221c9281e6758c2'  
RUN set -x \  
&& /install_wp_plugin.sh https://downloads.wordpress.org/plugin/broken-link-
checker.1.11.5.zip
'd9809a17fe79d274f903267341bb82b00a1c215a2e6c161b154eecf5c381f0b3'  
RUN set -x \  
&& /install_wp_plugin.sh https://downloads.wordpress.org/plugin/add-to-
any.1.7.25.zip
'926808945fc8293a7e3fe5b77fa5303f19bb7420a43c49484f0b7b8c8af5a038'  
RUN set -x \  
&& /install_wp_plugin.sh https://downloads.wordpress.org/plugin/cookie-
notice.1.2.42.zip
'da10e21fd480cf2d222ae07afbf33153cafe098424f5d49511771fd2d6a9f56e'  
RUN set -x \  
&& /install_wp_plugin.sh
https://downloads.wordpress.org/plugin/akismet.4.0.3.zip
'97bfb53e1fa15d6e830ee4b8530acc7fc2a0b15fcdc2d9f22592b5378ba03e5b'  
RUN set -x \  
&& /install_wp_plugin.sh https://downloads.wordpress.org/plugin/favicon-by-
realfavicongenerator.zip
'9721141ed1df9b4286fbef4b9e8b2a30bbae8d5d1342a30701017be852eeada3'  
RUN set -x \  
&& /install_wp_plugin.sh https://downloads.wordpress.org/plugin/wp-mail-
smtp.zip '82726c57fc010e8e9f71f036528f5287ab07d79d5287724c7901c84b1b128502'  
# Install themes  
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
  
USER ${WEB_USER}  
  
WORKDIR ${WEB_ROOT}  
  
ENTRYPOINT ["/docker-entrypoint.sh"]  
  
CMD ["php-fpm"]  

