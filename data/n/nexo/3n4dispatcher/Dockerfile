#  
# This file build a Docker image for deployment environment  
#  
FROM nexo/alpine:latest  
MAINTAINER Guido Ronchetti <guido.ronchetti@nexo.cloud>  
ENV REFRESHED_AT 2016-12-02  
LABEL nexo.product="3nigm4-ishtmdispatcher"  
  
#  
# prepare the fs environment  
#  
RUN mkdir -p /opt/nexo/3nigm4/bin /opt/nexo/3nigm4/resources
/opt/nexo/3nigm4/config  
  
#  
# add resources  
#  
ADD resources/3nigm4-linux-amd64.tar /opt/nexo/3nigm4/bin  
ADD resources/template.html /opt/nexo/3nigm4/resources/template.html  
  
#  
# setup environment vars  
#  
ENV PATH /opt/nexo/3nigm4/bin/linux-amd64:$PATH  
  
#  
# version environment vars  
#  
ENV 3NIGM4_MAJOR_VERSION 0  
ENV 3NIGM4_MINOR_VERSION 1  
ENV 3NIGM4_PATCH_VERSION 9  
ENV 3NIGM4_RELEASE_TYPE beta  
  
#  
# Set entrypoint  
#  
ENTRYPOINT ["ishtmdispatcher"]

