FROM alpine:3.2  
RUN echo "http://dl-3.alpinelinux.org/alpine/edge/testing/" >>
/etc/apk/repositories \  
&& apk add -U stunnel ca-certificates \  
&& rm -rf /var/cache/apk/*  
  
ENTRYPOINT [ "/usr/bin/stunnel" ]  
  

