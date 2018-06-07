FROM alpine:3.3  
MAINTAINER Troy Cauble <troycauble@gmail.com>  
  
RUN apk add --update openvpn && rm -rf /var/cache/apk/*  
  
COPY up2.sh /etc/openvpn/  
VOLUME ["/vpn"]  
  
ENTRYPOINT [ "openvpn", "--cd", "/vpn", "--config", "vpn.conf", "--up-delay",
"--up-restart", "--script-security", "2", "--up", "/etc/openvpn/up2.sh", "--
down-pre", "--down", "/etc/openvpn/down.sh" ]  

