FROM php:apache  
  
ENV ARCHIVE develop.tar.gz  
RUN mkdir /var/www/html/cacti  
WORKDIR /var/www/html/cacti  
ADD https://github.com/twhtanghk/cacti/archive/${ARCHIVE} /tmp  
RUN tar --strip-components=1 -xzf /tmp/${ARCHIVE} && \  
rm /tmp/${ARCHIVE} && \  
apt-get update && \  
apt-get install -y rrdtool mariadb-client snmp libsnmp-dev libldap-dev
libfreetype6-dev libjpeg-dev libpng12-dev libgmp-dev cron && \  
apt-get clean && \  
chown -R www-data.www-data . && \  
useradd cactiuser && \  
cp php.ini /usr/local/etc/php/ && \  
cp crontab /var/spool/cron/crontabs/cactiuser && \  
chown cactiuser.crontab /var/spool/cron/crontabs/cactiuser && \  
chmod 600 /var/spool/cron/crontabs/cactiuser && \  
chown -R cactiuser rra log && \  
ln -s /usr/include/x86_64-linux-gnu/gmp.h /usr/include/gmp.h && \  
docker-php-ext-configure ldap --with-libdir=lib/x86_64-linux-gnu/ && \  
docker-php-ext-install pdo pdo_mysql sockets snmp gd gmp ldap  
EXPOSE 80  
ENTRYPOINT ./entrypoint.sh  

