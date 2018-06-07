# based on https://github.com/just-containers/base-alpine.git  
FROM khipu/base-alpine  
MAINTAINER developers@khipu.com  
  
ARG S6O_VERSION=1.17.2.0  
# root filesystem  
COPY rootfs /  
  
# s6 overlay  
RUN curl -ssL https://github.com/just-
containers/s6-overlay/releases/download/v${S6O_VERSION}/s6-overlay-
amd64.tar.gz -o /tmp/s6-overlay.tar.gz \  
&& tar xvfz /tmp/s6-overlay.tar.gz -C / \  
&& rm -f /tmp/s6-overlay.tar.gz  
  
##  
## INIT  
##  
ENTRYPOINT [ "/init" ]  

