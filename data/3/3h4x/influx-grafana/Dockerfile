FROM tutum/curl:trusty  
MAINTAINER Feng Honglin <hfeng@tutum.co>  
  
# Install InfluxDB  
ENV INFLUXDB_VERSION 0.8.8  
RUN curl -s -o /tmp/influxdb_latest_amd64.deb
https://s3.amazonaws.com/influxdb/influxdb_${INFLUXDB_VERSION}_amd64.deb && \  
dpkg -i /tmp/influxdb_latest_amd64.deb && \  
rm /tmp/influxdb_latest_amd64.deb && \  
rm -rf /var/lib/apt/lists/*  
  
ENV GRAFANA_VERSION 1.9.1  
RUN apt-get update && \  
apt-get install -y wget pwgen apache2-utils && \  
wget http://grafanarel.s3.amazonaws.com/grafana-${GRAFANA_VERSION}.tar.gz -O
grafana.tar.gz && \  
tar zxf grafana.tar.gz && \  
rm grafana.tar.gz && \  
rm -rf app && \  
mv grafana-${GRAFANA_VERSION} app && \  
apt-get autoremove -y wget && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
RUN apt-get update && apt-get -qy install nginx  
RUN apt-get update && apt-get -qy install collectd  
  
ADD config.toml /config/config.toml  
ADD run.sh /run.sh  
RUN chmod +x /*.sh  
  
ENV PRE_CREATE_DB **None**  
ENV SSL_SUPPORT **False**  
ENV SSL_CERT **None**  
  
# Admin server  
EXPOSE 8083  
# HTTP API  
EXPOSE 8086  
# HTTPS API  
EXPOSE 8084  
ADD grafana/config.js /app/config.js  
ADD grafana/default /etc/nginx/sites-enabled/default  
  
# Environment variables for HTTP AUTH  
ENV HTTP_USER admin  
ENV HTTP_PASS **Random**  
  
ENV INFLUXDB_PROTO http  
ENV INFLUXDB_HOST **ChangeMe**  
ENV INFLUXDB_PORT 8086  
ENV INFLUXDB_NAME **ChangeMe**  
ENV INFLUXDB_USER root  
ENV INFLUXDB_PASS root  
ENV INFLUXDB_IS_GRAFANADB false  
  
ENV ELASTICSEARCH_PROTO http  
ENV ELASTICSEARCH_HOST **None**  
ENV ELASTICSEARCH_PORT 9200  
ENV ELASTICSEARCH_USER **None**  
ENV ELASTICSEARCH_PASS **None**  
  
ADD run.sh /run.sh  
ADD set_influx_db.sh /set_influx_db.sh  
ADD set_basic_auth.sh /set_basic_auth.sh  
ADD set_elasticsearch.sh /set_elasticsearch.sh  
RUN chmod +x /*.sh  
  
# Raft port (for clustering, don't expose publicly!)  
#EXPOSE 8090  
# Protobuf port (for clustering, don't expose publicly!)  
#EXPOSE 8099  
VOLUME ["/data"]  
  
CMD ["/run.sh"]  

