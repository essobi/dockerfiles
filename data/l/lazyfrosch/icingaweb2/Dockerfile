FROM alpine:3.7  
RUN apk add --no-cache \  
php7-fpm \  
ca-certificates \  
curl \  
nginx \  
php7-ctype \  
php7-curl \  
php7-dom \  
php7-fpm \  
php7-gettext \  
php7-gd \  
php7-iconv \  
php7-intl \  
php7-json \  
php7-ldap \  
php7-mbstring \  
php7-openssl \  
php7-pdo_mysql \  
php7-pdo_pgsql \  
php7-pear \  
php7-pgsql \  
php7-session \  
php7-xml \  
yaml \  
&& apk add --no-cache build-base php7-dev yaml-dev \  
&& (yes '' | pecl install yaml) \  
&& (yes '' | pecl install xdebug) \  
&& apk del --no-cache build-base php7-dev yaml-dev  
  
ENV ICINGAWEB_VERSION=2.5.3  
RUN curl -o /tmp/icingaweb2.tar.gz -SL
"https://github.com/Icinga/icingaweb2/archive/v${ICINGAWEB_VERSION}.tar.gz" \  
&& mkdir /usr/share/icingaweb2 \  
&& tar xf /tmp/icingaweb2.tar.gz --strip-components=1 -C /usr/share/icingaweb2
\  
&& rm -f /tmp/icingaweb2.tar.gz \  
&& ln -s /usr/share/icingaweb2/bin/icingacli /usr/local/bin/icingacli  
  
VOLUME /etc/icingaweb2  
  
#RUN (echo "en_US.UTF-8 UTF-8"; echo "de_DE.UTF-8 UTF-8"; echo "fr_FR.UTF-8
UTF-8") >> /etc/locale.gen \  
# && DEBIAN_FRONTEND=noninteractive dpkg-reconfigure locales  
RUN cd /etc/php7 \  
&& echo 'date.timezone = UTC' > conf.d/timezone.ini \  
&& echo 'extension=yaml.so' > conf.d/yaml.ini \  
&& { \  
echo 'zend_extension=/usr/lib/php7/modules/xdebug.so'; \  
echo; \  
echo '[Xdebug]'; \  
echo 'xdebug.remote_enable=true'; \  
echo 'xdebug.remote_connect_back=true'; \  
echo 'xdebug.profiler_enable=0'; \  
echo 'xdebug.profiler_output_dir=/tmp/profile'; \  
echo 'xdebug.profiler_enable_trigger=1'; \  
} | tee conf.d/xdebug.ini.disabled \  
&& { \  
echo '[global]'; \  
echo 'error_log = /proc/self/fd/2'; \  
echo 'log_level = warn'; \  
echo; \  
echo '[www]'; \  
echo 'access.log = /dev/null'; \  
echo; \  
echo 'clear_env = no'; \  
echo; \  
echo '; Ensure worker stdout and stderr are sent to the main error log.'; \  
echo 'catch_workers_output = yes'; \  
} | tee php-fpm.d/docker.conf \  
&& { \  
echo '[global]'; \  
echo 'daemonize = no'; \  
echo; \  
echo '[www]'; \  
echo 'listen = /run/php-fpm.sock'; \  
echo 'listen.owner = nginx'; \  
echo 'listen.group = nginx'; \  
} | tee php-fpm.d/zz-docker.conf  
  
COPY root/ /  
ENTRYPOINT ["/entrypoint.sh"]  
  
EXPOSE 80  
CMD ["/startup.sh"]  
  
# vi: ts=4 sw=4 noexpandtab  

