FROM debian:jessie  
  
RUN apt-get update && \  
apt-get install -y gcc make curl libpq-dev postgresql-client && \  
apt-get clean && \  
curl -Lo /tmp/zabbix.tar.gz
http://repo.zabbix.com/zabbix/2.4/debian/pool/main/z/zabbix/zabbix_2.4.6.orig.tar.gz
&& \  
tar -C /tmp/ -xf /tmp/zabbix.tar.gz && \  
(cd /tmp/zabbix-2.4.6 && ./configure --enable-server --with-postgresql && make
&& make install) && \  
cp -aP /tmp/zabbix-2.4.6/database/postgresql/*.sql /usr/local/share/zabbix/ &&
\  
rm -r /tmp/* && \  
useradd --system zabbix && \  
curl -Lo /usr/bin/confd
https://github.com/kelseyhightower/confd/releases/download/v0.10.0/confd-0.10.0-linux-
amd64 && \  
chmod +x /usr/bin/confd && \  
mkdir -p /etc/confd/templates/ && \  
mkdir -p /etc/confd/conf.d/  
  
COPY scripts/* /usr/local/share/zabbix/alertscripts/  
  
COPY *.toml /etc/confd/conf.d/  
COPY *.tmpl /etc/confd/templates/  
COPY entrypoint.sh /  
RUN chmod +x /entrypoint.sh  
RUN chmod +x /usr/local/share/zabbix/alertscripts/*  
  
CMD ["/entrypoint.sh"]  
EXPOSE 10051  

