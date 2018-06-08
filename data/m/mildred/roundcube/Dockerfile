FROM debian:stable  
MAINTAINER mildred  
  
RUN echo "deb http://http.debian.net/debian wheezy-backports main"
>/etc/apt/sources.list.d/backports.list  
  
RUN DEBIAN_FRONTEND=noninteractive apt-get update  
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y daemontools daemontools-
run  
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y -t wheezy-backports
--force-yes roundcube roundcube-sqlite3 curl php5-ldap roundcube-plugins
roundcube-plugins-extra  
  
# Debug  
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y net-tools netcat procps
man nano lsof less debconf-utils  
  
RUN { \  
( \  
echo "roundcube-core roundcube/dbconfig-install boolean true"; \  
echo "roundcube-core roundcube/database-type select sqlite3"; \  
) | debconf-set-selections; \  
DEBIAN_FRONTEND=noninteractive dpkg-reconfigure roundcube-core; \  
sed -i -re '/^\s*DocumentRoot/s, /.*, /var/lib/roundcube,' \  
/etc/apache2/sites-available/default-ssl; \  
sed -i -re '/^\s*DocumentRoot/s, /.*, /var/lib/roundcube,' \  
/etc/apache2/sites-available/default; \  
a2ensite default-ssl; \  
a2ensite default; \  
a2enmod ssl; \  
php5enmod mcrypt; \  
cp /etc/roundcube/main.inc.php /etc/roundcube/main.inc.default.php; \  
cat /etc/roundcube/debian-db.php; \  
}  
  
# Roundcube database  
VOLUME /var/lib/dbconfig-common/sqlite3/roundcube  
  
ADD entry.sh /  
EXPOSE 80  
EXPOSE 443  
CMD ["bash", "/entry.sh"]  
  

