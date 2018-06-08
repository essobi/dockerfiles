FROM alpine:3.4  
MAINTAINER exira.com <info@exira.com>  
  
# Install packages.  
RUN \  
apk --update add sniproxy && \  
rm -rf /var/cache/apk/*  
  
CMD ["/usr/sbin/sniproxy", "-f", "-c", "/etc/sniproxy/default.conf"]  

