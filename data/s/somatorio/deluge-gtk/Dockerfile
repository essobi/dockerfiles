FROM alpine:3.4  
MAINTAINER Marco Antonio Martins Junior <somatorio@gmail.com>  
  
RUN echo "@testing http://nl.alpinelinux.org/alpine/edge/testing" >>
/etc/apk/repositories && \  
apk update && \  
apk add deluge@testing ttf-dejavu py-pip && \  
pip install service_identity && \  
apk del py-pip && rm -rf /var/cache/apk/*  
  
ENTRYPOINT ["/usr/bin/deluge-gtk"]  

