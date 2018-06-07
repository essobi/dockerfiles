FROM alpine:edge  
  
RUN echo "@community http://dl-cdn.alpinelinux.org/alpine/edge/community" >>
/etc/apk/repositories && \  
echo "@main http://dl-cdn.alpinelinux.org/alpine/edge/main" >>
/etc/apk/repositories && \  
echo "@testing http://dl-cdn.alpinelinux.org/alpine/edge/testing" >>
/etc/apk/repositories && \  
apk add -U --no-cache \  
kea-dhcp6@testing && \  
rm -rf /var/cache/apk/*  
  
COPY entrypoint.sh /  
  
RUN chmod +x /entrypoint.sh  
  
CMD "/entrypoint.sh"

