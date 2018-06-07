FROM alpine:latest  
MAINTAINER Pichate Ins <cogent@cogentwebworks.com>  
  
# CREDITS  
# https://github.com/just-containers/base-alpine  
## S6 Overlay  
ENV S6_VERSION=v1.18.1.5  
##  
## ROOTFS  
##  
# root filesystem  
COPY rootfs /  
  
# s6 overlay  
RUN apk-install bash file  
  
ADD https://github.com/just-
containers/s6-overlay/releases/download/${S6_VERSION}/s6-overlay-amd64.tar.gz
/tmp/  
RUN gunzip -c /tmp/s6-overlay-amd64.tar.gz | tar -xf - -C / \  
&& rm /tmp/s6-overlay-amd64.tar.gz  
  
##  
## INIT  
##  
ENTRYPOINT [ "/init" ]  

