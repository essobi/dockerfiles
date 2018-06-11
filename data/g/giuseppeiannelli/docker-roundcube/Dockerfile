FROM nginx:1.10.1-alpine  
  
ENV ROUNDCUBE_VERSION=1.3.1 \  
NGINX_SERVER_NAME=localhost \  
NGINX_ROOT=/var/www/roundcube \  
NGINX_INDEX='index.php index.html' \  
NGINX_LABEL_HTTP_HOST='$http_host' \  
NGINX_LABEL_REQUEST_URI='$request_uri' \  
NGINX_LABEL_URI='$uri' \  
NGINX_LABEL_FASTCGI_PATH_INFO='$fastcgi_path_info' \  
NGINX_LABEL_REGEXP_END_DELIMETER='$' \  
NGINX_FASTCGI_PARAM_SCRIPT_FILENAME='$document_root$fastcgi_script_name' \  
NGINX_FASTCGI_PATH_TRANSLATED='$document_root$fastcgi_path_info' \  
NGINX_PHPFPM_UPSTREAM_SERVER=127.0.0.1:9000 \  
FPM_INDEX=index.php \  
PHP_DATE_TIMEZONE=UTC \  
LABEL_CONFIG='$config' \  
DB_TYPE=mysql \  
DB_USER=roundcube \  
DB_PASSWD=pass \  
DB_HOST=localhost \  
DB_PORT=3306 \  
DB_NAME=roundcubemail \  
ROUNDCUBE_HOSTNAME=localhost \  
ROUNDCUBE_NAME='Roundcube Webmail' \  
ROUNDCUBE_LOG_DRIVER='stdout' \  
SMTP_SERVER='' \  
SMTP_PORT=25 \  
SMTP_USER='' \  
SMTP_PASSWD='' \  
IMAP_SERVER='' \  
IMAP_PORT=143 \  
IMAP_USER='' \  
IMAP_PASSWD='' \  
DES_KEY=rcmail-!~p)*ALM.=;@Jcw)9  
#Install system dependencies  
RUN apk add --update curl file git gnupg mysql-client supervisor unzip \  
php5 php5-dom php5-pear php5-mysql php5-mcrypt php5-intl \  
php5-fpm php5-gd php5-ldap php5-phar php5-json php5-openssl \  
php5-mcrypt php5-xml php5-zlib php5-pdo_dblib php5-pdo_odbc \  
php5-pdo php5-pdo_mysql php5-pdo_pgsql php5-pdo_sqlite \  
php5-sockets php5-iconv php5-zip php5-pspell php5-exif  
  
#Download roundcube gpg key  
RUN gpg --keyserver http://pgp.mit.edu --recv-keys 41C4F7D5  
  
#Download roundcube  
RUN cd /tmp \  
&& curl -fSL
https://github.com/roundcube/roundcubemail/releases/download/${ROUNDCUBE_VERSION}/roundcubemail-${ROUNDCUBE_VERSION}.tar.gz.asc
-o /tmp/roundcube.tar.gz.asc \  
&& curl -fsL
https://github.com/roundcube/roundcubemail/releases/download/${ROUNDCUBE_VERSION}/roundcubemail-${ROUNDCUBE_VERSION}.tar.gz
-o /tmp/roundcube.tar.gz  
  
#Verify downloaded file  
RUN gpg --verify /tmp/roundcube.tar.gz.asc /tmp/roundcube.tar.gz  
  
#Extract roundcube source into webserver folder  
RUN mkdir -p /var/www && tar xvzf /tmp/roundcube.tar.gz -C /var/www/  
RUN mv /var/www/roundcubemail-${ROUNDCUBE_VERSION}/ ${NGINX_ROOT}/  
  
WORKDIR ${NGINX_ROOT}  
  
#Create roundcube logs and temp directories  
RUN mkdir -p ${NGINX_ROOT}/logs ${NGINX_ROOT}/temp  
  
#Copy configuration files  
COPY docker /docker  
  
RUN chmod +x /docker/scripts/entrypoints.sh  
  
# ensure www-data user exists  
RUN set -x \  
&& addgroup -g 82 -S www-data \  
&& adduser -u 82 -D -S -G www-data www-data  
  
#Download php composer and update php dependencies  
RUN curl -fsL https://getcomposer.org/composer.phar -o /usr/local/bin/composer
\  
&& chmod +x /usr/local/bin/composer \  
&& mv composer.json-dist composer.json \  
&& composer install --prefer-dist --no-dev  
  
RUN ./bin/install-jsdeps.sh  
  
#Change owner for webserver root  
RUN chown -R nginx:www-data ${NGINX_ROOT} ${NGINX_ROOT}/temp
${NGINX_ROOT}/logs  
  
#Remove installer folder  
RUN rm -rf ${NGINX_ROOT}/installer  
  
#Start webserver and roundcube  
ENTRYPOINT ["/docker/scripts/entrypoints.sh"]  
CMD ["roundcube"]  

