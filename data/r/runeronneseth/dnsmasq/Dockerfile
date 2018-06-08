FROM alpine:3.7  
  
MAINTAINER Rune Rønneseth <rune.ronneseth@kred.no>  
  
RUN apk --no-cache add \  
dnsmasq \  
&& \  
apk --no-cache add --virtual .build-deps \  
curl \  
&& \  
mkdir /var/lib/tftpboot && \  
curl -fsSL -o /var/lib/tftpboot/undionly.kpxe
http://boot.ipxe.org/undionly.kpxe && \  
curl -fsSL -o /var/lib/tftpboot/ipxe.efi http://boot.ipxe.org/ipxe.efi \  
&& \  
apk del .build-deps  
  
EXPOSE 53 \  
67 \  
69  
  
ENTRYPOINT ["/usr/sbin/dnsmasq"]  

