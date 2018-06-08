# Pull base image  
FROM ubuntu:14.04  
MAINTAINER Safelink Internet  
  
ENV ZABBIX_VERSION 2.4  
# Install Zabbix and dependencies  
RUN \  
apt-get update && apt-get install -y software-properties-common wget nano && \  
wget
http://repo.zabbix.com/zabbix/${ZABBIX_VERSION}/ubuntu/pool/main/z/zabbix-
release/zabbix-release_${ZABBIX_VERSION}-1+trusty_all.deb \  
-O /tmp/zabbix-release_${ZABBIX_VERSION}-1+trusty_all.deb && \  
dpkg -i /tmp/zabbix-release_${ZABBIX_VERSION}-1+trusty_all.deb && \  
apt-add-repository multiverse && apt-get update && \  
apt-get install -y monit \  
snmp-mibs-downloader \  
zabbix-get \  
zabbix-proxy-sqlite3 \  
zabbix-sender && \  
apt-get autoremove -y && \  
mkdir -p /var/lib/sqlite  
  
# Copy scripts, Monit config and Zabbix config into place  
COPY monitrc /etc/monit/monitrc  
COPY ./scripts/entrypoint.sh /bin/docker-zabbix  
COPY ./zabbix/zabbix_proxy.conf /etc/zabbix/zabbix_proxy.conf  
  
# Fix permissions  
RUN chmod 755 /bin/docker-zabbix && \  
chmod 600 /etc/monit/monitrc && \  
chown zabbix:zabbix /var/lib/sqlite  
  
# Expose ports for  
# * 10051 zabbix_proxy  
EXPOSE 10051  
# Will run `/bin/docker run`, which instructs  
# monit to start zabbix_proxy.  
ENTRYPOINT ["/bin/docker-zabbix"]  
CMD ["run"]  

