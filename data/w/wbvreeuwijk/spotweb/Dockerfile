FROM php:7.1.1-fpm-alpine  
  
# Install and configure nginx and php deps  
RUN apk add --no-cache --virtual .spotweb-rundeps \  
nginx \  
freetype \  
gd \  
gettext-libs \  
gmp \  
libldap \  
libsasl \  
mariadb-client \  
postgresql-libs \  
supervisor \  
&& { \  
echo 'pid /tmp/nginx.pid;'; \  
echo 'worker_processes 1;'; \  
echo 'daemon off;'; \  
echo 'events {'; \  
echo ' worker_connections 1024;'; \  
echo '}'; \  
echo 'http {'; \  
echo ' include mime.types;'; \  
echo ' default_type application/octet-stream;'; \  
echo ' sendfile on;'; \  
echo ' keepalive_timeout 65;'; \  
echo 'server {'; \  
echo ' listen 80;'; \  
echo; \  
echo ' root /var/www/html;'; \  
echo ' index index.php index.html index.htm;'; \  
echo ''; \  
echo ' location / {'; \  
echo ' try_files $uri $uri/ /index.php;'; \  
echo ' }'; \  
echo ''; \  
echo ' location = / {'; \  
echo ' rewrite ^ /spotweb/ permanent;'; \  
echo ' }'; \  
echo; \  
echo ' location /doc/ {'; \  
echo ' alias /usr/share/doc/;'; \  
echo ' autoindex on;'; \  
echo ' allow 127.0.0.1;'; \  
echo ' allow ::1;'; \  
echo ' deny all;'; \  
echo ' }'; \  
echo; \  
echo ' location /spotweb {'; \  
echo ' if ($uri !~ "api/"){'; \  
echo ' rewrite api/?$ /spotweb/index.php?page=newznabapi last;'; \  
echo ' }'; \  
echo ' }'; \  
echo; \  
echo ' location ~ \\.php$ {'; \  
echo ' fastcgi_split_path_info ^(.+\\.php)(/.+)$;'; \  
echo ' fastcgi_pass localhost:9000;'; \  
echo ' fastcgi_index index.php;'; \  
echo ' fastcgi_param SCRIPT_FILENAME $document_root$fastcgi_script_name;'; \  
echo ' include fastcgi_params;'; \  
echo ' }'; \  
echo; \  
echo ' location ~ /\\.ht {'; \  
echo ' deny all;'; \  
echo ' }'; \  
echo '}'; \  
echo; \  
echo '}'; \  
} | tee /etc/nginx/nginx.conf  
  
# Build and configure PHP modules  
RUN apk add --no-cache --virtual .spotweb-builddeps \  
gmp-dev \  
gettext-dev \  
freetype-dev \  
libpng-dev \  
libjpeg-turbo-dev \  
postgresql-dev \  
&& docker-php-ext-configure gd \  
\--with-freetype-dir=/usr/include/ \  
\--with-jpeg-dir=/usr/include/ \  
&& docker-php-ext-install \  
pdo \  
pdo_mysql \  
pdo_pgsql \  
mbstring \  
gd \  
zip \  
gettext \  
gmp \  
bcmath \  
opcache \  
&& apk del .spotweb-builddeps \  
&& { \  
echo 'date.timezone=Europe/Amsterdam'; \  
echo 'memory_limit=256M' ; \  
} | tee /usr/local/etc/php/conf.d/spotweb.ini && \  
{ \  
echo 'opcache.memory_consumption=128'; \  
echo 'opcache.interned_strings_buffer=8'; \  
echo 'opcache.max_accelerated_files=4000'; \  
echo 'opcache.revalidate_freq=60'; \  
echo 'opcache.fast_shutdown=1'; \  
echo 'opcache.enable_cli=1'; \  
} | tee /usr/local/etc/php/conf.d/opcache.ini  
  
# Install cron  
RUN echo '0 * * * * (. /root/profile.sh && cd /var/www/html/spotweb &&
/usr/local/bin/php retrieve.php) > /dev/null 2>&1' | crontab - \  
&& { \  
echo 'export MYSQL_PORT_3306_TCP_ADDR=$MYSQL_PORT_3306_TCP_ADDR'; \  
echo 'export MYSQL_ENV_MYSQL_DATABASE=$MYSQL_ENV_MYSQL_DATABASE'; \  
echo 'export MYSQL_ENV_MYSQL_USER=$MYSQL_ENV_MYSQL_USER'; \  
echo 'export MYSQL_ENV_MYSQL_PASSWORD=$MYSQL_ENV_MYSQL_PASSWORD' ; \  
} | tee /root/profile.sh \  
&& chmod 700 /root/profile.sh  
  
