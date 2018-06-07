FROM alpine:3.6  
LABEL name="opendkim" \  
version="2.10" \  
release="3" \  
architecture="x86_64" \  
vendor="Sergey Korolev"  
  
ADD https://github.com/just-
containers/s6-overlay/releases/download/v1.21.1.1/s6-overlay-amd64.tar.gz
/tmp/  
  
RUN \  
# s6 overlay  
gunzip -c /tmp/s6-overlay-amd64.tar.gz | tar -xf - -C / \  
# packages  
&& apk add \--no-cache opendkim  
  
# root filesystem  
ADD rootfs /  
  
VOLUME [ "/keys" ]  
EXPOSE 8891  
ENTRYPOINT [ "/init" ]  

