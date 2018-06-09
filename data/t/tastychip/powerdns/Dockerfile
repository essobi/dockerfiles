FROM alpine:3.7  
  
ENV POWERDNS_VERSION=4.1.3 \  
POWERDNS_MASTER=false \  
POWERDNS_AXFR="127.0.0.0/8,::1" \  
POWERDNS_APIKEY=false \  
MYSQL_HOST="mariadb" \  
MYSQL_PORT="3306" \  
MYSQL_USER="powerdns" \  
MYSQL_PASS="geheim" \  
MYSQL_DB="powerdns"  
  
RUN apk \--update add mysql-client mariadb-client-libs libpq libstdc++ libgcc
boost-program_options nano && \  
apk add \--virtual build-deps \  
g++ make mariadb-dev curl boost-dev && \  
curl -sSL
https://downloads.powerdns.com/releases/pdns-$POWERDNS_VERSION.tar.bz2 | tar
xj -C /tmp && \  
cd /tmp/pdns-$POWERDNS_VERSION && \  
./configure \--prefix="" \--exec-prefix=/usr \--sysconfdir=/etc/powerdns \  
\--with-modules="gmysql" \--without-lua && \  
make && make install-strip && cd / && \  
mkdir -p /etc/powerdns && \  
mkdir -p /pdns && \  
echo "export EDITOR=nano" > /etc/profile.d/editor.sh && \  
echo "include-dir=/pdns" > /etc/powerdns/pdns.conf && \  
addgroup -S pdns 2>/dev/null && \  
adduser -S -D -H -h /var/empty -s /bin/false -G pdns -g pdns pdns 2>/dev/null
&& \  
chown -R pdns:pdns /pdns && \  
apk del \--purge build-deps && \  
rm -rf /tmp/pdns-$POWERDNS_VERSION /var/cache/apk/*  
  
ADD entrypoint.sh /  
RUN chmod ugo+x /entrypoint.sh  
  
USER pdns:pdns  
  
ADD pdns.conf /pdns/  
  
EXPOSE 8053/tcp 8053/udp  
  
HEALTHCHECK \--interval=1m \--timeout=3s \--start-period=10s \  
CMD /usr/bin/pdns_control ping || exit 1  
  
ENTRYPOINT ["/entrypoint.sh"]  

