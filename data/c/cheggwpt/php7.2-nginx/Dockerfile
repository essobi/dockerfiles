FROM php:7.2-fpm-alpine3.7  
LABEL maintainer="Joel Gilley jgilley@chegg.com"  
  
ENV TIMEZONE=UTC \  
ENV=/etc/profile \  
APP_ENV=development  
  
RUN apk --update add dumb-init ca-certificates nginx supervisor bash && \  
apk add --virtual .build_package git curl build-base autoconf dpkg-dev \  
file libmagic re2c && \  
apk add --virtual .deps_run libxpm freetype xextproto inputproto xtrans \  
libwebp libxext libxt libx11 libxcb libxau libsm libice libxdmcp \  
libbsd xproto libuuid kbproto libpthread-stubs libpng tidyhtml-libs \  
tidyhtml libmemcached-libs zlib freetds unixodbc readline libpq \  
gettext-asprintf gettext-libs libintl gettext libunistring libldap zlib \  
icu-libs libmemcached cyrus-sasl libmcrypt hiredis gmp && \  
apk add --virtual .build_deps libxau-dev libbsd-dev libxdmcp-dev libxcb-dev \  
libx11-dev libxext-dev libice-dev libsm-dev libxt-dev libxpm-dev libpng-dev \  
freetype-dev libjpeg-turbo-dev libwebp-dev bzip2-dev gettext-dev gmp-dev \  
icu-dev freetds-dev postgresql-dev libxml2-dev tidyhtml-dev zlib-dev \  
libmemcached-dev cyrus-sasl-dev libmcrypt-dev hiredis-dev tzdata  
  
RUN cp /usr/share/zoneinfo/${TIMEZONE} /etc/localtime && \  
echo "${TIMEZONE}" > /etc/timezone && \  
update-ca-certificates && \  
rm -rf /etc/nginx/conf.d/default.conf && \  
mv /etc/profile.d/color_prompt /etc/profile.d/color_prompt.sh && \  
echo alias dir=\'ls -alh --color\' >> /etc/profile && \  
echo 'source ~/.profile' >> /etc/profile && \  
echo 'cat /etc/os-release' >> ~/.profile && \  
mkdir -p /app /run/nginx && \  
chown -R nginx:www-data /run/nginx && \  
chown -R :www-data /app && \  
chmod -R g+rw /app  
  
# Install known pacakages with docker-php-ext-install, install others with
pecl install  
RUN docker-php-ext-install -j$(nproc) bcmath bz2 gd gettext gmp intl mysqli \  
pdo_dblib pdo_mysql session soap tidy opcache zip && \  
pecl install apcu && \  
pecl install memcached && \  
pecl install mcrypt channel://pecl.php.net/mcrypt-1.0.1  
  
# Install phpiredis  
ENV phpiredis_version=1.0.0  
RUN echo INSTALL PHPIREDIS PHP MODULE && \  
curl -L "https://github.com/nrk/phpiredis/archive/v${phpiredis_version}.zip" \  
\--output "/tmp/phpiredis-${phpiredis_version}.zip" && \  
cd /tmp && unzip "/tmp/phpiredis-${phpiredis_version}.zip" && \  
cd phpiredis-${phpiredis_version} && \  
phpize && ./configure --enable-phpiredis && \  
make && make install && \  
cd /tmp && rm -rf phpiredis-${phpiredis_version}
phpiredis-${phpiredis_version}.zip  
  
# Install tideways  
ENV tideways_version=1.5.3 \  
tideways_ext_version=4.1.5 \  
tideways_php_version=2.0.16 \  
tideways_dl=https://github.com/tideways/  
RUN echo INSTALL TIDEWAYS PHP MODULE && \  
curl -L "${tideways_dl}/php-profiler-
extension/archive/v${tideways_ext_version}.zip" \  
\--output "/tmp/v${tideways_ext_version}.zip" && \  
cd /tmp && unzip "v${tideways_ext_version}.zip" && \  
cd "php-xhprof-extension-${tideways_ext_version}" && \  
phpize && \  
./configure && \  
make && make install && \  
cd /tmp && rm -rf php-xhprof-extension-${tideways_ext_version}/
v${tideways_ext_version}.zip && \  
echo INSTALL TIDEWAYS PROFILER && \  
curl -L
"${tideways_dl}/profiler/releases/download/v${tideways_php_version}/Tideways.php"
\  
\--output "$(php-config --extension-dir)/Tideways.php" && \  
ls -l "$(php-config --extension-dir)/Tideways.php" && \  
echo INSTALL TIDEWAYS DAEMON && \  
curl -L "https://s3-eu-
west-1.amazonaws.com/tideways/daemon/${tideways_version}/tideways-
daemon-v${tideways_version}-alpine.tar.gz" \  
\--output "/tmp/tideways-daemon-v${tideways_version}-alpine.tar.gz" && \  
cd /tmp && tar -zxf tideways-daemon-v${tideways_version}-alpine.tar.gz && \  
mv build/dist/tideways-daemon /usr/bin && \  
ls -l /usr/bin/tideways-daemon && \  
mkdir -p /var/run/tideways && \  
cd /tmp && rm -rf build/ tideways-daemon-v${tideways_version}-alpine.tar.gz  
  
# enable the above  
RUN docker-php-ext-enable apcu memcached mcrypt phpiredis tideways  
  
# Add the process control directories for PHP  
# make it user/group read write  
RUN mkdir -p /run/php && \  
chown -R www-data:www-data /run/php  
  
# Report on PHP build  
RUN php -m && \  
php -v  
  
# clean up apk  
RUN apk del .build_deps && \  
rm -rf /var/cache/apk/*  
  
# Add the config files  
COPY container_confs /  
RUN chmod a+x /entrypoint.sh /wait-for-it.sh /start_tideways.sh  
  
WORKDIR /app  
  
# Expose the ports for nginx  
EXPOSE 80 443  
# the entry point definition  
ENTRYPOINT ["/entrypoint.sh"]  
  
# default command for entrypoint.sh  
CMD ["supervisor"]  

