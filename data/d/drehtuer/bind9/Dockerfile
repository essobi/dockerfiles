# base image  
FROM debian:stable-slim  
  
LABEL name="bind9" \  
description="Bind9 DNS server" \  
version="1.0" \  
maintainer="drehtuer@drehtuer.net"  
  
# apt and create required directories  
RUN apt-get update \  
&& apt-get install -y \  
bind9 \  
&& rm -rf /var/lib/apt/lists/* \  
&& mkdir -p /run/named \  
&& chown bind:bind /run/named  
  
# required ports  
EXPOSE 53/tcp \  
53/udp  
  
VOLUME /etc/named  
  
# start application  
ENTRYPOINT ["/usr/sbin/named", "-c", "/etc/named/named.conf", "-u", "bind",
"-g"]  

