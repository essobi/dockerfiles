FROM ubuntu:14.04  
ENV ZABBIX_VER 2.4.3-1+trusty  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN groupadd -r zabbix && useradd -r -g zabbix zabbix  
  
RUN \  
apt-get update \  
&& DEBIAN_FRONTEND=noninteractive apt-get -y install \  
wget \  
monit \  
mysql-client \  
fping \  
libsnmp-base \  
libopenipmi0 \  
unixodbc \  
libldap-2.4.2 \  
libsnmp30 \  
libiksemel3 \  
dbconfig-common \  
curl \  
# openjdk-7-jre-headless \  
php5 \  
php5-mysql \  
php5-gd \  
ttf-dejavu-core \  
apache2 \  
mc  
  
WORKDIR /zabbix  
  
RUN \  
wget http://repo.zabbix.com/zabbix/2.4/ubuntu/pool/main/z/zabbix/zabbix-
server-mysql_${ZABBIX_VER}_amd64.deb \  
&& wget http://repo.zabbix.com/zabbix/2.4/ubuntu/pool/main/z/zabbix/zabbix-
frontend-php_${ZABBIX_VER}_all.deb \  
## && wget http://repo.zabbix.com/zabbix/2.4/ubuntu/pool/main/z/zabbix/zabbix-
java-gateway_${ZABBIX_VER}_amd64.deb \  
&& wget http://repo.zabbix.com/zabbix/2.4/ubuntu/pool/main/z/zabbix/zabbix-
agent_2.4.3-1+trusty_amd64.deb  
  
COPY zabbix_server.conf /etc/zabbix/  
  
COPY monitrc /etc/monitrc  
RUN chmod 600 /etc/monitrc  
  
#VOLUME /var/lib/mysql \  
# /usr/lib/zabbix/alertscripts \  
# /usr/lib/zabbix/externalscripts \  
# /etc/zabbix/zabbix_agentd.d \  
# /var/log  
COPY zabbix-server-mysql.conf /etc/dbconfig-common/  
  
COPY init-zabbix.sh init-mysql.sh init-schema.sh /zabbix/  
  
EXPOSE 10051 10052 80 2812  
#CMD ["monit", "-d", "10", "-Ic", "/etc/monitrc"]  
CMD ["/zabbix/init-zabbix.sh"]  

