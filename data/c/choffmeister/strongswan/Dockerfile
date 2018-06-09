FROM alpine:3.3  
MAINTAINER Christian Hoffmeister <mail@choffmeister.de>  
  
RUN \  
echo http://dl-cdn.alpinelinux.org/alpine/v3.3/main > /etc/apk/repositories &&
\  
echo http://dl-cdn.alpinelinux.org/alpine/edge/testing >>
/etc/apk/repositories && \  
apk add --update iptables bash strongswan && \  
rm -rf /var/cache/apk/*  
  
ADD src /  
  
ENTRYPOINT ["/run.sh"]  

