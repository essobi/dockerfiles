FROM alpine:3.6  
LABEL author='renothing' role='php-fpm' tags='php,php5,php-fpm,php-cli'
description='php5 fpm based on alpine'  
#set language enviroments  
ENV LANG=en_US.UTF-8 LC_ALL=en_US.UTF-8 \  
TIMEZONE="Asia/Shanghai" \  
PHP_MAX_EXECUTION=900 \  
PHP_MEMORY_LIMIT=256m \  
PHP_MAX_UPLOAD_SIZE=50m \  
PHP_MAX_UPLOAD=200 \  
PHP_MAX_POST=100m \  
FPM_RESTART_THRESHOLD=30 \  
FPM_RESTART_INTERVAL=30s \  
FPM_MAX=512 \  
FPM_MAX_REQUESTS=8192 \  
FPM_SLOW_TIME=6s  
#install software  
#RUN sed -i 's/dl-cdn.alpinelinux.org/mirrors.ustc.edu.cn/g;s/http/https/g'
/etc/apk/repositories && apk upgrade --update && \  
RUN apk upgrade --update && \  
# ensure www-data user exists  
addgroup -g 82 -S www-data && \  
adduser -u 82 -D -S -G www-data -h /var/www www-data && \  
# 82 is the standard uid/gid for "www-data" in Alpine  
apk add --no-cache --virtual .pre-deps \  
ssmtp \  
imagemagick \  
tzdata \  
execline \  
libssl1.0 \  
ca-certificates \  
curl \  
tar \  
xz && \  
# install php  
apk add \  
# php5-apcu \  
php5-bcmath \  
php5-bz2 \  
php5-cli \  
php5-ctype \  
php5-curl \  
php5-dom \  
php5-exif \  
php5-fpm \  
php5-gd \  
php5-gettext \  
php5-iconv \  
# php5-imagick \  
php5-imap \  
php5-intl \  
php5-json \  
php5-mcrypt \  
# php5-mysqlnd \  
php5-mysqli \  
php5-odbc \  
php5-openssl \  
php5-phar \  
php5-pdo \  
php5-pdo_mysql \  
php5-pdo_odbc \  
php5-pdo_pgsql \  
php5-pdo_sqlite \  
php5-pear \  
php5-posix \  
# php5-redis \  
php5-soap \  
php5-sockets \  
php5-sqlite3 \  
php5-xml \  
php5-xmlreader \  
php5-xmlrpc \  
php5-zip \  
php5-zlib && \  
# Set environments  
sed -n '/^\\[www\\]/,$p' /etc/php5/php-fpm.conf > /etc/php5/fpm.d/www.conf &&
\  
sed -i '/^\\[www\\]/,$d' /etc/php5/php-fpm.conf && \  
sed -i "s|\s*error_log\s*=\s*/var/log/php-fpm.log|error_log = /dev/stderr|i"
/etc/php5/fpm.d/www.conf && \  
sed -i "s|;*daemonize\s*=\s*yes|daemonize = no|g" /etc/php5/php-fpm.conf && \  
sed -i "s|;*listen\s*=\s*127.0.0.1:9000|listen = 9000|g"
/etc/php5/fpm.d/www.conf && \  
sed -i "s|;*listen\s*=\s*/||g" /etc/php5/fpm.d/www.conf && \  
sed -i "s|;\s*process_control_timeout\s*=.*|process_control_timeout =1d|i"
/etc/php5/php-fpm.conf && \  
sed -i "s|;\s*pm.status_path\s*=.*|pm.status_path =/pstatus|i"
/etc/php5/fpm.d/www.conf && \  
sed -i "s|;\s*ping.path\s*=.*|ping.path =/pping|i" /etc/php5/fpm.d/www.conf &&
\  
sed -i "s|\s*;access.log\s*=.*|access.log = /dev/stderr|i"
/etc/php5/fpm.d/www.conf && \  
sed -i "s|\s*;slowlog\s*=.*|slowlog = /dev/stderr|i" /etc/php5/fpm.d/www.conf
&& \  
sed -i "s|;\s*access.format\s*=.*|access.format =\"%R - %u %t \"%m %r%Q%q\" %s
%f %{micro}d %{kilo}M %C%%\"|i" /etc/php5/fpm.d/www.conf && \  
sed -i "s|;catch_workers_output\s*=.*|catch_workers_output = yes|i"
/etc/php5/fpm.d/www.conf && \  
sed -i "s|;\s*clear_env\s*=.*|clear_env = no|i" /etc/php5/fpm.d/www.conf && \  
sed -i "s|nobody|www-data|g" /etc/php5/fpm.d/www.conf && \  
sed -i "s|;\s*cgi.fix_pathinfo\s*=.*|cgi.fix_pathinfo = 0|i" /etc/php5/php.ini
&& \  
sed -i "s|short_open_tag\s*=.*|short_open_tag = On|i" /etc/php5/php.ini && \  
sed -i "s|;\s*sendmail_path\s*=|sendmail_path = /usr/sbin/ssmtp -t|i"
/etc/php5/php.ini  
RUN apk add --no-cache -t .fetch-deps \  
autoconf \  
dpkg-dev dpkg \  
file \  
g++ \  
gcc \  
libc-dev \  
make \  
pcre-dev \  
pkgconf \  
re2c \  
coreutils \  
curl-dev \  
libedit-dev \  
libxml2-dev \  
openssl-dev \  
sqlite-dev \  
php5-dev \  
imagemagick-dev \  
libtool && \  
#install mongodb module  
ln -s /usr/bin/php5 /usr/bin/php && \  
ln -s /usr/bin/phpize5 /usr/bin/phpize && \  
sed -i "$ s|\\-n||g" /usr/bin/pecl && \  
pecl install mongodb redis imagick memcache && \  
echo "extension=mongodb.so"> /etc/php5/conf.d/02_mongodb.ini && \  
echo "extension=redis.so"> /etc/php5/conf.d/03_redis.ini && \  
echo "extension=imagick.so"> /etc/php5/conf.d/03_imagick.ini && \  
echo "extension=memcache.so"> /etc/php5/conf.d/03_memcache.ini && \  
# # Cleaning up  
# # Cleaning up  
# apk del tzdata && \  
apk del --purge -r .fetch-deps && \  
rm -rf /var/cache/apk/* /tmp/* ~/.pearrc  
#start scripts  
COPY run.sh /opt/  
# Set Workdir  
WORKDIR /var/www  
# Expose volumes  
#VOLUME ["/var/www"]  
# Entry point  
# ENTRYPOINT ["/usr/bin/php-fpm","-F"]  
ENTRYPOINT ["sh"]  
CMD ["/opt/run.sh"]  

