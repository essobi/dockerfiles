FROM debian:jessie  
  
ENV GRAFANA_VERSION 2.6.0  
RUN apt-get update && \  
apt-get -y install libfontconfig wget adduser openssl ca-certificates vim
sqlite3 git && \  
apt-get clean && \  
wget
https://grafanarel.s3.amazonaws.com/builds/grafana_${GRAFANA_VERSION}_amd64.deb
-O /tmp/grafana.deb && \  
dpkg -i /tmp/grafana.deb && \  
rm /tmp/grafana.deb  
  
RUN git clone https://github.com/alexanderzobnin/grafana-zabbix /tmp/grafana-
zabbix && \  
mv /tmp/grafana-zabbix/zabbix/
/usr/share/grafana/public/app/plugins/datasource/ && \  
rm -rf /tmp/grafana-zabbix/  
  
VOLUME ["/var/lib/grafana", "/var/log/grafana", "/etc/grafana"]  
  
EXPOSE 3000  
COPY ./template/credentials /root/.aws/credentials  
  
ENTRYPOINT ["/usr/sbin/grafana-server", "--homepath=/usr/share/grafana", "--
config=/etc/grafana/grafana.ini", "cfg:default.paths.data=/var/lib/grafana",
"cfg:default.paths.logs=/var/log/grafana"]  

