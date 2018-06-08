FROM rawmind/alpine-tools:3.5-1  
MAINTAINER Raul Sanchez <rawmind@gmail.com>  
  
ENV SERVICE_ARCHIVE=/opt/k8s-tools.tgz \  
KEEP_ALIVE=1  
# Add files  
ADD root /  
RUN cd ${SERVICE_VOLUME} && \  
tar czvf ${SERVICE_ARCHIVE} * ; rm -rf ${SERVICE_VOLUME}/*

