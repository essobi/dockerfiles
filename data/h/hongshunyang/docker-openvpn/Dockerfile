FROM hongshunyang/docker-alpine  
MAINTAINER Hongshun Yang<yanghongshun@outlook.com>  
  
#openvpn 2.4.0 with xor  
RUN echo '@alpine-abuild-mirror http://alpine-repo.ddns.net/main' >>
/etc/apk/repositories  
  
RUN apk add -U easy-rsa openvpn@alpine-abuild-mirror=2.4.0-r0 \  
&& ln -s /usr/share/easy-rsa/easyrsa /usr/local/bin  
  
VOLUME ["/etc/openvpn"]  
  
EXPOSE 1194/udp  
  

