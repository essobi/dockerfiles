FROM alpine:latest  
MAINTAINER Martijn Pepping <martijn@xbsd.nl>  
  
RUN apk add --update haproxy && rm -rf /var/cache/apk/*  
  
CMD ["haproxy", "-f", "/etc/haproxy/haproxy.cfg"]  

