FROM alpine  
  
RUN apk add --no-cache \  
bash \  
ca-certificates \  
iptables \  
nss-pam-ldapd \  
openvpn-auth-pam \  
openvpn  
  
ADD https://raw.githubusercontent.com/tests-always-included/mo/master/mo
/usr/bin/mo  
RUN chmod +x /usr/bin/mo  
  
COPY etc/nslcd.conf.mo /etc/  
COPY etc/openvpn/server.conf.mo /etc/openvpn/  
COPY etc/pam.d/openvpn /etc/pam.d/  
  
COPY docker-entrypoint.sh /usr/bin/  
  
WORKDIR /etc/openvpn  
CMD ["docker-entrypoint.sh"]  
  
EXPOSE 1194/udp 1194/tcp  

