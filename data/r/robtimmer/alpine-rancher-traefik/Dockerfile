# Use robtimmer/alpine-rancher-tools as base image  
FROM robtimmer/alpine-rancher-tools  
  
# Set maintainer  
MAINTAINER Rob Timmer <rob@robtimmer.com>  
  
# Set environment variables  
ENV SERVICE_NAME=traefik \  
SERVICE_USER=traefik \  
SERVICE_UID=10001 \  
SERVICE_GROUP=traefik \  
SERVICE_GID=10001 \  
SERVICE_ARCHIVE=/opt/traefik-rancher-tools.tgz  
  
# Add root files to the image root  
ADD root /  
  
# Set the run command  
RUN cd ${SERVICE_VOLUME} && \  
tar czvf ${SERVICE_ARCHIVE} * ; rm -rf ${SERVICE_VOLUME}/*  