# Configure supervisord  
RUN { \  
echo '[supervisord]'; \  
echo 'nodaemon=true' ; \  
echo; \  
echo '[program:cron]'; \  
echo 'command=/usr/sbin/crond -f'; \  
echo; \  
echo '[program:php-fpm]'; \  
echo 'command=/usr/local/sbin/php-fpm'; \  
echo; \  
echo '[program:nginx]'; \  
echo 'command=/usr/sbin/nginx'; \  
} | tee /etc/supervisord.conf  
  
# Deploy spotweb  
RUN apk add --no-cache --virtual .spotweb-deploydeps git \  
&& git clone https://github.com/spotweb/spotweb.git /var/www/html/spotweb \  
&& mkdir -m777 /var/www/html/spotweb/cache \  
&& { \  
echo '<?php'; \  
echo '$dbsettings["engine"] = "mysql";'; \  
echo '$dbsettings["host"] = getenv("MYSQL_PORT_3306_TCP_ADDR");'; \  
echo '$dbsettings["dbname"] = getenv("MYSQL_ENV_MYSQL_DATABASE");'; \  
echo '$dbsettings["user"] = getenv("MYSQL_ENV_MYSQL_USER");'; \  
echo '$dbsettings["pass"] = getenv("MYSQL_ENV_MYSQL_PASSWORD");'; \  
echo '?>'; \  
} | tee /var/www/html/spotweb/dbsettings.inc.php \  
&& apk del .spotweb-deploydeps \  
&& { \  
echo '#!/bin/sh'; \  
echo; \  
echo 'MYSQL="mysql -h${MYSQL_PORT_3306_TCP_ADDR} -u${MYSQL_ENV_MYSQL_USER}
-p${MYSQL_ENV_MYSQL_PASSWORD} ${MYSQL_ENV_MYSQL_DATABASE} -s"'; \  
echo; \  
echo 'echo "Check if db is online ..."'; \  
echo 'while [ 1 ]; do'; \  
echo ' echo "select 1" | $MYSQL > /dev/null 2>&1 && break'; \  
echo ' echo "Retrying ..."'; \  
echo ' sleep 1'; \  
echo 'done'; \  
echo; \  
echo 'echo "Db is online"'; \  
echo '# Check if tables exists and create them if not'; \  
echo 'echo "select count(*) from settings" | $MYSQL > /dev/null 2>&1'; \  
echo 'retval=$?'; \  
echo 'if [ $retval == 1 ]; then'; \  
echo ' echo "Initializing database"'; \  
echo ' # Run upgrade-db.php twice to update global options ...'; \  
echo ' /usr/local/bin/php /var/www/html/spotweb/bin/upgrade-db.php'; \  
echo ' /usr/local/bin/php /var/www/html/spotweb/bin/upgrade-db.php --reset-
password admin'; \  
echo; \  
echo ' echo "update settings set value =
\"http://jijhaatmij.hopto.me/blacklist.txt\" where name = \"blacklist_url\"" |
$MYSQL'; \  
echo ' echo "update settings set value =
\"http://jijhaatmij.hopto.me/whitelist.txt\" where name = \"whitelist_url\"" |
$MYSQL'; \  
echo ' echo "update settings set value = 1 where name = \"external_blacklist\"
or name = \"external_whitelist\"" | $MYSQL'; \  
echo 'else'; \  
echo ' echo "Database already exists"'; \  
echo ' /usr/local/bin/php /var/www/html/spotweb/bin/upgrade-db.php'; \  
echo 'fi'; \  
echo; \  
echo 'exit 0'; \  
} | tee /root/init_db.sh \  
&& chmod +x /root/init_db.sh  
  
# Install entrypoint  
RUN { \  
echo '#!/bin/sh'; \  
echo '/root/init_db.sh'; \  
echo 'chown -R www-data: /var/www/html/spotweb/cache'; \  
echo '/usr/bin/supervisord'; \  
} | tee /entrypoint.sh \  
&& chmod +x /entrypoint.sh  
  
VOLUME ["/var/www/html/spotweb/cache"]  
EXPOSE 80  
CMD ["/entrypoint.sh"]

