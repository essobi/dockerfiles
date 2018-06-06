FROM rawmind/rancher-tools:0.3.4-5  
MAINTAINER Raul Sanchez <rawmind@gmail.com>  
  
#Set environment  
ENV SERVICE_NAME=go-dnsmasq \  
SERVICE_HOME=/opt/go-dnsmasq \  
SERVICE_CONF=/opt/go-dnsmasq/etc/go-dnsmasq-source \  
SERVICE_VERSION=1.0.6 \  
SERVICE_USER=go-dnsmasq \  
SERVICE_UID=10009 \  
SERVICE_GROUP=go-dnsmasq \  
SERVICE_GID=10009 \  
SERVICE_ARCHIVE=/opt/go-dnsmasq-rancher-tools.tgz  
  
# Add files  
ADD root /  
RUN cd ${SERVICE_VOLUME} && \  
chmod 755 ${SERVICE_VOLUME}/confd/bin/*.sh && \  
tar czvf ${SERVICE_ARCHIVE} * && \  
rm -rf ${SERVICE_VOLUME}/*  
  

