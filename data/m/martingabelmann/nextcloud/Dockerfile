FROM alpine  
MAINTAINER martin@gabelmann.biz  
  
ENV NC_VERSION="nextcloud-12.0.0" \  
DB_TYPE=mysql \  
DB_HOST=localhost \  
DB_NAME=nextcloud_db \  
DB_USER=nextcloud \  
DB_PASS=changemepls \  
DB_ROOT_PASS=changemepls \  
DB_PREFIX="" \  
DB_DATA_PATH=/nextcloud/sql \  
DB_MAX_ALLOWED_PACKET="200M" \  
DB_EXTERNAL=false \  
SSL_CERTIFICATE_FILE=/nextcloud/ssl/server.crt \  
SSL_CERTIFICATE_KEY_FILE=/nextcloud/ssl/server.key \  
SSL_CERTIFICATE_CHAIN_FILE=/nextcloud/ssl/server.crt \  
NC_ADMIN=admin \  
NC_EMAIL="admin@localhost" \  
NC_ADMINPASS=changemepls \  
NC_WWW=/var/www/localhost/htdocs \  
NC_DATADIR=/nextcloud/data \  
NC_DOMAIN=localhost \  
NC_TIME="Europe/Berlin" \  
NC_LC="en_US.UTF-8" \  
NC_TRUSTED_DOMAINS="'localhost','127.0.0.1'," \  
NC_LANGUAGE=en \  
NC_DEFAULTAPP=files \  
NC_OVERWRITEHOST="" \  
NC_LOGLEVEL=1 \  
NC_MAIL_FROM_ADDRESS=admin \  
NC_MAIL_SMTPMODE=smtp \  
NC_MAIL_DOMAIN=localhost \  
NC_MAIL_SMTPAUTHTYPE=LOGIN \  
NC_MAIL_SMTPAUTH=1 \  
NC_MAIL_SMTPHOST='smtp.localhost' \  
NC_MAIL_SMTPPORT=465 \  
NC_MAIL_SMTPNAME=admin@localhost \  
NC_MAIL_SMTPSECURE=ssl \  
NC_MAIL_SMTPPASSWORD=changemepls  
  
RUN sed -i -e 's/v3\.5/edge/g' /etc/apk/repositories && apk update && apk
upgrade &&\  
apk add tzdata openssl ca-certificates apache2 apache2-ssl gettext mariadb
mariadb-client \  
php7 php7-apache2 php7-gd php7-memcached php7-imagick php7-bz2 php7-posix \  
php7-json php7-pdo_mysql php7-mcrypt php7-intl php7-apcu php7-openssl
php7-fileinfo \  
php7-curl php7-zip php7-mbstring php7-dom php7-xmlreader php7-ctype php7-zlib
\  
php7-iconv php7-xmlrpc php7-simplexml php7-xmlwriter php7-pcntl php7-ldap  
VOLUME "/nextcloud"  
  
WORKDIR /var/www/localhost/htdocs  
  
RUN /usr/bin/install -g apache -m 775 -d /run/apache2 &&\  
/usr/bin/install -g mysql -m 775 -d /run/mysqld &&\  
wget https://download.nextcloud.com/server/releases/"$NC_VERSION".tar.bz2 -O
/tmp/nextcloud.tar.bz2 &&\  
tar \--strip-components=1 -jxf /tmp/nextcloud.tar.bz2 -C "$NC_WWW" &&\  
chown -R apache:apache "$NC_WWW" &&\  
rm -f /tmp/nextcloud* &&\  
sed -i '/proxy_module/s/^#//g' /etc/apache2/httpd.conf &&\  
sed -i '/proxy_connect_module/s/^#//g' /etc/apache2/httpd.conf &&\  
sed -i '/proxy_ftp_module/s/^#//g' /etc/apache2/httpd.conf &&\  
sed -i '/proxy_http_module/s/^#//g' /etc/apache2/httpd.conf &&\  
sed -i '/proxy_wstunnel_module/s/^#//g' /etc/apache2/httpd.conf &&\  
sed -i '/proxy_ajp_module/s/^#//g' /etc/apache2/httpd.conf &&\  
sed -i '/proxy_balancer_module/s/^#//g' /etc/apache2/httpd.conf &&\  
sed -i '/ssl_module/s/^#//g' /etc/apache2/httpd.conf &&\  
sed -i '/cgi_module/s/^#//g' /etc/apache2/httpd.conf &&\  
sed -i '/mpm_prefork_module/s/^#//g' /etc/apache2/httpd.conf &&\  
sed -i '/mpm_event_module/s/^/#/g' /etc/apache2/httpd.conf &&\  
sed -i '/rewrite_module/s/^#//g' /etc/apache2/httpd.conf &&\  
sed -i
's/^;open_basedir.*$/open_basedir=\/nextcloud:\/var\/www\/localhost\/htdocs:\/tmp\/:\/dev\/urandom/'
/etc/php7/php.ini &&\  
sed -i '/extension=apcu/a extension=apc\.so' /etc/php7/php.ini &&\  
sed -i '/apc\.enabled=1/a apc\.shm_size=64M' /etc/php7/conf.d/apcu.ini &&\  
sed -i '/apc\.shm_size=64M/a apc\.ttl=7200' /etc/php7/conf.d/apcu.ini &&\  
sed -i '/apc\.ttl=7200/a apc\.enable_cli=1' /etc/php7/conf.d/apcu.ini &&\  
ln -s /var/www/localhost/htdocs/occ /usr/local/bin/occ  
  
ADD nc-install /usr/local/bin/nc-install  
ADD tpl /tpl  
ADD server.key /nextcloud/ssl/server.key  
ADD server.crt /nextcloud/ssl/server.crt  
  
EXPOSE 80 443  
  
ENTRYPOINT ["nc-install"]  
CMD ["/usr/sbin/httpd", "-kstart", "-DFOREGROUND"]  

