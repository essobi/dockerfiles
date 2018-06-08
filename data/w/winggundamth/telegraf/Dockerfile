# Telegraf  
#  
# Time-Series Data Collection  
FROM winggundamth/ubuntu-base:trusty  
MAINTAINER Jirayut Nimsaeng <w [at] winginfotech.net>  
ENV FROM_BASE=trusty-20160624  
# 1) Install Telegraf as describe here  
# https://docs.influxdata.com/telegraf/v0.13/introduction/installation/  
# 2) Clean to reduce Docker Image size  
ARG APT_CACHER_NG  
RUN [ -n "$APT_CACHER_NG" ] && \  
echo "Acquire::http::Proxy \"$APT_CACHER_NG\";" \  
> /etc/apt/apt.conf.d/11proxy || true; \  
apt-get update && \  
apt-get install -y wget apt-transport-https && \  
wget -qO - https://repos.influxdata.com/influxdb.key | apt-key add - && \  
. /etc/lsb-release && \  
echo "deb https://repos.influxdata.com/$(echo $DISTRIB_ID | \  
tr '[:upper:]' '[:lower:]') ${DISTRIB_CODENAME} stable" \  
> /etc/apt/sources.list.d/influxdata.list && \  
apt-get update && \  
apt-get install -y telegraf && \  
service telegraf start && \  
service telegraf stop && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /etc/apt/apt.conf.d/11proxy  
  
USER telegraf  
CMD ["/usr/bin/telegraf", "-pidfile", "/var/run/telegraf/telegraf.pid", \  
"-config", "/etc/telegraf/telegraf.conf", "-config-directory", \  
"/etc/telegraf/telegraf.d"]  
VOLUME ["/var/log", "/etc/telegraf"]  

