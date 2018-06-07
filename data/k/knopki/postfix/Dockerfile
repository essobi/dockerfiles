FROM alpine:3.6  
LABEL name="postfix-relay" \  
version="3.2.4" \  
release="10" \  
architecture="x86_64" \  
vendor="Sergey Korolev"  
  
ADD https://github.com/just-
containers/s6-overlay/releases/download/v1.21.1.1/s6-overlay-amd64.tar.gz
/tmp/  
  
RUN \  
# s6 overlay  
gunzip -c /tmp/s6-overlay-amd64.tar.gz | tar -xf - -C / \  
# packages  
&& apk add \--no-cache postfix ca-certificates \  
# postfix  
&& postconf -e "smtputf8_enable = no"  
# root filesystem  
ADD rootfs /  
  
VOLUME [ "/var/spool/postfix", "/etc/postfix", "/var/log" ]  
EXPOSE 25  
ENTRYPOINT [ "/init" ]  

