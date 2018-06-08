FROM debian:stretch-slim  
  
ENV MYBB_VER=1812 \  
APACHE_RUN_USER=www-data \  
APACHE_RUN_GROUP=www-data \  
APACHE_PID_FILE=/var/run/apache2/apache2.pid \  
APACHE_RUN_DIR=/var/run/apache2 \  
APACHE_LOCK_DIR=/var/lock/apache2 \  
APACHE_LOG_DIR=/var/log/apache2 \  
APACHE_ULIMIT_MAX_FILES='ulimit -n 65536' \  
APACHE_SERVERNAME=fake.server.com \  
CONFD_VERSION=0.12.0-alpha4  
  
WORKDIR /var/www/html  
  
RUN set -x; \  
fetchDeps=' \  
curl \  
unzip \  
'; \  
apt-get update \  
&& DEBIAN_FRONTEND=noninteractive apt-get install -y apache2 libapache2-mod-
php7.0 php7.0-mcrypt \  
php7.0-gd php7.0-mysql php7.0-xml ca-certificates $fetchDeps \  
&& rm * \  
&& curl https://resources.mybb.com/downloads/mybb_${MYBB_VER}.zip -o mybb.zip
\  
&& unzip mybb.zip "Upload/*" \  
&& mv Upload/* . \  
&& rm -Rf Upload mybb.zip \  
&& mv inc/config.default.php inc/config.php \  
&& chmod -R 0777 cache uploads inc/settings.php inc/config.php \  
&& chown -R www-data:www-data /var/www/html \  
&& curl -L
https://github.com/mariomarin/confd/releases/download/v$CONFD_VERSION/confd-$CONFD_VERSION-
linux-amd64 -o /usr/local/bin/confd \  
&& apt-get purge -y --auto-remove $fetchDeps \  
&& chmod +x /usr/local/bin/confd \  
&& ln -sf /dev/stdout /var/log/apache2/access.log && \  
ln -sf /dev/stderr /var/log/apache2/error.log  
  
COPY entrypoint /usr/local/bin/  
  
ADD config/confd /etc/confd  
  
ENTRYPOINT ["entrypoint"]  
  
CMD ["apache2", "-D", "FOREGROUND"]  

