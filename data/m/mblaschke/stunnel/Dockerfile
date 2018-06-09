FROM alpine  
  
RUN apk add --no-cache \  
ca-certificates \  
stunnel  
  
CMD ["/usr/bin/stunnel", "/etc/stunnel/stunnel.conf"]  

