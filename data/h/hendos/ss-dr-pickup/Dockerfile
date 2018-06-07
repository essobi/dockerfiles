# dr-backup  
# Copyright (C) 2016 Henderson Group  
FROM alpine:3.3  
MAINTAINER Michael Gliwinski <michael.gliwinski@henderson-group.com>  
  
RUN apk update \  
&& apk add darkhttpd=1.11-r5 zip=3.0-r4 \  
&& rm -rf /var/cache/apk/*  
  
COPY dkr-init.sh /usr/local/sbin/dkr-init  
ENTRYPOINT ["/usr/local/sbin/dkr-init"]  
  
EXPOSE 80/tcp  

