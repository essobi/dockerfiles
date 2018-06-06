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
# Node_ExportedD  
#---------------------------------------------  
ENV NODEEXPORTERD_VERSION 0.1  
ENV NODEEXPORTER_VERSION 0.15.2  
RUN wget -O -
https://github.com/prometheus/node_exporter/releases/download/v${NODEEXPORTER_VERSION}/node_exporter-${NODEEXPORTER_VERSION}.linux-
amd64.tar.gz | tar xz -C /tmp && \  
cp /tmp/node_exporter-${NODEEXPORTER_VERSION}.linux-amd64/node_exporter
/usr/local/bin && \  
rm -rf /tmp/node_exporter-${NODEEXPORTER_VERSION}.linux-amd64  
  
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

