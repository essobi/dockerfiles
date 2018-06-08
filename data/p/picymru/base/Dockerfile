FROM alpine:3.5  
MAINTAINER Matthew Gall <matthew@picymru.org.uk>  
  
ADD dosu /usr/bin/dosu  
ADD apk-install /usr/bin/apk-install  
  
RUN apk add --update --repository http://dl-
cdn.alpinelinux.org/alpine/edge/community/ tini &&\  
rm -rf /var/cache/apk/*  
  
RUN chmod +x /usr/bin/dosu /usr/bin/apk-install && \  
apk-install ca-certificates curl  
  
ENTRYPOINT ["/sbin/tini", "--"]  
CMD ['/bin/sh']

