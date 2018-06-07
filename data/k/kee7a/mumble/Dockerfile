FROM alpine:edge  
MAINTAINER Jeff Siqueira <root@kee7a.com>  
  
RUN apk add --update murmur icu-libs && rm -rf /var/cache/apk/*  
  
RUN addgroup \  
-S -g 1000 \  
mumble && \  
adduser \  
-S -H -D \  
-h /data \  
-s /bin/sh \  
-u 1000 \  
-G mumble \  
mumble  
  
VOLUME ["/data/config"]  
VOLUME ["/data/db"]  
VOLUME ["/data/cert"]  
  
EXPOSE 64738/udp  
EXPOSE 64738/tcp  
  
USER mumble  
  
ENTRYPOINT ["/usr/bin/murmurd", "-fg", "-ini", "/data/config/mumble-
server.ini"]  

