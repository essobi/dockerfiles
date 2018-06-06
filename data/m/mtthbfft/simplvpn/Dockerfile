FROM alpine:3.5  
LABEL maintainer "Matthieu Buffet <mtth.bfft@gmail.com>"  
  
RUN apk add --no-cache \  
openssl \  
openvpn \  
git  
  
RUN mkdir -p /dev/net && { [ -c /dev/net/tun ] || mknod /dev/net/tun c 10 200;
}  
  
EXPOSE 9090 8000  
HEALTHCHECK \--timeout=2s --interval=2m \  
CMD echo status | nc localhost 8000 || exit 1  
  
VOLUME ["/etc/openvpn/","/var/log/openvpn/"]  
  
CMD ['/usr/sbin/openvpn', '--config', '/etc/openvpn/server.conf', '--
management', '127.0.0.1', '8000']  

