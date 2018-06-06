FROM rawmind/rancher-tools:0.3.4-6  
MAINTAINER Raul Sanchez <rawmind@gmail.com>  
  
#Set environment  
ENV SERVICE_NAME=etcd \  
SERVICE_USER=etcd \  
SERVICE_UID=10005 \  
SERVICE_GROUP=etcd \  
SERVICE_GID=10005 \  
SERVICE_HOME=/opt/etcd \  
SERVICE_ARCHIVE=/opt/etcd-rancher-tools.tgz  
  
# Add files  
ADD root /  
RUN cd ${SERVICE_VOLUME} && \  
chmod 755 ${SERVICE_VOLUME}/confd/bin/*.sh && \  
tar czvf ${SERVICE_ARCHIVE} * && \  
rm -rf ${SERVICE_VOLUME}/*  

