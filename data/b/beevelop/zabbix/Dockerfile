FROM beevelop/base  
  
MAINTAINER Maik Hummel <m@ikhummel.com>  
  
WORKDIR /opt/  
  
COPY zabbix_server.conf.tpl ./  
COPY conf.env ./  
COPY start ./  
  
RUN apt-get -qq update && \  
apt-get -qq install curl gettext netcat mysql-client -y && \  
apt-get -qq install libcurl4-openssl-dev libxml2-dev libsnmp-dev build-
essential libmysqld-dev -y && \  
mkdir zabbix && \  
curl -sL
"http://sourceforge.net/projects/zabbix/files/ZABBIX%20Latest%20Development/3.0.0alpha6/zabbix-3.0.0alpha6.tar.gz/download"
| tar xz -C zabbix --strip-components=1 && \  
  
groupadd zabbix && \  
useradd -g zabbix zabbix && \  
cd zabbix && \  
./configure --enable-server --enable-agent --with-mysql --enable-ipv6 --with-
net-snmp --with-libcurl --with-libxml2 && \  
make install && \  
chmod +x /opt/start  
  
CMD /opt/start

