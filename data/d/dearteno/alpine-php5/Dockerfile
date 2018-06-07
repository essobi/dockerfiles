FROM dearteno/alpine-base  
MAINTAINER Pichate Ins <cogent@cogentwebworks.com>  
  
ENV TIMEZONE Asia/Bangkok  
ENV PHP_MEMORY_LIMIT 512M  
ENV MAX_UPLOAD 50M  
ENV PHP_MAX_FILE_UPLOAD 200  
ENV PHP_MAX_POST 100M  
  
# Install packages  
RUN apk-install git curl tzdata php5 php5-fpm php5-pear php5-apcu php5-bcmath
php5-bz2 php5-cli php5-ctype php5-curl php5-dom php5-exif php5-gd php5-gettext
php5-iconv php5-intl php5-json php5-mcrypt php5-memcache php5-mysql
php5-mysqli php5-openssl php5-pcntl php5-pdo_mysql php5-pdo_pgsql
php5-pdo_sqlite php5-phar php5-posix php5-soap php5-xcache php5-xmlreader
php5-xmlrpc php5-xsl php5-zip php5-zlib  
  
# Configure PHP-FPM  
COPY config/fpm-pool.conf /etc/php5/fpm.d/zzz_custom.conf  
COPY config/php.ini /etc/php5/conf.d/zzz_custom.ini  
RUN mkdir -p /var/log/php-fpm  
RUN touch /var/log/php-fpm/fpm-error.log  
  
# SED php.ini  
RUN sed -i -e "s|;daemonize\s*=.*|daemonize = no|" -e "s|listen\s*=.*|listen =
9000|" /etc/php5/php-fpm.conf  
RUN sed -i "s|;*date.timezone =.*|date.timezone = ${TIMEZONE}|i"
/etc/php5/php.ini && \  
sed -i "s|;*memory_limit =.*|memory_limit = ${PHP_MEMORY_LIMIT}|i"
/etc/php5/php.ini && \  
sed -i "s|;*upload_max_filesize =.*|upload_max_filesize = ${MAX_UPLOAD}|i"
/etc/php5/php.ini && \  
sed -i "s|;*max_file_uploads =.*|max_file_uploads = ${PHP_MAX_FILE_UPLOAD}|i"
/etc/php5/php.ini && \  
sed -i "s|;*post_max_size =.*|post_max_size = ${PHP_MAX_POST}|i"
/etc/php5/php.ini && \  
sed -i "s|;*cgi.fix_pathinfo=.*|cgi.fix_pathinfo= 0|i" /etc/php5/php.ini  
  
RUN pear channel-update pear.php.net && \  
pear upgrade-all && \  
pear config-set auto_discover 1 && \  
# Install composer global bin  
curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin/ --filename=composer && \  
# PECL workaround  
sed -i "s/ -n / /" $(which pecl) && \  
# Clean up  
apk del tzdata && \  
rm -rf /var/cache/apk/* && \  
rm -rf /var/lib/apt/lists/* && \  
rm -rf /tmp/*  
# root filesystem (S6 config files)  
COPY rootfs /  
  
EXPOSE 9000  
# S6 init script  
ENTRYPOINT [ "/init" ]  

