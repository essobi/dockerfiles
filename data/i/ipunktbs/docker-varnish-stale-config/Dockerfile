FROM rawmind/rancher-tools:0.3.4-5  
ENV SERVICE_NAME=varnish \  
SERVICE_USER=varnish \  
SERVICE_UID=100 \  
SERVICE_GROUP=varnish \  
SERVICE_GID=101 \  
SERVICE_ARCHIVE=/opt/varnish-rancher-tools.tgz  
VOLUME ${SERVICE_VOLUME}  
  
COPY root /  
RUN cd ${SERVICE_VOLUME} && \  
tar czvf ${SERVICE_ARCHIVE} * ; rm -rf ${SERVICE_VOLUME}/*  

