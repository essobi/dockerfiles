FROM alpine:3.3  
MAINTAINER Chao Shen <shen218@gmail.com>  
RUN echo http://dl-cdn.alpinelinux.org/alpine/v3.3/main >
/etc/apk/repositories;\  
echo http://dl-cdn.alpinelinux.org/alpine/edge/testing >>
/etc/apk/repositories;\  
apk add --update iptables bash strongswan;\  
rm -rf /var/cache/apk/*  
ADD src /  
ENV VPN_DOMAIN myvpndomain.com  
ENV VPN_SUBNET 192.168.2.0/24  
ENV VPN_DNS 192.168.1.1  
ENV VPN_PSK yourrpresharedkeyhere  
ENV VPN_USERNAME username  
ENV VPN_PASSWORD yourpasswordhere  
ENV VPN_P12_PASSWORD yourpasswordhere  
  
ENTRYPOINT ["/init.sh"]  
  

