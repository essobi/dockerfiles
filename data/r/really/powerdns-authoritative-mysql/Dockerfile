FROM alpine  
  
MAINTAINER Troy Kelly <troy.kelly@really.ai>  
  
COPY powerdns_create.sql .  
COPY docker-entrypoint.sh /usr/local/bin/  
  
RUN echo "ipv6" >> /etc/modules && \  
apk update && \  
mkdir -p /var/empty/var/run/ && \  
chmod 777 /var/empty && \  
addgroup -g 1001 pdns && \  
adduser -u 1001 -G pdns -h /var/empty -D pdns && \  
chown -R pdns:pdns /var/empty/var && \  
apk add --no-cache pdns pdns-backend-mysql mariadb-client rsyslog && \  
ln -s /usr/lib/pdns/pdns/libgmysqlbackend.so /usr/lib/pdns/libgmysqlbackend.so
&& \  
sed -i "s|^# master=no|# master=no\n#\t\n# Added by
Dockerfile\nmaster=yes\n|g" /etc/pdns/pdns.conf && \  
sed -i "s|^use-logfile=no|# Added by Dockerfile\n# use-logfile=no|g"
/etc/pdns/pdns.conf && \  
sed -i "s|^wildcards=yes|# Added by Dockerfile\n# wildcards=yes|g"
/etc/pdns/pdns.conf && \  
sed -i "s|^chroot=/var/empty|# Added by Dockerfile\n# chroot=/var/empty|g"
/etc/pdns/pdns.conf && \  
rm -rf /var/cache/apk/* && \  
ln -s usr/local/bin/docker-entrypoint.sh /  
  
EXPOSE 53 53/udp 8081  
  
ENTRYPOINT ["docker-entrypoint.sh"]  

