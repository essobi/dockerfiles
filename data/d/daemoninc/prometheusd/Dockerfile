FROM ubuntu:16.04  
MAINTAINER "Rsrp Sinr" <rsrp.sinr@gmail.com>  
  
RUN apt-get update && \  
DEBIAN_FRONTEND=noninteractive apt-get install -y \  
locales \  
&& rm -rf /var/lib/apt/lists/*  
RUN locale-gen en_US.UTF-8  
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US:en  
ENV LC_ALL en_US.UTF-8  
RUN apt-get update && \  
DEBIAN_FRONTEND=noninteractive apt-get install -y \  
tar \  
wget \  
&& rm -rf /var/lib/apt/lists/*  
  
#---------------------------------------------  
# PrometheusD  
#---------------------------------------------  
ENV PROMETHEUSD_VERSION 0.1  
ENV PROMETHEUS_VERSION 2.0.0  
RUN wget -O -
https://github.com/prometheus/prometheus/releases/download/v${PROMETHEUS_VERSION}/prometheus-${PROMETHEUS_VERSION}.linux-
amd64.tar.gz | tar xz -C /tmp && \  
cp /tmp/prometheus-${PROMETHEUS_VERSION}.linux-amd64/prometheus
/usr/local/bin/ && \  
cp /tmp/prometheus-${PROMETHEUS_VERSION}.linux-amd64/promtool /usr/local/bin/
&& \  
mkdir -p /etc/prometheus && \  
rm -rf /tmp/prometheus-${PROMETHEUS_VERSION}.linux-amd64  
  
RUN apt-get update && \  
apt-get install -y \  
nginx \  
apache2-utils \  
&& rm -rf /var/lib/apt/lists/*  
  
ADD entrypoint.sh /entrypoint.sh  
RUN chmod 700 /entrypoint.sh  
  
ADD app.sh /app.sh  
RUN chmod 700 /app.sh  
  
ENTRYPOINT ["/entrypoint.sh"]  

