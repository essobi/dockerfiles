FROM alpine:edge  
MAINTAINER Tim Dettrick <t.dettrick@uq.edu.au>  
  
RUN echo "http://dl-cdn.alpinelinux.org/alpine/edge/testing" >>
/etc/apk/repositories && \  
adduser -S -D -h /dev/null -s /sbin/nologin nghttpx && \  
apk add --update nghttp2 python openssl ca-certificates && \  
rm -rf /var/cache/apk/*  
  
ENTRYPOINT ["/usr/bin/nghttpx", "--user=nghttpx"]  
  
EXPOSE 3000  

