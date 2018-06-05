FROM alpine:latest  
  
RUN apk add --no-cache bind  
  
EXPOSE 53/tcp 53/udp  
  
VOLUME ["/etc/bind", "/var/lib/bind"]  
  
CMD ["/usr/sbin/named", "-f", "-g"]  

