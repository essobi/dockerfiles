FROM alpine:3.6  
ARG VERSION=1.33  
ARG librenms_base=/opt/librenms  
LABEL version="${VERSION}" \  
description="librenms container with alpine" \  
maintainer="Veovis <veovis@kveer.fr>"  
  
RUN apk upgrade --no-cache && \  
apk add --no-cache \  
ca-certificates \  
openssl \  
tzdata \  
bash \  
php7 \  
php7-ctype \  
php7-curl \  
php7-fpm \  
php7-gd \  
php7-json \  
php7-mcrypt \  
php7-memcached \  
php7-mysqli \  
php7-openssl \  
php7-pear \  
php7-session \  
php7-simplexml \  
php7-snmp \  
net-snmp \  
net-snmp-tools \  
graphviz \  
nginx \  
fping \  
imagemagick \  
whois \  
nmap \  
rrdtool \  
python2 \  
py-mysqldb \  
runit \  
dcron \  
mysql-client \  
mtr && \  
update-ca-certificates && \  
pear channel-update pear.php.net && \  
pear install pear/Net_IPv4 && \  
pear install pear/Net_IPv6 && \  
mkdir -p /opt  
  
RUN rm /etc/nginx/conf.d/default.conf && \  
sed -i -e 's/^;pid/pid/' /etc/php7/php-fpm.conf && \  
sed -i -e 's!^; \?include_path.*!include_path=".:/usr/share/php7"!'
/etc/php7/php.ini && \  
rm /etc/php7/php-fpm.d/www.conf  
  
RUN wget -q -O - -c
"https://github.com/librenms/librenms/archive/${VERSION}.tar.gz" | tar -zx -f
- -C /opt && \  
mv ${librenms_base}-${VERSION} $librenms_base && \  
sed -i -e 's/ALTER IGNORE TABLE/ALTER TABLE/' $librenms_base/sql-
schema/109.sql && \  
sed -i -e 's/ALTER IGNORE TABLE/ALTER TABLE/' $librenms_base/sql-
schema/181.sql && \  
adduser -D -h $librenms_base librenms && \  
adduser nginx librenms && \  
install -m 775 -d $librenms_base/rrd && \  
install -d $librenms_base/logs && \  
chown -R librenms:librenms $librenms_base && \  
cp $librenms_base/snmpd.conf.example /etc/snmp/snmpd.conf && \  
cp $librenms_base/config.php.default $librenms_base/config.php && \  
echo "\$config['fping'] = '/usr/sbin/fping';" >> $librenms_base/config.php &&
\  
echo "if(file_exists(realpath(__DIR__) . '/config.d/config.php')) include
realpath(__DIR__) . '/config.d/config.php';" >> $librenms_base/config.php && \  
echo "if(file_exists(realpath(__DIR__) . '/config.d/_memcache.php')) include
realpath(__DIR__) . '/config.d/_memcache.php';" >> $librenms_base/config.php
&& \  
wget -q -O /usr/local/bin/distro
https://raw.githubusercontent.com/librenms/librenms-agent/master/snmp/distro
&& \  
chmod +x /usr/local/bin/distro && \  
cp $librenms_base/librenms.nonroot.cron /etc/crontabs/librenms && \  
sed -i -e 's/ librenms //' /etc/crontabs/librenms && \  
sed -i 's/^#\\($config\\['"'"'update'"'"'\\].*\\)/\1/'
"$librenms_base/config.php"  
  
COPY patches /tmp/patches  
WORKDIR $librenms_base  
RUN patch -p 1 -i /tmp/patches/002_missing_menu_index.patch && \  
patch -p 1 -i /tmp/patches/003_missing_used_sensors_index.patch  
  
COPY services /etc/sv  
COPY docker-entrypoint.sh /  
COPY nginx-librenms.conf /etc/nginx/conf.d/librenms.conf  
COPY php-librenms.conf /etc/php7/php-fpm.d/librenms.conf  
  
ENTRYPOINT [ "/docker-entrypoint.sh" ]  
CMD [ "runsvdir", "-P /etc/sv" ]  
  
EXPOSE 80  
WORKDIR /  
VOLUME ["$librenms_base/logs", "$librenms_base/rrd",
"$librenms_base/config.d"]  

