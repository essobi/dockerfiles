FROM debian:jessie  
MAINTAINER Filiphe Vilar <liphvf@gmail.com>  
  
ADD zabbix/ /usr/src/zabbix  
  
ADD sources.list /etc/apt/  
  
# add webupd8 repository  
RUN apt-get update && \  
DEBIAN_FRONTEND=noninteractive apt-get install -y --force-yes openjdk-7-jdk
openjdk-7-jre \  
make flex gcc gpp libpq5 libpq-dev snmp automake snmpd libiksemel-dev
libcurl4-gnutls-dev libssh2-1-dev libssh2-1 libopenipmi-dev libsnmp-dev curl
fping \  
sudo libcurl3-gnutls libxml2-dev php5 php5-pgsql php5-ldap php5-fpm php-apc
php5-curl php5-xmlrpc php5-gd php-net-socket nano nginx pkg-config
libldap2-dev snmp-mibs-downloader traceroute && \  
\  
\  
echo "===> clean up..." && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
RUN rm -v /etc/nginx/sites-available/default  
ADD default /etc/nginx/sites-available/  
  
WORKDIR /usr/src/zabbix  
RUN chmod +x configure  
  
# Compilando o zabbix  
RUN ./configure --enable-server --enable-agent --with-postgresql --with-net-
snmp --with-libcurl --with-ssh2 \  
\--with-openipmi --with-libxml2 --with-openssl --with-jabber --with-ldap
--with-iconv  
  
# --enable-java  
RUN make && make install  
  
RUN useradd -s /bin/false zabbix && \  
cp misc/init.d/debian/zabbix-* /etc/init.d/ && \  
chmod +x /etc/init.d/zabbix-*  
  
#INSTALAR E CONFIGURAR A INTERFACE WEB  
RUN mkdir /var/www/html/zabbix && \  
cp -r frontends/php/* /var/www/html/zabbix/ && \  
chown -R www-data:www-data /var/www/html/zabbix  
  
RUN cp /usr/bin/fping /usr/sbin && chown root:zabbix /usr/sbin/fping  
RUN rm /usr/local/etc/zabbix_server.conf  
ADD zabbix_server.conf /usr/local/etc/  
  
RUN rm /etc/php5/fpm/php.ini  
ADD php.ini /etc/php5/fpm/  
  
# Setup Volume  
VOLUME ["/var/www/html/zabbix"]  
  
ADD ./startup.sh /  
# ENTRYPOINT ["/startup.sh"]  
CMD ["/startup.sh"]  

