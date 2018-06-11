FROM alpine:3.5  
  
RUN apk add \--no-cache opendkim=2.10.3-r4 openssl=1.0.2k-r0 perl=5.24.0-r0  
  
ENTRYPOINT ["/usr/sbin/opendkim", "-f", "-x", "/etc/opendkim/opendkim.conf"]  

