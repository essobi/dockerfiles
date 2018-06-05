FROM alpine:latest  
VOLUME ["/etc/unbound"]  
RUN apk add --no-cache unbound && chown -R unbound:unbound /etc/unbound/  
COPY unbound.conf /etc/unbound/  
EXPOSE 53 53/udp  
ENTRYPOINT ["/usr/sbin/unbound", "-dd"]  

