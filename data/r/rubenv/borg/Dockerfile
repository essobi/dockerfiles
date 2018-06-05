FROM alpine:edge  
  
RUN echo http://nl.alpinelinux.org/alpine/edge/testing >>
/etc/apk/repositories && \  
apk add --update borgbackup && \  
rm -rf /var/cache/apk/*  

