FROM gliderlabs/alpine  
  
MAINTAINER cd <cleardevice@gmail.com>  
  
RUN set -o nounset -o errexit -o xtrace -o verbose && \  
# update index and install packages  
apk add \--update-cache \  
curl ca-certificates bash curl wget && \  
# remove package index  
rm -rf /var/cache/apk/*  
  
ENV S6_VERSION=1.17.1.2 \  
SVC_TL_DIR=/etc/s6/svc-templates \  
SVC_DIR=/etc/services.d  
  
RUN set -o nounset -o errexit -o xtrace -o verbose && \  
curl -sSL https://github.com/just-
containers/s6-overlay/releases/download/v${S6_VERSION}/s6-overlay-amd64.tar.gz
\  
| tar -zxf - -C / && \  
mkdir -p $SVC_TL_DIR && \  
echo "#!/usr/bin/with-contenv sh" \  
> ${SVC_TL_DIR}/run.container.env && \  
echo -e "#!/bin/sh\ns6-svscanctl -t /var/run/s6/services" \  
> ${SVC_TL_DIR}/finish.stop.container && \  
chmod -R +x ${SVC_TL_DIR}/*  
  
ENTRYPOINT ["/init"]  

