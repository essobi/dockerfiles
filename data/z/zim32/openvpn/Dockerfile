FROM debian:jessie  
  
ENV REMOTE_HOST 127.0.0.1  
ENV REMOTE_PORT 1194  
ENV OPENVPN_PROTO udp  
ENV OPENVPN_PORT 1194  
ENV OPENVPN_DEV tun  
ENV OPENVPN_NET_ADDR 10.8.0.0  
ENV OPENVPN_NET_MASK 255.255.255.0  
ENV ALLOW_INET true  
  
RUN \  
apt-get update && apt-get install -y \  
iptables \  
openvpn \  
easy-rsa \  
zip  
  
RUN \  
mkdir /etc/openvpn/easy-rsa/ && \  
cp -r /usr/share/easy-rsa/* /etc/openvpn/easy-rsa  
  
COPY /copy /  
  
RUN chmod a+x /root/scripts/*  
  
ENV PATH "$PATH:/root/scripts"  
ENTRYPOINT ["/bin/bash", "/root/scripts/entrypoint.sh"]

