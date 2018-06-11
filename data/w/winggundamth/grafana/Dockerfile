# Grafana  
#  
# Visualizing time series data  
FROM winggundamth/ubuntu-base:trusty  
MAINTAINER Jirayut Nimsaeng <w [at] winginfotech.net>  
ENV FROM_BASE=trusty-20160624  
# 1) Install Grafana as describe here  
# http://docs.grafana.org/installation/debian/  
# 2) Clean to reduce Docker Image size  
ARG APT_CACHER_NG  
RUN [ -n "$APT_CACHER_NG" ] && \  
echo "Acquire::http::Proxy \"$APT_CACHER_NG\";" \  
> /etc/apt/apt.conf.d/11proxy || true; \  
apt-get update && \  
apt-get install -y wget apt-transport-https && \  
wget -qO - https://packagecloud.io/gpg.key | apt-key add - && \  
echo "deb https://packagecloud.io/grafana/stable/debian/ wheezy main" \  
> /etc/apt/sources.list.d/grafana.list && \  
apt-get update && \  
apt-get install -y grafana && \  
service grafana-server start && \  
service grafana-server stop && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /etc/apt/apt.conf.d/11proxy  
  
USER grafana  
WORKDIR /usr/share/grafana  
CMD ["/usr/sbin/grafana-server", "--", \  
"--pidfile=/var/run/grafana-server.pid", \  
"--config=/etc/grafana/grafana.ini", \  
"cfg:default.paths.data=/var/lib/grafana", \  
"cfg:default.paths.logs=/var/log/grafana", \  
"cfg:default.paths.plugins=/var/lib/grafana/plugins"]  
EXPOSE 3000  
VOLUME ["/var/log", "/etc/grafana"]  

