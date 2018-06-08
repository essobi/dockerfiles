# Use Alpine Linux  
FROM alpine:3.3  
  
# Timezone  
ENV TIMEZONE=Europe/Brussels \  
PHP_MEMORY_LIMIT=512M \  
MAX_UPLOAD=50M \  
PHP_MAX_FILE_UPLOAD=200 \  
PHP_MAX_POST=100M \  
ROOT=/www  
  
# Let's roll  
RUN apk update && \  
apk upgrade && \  
apk add --update tzdata && \  
cp /usr/share/zoneinfo/${TIMEZONE} /etc/localtime && \  
echo "${TIMEZONE}" > /etc/timezone && \  
apk add --update \  
bash \  
curl \  
php-mcrypt \  
php-soap \  
php-openssl \  
php-gmp \  
php-pdo_odbc \  
php-json \  
php-dom \  
php-pdo \  
php-zip \  
php-mysql \  
php-sqlite3 \  
php-apcu \  
php-pdo_pgsql \  
php-bcmath \  
php-gd \  
php-xcache \  
php-odbc \  
php-pdo_mysql \  
php-pdo_sqlite \  
php-gettext \  
php-xmlreader \  
php-xmlrpc \  
php-bz2 \  
php-memcache \  
php-mssql \  
php-iconv \  
php-pdo_dblib \  
php-curl \  
php-ctype \  
php-fpm \  
php-intl \  
php-phar && \  
curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer && \  
composer global require hirak/prestissimo && \  
curl -o /usr/local/bin/gosu -sSL
"https://github.com/tianon/gosu/releases/download/1.7/gosu-amd64" && \  
chmod +x /usr/local/bin/gosu && \  
sed -i -e "s/;clear_env\s*=\s*no/clear_env = no/g" /etc/php/php-fpm.conf && \  
sed -i -e "s/;daemonize\s*=\s*yes/daemonize = no/g" /etc/php/php-fpm.conf && \  
sed -i -e "s/listen\s*=\s*127.0.0.1:9000/listen = 9000/g" /etc/php/php-
fpm.conf && \  
sed -i "s|;date.timezone =.*|date.timezone = ${TIMEZONE}|" /etc/php/php.ini &&
\  
sed -i "s|memory_limit =.*|memory_limit = ${PHP_MEMORY_LIMIT}|"
/etc/php/php.ini && \  
sed -i "s|upload_max_filesize =.*|upload_max_filesize = ${MAX_UPLOAD}|"
/etc/php/php.ini && \  
sed -i "s|max_file_uploads =.*|max_file_uploads = ${PHP_MAX_FILE_UPLOAD}|"
/etc/php/php.ini && \  
sed -i "s|post_max_size =.*|post_max_size = ${PHP_MAX_POST}|" /etc/php/php.ini
&& \  
sed -i "s/;cgi.fix_pathinfo=1/cgi.fix_pathinfo=0/" /etc/php/php.ini && \  
sed -i "s/;pm.status_path = \/status/pm.status_path=\/status/g" /etc/php/php-
fpm.conf && \  
sed -i "s/;ping.path = \/ping/ping.path=\/ping/g" /etc/php/php-fpm.conf && \  
sed -i "s/;pm.max_requests = 500/pm.max_requests=500/g" /etc/php/php-fpm.conf
&& \  
mkdir -p ${ROOT} && \  
apk del tzdata && \  
rm -rf /var/cache/apk/*  
  
# Set Workdir  
WORKDIR ${ROOT}  
  
# Expose ports  
EXPOSE 9000  
  
# Entry point  
ENTRYPOINT ["/usr/bin/php-fpm"]  

