# Graylog Collector  
#  
# Lightweight Java application that allows you to forward data from log files  
# to a Graylog cluster.  
FROM winggundamth/ubuntu-java:xenial  
MAINTAINER Jirayut Nimsaeng <w [at] winginfotech.net>  
ENV FROM_BASE=xenial-20160809  
# 1) Install Graylog2 Collector  
# 2) Copy initial collector.conf file  
# 3) Clean to reduce Docker Image size  
ARG APT_CACHER_NG  
RUN [ -n "$APT_CACHER_NG" ] && \  
echo "Acquire::http::Proxy \"$APT_CACHER_NG\";" \  
> /etc/apt/apt.conf.d/11proxy || true; \  
wget \  
https://packages.graylog2.org/repo/packages/graylog-collector-latest-
repository-ubuntu14.04_latest.deb && \  
apt-get update && \  
apt-get install -y apt-transport-https && \  
dpkg -i graylog-collector-latest-repository-ubuntu14.04_latest.deb && \  
apt-get update && \  
apt-get install -y graylog-collector && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /etc/apt/apt.conf.d/11proxy *.deb \  
/etc/graylog/collector/collector-id  
ADD build-files/collector.conf /etc/graylog/collector/collector.conf  
  
CMD ["/usr/share/graylog-collector/bin/graylog-collector", "run", "-f", \  
"/etc/graylog/collector/collector.conf"]  
VOLUME ["/etc/graylog/collector", "/var/log/graylog-collector"]  

