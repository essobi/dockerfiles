FROM alpine:3.5  
RUN apk add --no-cache unbound openssl && \  
unbound-control-setup && \  
apk del openssl  
ADD unbound.conf /etc/unbound/unbound.conf  
  
CMD ["/usr/sbin/unbound"]  
EXPOSE 53/udp  

