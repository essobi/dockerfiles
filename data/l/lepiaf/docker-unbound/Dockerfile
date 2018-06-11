FROM alpine:latest  
LABEL maintainer="Thierry Thuon <lepiaf@users.noreply.github.com>"
description="Unbound DNS cache"  
  
COPY unbound.conf /etc/unbound/unbound.conf  
RUN apk add --update --no-cache unbound tini && \  
mkdir -p /etc/unbound/conf.d && \  
wget http://www.internic.net/domain/named.root -O /etc/unbound/root.hints && \  
unbound-anchor && \  
unbound-checkconf  
  
VOLUME [ "/etc/unbound/conf.d" ]  
  
ENTRYPOINT ["/sbin/tini", "--"]  
CMD ["unbound", "-v", "-d", "-c", "/etc/unbound/unbound.conf"]  

