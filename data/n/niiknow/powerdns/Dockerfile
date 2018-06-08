FROM niiknow/mariadb:0.2.0  
MAINTAINER noogen <friends@niiknow.org>  
  
ENV MYSQL_AUTOCONF=true \  
MYSQL_HOST="127.0.0.1" \  
MYSQL_PORT="3306" \  
MYSQL_DATABASE="powerdns_db" \  
MYSQL_USER="powerdns_dbuser" \  
MYSQL_PASSWORD=""  
RUN \  
# Make info file about this build  
printf "Build of niiknow/powerdns, date: %s\n" `date -u +"%Y-%m-%dT%H:%M:%SZ"`
>> /etc/BUILDS/powerdns && \  
apk --update add \  
pdns pdns-backend-sqlite3 pdns-backend-mysql pdns-recursor \  
mariadb-client bash rsync && \  
rm -rf /var/cache/apk/*  
  
COPY rootfs/. /  
  
RUN \  
# move syspreps  
mkdir -p /var/run/pdns && \  
chown -R pdns:pdns /var/run/pdns && \  
rsync -a /etc/pdns/ /etc/pdns-bak  
  
EXPOSE 53/udp 53/tcp 3306 5300/udp 5300/tcp 8081  
VOLUME ["/etc/mysql", "/var/lib/mysql", "/var/log/mysql", "/etc/pdns"]  

