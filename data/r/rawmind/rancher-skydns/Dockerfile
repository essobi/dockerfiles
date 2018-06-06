FROM rawmind/rancher-tools:0.3.4-5  
MAINTAINER Raul Sanchez <rawmind@gmail.com>  
  
#Set environment  
ENV SERVICE_NAME=skydns \  
SERVICE_HOME=/opt/skydns \  
SERVICE_CONF=/opt/skydns/etc/skydns-source \  
SERVICE_USER=skydns \  
SERVICE_UID=10006 \  
SERVICE_GROUP=skydns \  
SERVICE_GID=10006 \  
SERVICE_ARCHIVE=/opt/skydns-rancher-tools.tgz  
  
# Add files  
ADD root /  
RUN cd ${SERVICE_VOLUME} && \  
chmod 755 ${SERVICE_VOLUME}/confd/bin/*.sh && \  
tar czvf ${SERVICE_ARCHIVE} * && \  
rm -rf ${SERVICE_VOLUME}/*  
  

