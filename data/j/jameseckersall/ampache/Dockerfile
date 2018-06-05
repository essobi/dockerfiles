FROM jameseckersall/alpine-base  
  
MAINTAINER James Eckersall <james.eckersall@gmail.com>  
  
RUN \  
echo -e "@edge http://nl.alpinelinux.org/alpine/edge/main\n@testing
http://nl.alpinelinux.org/alpine/edge/testing\n" >> /etc/apk/repositories && \  
echo -e "@community http://nl.alpinelinux.org/alpine/edge/community" >>
/etc/apk/repositories && \  
apk update && \  
apk add bash curl gettext inotify-tools vlc nginx php5 php5-common php5-fpm
php5-gd php5-phar php5-gettext php5-curl php5-iconv php5-json php5-openssl
libressl2.4-libcrypto@edge libressl2.4-libssl@edge php5-pdo php5-pdo_mysql
php5-xml php5-zlib pwgen lame libvorbis-dev flac libtheora-dev libvpx-dev git  
#RUN \  
# ln -sf /usr/bin/php5 /usr/bin/php  
  
RUN \  
curl -o /tmp/composer-setup.php https://getcomposer.org/installer && \  
cd /tmp && \  
php -r "if (hash_file('SHA384', '/tmp/composer-setup.php') ===
'aa96f26c2b67226a324c27919f1eb05f21c248b987e6195cad9690d5c1ff713d53020a02ac8c217dbf90a7eacc9d141d')
{ echo 'Installer verified'; } else { echo 'Installer corrupt';
unlink('/tmp/composer-setup.php'); } echo PHP_EOL;" && \  
php /tmp/composer-setup.php && \  
rm /tmp/composer-setup.php && \  
git clone https://github.com/ampache/ampache /www && \  
/tmp/composer.phar -d=/www install \--prefer-source \--no-interaction  
  
COPY files /  
  
RUN \  
mkdir -p /run /run/nginx /www /var/log/ampache && \  
chmod 0644 /etc/crontabs/root && \  
chmod 0755 -R /mediawatch.sh /etc/periodic && \  
chmod 0777 -R /run /var/log /var/log/ampache /var/log/nginx /var/lib/nginx
/www && \  
sed -i \  
-e '/^listen\.owner =.*/d' \  
-e '/^listen\.group =.*/d' \  
/etc/php5/php-fpm.conf  
# sed -i \  
# -e '/^user =/d' \  
# -e '/^group =/d' \  
# /etc/php5/fpm.d/www.conf  
  
ENV \  
AMPACHE_TAG=3.8.2 \  
AMPACHE_USER=admin \  
AMPACHE_PASS=changeme \  
AMPACHE_USER_EMAIL=admin@example.com \  
AMPACHE_USER_NAME=admin \  
HTTP_HOST=localhost \  
HTTP_PORT=8080 \  
MYSQL_HOST=localhost \  
MYSQL_PORT=3306 \  
MYSQL_DB=ampache \  
MYSQL_USER=ampache \  
MYSQL_PASS=ampache  
  
EXPOSE 8080  
  
VOLUME /media  

