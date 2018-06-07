FROM debian:jessie  
  
ARG DOWNLOAD_URL=https://s3-us-west-2.amazonaws.com/grafana-
releases/master/grafana_latest_amd64.deb  
  
RUN apt-get update && \  
apt-get -y \--no-install-recommends install libfontconfig curl ca-certificates
&& \  
apt-get clean && \  
curl ${DOWNLOAD_URL} > /tmp/grafana.deb && \  
dpkg -i /tmp/grafana.deb && \  
rm /tmp/grafana.deb && \  
curl -L https://github.com/tianon/gosu/releases/download/1.10/gosu-amd64 >
/usr/sbin/gosu && \  
chmod +x /usr/sbin/gosu && \  
apt-get autoremove -y && \  
rm -rf /var/lib/apt/lists/* && \  
grafana-cli plugins install grafana-kairosdb-datasource && \  
grafana-cli plugins install camptocamp-prometheus-alertmanager-datasource && \  
grafana-cli plugins install natel-influx-admin-panel && \  
grafana-cli plugins install grafana-worldmap-panel && \  
grafana-cli plugins install grafana-clock-panel && \  
grafana-cli plugins install grafana-piechart-panel && \  
grafana-cli plugins update-all  
  
VOLUME ["/var/lib/grafana", "/var/log/grafana", "/etc/grafana"]  
  
EXPOSE 3000  
  
COPY ./run.sh /run.sh  
  
ENTRYPOINT ["/run.sh"]  

