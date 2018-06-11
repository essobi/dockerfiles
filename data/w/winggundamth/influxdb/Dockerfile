# InfluxDB  
#  
# Time-Series Database  
FROM winggundamth/ubuntu-base:trusty  
MAINTAINER Jirayut Nimsaeng <w [at] winginfotech.net>  
ENV FROM_BASE=trusty-20160503.1  
# 1) Install InfluxDB as describe here  
# https://docs.influxdata.com/influxdb/v0.13/introduction/installation/  
# 2) Clean to reduce Docker Image size  
ARG APT_CACHER_NG  
RUN [ -n "$APT_CACHER_NG" ] && \  
echo "Acquire::http::Proxy \"$APT_CACHER_NG\";" \  
> /etc/apt/apt.conf.d/11proxy || true; \  
apt-get update && \  
apt-get install -y wget apt-transport-https && \  
wget -qO - https://repos.influxdata.com/influxdb.key | \  
sudo apt-key add - && \  
. /etc/lsb-release && \  
echo "deb https://repos.influxdata.com/$(echo $DISTRIB_ID | \  
tr '[:upper:]' '[:lower:]') ${DISTRIB_CODENAME} stable" \  
> /etc/apt/sources.list.d/influxdata.list && \  
apt-get update && \  
apt-get install -y influxdb && \  
service influxdb start && \  
service influxdb stop && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /etc/apt/apt.conf.d/11proxy  
  
USER influxdb  
CMD ["/usr/bin/influxd", "-pidfile", "/var/run/influxdb/influxd.pid",
"-config", "/etc/influxdb/influxdb.conf"]  
EXPOSE 8083 8086  
VOLUME ["/var/log", "/etc/influxdb"]  

