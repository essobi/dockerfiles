#  
# Dockerfile for dante-server  
#  
FROM alpine:edge  
MAINTAINER Samuel X.S. Tseng <samuel.zxs@gmail.com>  
  
RUN set -xe \  
&& echo "@testing http://nl.alpinelinux.org/alpine/edge/testing/" >>
/etc/apk/repositories \  
&& apk --update add --no-cache dante-server@testing  
  
EXPOSE 1080/tcp  
EXPOSE 1080/udp  
  
ENTRYPOINT ["/usr/sbin/sockd"]  
CMD ["-h"]

