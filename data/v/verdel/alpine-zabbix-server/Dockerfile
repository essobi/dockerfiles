FROM verdel/alpine-base:latest  
MAINTAINER Vadim Aleksandrov <valeksandrov@me.com>  
  
ENV DB_HOST localhost  
ENV DB_PORT 3306  
ENV DB_USER zabbix  
ENV DB_PASS zabbix  
  
# Install zabbix  
RUN apk --update add \  
bash \  
python \  
py-pip \  
net-snmp-dev \  
net-snmp-libs \  
net-snmp \  
net-snmp-perl \  
net-snmp-tools \  
mysql-client \  
zabbix@community \  
zabbix-setup@community \  
zabbix-mysql@community \  
zabbix-agent@community \  
zabbix-utils@community \  
&& pip install --upgrade pip \  
&& pip install requests \  
# Clean up  
&& rm -rf \  
/usr/share/man \  
/tmp/* \  
/var/cache/apk/*  
  
# Copy init scripts  
COPY rootfs /  
  
RUN chmod 640 /etc/zabbix/zabbix_server.conf  
RUN chown root:zabbix /etc/zabbix/zabbix_server.conf  
  
# Export volumes directory  
VOLUME ["/etc/zabbix/alertscripts", "/etc/zabbix/externalscripts",
"/etc/zabbix/tls"]  
  
# Export ports  
EXPOSE 10051/tcp 10052/tcp  

